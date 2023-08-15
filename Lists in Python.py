my_marks = []
marks_count = int(input("Enter Total Number of Marks"))
for i in range (0,marks_count):
    mark = float(input(f"Enter mark{i*1} :"))
    my_marks.append(mark)
average = sum(my_marks) / len(my_marks)
print(my_marks)
print(average)
print("Max Mark = ",max(my_marks))
print("Min Mark = ",min(my_marks))



