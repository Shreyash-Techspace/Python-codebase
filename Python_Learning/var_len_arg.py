# *arg = variable length positional arguments (0 to n)

def add(*numbers):
    return sum(numbers)


result = add(10, 2, 30, 4, 50, 6, 70, 8, 90)
print(result)


def student_details(sid, sname, *marks):
    percentage = sum(marks) / len(marks)
    print(f"{sname} with id {sid} secured {percentage}%")


student_details(10, "Shreyash", 30, 40, 50, 60, 70, 80, 90)
student_details(11, "Karan", 60, 64, 70, 40, 30)
