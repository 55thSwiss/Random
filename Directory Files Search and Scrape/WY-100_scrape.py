import os

dictionary = {}

root = (r'\\REST-SAVEIT\\Users\\TaylorR\\OLD SAVEIT2\\CNC Master File'
        r'\\ALL HARDINGE\\WY-100')
for path, subdirs, files in os.walk(root + '\\'):
    for name in files:
        directory = os.path.join(path, name)
        split = name.split('-')
        try:
            if split[1] == 'WY':
                o = open(directory, 'r', encoding='Latin-1')
                for line in o.readlines():
                    line = str(line.lower())
                    if 'm428' in line:
                        print(name)
                        break
            else:
                pass
        except IndexError:
            pass
