motep= open('mbox-short.txt')
lines=[]
count= 0
for line in motep:
    if line.startswith('From '):
        line= line.strip()
        word= line.split()
        lines.append(word)
        count= count +1
for i in lines:
    print(i[1])
print ('There are ', count,'lines in the file with From as the first word')


