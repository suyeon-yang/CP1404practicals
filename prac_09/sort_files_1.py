import os

os.chdir("FilesToSort")
for filename in os.listdir('.'):
    if os.path.isdir(filename):
        continue

    extension = filename.split('.')[-1]

    try:
        os.mkdir(extension)
    except FileExistsError:
        print("That file already exists")

    print("{}/{}".format(extension, filename))
    os.rename(filename, "{}/{}".format(extension, filename))


