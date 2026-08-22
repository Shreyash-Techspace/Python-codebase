students_detail = {"Alice": 86,
                   "Boron": 90,
                   "Carolina": 91,
                   "Denil": 99}

sname = input("Enter student name: ")

if sname in students_detail:
    print(f"{sname}'s marks: {students_detail[sname]}")
else:
    print("Student not found")
