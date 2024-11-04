#Use Lambda with map() to Convert Celsius to Fahrenheit
#Given a list of temperatures in Celsius [0, 10, 20, 30, 40], use map() and a lambda 
# function to convert them to Fahrenheit using the formula: F=(C×9/5)+32

celsius=[0, 10, 20, 30, 40]
fehrenheit=list(map(lambda celsius:(celsius * 9/5)+32,celsius))
print(fehrenheit)