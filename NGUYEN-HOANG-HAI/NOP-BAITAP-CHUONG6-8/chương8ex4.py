motep=open('romeo.txt')
words = []            
for line in motep:       
    line_words = line.split()   
    for i in line_words:
        if i not in words:     
            words.append(i)     
words.sort()          
print(words)