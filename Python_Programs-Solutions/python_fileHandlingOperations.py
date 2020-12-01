import json
import requests #used for web scraping


#Ex-1 File create and write
# file=open("funny.txt","wt") #'wt' to write text file
# content="Hello, I am a funny file..Just Kidding!!"
# file.write(content)
# print(file.write(content)) #this prints length of the data written into file
# #now close the file
# file.close()
# print(file.closed) #this returns true or false
# 
# #Ex--2 File read
# file2=open("funny.txt","rt")
# s=file2.read()
# print(s)
# file2.close()

#Ex-3
# rel=open("../test/abc.txt","rt")
# rel.read()

#Ex-binary file
binary=open("bin.txt","wb")
binary.write(b"This is binary data") #'b' is format specifier used to write binary format data
binary.close()

bin2=open("bin.txt","rb")
bdata=bin2.read()
print(bdata)
bin2.close()

#Ex-
f3=open("funny.txt","wt")
data="flushed data"
f3.write(data)
print(f3.closed)
f3.flush() #to clear the data in file
f3.close()

#Ex-with open() function-here file closes automatically
with open("sun.txt","wt") as f:
    f.write("This is a better way to write.")

print(f.closed)

#------------------------------------------------------------------
#Ex-using json(javascript object notation) so import json module
d={"Sunanda":"Mentor",
   "Jack":"Student",
   "Iant":["Manager","Counsellor"]
   }
print(d)
#how to write json file
with open("intro.json","w") as jf:
    json.dump(d,jf)   #dump is alternative to write function
    
#now to open json file
with open("intro.json","r") as jf:
    print(json.load(jf) ) #reads the json file
    
#Web Scraping
url="https://www.google.com"
data=requests.get(url)
print(data.content)

#ex
with open("google.html","wb") as f:
    f.write(data.content)
    
img=requests.get(url)
with open("scrap.jpeg","wb") as f:
    f.write(img.content)  #if img doesnt have proper https protocol to url then error will occur