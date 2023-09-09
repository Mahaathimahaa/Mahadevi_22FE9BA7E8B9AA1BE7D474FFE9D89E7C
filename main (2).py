num=int(input("Enter a Number:"))
fact=1
if num<0:
  print("Negative Number")
elif num==0:
  print("The factorial of a given number 0 is 1")
else:
  for i in range(1,num+1):
   fact=fact*i
print(fact)