# write your code here
import math
import random

total_friends = int(input("Enter the number of friends joining (including you):\n"))
print()
friend_list = {}

if total_friends <= 0:
    print("No one is joining for the party\n")
else:
    print("Enter the name of every friend (including you), each on a new line:\n")
    # adds the list of friends with 0 dollars each
    for friend in range(0, total_friends):
        name = input()
        friend_list[name] = 0

    total_bill = int(input("Enter the total bill value:\n"))

    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_feature == "Yes":
        lucky_person = random.choice(list(friend_list.keys()))
        print(lucky_person + " is the lucky one!\n")
        for friend in friend_list:
            if friend == lucky_person:
                continue
            friend_list[friend] = round(total_bill / (total_friends - 1), 2)
    elif lucky_feature == "No":
        print("No one is going to be lucky\n")
        for friend in friend_list:
            friend_list[friend] = round(total_bill / total_friends, 2)
    print(friend_list)
