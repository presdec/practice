# Importa pandas library for importing csv
import pandas as pd


#  Imports the Google Cloud client library
from googletrans import Translator
proxy = {
        'http':  'http: //username: password@1.1.1.1: 1234',
        'https':  'http: //username: password@1.1.1.1: 1234',
}

translator = Translator(proxies=proxy)


# Translating the text to specified target language
def translate(word):
    translation = translator.translate(word)

    return (translation)


# Import data from CSV
def importCSV():
    data = pd.read_csv('/home/presdec/temp/other.csv')
    countRows = (len(data))

    # Create a dictionary with translated words
    translatedCSV = {"imgalt": [], "title": [], "desciption": [], "difficulty": [], "categories": [], "method": [], "ingredients2": []}  # Change the column names accordingly to your coumns names

    count = 0
    # Translated word one by one from the CSV file and save them to the dictionary
    for index, row in data.iterrows():
        count += 1
        print(str(count) + row["imgalt"])  # Check to see it is running
        translatedCSV["imgalt"].append(translator.translate(str(row["imgalt"]), dest='en'))
        translatedCSV["title"].append(translator.translate(row["title"]))
        print(translatedCSV["title"])  # Check to see it is translating
        translatedCSV["desciption"].append(translator.translate(row["desciption"]))
        translatedCSV["difficulty"].append(translator.translate(row["difficulty"]))
        translatedCSV["categories"].append(translator.translate(row["categories"]))
        translatedCSV["method"].append(translator.translate(row["method"]))
        translatedCSV["ingredients2"].append(translator.translate(row["ingredients2"]))

    # Create a Dataframe from Dictionary
    # Save the DataFrame to a CSV file
    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("translatedCSV.csv", sep='\t')


# Call the function
importCSV()
