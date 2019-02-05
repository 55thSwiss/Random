'''
format directory (single level of folders with subfiles) 
into single whitespace strings.
Just change 'src' for source directory

'''
import os

src = r'C:\Users\MacalusoC\Desktop\Technical Docs\TLC_Program_Release\Machine_Folders\EvoDECO 10'


def stringFormat(src): 
    '''
    iterate folders in directory
    '''
    # create a list of the folders in the src directory  
    folder_list = os.listdir(src)
    # iterate over the folders
    for f in folder_list:
        # split folder names
        s = f.split()
        # create an empty variable
        string = ''
        # get index iteration for the length of segments (s)
        for x in range(len(s)):
            # building the string up
            string = str(string) + (' ' + str(s[x]))
            # strip whitespace infront of folder name
            string = string.lstrip()
        # rename the folder with the new formatted name
        try:
            os.rename(src + '\\' + f, src + '\\' + string)
        except:
            print(string)
        '''
        iterate files in sub directory
        '''
        sub_dir = (src + '\\' + string)
        # create a list of files inside each folder
        file_list = os.listdir(sub_dir)
        # iterate over the files
        for f in file_list:
            # split the file names
            s = f.split()
            # empty string
            string = ''
            # index iteration for the length of segments (s)
            for x in range(len(s)):
                # build up the string
                string = str(string) + (' ' + str(s[x]))
                # strip whitespace infront of file name
                string = string.lstrip()
            # rename the file with the formatted name
            try:
                os.rename(sub_dir + '\\' + f, sub_dir + '\\' + string)
            except:
                print(string)


def main():
    stringFormat(src)

if __name__ == "__main__":
    main()