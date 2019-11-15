#Ryan Middle
#CSCI 101 - A
#Python Lab 1B - Fibonacci

a=1 #initializing n var in fibonacci sequence
b=0 #initializing n-1 var in fibonacci sequence
c=1
n=int(input("please enter how many numbers in the Fibonacci sequence you would like to see")) #initializing step var
for i in range (1, n, 1):
	print(c)
	c=a+b #fibonacci recurrence statement
	b=a #re-initializing n-1 term
	a=c #re-initializing n term
	n=n+1 #increasing step var

print("end") #that's all, folks!



