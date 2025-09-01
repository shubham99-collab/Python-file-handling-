# >>File Handling
# Opening a file by using open function.
# f=open("Test.txt","r")
# myfile=f.read()
# print(myfile)
# f.close()

# You can also specify how many characters
# You want to print
# f=open("Test.txt","r")
# myfile=f.read(5)
# print(myfile)
# f.close()

# If you want to read line by line then you can use it.
# f=open("Test2.txt","r")
# print(f.readline())  #Only Line1 will show
# # You can use many time
# f.close()   

# IF YOU WANT TO READ THE WHOLE FILE, LINE BY LINE.
# f=open("Test2.txt","r")
# for x in f:
#     print(x)

# f=open("demofile1.txt","x")

# f=open("demofile1.txt","w")
# f.write("Good Vibes!")
# f.close()

# f=open("demofile1.txt","a")
# f.write("\n Be healthy and wise.")
# f.close()

# The other way to open & close the file
# is the with statement. If you are use
# with statement. you don't need to close
# file.
# with open('Test2.txt','r') as f:
#     a = f.read()
#     print(a)

# Rename & Delete python files.
# import os
# old_file_name = "demofile1.txt"
# new_file_name = "demofile2.txt"
# with open(old_file_name) as f:
#     data = f.read()

# with open(new_file_name, "w") as f:
#     f.write(data)

# os.remove(old_file_name)
