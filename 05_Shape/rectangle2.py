length = int(input("Length Rectangle: "))  

for row in range(0,length):
    for col in range(0, length):
        if (row + col) % 2 == 0:
            print('-', end=' ')
        else:
            print('|', end=' ')
        # if row % 2 == 0 and col % 2 == 0:
        #     print ('-', end=' ')
        # elif row % 2 == 0 and col % 2 == 1 :
        #     print ('|', end=' ') 
        # elif row % 2 == 1 and col % 2 == 0:
        #     print ('|', end=' ')   
        # elif row % 2 == 1 and col % 2 == 1: 
        #     print ('-', end=' ')
        #print ('-', end='|')
        
    print ('')
