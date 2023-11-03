tmp_input = input("Type your number : ")
tmp_input_m = tmp_input.split(',')
nm1 = int(tmp_input_m[0])
nm2 = int(tmp_input_m[1])
nm3 = int(tmp_input_m[2])

if (nm1 > nm2 and nm1 > nm3):
    print (tmp_input_m[0] + "is bigger")

elif (nm2 > nm1 and nm2 > nm3):
    print (tmp_input_m[1] + "is bigger")

elif (nm3 > nm1 and nm3 > nm2):
    print (tmp_input_m[2] + "is bigger")

elif (nm3 == nm1 and nm3 > nm2):
    print (tmp_input_m[2] + "is bigger")

elif (nm3 == nm2 and nm3 > nm1):
    print (tmp_input_m[2] + "is bigger")

elif (nm2 == nm1 and nm2 > nm3):
    print (tmp_input_m[1] + "is bigger")

else:
    print("They are all the same")