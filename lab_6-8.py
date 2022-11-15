#author: RED 11/10/22
# setting variables
l1= int(input("number"))
l2= int(input("number"))
l3= int(input("number"))

numbers = [l1, l2, l3] # Put them in a list

# Check if they are odd or even using modulus 2
if l1 % 2 == 0 and l2 % 2 == 0 and l3 % 2 == 0: # This would be a great place for a loop
    print('even')
elif l1 % 2 == 1 and l2 % 2 == 1 and l3 % 2 == 1:
    print('odd')
else: # If they aren't all even or odd they must be mixed
    print('mixed')