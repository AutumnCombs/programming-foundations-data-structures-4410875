#dictionaries are built from lists

# Key: State
# Value: Capital

states_to_capitals = {
    "Texas" : "Austin",
    "New York" : "Albany"
}

print(states_to_capitals["New York"])

#items allows you to see both at the same time
for key, value in states_to_capitals.items():
    print(key + " | " + value)
    