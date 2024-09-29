numbers=[]
for i in range(10):
	num=float(input(f"Enter number {i+1}: "))
	numbers.append(num)

smallest=numbers[0]
for num in numbers[1:] :
	if (num<smallest):
	   smallest=num
print("The smallest number is : ",smallest)





userStr= input("Enter a string: ")
reversedStr=""
for char in userStr:
	reversedStr= char + reversedStr

print(" the reversed string is: ", reversedStr )





employees={}
while True:
	name=input("enter emplyeee name or say no to stop ")
	if name.lower()=="no":
		break

	age=int(input(f"enter {name} age : ")
	emplyees[name]=age
	print( emplyee data:)

for name,age in emplyees.items()
	print(f" the emplyee name is : {name} and the age is {age}")



totalD=int(input("enter the number of the days : ")
weeks= totalD//7
days=totalD%7

print(f"{totalD} dayes is = {weeks} weeks and {days} day")


