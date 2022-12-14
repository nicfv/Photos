import os
import re
from datetime import datetime

base = '.'
extension = ['.jpg', '.JPG']
indexFileName = 'index.md'
newLine = '\n'

# Generate a human-readable title given the raw folder name
def generateTitle(raw) -> str:
    found = re.search('([0-9]{4})_([0-9]{2})_(.+)', raw)
    if found:
        months = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
        year = found[1]
        month = months[int(found[2]) - 1]
        location = found[3].replace('_', ' ')
        return location + ' (' + month + ', ' + year + ')'
    return None

# Write the contents in the homepage
i = open(os.path.join(base, indexFileName), 'x')
i.write('# Homepage' + newLine + newLine)
i.write('Hello, there! You stumbled across one of my many websites. This is just an informal space to show off my pictures from traveling.' + newLine + newLine)

# Get valid directories in base folder
directories = os.listdir(base)
directories = list(filter(lambda directory: os.path.isdir(directory), directories))
directories.sort()

# Loop through each directory and generate the index
for directory in directories:
    cleanName = generateTitle(directory)
    if not cleanName:
        print('Skipping ' + directory + '...')
        continue
    print('Generating index in ' + directory + '...')
    currentPath = os.path.join(base, directory)
    i.write('- [' + cleanName + '](' + directory + ')' + newLine)
    indexFilePath = os.path.join(currentPath, indexFileName)
    f = open(indexFilePath, 'x')
    f.write('# ' + cleanName + newLine + newLine)
    f.write('[Go Back](/)' + newLine + newLine)
    for fileName in os.listdir(currentPath):
        finalPath = os.path.join(currentPath, fileName)
        splitName = os.path.splitext(fileName)
        if(os.path.isfile(finalPath) and splitName[1] in extension):
            f.write('![' + splitName[0] + '](' + fileName + ')' + newLine + newLine)
    f.write('[Go Back](/)')
    f.close()
    print('Success!')

i.write(newLine + 'Last updated ' + datetime.now().strftime('%h %d, %Y'))
i.close()