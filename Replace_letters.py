import sys, os
from pathlib import Path

""" z = input("Input path: ")
print(z)
print("______________________________") """

def Path1():
    
    #path = str(z)
    path =r"F:"

    #permission = 'chown -R ZOHAN ' #  1. 'chmod -R 777 ' 2. 'chown -R ZOHAN '

    #Non-english alphabetical characters stored in variable 'strange_char' and there replacement
    strange_char = ('č','c'), ('ć','c'), ('Č','C'), ('Ć','C'), ('Ž','Z'), ('ž','z'), ('Đ','Dj'), ('đ','dj'), ('š','s'), ('Š','S'), ('æ','c'), ('ð','dj'), ('Æ','C'), ('É','C'), ('é','c'), ('È','C'), ('è','c'), ('ä','a'), ('ü','u'), ('ë','e'), ('ï','i'), ('ö','o'), ('Ä','A'), ('Ë','E'), ('Ï','I'), ('Ö','O'), ('Ü','U')
    srt_files = []
    for (path, folders, files) in os.walk(path): # get every single file path from folder 'test'
        filePaths = [
            os.path.join(path, file)
            for file in files
        ]

        srt_files.extend(filePaths) # saves all file paths to 'srt_files'

    for file in srt_files:
        if file.endswith(".srt"):
            input = open(file, "r", encoding="ISO-8859-1" and "utf8") # try ="utf8" or ="ISO-8859-1" <-- UnicodeEncodeError: 'charmap' codec can't encode character '\u?' in position ?: character maps to <undefined>
            print(file)

            data = input.read()
            for r in (strange_char):
                data=data.replace(*r) # *r loops and replace every non-english alphabetical letters
            input.close()
            output=open(file,'w')
            output.write(data)
            output= open(file, "r")

Path1()

""" if len(sys.argv) == 1:
            path = r"C:\Users\ZOHAN\Documents\VS_Code_Projects\Titlovi\test"
            # path = r"D:\Torrents_Movies\Torrenti\Better.Call.Saul.Season.6"
	        # path =r"F:"
    else:
        #try:
        path = sys.argv[1]
        print(path)
     except Exception:
        print("Error: Invalid or incorrect path!")"""

""" print(all_srt_files)
print(len(all_srt_files))
for i in all_srt_files:
    print(i)
 """

"""  infiles = path + file
    print("started Conversion: " + infiles)
    with open(infiles, 'r') as infiles:
        filedata = infiles.read()
        freq = 0
        freq = filedata.count(lett1)
    destination = path + file
    filedata = filedata.replace(lett1.lett2)
    with open(destination, 'w+') as file:
        file.write(filedata)
    print ('Total %d Replaced' %freq) """

# __________________IMPORTANT____________________#
# Error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc6 in position 0: invalid continuation byte -> [ Because there is � broken char in file ] or someting else