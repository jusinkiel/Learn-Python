def menu():
    print("Choose Menu")
    print("1. Rectangle 1")
    print("2. Rectangle 2")
    print("3. Triangle")

    choosen_menu = input("Menu : ")

    if choosen_menu == 3: 
        length = input("Length : ")
        print(length)


    # Outside If Section
    print(length)


    return choosen_menu


choosen = menu()
print("Choosen ", choosen) 


# print("Choosen Menu ", choosen_menu) Local V