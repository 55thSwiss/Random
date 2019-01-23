import os
import json

G76_dict = {}

def swiss_G76():
        root = r'\\REST-SAVEIT\\Users\\TaylorR\\OLD SAVEIT2\\CNC Master File\\ALL SWISS MACHINES\\'
        for path, subdirs, files in os.walk(root + '\\'):
                for name in files:
                        directory = os.path.join(path, name)
                        new_name = (name + '_block_1')
                        if not directory.lower().endswith('.pdf'):
                                if not directory.lower().endswith('.doc'):
                                        if not directory.lower().endswith('.part'):
                                                if not directory.lower().endswith('.ppt'):
                                                        if not directory.lower().endswith('.dbp'):
                                                                if not directory.lower().endswith('.back'):
                                                                        if not directory.lower().endswith('.cpd'):
                                                                                if not directory.lower().endswith('.trf'):
                                                                                        if not directory.lower().endswith('.db'):
                                                                                                o = open(directory, 'r', encoding='Latin-1')
                                                                                                s = os.path.split(directory)
                                                                                                a = s[1]
                                                                                                b = s[0]
                                                                                                s = os.path.split(b)
                                                                                                c = s[1] 
                                                                                                b = s[0]
                                                                                                s = os.path.split(b)
                                                                                                e = s[1]
                                                                                                b = s[0]
                                                                                                print(a + '\n' + c + '\n' + e + '\n\n')
                                                                                                for line in o.readlines():
                                                                                                        line = str(line.lower())
                                                                                                        line = line.strip().lower()
                                                                                                        if 'g76' in line:
                                                                                                                if new_name in G76_dict:
                                                                                                                        G76_dict.update({name + '_block_2' : [line, c, e]})
                                                                                                                else:
                                                                                                                        G76_dict.update({new_name : [line, c, e]})


def lathe_G76():
        root = r'\\REST-SAVEIT\\Users\\TaylorR\\OLD SAVEIT2\\CNC Master File\ALL HARDINGE\\'
        for path, subdirs, files in os.walk(root + '\\'):
                for name in files:
                        directory = os.path.join(path, name)
                        new_name = (name + '_block_1')
                        if not directory.lower().endswith('.pdf'):
                                if not directory.lower().endswith('.doc'):
                                        if not directory.lower().endswith('.part'):
                                                if not directory.lower().endswith('.ppt'):
                                                        if not directory.lower().endswith('.dbp'):
                                                                if not directory.lower().endswith('.back'):
                                                                        if not directory.lower().endswith('.cpd'):
                                                                                if not directory.lower().endswith('.trf'):
                                                                                        if not directory.lower().endswith('.db'):
                                                                                                o = open(directory, 'r', encoding='Latin-1')
                                                                                                s = os.path.split(directory)
                                                                                                a = s[1]
                                                                                                b = s[0]
                                                                                                s = os.path.split(b)
                                                                                                c = s[1] 
                                                                                                b = s[0]
                                                                                                s = os.path.split(b)
                                                                                                e = s[1]
                                                                                                b = s[0]
                                                                                                print(a + '\n' + c + '\n' + e + '\n\n')
                                                                                                for line in o.readlines():
                                                                                                        line = str(line.lower())
                                                                                                        line = line.strip().lower()
                                                                                                        if 'g76' in line:
                                                                                                                if new_name in G76_dict:
                                                                                                                        G76_dict.update({name + '_block_2' : [line, c, e]})
                                                                                                                else:
                                                                                                                        G76_dict.update({new_name : [line, c, e]})

def write_dict():
        myfile = 'file.csv'
        with open(myfile, 'w') as f:
                for key, value in G76_dict.items():
                        f.write('%s, %s\n' % (key, value))

def main():
        swiss_G76()
        lathe_G76()
        write_dict()

if __name__ == "__main__":
	main()
