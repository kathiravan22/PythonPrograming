a=int(input("enter a number");
temp=a
rev=0
while(a<=1000):
  b=a%10
  rev=rev*10+b
  a=a//10
if(temp==rev):
  print("its a palindrome")
else:
  print("its not a palindrome")
