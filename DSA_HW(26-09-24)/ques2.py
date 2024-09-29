#2. Given a list of numbers, find the two numbers which sums to the given X. 
# input 
# list = [1,2,3,4,5] (non-duplicate)
# X = 5
# output = [[1,4], [2,3]]

list = [1, 2, 3, 4, 5]
X = 5
def func(list, X):
    pairs = []
    present = {}  # Dictionary to store the difference(j) as the key    
    for i in list:                  #time complexity O(n)
        j= X - i
        if j in present:
            pairs.append([j, i])
        present[i] = True   
    return pairs

output = func(list, X)
print(output)
