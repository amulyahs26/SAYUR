#Top Scorers:Given a dictionary of students with their scores, write a lambda function 
# to extract students who scored above 80:{'Alice': 85, 'Bob': 70, 'Charlie': 95}

students = {'Alice': 85, 'Bob': 70, 'Charlie': 95}
top_scorers = dict(filter(lambda item: item[1] > 80, students.items()))

print(top_scorers)