#author: RED 11/7/22

#aetting list
colors = ["green", "blue", "red", "yellow"]

colors.extend(["orange", "purple", "brown"])
colors.append("black")
colors.insert(3, "white")

v1= colors[:]
v1.remove("orange")
print(colors)
print(v1)
