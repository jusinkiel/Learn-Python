length = int(input("Length Triangle: "))  

max_number = 1

for row in range (0, length):  
    # print("Change the line", row)
    for col in range (0, max_number):
        print('x', end=' ')
        # print("Print the star", col)

    max_number = max_number + 1 # Python will increase every column & row
    # print("Max Number", max_number)


    print ('')