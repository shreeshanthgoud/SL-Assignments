list= input("Enter the  numbers").split()
list= [int(i) for i in list]

large = list[0]  

for i in list:
  if i > large:
    large= i

print("The largest number is:", large)