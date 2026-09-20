# from turtle import Turtle, Screen #Turtle is a class and we are importing it from turtle module

# timmy = Turtle()  #turtle is an object of class Turtle
# timmy.shape("turtle") #shape is a method of Turtle class and it associated with object timmy
# timmy.color("coral") #color is a method of Turtle class and it associated with
# timmy.left(90) #left is a method of Turtle class and it associated with object timmy
# timmy.forward(100) #forward is a method of Turtle class and it associated with object
# print(timmy)
# my_screen = Screen() #Screen is a class and we are creating an object of it my_screen
# print(my_screen.canvheight)#canvheight is an attribute of Screen class and it associated with object my_screen

# print(my_screen.title("My Screen")) #title is a method of Screen class and it associated with object my_screen
# my_screen.exitonclick() #exitonclick is a method of Screen class and it associated with object my_screen


import prettytable  #is a module which is used to create a table in python, install using : pip install prettytable in cmd
# table = prettytable.PrettyTable()
# # table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander","Nabin"])
# # table.add_column("Type", ["Electric", "Water", "Fire", "Human"])
# print(table)
country = prettytable.PrettyTable()
country.add_column("Country Name", ["Nepal", "India", "China", "USA "])
country.add_column("Country Code", ["NP", "IN", "CN", "US"])
country.add_column("Country Population", ["30 Million", "1.4 Billion", "1.4 Billion", "330 Million"])
country.add_column("Country Capital", ["Kathmandu", "New Delhi", "Beijing", "Washington D.C."])
country.border = True
country.align = "c"
country.add_row(["Bhutan", "BT", "700 Thousand","London"])
print(country)
