from os import listdir
from os.path import isfile, splitext, exists
from os.path import join as joinPath
import os
import shutil
import argparse
import logging

"""NAME
       filesort - sorts files to directories named after their extensions

USAGE
       python filesort.py [OPTION]... DIRECTORY...

DESCRIPTION
       Sorts all files in folder to directories named by their extensions.

       Creates the DIRECTORY(ies), if they do not already exist.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -p, --path
              set directory path to filesort, defaults to current directory.
       -r, --recursive
              go through all subdirectories, move files to path, deletes
              sub directories and then sorts."""


def parse_arguments():
    parser = argparse.ArgumentParser(description='filesort - sorts files to directories named after their extensions')
    parser.add_argument('-p', '--path', type=dir_path, default=os.getcwd(), help="set directory path to filesort, defaults to current directory.")
    parser.add_argument('-r', '--recursive', action="store_true", help="go through all subdirectories, move files to path, delete sub directories and then sort.")

    return parser.parse_args()


def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


DUPLICATE_MARKER = ' (1)'


def flattenFiles(here):
    '''Move all files in subdirs to here, then delete subdirs.
       Conflicting files are renamed, with 1 appended to their name.'''
    for root, dirs, files in os.walk(here, topdown=False):
        if root != here:
            for name in files:
                source = joinPath(root, name)
                target = handleDuplicates(joinPath(here, name))
                os.rename(source, target)

        for name in dirs:
            os.rmdir(joinPath(root, name))


def handleDuplicates(target):
    while exists(target):
        base, ext = splitext(target)
        target = base + DUPLICATE_MARKER + ext
    return target


def sort_files_in_a_folder(mypath):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    files = [f for f in listdir(mypath) if isfile(joinPath(mypath, f))]
    file_type_variation_list = []
    filetype_folder_dict = {}
    for file in files:
        filetype = file.split('.')[-1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name = mypath + '/' + filetype
            filetype_folder_dict[str(filetype)] = str(new_folder_name)
            if os.path.isdir(new_folder_name):
                continue
            else:
                os.mkdir(new_folder_name)
    for file in files:
        src_path = mypath+'/'+file
        filetype = file.split('.')[-1]
        if filetype in filetype_folder_dict.keys():
            dest_path = filetype_folder_dict[str(filetype)]
            logging.info("Moving: " + file + ' >>> ' + filetype_folder_dict[str(filetype)])
            print("Moving: " + file + ' >>> ' + filetype_folder_dict[str(filetype)])
            shutil.move(src_path, dest_path)


def check_recursive(args):
    i = 0
    if args.recursive:
        x = input("This will delete all subdirectories in" + args.path + " after moving files to root directory!! \nContinue? y/n: ")
        while i == 0:
            if x == "y":
                logging.warning('Recursive Confirmed. Deleting Directories.')
                mypath = str(args.path)
                here = mypath + '/'
                flattenFiles(here)
                sort_files_in_a_folder(str(args.path))
                i += 1
                break
            if x == "n":
                print("Recursive Denied. Sorting only loose files in Root directory")
                logging.warning('Recursive Denied. Sorting only loose files in Root directory')
                i += 1
    return False


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', filename='Sorter.log', level=logging.INFO)
    parsed_args = parse_arguments()
    logging.info('==                    Started                            ==')
    logging.info('Working Directory: ' + str(parsed_args.path))
    logging.info('===========================================================')
    if not check_recursive(parsed_args):
        logging.info('===========================================================')
        logging.info('Started Moving Files, please be patient.')
        logging.info('===========================================================')
        sort_files_in_a_folder(str(parsed_args.path))


if __name__ == "__main__":
    main()
