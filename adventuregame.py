name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swin accross: ")
    if answer == "swim":
        print("You swam acrross and were eaten by alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid answer. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    if answer == "back":
            print("You go back and lose.")
    elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

            if answer == "yes":
                print("You talked to the stranger and they give you gold. You win!")
            elif answer == "no":
                print("You ignored the stranger and they were offended and you lose.")
            else:
                print("Not a valid answer. You lose.")
    else:
            print("Not a valid answer. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for trying {name}")
