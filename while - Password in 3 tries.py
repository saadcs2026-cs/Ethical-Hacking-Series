password = "Codeshield"
print("Account will be freezed after 3 wrong entries")

take = 3  # Total attempts

while take > 0:
    enter = input("Enter your Password:  ")
    if enter == password:
        print("Correct Password!")
        break
    else:
        take -= 1
        if take == 0:
            print("Wrong Password! Account freezed for some time.")
        else:
            print("Incorrect Password!\n", take, "TRIES LEFT!")

input("Press Enter to exit...")
