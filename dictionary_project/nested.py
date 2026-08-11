capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Nepal": "Kathmandu",
}
print(capitals["France"])  # Output: Paris

#Nested Dictionary using List
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
    "Nepal": ["Kathmandu", "Pokhara", "Chitwan"]
}

print(travel_log["Germany"])  # Output: ['Berlin', 'Hamburg', 'Stuttgart']
print(travel_log["Nepal"][1])  # Output: Pokhara

#Nested List
nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])  # Output: D
print(nested_list[1][0])  # Output: B

#Nested Dictionary using Dictionary
nested_dict = {
    "France":{
        "Cities Visited": ["Paris", "Lille", "Dijon"],
        "Total Visits": 12
    },
    "Germany":{
        "Cities Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits": 5
    },
    "Nepal":{
        "Cities Visited": ["Kathmandu", "Pokhara", "Chitwan"],
        "Total Visits": 8
    }
}
print(nested_dict["France"]["Cities Visited"])  # Output: ['Paris', 'Lille', 'Dijon']
print(nested_dict["Germany"]["Cities Visited"][2])  # Output: 'Stuttgart'
print(nested_dict["Germany"]["Total Visits"])  # Output: 5
print(nested_dict["Nepal"]["Cities Visited"])  # Output: ['Kathmandu', 'Pokhara', 'Chitwan']
