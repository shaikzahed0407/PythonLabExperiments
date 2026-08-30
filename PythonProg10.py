students = [] 
n = int(input("Enter number of students: ")) 
for i in range(n): 
    print(f"\nEnter details for Student {i+1}") 
    name = input("Enter student name: ") 
    marks = float(input("Enter student marks: ")) 
    student = { 
        "name": name, 
        "marks": marks 
        }
    students.append(student) 

print("\n--- Student Records ---") 
for student in students: 
    print(f"Name: {student['name']}, Marks: {student['marks']}") 
total = sum(student['marks'] for student in students) 
average = total / n 
topper = max(students, key=lambda x: x["marks"])
lowest = min(students, key=lambda x: x["marks"])
print("\n--- Summary Report ---") 
print(f"Average Marks: {average:.2f}") 
print(f"Topper: {topper['name']} " 
      f"with {topper['marks']} marks") 
print(f"Lowest Scorer: {lowest['name']} " 
      f"with {lowest['marks']} marks")  
