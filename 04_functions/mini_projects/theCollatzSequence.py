#Function Definition that performs the Collatz sequence
def collatz(number):
    if (number % 2) == 0:
        print(number//2)
        return(number//2)
    elif (number % 2) != 0:
        print (3*number+1)
        return(3*number+1)

#Beginning of program, asks for user input
print('Type any whole number below. press enter when ready')

#Stores user input in n, prints error if input is not a natural number
try:
    n = int(input())
except ValueError:
    print('Error:Invalid argument')


#Collatz sequence is repeatedly called upon until it returns 1
while n != 1:
    n = collatz(n)
    
