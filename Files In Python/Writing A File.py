user_name = input("Enter Your Name: ")

write_file = open("demo.txt", 'w')

write_file.write(user_name)

write_file.close()