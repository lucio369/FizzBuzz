##push fizz if multiple of 3
##push buzz if multiple of 5
##otherwise push number


##use of comments


def fizzbuzz(number): # use of functions
    returnStatement=''
    conditions=[(number%3==0,'Fizz'),(number%5==0,'Buzz'),[-1,number]] # use of tuples and lists
    for cond in conditions: #for loops
        if cond[0]==True: #use of tuples with conditions (as instructions)
            returnStatement=returnStatement+cond[1] #concatenation
        elif cond[0]==-1:
            if returnStatement=='':
                returnStatement=str(number) #assigning a value
    return returnStatement

for i in range(1,101):
    print(fizzbuzz(i)) # iterative function calls

