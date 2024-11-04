students={'Alice':85,'bob':70,'charlie':95}

#find the student with the highest score
top_student=max(students.items(),key=lambda item:item[1])
print(top_student)