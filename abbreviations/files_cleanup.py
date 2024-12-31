import os

""" dir_path = os.path.dirname(os.path.realpath(__file__))
current = os.getcwdb()
print(
    "\n","-------------------------------","\n",
    "dir_path:",dir_path,"\n",
    "current:",current,"\n",
    "-------------------------------","\n",
)

def scanRecurse(base):
    for entry in os.scandir(base):
        if os.path.isfile(entry):
            yield os.path.join(base, entry.name)
        elif os.path.isdir(entry):
            print(entry.path)
            yield scanRecurse(entry.path)
            # os.mkdir('./CleanedUp')

for file in scanRecurse(current):
    print(file)
 """

""" dirname = os.path.dirname(__file__)
abspath = os.path.abspath(os.path.dirname(__file__))
realpath = os.path.realpath(__file__)
file_path =  os.path.join(os.path.abspath(os.path.dirname(__file__)), '../public/files/programs.txt') """

folderToClean = os.path.join(os.path.dirname(__file__), '../public/files')
folderTrash = os.path.join(os.path.dirname(__file__), './CleanedUp')

print(
    "\n","-------------------------------","\n",
    "folderToClean:",folderToClean,"\n",
    "folderTrash:",folderTrash,"\n",
    "-------------------------------","\n",
)

for entry in os.scandir(folderToClean):
    location_origin = os.path.join(folderToClean, entry.name)
    location_desitination = os.path.join(folderTrash, entry.name)

    print(entry.name)
    print(location_origin)
    print(location_desitination)

    if os.path.isfile(location_origin) and 'programs' not in location_origin:
        print(location_origin)
        os.rename(location_origin, location_desitination)