inputs = input("Input a number : ")
print(type(inputs)) # str

number = int(inputs) # weneed to convert into number (int)å

if number > 100:
    
    #  Job - 1
    print('Its big number 1')

    # Job - 2
    if number > 200:
        print('Its big number 2') # this one will be run only when number > 200

    # Job - 3
    print('Other 1')

print("Lastly")
