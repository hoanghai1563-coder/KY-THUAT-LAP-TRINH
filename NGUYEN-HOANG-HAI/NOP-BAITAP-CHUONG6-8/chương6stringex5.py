str = 'X-DSPAM-Confidence:0.8475' 
a= str.find('0') 
print(a) 
b= str[a:None] 
print(b) 
C=float(b) 
print(C)