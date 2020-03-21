
# filesort.py

filesort is a Python program that sorts files in a given directory to directories named after their extensions. It can even find files in subdirectories.


## Description
       Sorts all files in the path folder to directories named by their extensions.

       Creates the DIRECTORY(ies), if they do not already exist.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.


## Installation

No packages are required.


## Usage

python filesort.py [OPTION]

If no option is provided it

## Options

       -p, --path
              set directory path to filesort, defaults to the current directory.
       -r, --recursive
              go through all subdirectories, moves files to the path, deletes
              subdirectories and then sorts.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
