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

import pdb

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

def l_money(lender, lendee, amount):
    lender["monies"] -= amount
    lendee["monies"] += amount

    # return lender["monies"], lendee["monies"]
    # it seems the return statement is not necessary

# l_money(person1, person2, 2)

def all_favourite_foods(list):
    list_of_favourite_foods = []
    for person in list:
        list_of_favourite_foods += person["favourites"] ["snacks"]
    return list_of_favourite_foods

# pdb.set_trace()
def find_no_friendends(list):
    losers = []
    for person in list:
        if person["friends"] == None:
            losers.append(person)
    return losers

