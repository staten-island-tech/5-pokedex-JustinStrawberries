import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# print(data[0])

for i, a in enumerate(data, start=0):
    print(i, a["name"])

language = input("Choose your Language: ")
choose = True
while choose == True:
    for i in range(809):
        if language in data[i]["name"]:
            print([language])
            choose = False
        else:
            print ("That is not viable language")
            language = input("try again: ")
            

for i, a in enumerate(data, start=0):
    print(i,a["name"][language],a["type"])

list = []
type = input("Choose your Type: ")
for i in range(809):
    if type in data[i]["type"]:
        list.append(data[i]["name"][language], data[i]["type"])
if list == []:
    print("Invalid")
print(list)
        

# cart = []




# search = input("Search up a pokemon: ")
# while True:
#     for a in data:
#         if search == a["name"]:
#             found = True
#             search = input("What other pokemon would you like to search up?: ")
#             cart.append({
#                     "name": a["name"],
#                      })
#             break
#     if found == False:
#         print ("Pokemon not found")
#         search = input("What other pokemon would you like to search up: ")



















    # Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

