# This is How we run the your.txt file in python

#Readin the File
f=  open("test.txt","r")
text = f.read()
print(text)
f.close()

#Writting the File
g= open("test2.txt","w")
g.write("This is what I write using the Function")
g.close()

#Appen the files
h= open("append.txt","a")
h.write("Hey, how are You doing?")
h.close()
#In Append as many times i run the code it rewrite the sentence 
