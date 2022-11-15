#author: RED 11/4/22
#making list of names
my_row = ["Nic" , "Ethan"]
#replacing name with my name
my_row[1] = "Robbie"
#setting equal to each other
my_row2= my_row
#Printing row 2
print(my_row2)
#deleting first name
del my_row[0]
#printing
print(my_row)
#first name deletes in my row but my row 2 stays the same because the delete statement was after we set them equal to each other