#author: RED 11/7/22

#aetting list
colors = ["green", "blue", "red", "yellow"]
#extending appending and inserting

colors.extend(["orange", "purple", "brown"])
colors.append("black")
colors.insert(3, "white")

#cloning my list

v1= colors[:]

#removing

v1.remove("orange")

#printing

print(colors)
print(v1)
