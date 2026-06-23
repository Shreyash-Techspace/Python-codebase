student1 = {"English", "Maths", "CS", "Chemistry", "Physics"}
student2 = {"English", "Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}

print(student1)
print(student2)
print(student3)

# Common subjects of student1 and student2 - intersection
# SYNTAX1 >> set1,intersection(set2,set3,....)
# SYNTAX2 >> set1 & set2 & set3
common_subjects1 = student1.intersection(student2, student3)
common_subjects2 = student1 & student2 & student3
print(common_subjects1)
print(common_subjects2)

# all subjects of student1 and student2 - union
# SYNTAX1 >> set1.union(set2,set3,....)
# SYNTAX2 >> set1 | set2 | set3
all_subjects1 = student1.union(student2 | student3)
all_subjects2 = student1 | student2 | student3
print(all_subjects1)
print(all_subjects2)

# Difference of sets - difference

days = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

# SYNTAX1 >> set1.difference(set2)
# SYNTAX2 >> set1 - set2
weekdays1 = days.difference(weekends)
weekdays2 = days - weekends
print(weekdays1)
print(weekdays2)
