import sys, os
import chardet 
from pathlib import Path

def Path1():
    
    path = r"F:"
    #path = r"D:\Torrents_Movies\Torrenti\Better.Call.Saul.Season.6"

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

            rawdata = open(file, 'rb').read() # detects which encoding text format is in the file
            result = chardet.detect(rawdata)
            charenc = result['encoding']
            
            input = open(file, "r", encoding=charenc) # puts the right encoding format // It fixed the error <-- UnicodeEncodeError: 'charmap' codec can't encode character '\u?' in position ?: character maps to <undefined>
            print(f"{file}\t(encoding = {charenc})")

            data = input.read()
            for r in (strange_char):
                data=data.replace(*r) # *r loops and replace every non-english alphabetical letters
            input.close()
            output=open(file,'w')
            output.write(data)
            output= open(file, "r")

            
    print(f"\nDone - Characters replaced successfully!")

Path1()



# __________________IMPORTANT____________________#
# Error: UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc6 in position 0: invalid continuation byte -> Shows up because of different encoding fomats like: utf8, ANSI, ISO-8859-1, utf16 etc.