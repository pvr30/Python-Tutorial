student_info = [
    {"Name": "Harsh", "Physics": 90, "Chemistry": 80, "Maths": 70},
    {"Name": "Sahil", "Physics": 52, "Chemistry": 60, "Maths": 75},
    {"Name": "Manthan", "Physics": 40, "Chemistry": 33, "Maths": 50},
    {"Name": "Sanjay", "Physics": 45, "Chemistry": 80, "Maths": 79},
    {"Name": "Chirag", "Physics": 100, "Chemistry": 80, "Maths": 95},
]

def display_name(student):
     name = student["Name"]
     print(name.upper(),":")

def average_marks(student):
    avg = ( student["Physics"] + student["Chemistry"] +student["Maths"] )/ 3
    print(f"Your Average Is {avg}")

def good_subject(student):
    if  (student["Physics"]>=student["Chemistry"])  and (student["Physics"]>=student["Maths"]):
        print("You Got Highest Marks In Physics.")
    elif (student["Chemistry"]>=student["Physics"]) and (student["Chemistry"]>=student["Maths"]):
        print("You Got Highest Marks In Chemistry.")
    else:
        print("You Got Highest Marks In Maths.")



for i in student_info:
    display_name(i)
    average_marks(i)
    good_subject(i)