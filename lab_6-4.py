#author: RED 11/8/22

#creating list

subjects= ["gov", "theology", "programming"]

#adding to end

subjects.append("english")
print(subjects)

#finding the index
iluv= subjects.index("english")

#sorting by alphabet
subjects.sort()

#making copy
prep = subjects.copy()
#reversing
prep.reverse()
#printing
print(iluv)
print(prep)
print(subjects)