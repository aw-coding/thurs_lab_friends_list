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

def add_friend(person, friend):
    person["friends"].append(friend)


def remove_friend(person, friend):
    person["friends"].remove(friend)


def total_money(list):
    total = 0
    for person in list:
       total = total + person["monies"]
    return total
    
    # total = sum(list["monies"])