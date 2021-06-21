friends = input("Enter Your Friends Name (Put ',' between two names only) : ").split(',')

people = open("friend.txt", 'r')

near_by_friends = [line.strip() for line in people.readlines()]

people.close()


friend_set = set(friends)
near_by_friends_set = set(near_by_friends)

real_friend_set = friend_set.intersection(near_by_friends_set)

real_friends = open("nearby friends.txt", 'w')

for friend in real_friend_set:
    print(f"{friend} is My Real Friend.")
    real_friends.write(f"{friend}\n")

real_friends.close()