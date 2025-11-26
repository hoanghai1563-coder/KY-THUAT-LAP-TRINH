name = input("Enter file name: ") 
try: 
    fhand = open(name) 
except: 
    print("ERROR:", name) 
    quit() 
count = 0 
total = 0.0 
for line in fhand: 
    line = line.rstrip() 
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue 
    pos = line.find(':') 
    value = float(line[pos+1:].strip()) 
    total += value 
    count += 1 
average = total / count 
print("Average spam confidence:", average)