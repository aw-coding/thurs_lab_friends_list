# person3 = {
# "name": "Scooby",
# "age": 18,
# "monies": 20,
# "friends": ["Shaggy", "Velma"],
# "favourites": {
# "tv_show": "Pokemon",
# "snacks": ["Scooby snacks"]
# } 
# }
def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True       
    return False     
 # 
# print(likes_to_eat(person3, "spinach"))  