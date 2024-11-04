#condition based lambda function
#in this case if condition is true then it prints true otherwise false
even_number=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x: x % 2 ==0 , even_number))

print(result)
#using filter
even_number=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x: x % 2 ==0 , even_number))

print(result)