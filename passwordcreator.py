import random
#Welcome, this is an example python project for my Cybersecurity portfolio, where I'll display some core pytyhon skills.
print("Welcome to Password Creator! Let's make a password that is 8-64 characters and up to NIST framework standards.")
#Collect user inputs for password characterization
def pas():
    password_length = input("How many charcters would you like password to be?: ")
    o= int()
    for o in range(len(password_length)):
        if password_length[o].isalpha():
            print ("Must be number. Try again.")
            pas ()
        o = o+1
    while int(password_length) >= 8 and int(password_length) <= 64:
        b = input("Enter 4 characters which are easily rememberable and recognizable for you: ")
        blen = int(len(b))
        cat = int()
#create password
        while blen == 4:
            x = 0
            cats= str("")
            for x in range(int(password_length) - 5):
                cat = int(random.uniform(0,9))
                catstr = str(cat)
                cats = catstr + cats
                x = x + 1
            
            password = b[0].upper() + b [1:4] + cats + "!"
            break
        else:
            print("4 characters please. Try again.")
            pas()
        break
    else:
        print("Password length must be between 8 and 64. Try again.")
        pas ()
#Display password
    print ("Your new password is: " + password)

pas()


