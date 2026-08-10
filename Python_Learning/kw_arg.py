# **kwargs - Variable length keyword argument

def func(**kwargs):
    print(kwargs, type(kwargs))


func(x=10, y=20)


def student_details(sid, sname, *extras, **marks):
    if marks == 0:
        print(f"{sname} did not attend the exam")
    else:
        percent = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} secured {percent}% with extra-curriculum activity {extras}")


student_details(101, "Zishan", 'football', s1=80, s2=75.5, s4=55)
student_details(102, "Kelvin", 'cricket', 'basketball', s2=76, s3=84, s1=70, s4=55)
