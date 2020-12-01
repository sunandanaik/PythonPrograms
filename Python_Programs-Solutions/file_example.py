#Ex-1 File create and write
# file=open("NewPython.txt","wt") #'wt' to write text file
# data="This is my new text file created today."
# file.write(data)
# file.close()
# print("File finished writing and now closed")

#Ex-1 to read the file
# file2=open("NewPython.txt","rt") #"rt" to read text file
# info=file2.read()
# print(info)
# file2.close()

#Ex-3 to create and write binary file
# binary=open("bintest.txt","wb") #'wb' means write to binary file
# binary.write(b"This is binary data our new testing file created today..hello good evening") #'b' is format specifier used to write binary format data
# binary.close()

#Ex-4 to read binary data file
# bin2=open("bintest.txt","rb") #'rb' means read binary file
# bdata=bin2.read(15) #count of data into ur file
# print(bdata)
# bin2.close()

#Ex-5
# f = open("NewPython.txt",'r')
# r1=f.read(4)    # read the first 4 data
# r2=f.read(4)    # read the next 4 data
# print(r1)
# print(r2)
# print(f.read())    # read in the rest till end of file
# print(f.read())  # further reading returns empty sting
# print(f.tell())    # get the current file position
# print(f.seek(0))   # bring file cursor to initial position

#Ex-6-Using for loop reading the file
# f = open("NewPython.txt",'r')
# for i in f:
#     print(i)
    
#Ex-7
f = open("NewPython.txt",'r')
print(f.readlines())
f.close()

#Ex-8->with open() used when you want file to be closed automatically
with open("testing1.txt","wt") as f:
    f.write("This is my new testing file")
    f.write("\nHello everyone")
    f.write("\nGood evening")
    
#Ex-9
with open("testing1.txt","rt") as f1:
    print(f1.readline())
    
#Ex-10 using for loop reading the file data
with open("testing1.txt","rt") as f2:
    for i in f2:
        print(i)
