# * * * * * 
# * *   * * 
# *   *   * 
# * *   * * 
# * * * * *
length = int(input("Length Rectangle : "))

# for row in range(0, length):
#     for col in range(0, length):
#         print('*', end=' ')

#     # Change the line
#     print('')


for row in range(0, length):
    for col in range(0, length):
        if row == 0 or col == 0 or row == length - 1 or col == length -1:
            print('*', end=' ')
        elif col == row:
            print ('*', end=' ')
        elif row == length - 1 - col:
            print  ('*', end=' ')
        else:
            print(' ', end=' ')
            
    print('')