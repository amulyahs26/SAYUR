'''Count words in a dictionary'''

words=["apple","bag","cat","sun","moon","sun","bag","sun"]
keyword=input("enter the word you want to find:")

def find(words,keyword):
    count=0
    for i in words:
       # count+=1
       if i==keyword:
           count+=1
    return count

result=find(words,keyword)
print(result)
