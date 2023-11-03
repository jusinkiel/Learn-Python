tmp_input = input("Type your number : ")
tmp_input_m = tmp_input.split(',')
nm = int(tmp_input_m[0])
nm2 = int(tmp_input_m[1])

if (nm > nm2):
    print (tmp_input_m[0] + " is bigger")

elif (nm2 > nm):
    print (tmp_input_m[1] + " is bigger")

else:
    print("Those are a same number")