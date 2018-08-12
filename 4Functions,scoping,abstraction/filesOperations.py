# creates a file for writing and returns a file handle
fileHandle=open('filename.txt','w')
fileHandle.close()

#opens an existing file for reading and returns a file handle
fileHandle=open('filename.txt','r')
fileHandle.close()

#opens an existing file for appending and returns a file handle
fileHandle=open('filename.txt','a')

#write the string to the end of the file associated with the fileHandle
fileHandle.write('test if append')
fileHandle.close()

#write each element of string as a seprate line to the file
fileHandle=open('filename.txt','w')
#fileHandle.writeLines('write each','element of','string as','seprate line')
fileHandle.close()

#returns a string containing the contents of the file associated with the fileHandle
fileHandle=open('filename.txt','r')
print(fileHandle.read())
fileHandle.close()
#
#print(fileHandle.readLines())
