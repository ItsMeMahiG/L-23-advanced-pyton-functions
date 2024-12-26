num1=[1,2,3,4,5]
num2=[6,7,8,9,10]
result=map(lambda x,y:x+y, num1, num2)
print("addition of 2 lists : ")
print(list(result))

nums=[1,2,3,4,5]
def sq(m):
    return m*m
squ=list (map(sq, nums))
print("square if numbers in list : ")
print(squ)