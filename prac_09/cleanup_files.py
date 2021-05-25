
import shutil
import os
import re

def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))
    os.chdir('Lyrics/Christmas')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    try:
        os.mkdir('temp')
    except FileExistsError:
        print("The file already exist")

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    first_name = filename.replace(".TXT", ".txt").replace(" ", "_")
    pattern = "[A-Z]"
    new_name = re.sub(pattern, lambda x: "_" + x.group(0), first_name)
    last_name = new_name.replace("__", "_")

    if last_name[0] == "_":
        m = last_name[1:]

    return m


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(old_name, new_name)

main()
