#author:RED 11/10/22

#making list of numbers
l1= [1000, 3000, 2500, 1]
l2= sorted(l1)


if len(l1) <2:
    print("error: does not match qualifications")
elif l2[0] == l2[-1]:
    print("error: list does not meet qualifications")
else:
    print (str(l2[-1]))
    print(str(l2[0]))