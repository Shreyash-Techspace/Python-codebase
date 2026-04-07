s1 = "Hello World"
"""
Syntax of Slicing : string[start:end:step]
start : Starting index at which the slicing operation starts
end : Ending index at which the slicing stops (excluded)
step : Integer that specifies the step for the slicing 
"""
print(s1[2:7:1])
"""
H e l l o   W o r l d
0 1 2 3 4 5 6 7 8 9 10

start (2): it will start from index 2 i.e l
end (7): will end at index 7 i.e o , as index 7 will excluded 
step (1): means it will traverse the string by 1 step 
"""
print(s1[2:9:2])
print(s1[3:10:4])
print(s1[1:12:3])

# another way for slicing
s1_slice = s1[2:9:2]
print(s1_slice)
print(type(s1_slice))
