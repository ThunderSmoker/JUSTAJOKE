file1=open("C:/Users/ARADHYA/OneDrive/Documents/VsCode/python/python_session/file_handling/data1.txt","r")
file2=open("C:/Users/ARADHYA/OneDrive/Documents/VsCode/python/python_session/file_handling/data2.txt","w")
a=file1.readlines()
for i in a:
    file2.write(i)
file1.close()
file2.close()