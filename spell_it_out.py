def say_hi(name):
    if name == '':
        print("Yo wheres the input??")
    else:
        print("Hi there...")
        for letter in name:
            print(letter)


name = input("Your name: ")
say_hi(name)
