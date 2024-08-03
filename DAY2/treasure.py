'''FInd the treasure, count treasure. 
Given a matric as inout, find the treasure (1) and count the treasure, 
0 0 1
1 0 1
'''
matric = [
    [0, 0, 1],
    [1, 0, 1]
]

def find_treasure(matric):
    for row in matric:
        for item in row:
            if item==1:
                print("Treasure is found!!")
                return True
    print("Treasure is not found!!")
    return False

def count_treasure(matric):
    count=0
    for row in matric:
        count+=row.count(1)
    return count
    
result_find=find_treasure(matric)
result_count=count_treasure(matric)
print(f"The number of treasures found {result_count}")
