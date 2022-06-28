# ask the user for their name
name = input("what is your name? ")
# remove white spaces from the string
name = name.strip() 
# print hello
print(f"Hello,", name,"!")
print("Where have you been",end=" ")
print(name,"?")
# using " in a text in the print command
print("May I call you \"friend\"",name,"?")
num1=input("Enter first number: ")
num2=input("Enter second number: ")
sum=float(num1)+float(num2)
print("The sum of",num1, "and", num2,"is",sum)
