import requests

URL = "http://api.open-notify.org/astros.json"

WEB = "https://swapi.co/api/people/1/"

data = {
  "message": "success",
  "number": 3,
  "people": [
    {
      "name": "Andrew Morgan",
      "craft": "ISS"
    },
    {
      "name": "Oleg Skripochka",
      "craft": "ISS"
    },
    {
      "name": "Jessica Meir",
      "craft": "ISS"
    },
  ]
}


info = {
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "19BBY",
	"gender": "male",
	"homeworld": "https://swapi.co/api/planets/1/",
	"films": [
		"https://swapi.co/api/films/2/",
		"https://swapi.co/api/films/6/",
		"https://swapi.co/api/films/3/",
		"https://swapi.co/api/films/1/",
		"https://swapi.co/api/films/7/"
	],
	"species": [
		"https://swapi.co/api/species/1/"
	],
	"vehicles": [
		"https://swapi.co/api/vehicles/14/",
		"https://swapi.co/api/vehicles/30/"
	],
	"starships": [
		"https://swapi.co/api/starships/12/",
		"https://swapi.co/api/starships/22/"
	],
	"created": "2014-12-09T13:50:51.644000Z",
	"edited": "2014-12-20T21:17:56.891000Z",
	"url": "https://swapi.co/api/people/1/"
}

planet = {"name": "Tatooine", 
    "rotation_period": "23", 
    "orbital_period": "304", 
    "diameter": "10465", 
    "climate": "arid", 
    "gravity": "1 standard", 
    "terrain": "desert", 
    "surface_water": "1", 
    "population": "200000", 
    "residents": [
        "https://swapi.co/api/people/1/", 
        "https://swapi.co/api/people/2/", 
        "https://swapi.co/api/people/4/", 
        "https://swapi.co/api/people/6/", 
        "https://swapi.co/api/people/7/", 
        "https://swapi.co/api/people/8/", 
        "https://swapi.co/api/people/9/", 
        "https://swapi.co/api/people/11/", 
        "https://swapi.co/api/people/43/", 
        "https://swapi.co/api/people/62/"
    ], 
    "films": [
        "https://swapi.co/api/films/5/", 
        "https://swapi.co/api/films/4/", 
        "https://swapi.co/api/films/6/", 
        "https://swapi.co/api/films/3/", 
        "https://swapi.co/api/films/1/"
    ], 
    "created": "2014-12-09T13:50:49.641000Z", 
    "edited": "2014-12-21T20:48:04.175778Z", 
    "url": "https://swapi.co/api/planets/1/"
}

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

wop = requests.get(WEB) # get the data
wop = wop.json() # convert data to Python format

print("...Signing on...")
print("")
print("Hello User!")
print("")
input("You must 'Enter' to continue")
print("")
input("I'd like you to meet a good friend of mine.")
input("Their name is " + data["people"][2]["name"] + "!")
input("They are actually one of three people in space, so that means they're an astronaut.")
input("It must be amazing to be able to see outer space with your own eyes")
answer = input("  Would you like to go to space?  ")

if answer == "Yes" :
    input("Really? Me too! Maybe we should go together.")
    input("I'm only kidding, although it would probably be exciting.")
else:
    print("I guess you're not really an outer space person huh?")
    input("That's okay, everyone has their likes and dislikes.")

print("")
input("Since we're on the topic of space,")
response = input("have you ever heard of " + info["name"] + "?  ")
if response == "No" :
	print("Well he's from Star Wars, maybe you've heard of that.")
else:
	print("Well then I hope you're as big of a geek as I am.")

print("")
input("Anyways, I wanted to share some fun facts about the guy.")
input("Even if you don't think he's that interesting, who doesn't like hearing random facts?")
print("")
print(info["name"] + " actually grew up on the planet " + planet["name"] + ".")
input(planet["name"] + " is sort of a " + planet["terrain"])
input("Along with being an " + planet["climate"] + " place.")
input("And it has a population of about " + planet["population"] + ".")

print("")
print("Last fun fact of our dear friend today:")
input("It's pretty uncommon to find someone who has " + info["eye_color"] + " eyes, but " + info["name"] + " does!")
input("And he's also " + info["hair_color"] + ".")

print("")
input("I hope you enjoyed some random facts today.")
input("Actually user... I never got your name.")
answer = input("What is it by the way?")
input("Well nice to meet you " + answer + "!")
input("Hope to speak with you again soon!")
print("")
print("...Signing off...")