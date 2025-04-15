print("Welcome motherfucker")

    #Strings
Name = "Rojer"
#Intergers
Age = 20
#Booleans
isStudent = True
isFEMALE = False
#LISTS
myWives = ["Sophia", "Vivian", "Mary"]

#dictionary
Student ={
    "name": "Rojer",
    "age": 20,
    "isStudent": True,
    "isFEMALE": False,
    "myWives": ["Sophia", "Vivian", "Mary"]
}
print (Student["name"])
print(f"This motherfucker is called {Student['name']} with {Student['age']} years")

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
is_student = input("Is the student currently enrolled? (yes/no): ").strip().lower() == "yes"
is_female = input("Is the student female? (yes/no): ").strip().lower() == "yes"
my_wives = input("Enter the student's wives (comma-separated): ").split(",")
#Collecting user data 
Student ={
    "name": name,
    "age": age,
    "isStudent": is_student,
    "myWives": [wife.strip() for wife in my_wives]
}
print (f"Student details: {Student}")
for keyword,response in Student.items():
    print (keyword)
