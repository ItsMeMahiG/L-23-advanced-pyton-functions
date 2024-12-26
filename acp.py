num= int(input("under which value do you want your odd and even numbers? : "))
ol=[i for i in range (num)if i%2!=0]
print("list of odd numbers:", ol,"\n")
el=[i for i in range (num)if i%2==0]
print("list of even numbers:", el,"\n")


fruits=['apple', 'banana', 'coconut','dragonfruit','elderberry']
Fruits=[x[0].upper()+x[1:] for x in fruits]
print(("fruits as proper nouns :",Fruits))