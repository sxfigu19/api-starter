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

res = requests.get(URL) # get the data
res = res.json() # convert data to Python format

wop = requests.get(WEB) # get the data
wop = wop.json() # convert data to Python format

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
if response == "Yes" :
    star = input(" Wait, wait... are you a Star Wars geek too?  ")
    if star == "Yes"