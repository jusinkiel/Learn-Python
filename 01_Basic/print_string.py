names = ["Malvin", "Kiel", "David"]
ages = [25, 17, 20]

# Malvin - 25
# Kiel - 17

for name in names:
    print(name, end = ' ')

for index, name in enumerate(names):
    # print(str(index) + " - " + name + " - " + str(ages[index]))
    # print("{}. {} - {}".format(index, name, ages[index])) 
    print("{seq}. {user_name} - {user_age}".format(
        seq = index, 
        user_name = name, 
        user_age = ages[index]
    )) 