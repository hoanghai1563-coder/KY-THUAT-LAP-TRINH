hours = float(input('Enter hours:'))
rate = float(input('Enter rate:'))
pay= hours*rate 
pay2= 40*rate+(hours-40)*1.5*10 
print( 'Enter hours:',hours) 
print(' Enter rate:',rate) 
if hours>40: 
    print('pay:', pay2) 
else: 
    print('Pay:',pay)