#1
market = ["yam", "tomato", "onion"]
market.append("fish")
print(market)

#2
grades = [80, 90, 70]
grades.insert(1, 85)
print(grades)

#3
gadgets = ["laptop", "phone", "tablet", "phone"]
gadgets.remove("phone")
print(gadgets)

#4
colors = ["red", "blue", "green"]
colors.clear()
print(colors)

#5
Votes = ["Yes", "No", "Yes", "Yes", "No"]
print(Votes.count("Yes"))
print(Votes)

#6
alphabets = ["a", "b", "c", "d","e", "f"]
alphabets = alphabets[2:5]
print(alphabets)

#7
students = ["Kofi", "Ama", "yaw"]
print(students[::-1])

#8
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)

#9
City = ["Accra", "Kumasi", "Tamale"]
removed_city = City.pop(2)
print(removed_city)
print(City)

#10
list_items = ["Pen", "Ruler", "Eraser"]
print(list_items[1])

# #Section 2
# #1
# student_info = ("Araba", 20)
# student_info[1] = 21


#2
tup = (1, 2, 3)
temp = list(tup)
temp.append(4)
tup = tuple(temp)
print(tup)

#3
Given_data = (10, 20, 10, 30,10)
print(Given_data.count(10))

#4
tuple_colors = ("red", "blue", "green",)
print(tuple_colors[1])

#5
tuple_coords = (5.6, -0.1)
lat, lon = tuple_coords
print("Latitude:", lat)
print("Longitude:", lon)

#6
nest = [(5,10)]
print(len(nest))

#7
Given_number = (10, 20, 30, 40, 50)
print(Given_number[-2:])

#8
my_list = [1, 2]
my_list_b = [3, 4]
my_list.extend(my_list_b)
print(my_list)

#9
#my_tup = (1, 2, 3)
#del my_tup()

#10
variable_x = (5)
variable_y = (5,)
print(type(variable_x))
print(type(variable_y))
