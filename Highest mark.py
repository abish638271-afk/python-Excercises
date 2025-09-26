n=int(input("How many students :"))

students={}

for i in range(n):
    name=input("Enter the name: ")
    mark=int(input("Enter the mark: "))
    students [name]=mark
print(" Dictionary",students)

highest_mark = max(students.values())

print("\nStudents with highest mark:")
for name, mark in students.items():
    if mark == highest_mark:
        print(f"{name} - {mark}")
