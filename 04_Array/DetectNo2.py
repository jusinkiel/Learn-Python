tmp_input = input("Type your number : ")
tmp_input_m = tmp_input.split(',')
nm1 = int(tmp_input_m[0])
nm2 = int(tmp_input_m[1])
nm3 = int(tmp_input_m[2])

if nm1 == nm2 and nm1 == nm3 and nm2 == nm3:
    print("All is same")
    exit()

max_number = 0

if nm1 > max_number:
    max_number = nm1

if nm2 > max_number: 
    max_number = nm2

if nm3 > max_number:
    max_number = nm3

print(str(max_number) + ' is the biggest')