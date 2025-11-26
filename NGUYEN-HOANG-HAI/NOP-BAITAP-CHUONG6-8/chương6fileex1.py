try: 
    file= input('Nhập tên tệp:') 
    file_object= open(file) 
    print (file_object.read()) 
except: 
    print(' ERROR ') 
    quit() 
for line in file: 
    line=line.rstrip() 
    print(line.upper())