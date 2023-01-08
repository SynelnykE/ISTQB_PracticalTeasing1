#returns the number of users in a chatroom based on the following rules

def chatroom_status(users_list):
    sum_user = len(users_list)
    if not users_list:
        return "no one online"
    elif sum_user == 1:
        user1 = users_list[0]
        return user1 + " online"    
    elif sum_user >= 2:
        for i in users_list:
            user1 = users_list[0]
            user2 = users_list[1]
            if sum_user == 2:
                return user1 + " and " + user2 + " online"
            elif sum_user > 2:
                return '"' + user1 + ", " + user2 + " and " + str(sum_user - 2) + " more online" + '"'

print(chatroom_status(["Ann", "Mark", "Jhon", "Joy", "Pet"]))

# chatroom_status(["Ann", "Mark", "Jhon", "Joy", "Pet"]) == "Ann, Mark and 3 more online"
