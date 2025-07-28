#EMI Calculator
P=int(input("Enter Principal Amount:"))
rate=float(input('Enter rate of interest:'))
r=rate/12/100
n=float(input("Enter number of months:"))
A=(1+r)**n
EMI=(P*r*A)/(A-1)
print('The total EMI is:', EMI)