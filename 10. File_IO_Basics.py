import os
proj_path = os.path.abspath("./")

readfile = open(proj_path+'/resources/testfile.txt', 'r') #open in read mode 
print(readfile.readable())

# print(readfile.readline()) #read a single line

# print(readfile.readlines()[0]) #read a line at a purticular position starting from the current head

# print(readfile.readlines()) #read all Lines into a list

for lines in readfile.readlines():
    print(lines, end="") #end="" will print "" at the end of each line instead of default "\n"
readfile.close()

writefile = open(proj_path+'/resources/newfile.txt', 'w') #open in write mode , willl create a new file
writefile.write('New\nFile\n')
writefile.close()

appendFile = open(proj_path+'/resources/newfile.txt', 'a') #open in append mode
appendFile.write('Appended\nText\n')
appendFile.close()

