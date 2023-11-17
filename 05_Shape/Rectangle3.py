length = int(input("Length Triangle: "))  

max_number = 1

for row in range (0, length):  
    for col in range (0, max_number):
        print('x', end=' ')

    max_number = max_number + 1
    print ('')