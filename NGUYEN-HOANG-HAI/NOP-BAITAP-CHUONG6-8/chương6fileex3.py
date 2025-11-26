name = input("Enter the file name: ") 
if name == "na na boo boo": 
    print("NA NA BOO BOO TO YOU - You have been punk'd!") 
    quit() 
try: 
    fhand = open(name) 
except: 
    print("File cannot be opened:", name) 
    quit() 
count = 0 
for line in fhand: 
    if line.startswith("Subject:"): 
        count += 1 
    print("There were", count, "subject lines in", name)