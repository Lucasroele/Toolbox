import os
import argparse

"""
Provide overview of the files in the current directory and its subdirectories
Find files with a specific extension in a directory tree
"""

def count_files_by_extension(directory, extension):

    # Not used currently
    """
    Count the number of files with a specific extension in a given directory.

    Args:
        directory (str): The directory to search for files.
        extension (str): The file extension to count.

    Returns:
        int: The number of files with the specified extension.
    """
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                count += 1
    return count

def traverse_directory_tree(directory):
    """
    Traverse a directory tree and count the number of files for each extension.

    Args:
        directory (str): The directory to traverse.

    Returns:
        dict: A dictionary where the keys are file extensions and the values are the corresponding counts.
    """
    extensions = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            extension = os.path.splitext(file)[1]
            if extension not in extensions:
                extensions[extension] = 1
            else:
                extensions[extension] += 1
    return extensions

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--print-filenames", type=str, metavar="<extension>", default=None, help="Print filenames with the given extension")
    args = parser.parse_args()

    directory = os.getcwd()
    extensions = traverse_directory_tree(directory)
    # printing the extensions and their incidences
    print("This directory tree contains the following filetypes:")
    extensionTextMaxLen = max(map(len, extensions.keys()))
    countTextMaxLen = max(map(len, map(str, extensions.values())))
    for extension, count in extensions.items():
        display_ext = "<None>" if extension == "" else extension
        print(f"{display_ext:<{extensionTextMaxLen}}: {count:>{countTextMaxLen}}")
    print()
    # `--print-filenames` functionality
    if not args.print_filenames in [None, ""]:
        search_ext = args.print_filenames if args.print_filenames[0] == '.' else '.' + args.print_filenames
        for extension, count in extensions.items():
            if extension == search_ext:
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if os.path.splitext(file)[1] == extension:
                            print(os.path.join(root, file))