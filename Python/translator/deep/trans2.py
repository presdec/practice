try:
    from xml.etree.cElementTree import XML
except ImportError:
    from xml.etree.ElementTree import XML
import zipfile
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)
from easygui import choicebox, textbox, fileopenbox
import os
import pyperclip
import shutil


"""
Module that provides a destination and source language choice.
Further languages can be added from the following list under choices:
https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
"""

s_choices = ["en","el","fr"]
source_lang = choicebox(
    "What is the Source Language?", "translator", choices=s_choices
)

choices = ["el","en","fr"]
desti_lang = choicebox(
    "What is the Destination Language?", "translator", choices=choices
)


"""
Module that extracts text from MS XML Word document (.docx).
(Inspired by python-docx <https://github.com/mikemaccana/python-docx>)
"""


WORD_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
PARA = WORD_NAMESPACE + "p"
TEXT = WORD_NAMESPACE + "t"


def get_docx_text(filename):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(filename)
    xml_content = document.read("word/document.xml")
    document.close()
    tree = XML(xml_content)

    paragraphs = []
    for paragraph in tree.iter(PARA):
        texts = [node.text for node in paragraph.iter(TEXT) if node.text]
        if texts:
            paragraphs.append("".join(texts))

    return "\n\n".join(paragraphs)


def splitIntoSentences(text):
    text = text.split("\n")
    return text


def translate(text, source, dest):
    if text is None:
        print("Invalid Text")
    elif text != "":
        translation = GoogleTranslator(source='en', target=desti_lang).translate(text=text)
        pyperclip.copy(translation)
    return translation


def translate2(text, source, dest):
    if text is None:
        print("Invalid Text")
    elif text != "":
        translation2 = MyMemoryTranslator(source='auto', target=desti_lang).translate(text)
    return translation2


def translate3(text, source, dest):
    if text is None:
        print("Invalid Text")
    elif text != "":
        translation3 = LingueeTranslator(source='auto', target=desti_lang).translate(text)
    return translation3


def split_text(filename):
    """
    Split the clean text temp file into 4900 byte files. Filenames: 0 1 2 ...
    """
    i = 0
    with open(filename, "r", encoding="utf8") as in_file:
        bytes = in_file.read(4900) # read 4900 bytes
        while bytes:
            with open("./tmp/" + str(i), 'w', encoding="utf8") as output:
                output.write(bytes)
            bytes = in_file.read(4900) # read another 4900 bytes
            i += 1
    return i


def temp_files(clean_txt):   # create a temporary directory to store files
    try:
        os.makedirs('tmp')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    f = open("./tmp/clean", "w", encoding="utf8")
    f.writelines(clean_txt)
    f.close()


def temp_clean():   # remove the temporary directory
    dir_path = './tmp/'
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


def main(filename, source_lang, desti_lang):
    print("Translating:  " + os.path.basename(filename))
    count = 0
    clean = get_docx_text(filename)
    para = splitIntoSentences(clean)
    print('Approximately: ' + str(len(clean)) + ' characters long.')
    temp_files(clean)
    filecount = split_text("./tmp/clean")
    print(filecount)
    #  shutil.copytree('./tmp', './tmp2')    # retain a copy of the tmp files
    temp_clean()


if __name__ == "__main__":
    filename = fileopenbox()
    main(filename, source_lang, desti_lang)