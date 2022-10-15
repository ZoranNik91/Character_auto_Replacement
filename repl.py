path = r"C:\Users\ZOHAN\Documents\VS_Code_Projects\Titlovi\1.srt"
#input = open(path, "rt")

myFile = open(path, "r", encoding="utf8")
new_content = myFile.read()
new_content=new_content.replace('æ','c')
myFile.close()
myFile3=open(path,'w')
myFile3.write(new_content)
myFile3= open(path, "r")
print(myFile3.read())



""" output = open("2.txt", "wt")

for line in input:
    print(line)
    output.write(line.replace("æ", "c"))

input.close()
output.close() """

''' myFile = open("myFile1.txt", "r")

new_content = myFile.read()

new_content=new_content.replace('content','information')

myFile.close()

myFile3=open('myFile1.txt','w')

myFile3.write(new_content)

myFile3= open("myFile1.txt", "r")

print(myFile3.read())'''