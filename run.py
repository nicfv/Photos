import os

base = '.'
ignore = ['.git', '.github']
extension = ['.jpg', '.JPG'] # may not be necessary...
indexFileName = 'index.md'
newLine = '\r\n'

# Generate a human-readable title given the raw folder name
def generateTitle(raw):
    months = {
        '01' : 'Jan',
        '02' : 'Feb',
        '03' : 'Mar',
        '04' : 'Apr',
        '05' : 'May',
        '06' : 'Jun',
        '07' : 'Jul',
        '08' : 'Aug',
        '09' : 'Sep',
        '10' : 'Oct',
        '11' : 'Nov',
        '12' : 'Dec',
    }
    parts = raw.split('_')
    year = parts[0]
    month = months[parts[1]]
    location = ' '.join(parts[2:])
    return location + ' (' + month + ', ' + year + ')'

# Write the contents in the homepage
i = open(os.path.join(base, indexFileName), 'x')
i.write('# Homepage' + newLine + newLine)
i.write('Hello, there! You stumbled across one of my many websites. This is just an informal space to show off my pictures from traveling.' + newLine + newLine)

# Get directories in base folder
directories = os.listdir(base)
print(directories) # debugging
directories.sort()
print(directories) # debugging

for directory in directories:
    if(os.path.isdir(directory) and not directory in ignore):
        print('Generating index in ' + directory + '...')
        currentPath = os.path.join(base, directory)
        cleanName = generateTitle(directory)
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
        f.write('[Go Back](/)' + newLine)
        f.close()
        print('Success!')

i.close()