from random import choice,randint
def challenge():
    a = randint(10,30)
    b = randint(10,30)
    cities = [
    "New York", "London", "Paris", "Tokyo", "Mumbai",
    "Los Angeles", "Chicago", "Toronto", "Berlin", "Sydney",
    "Dubai", "Singapore", "Hong Kong", "Rome", "Barcelona",
    "Istanbul", "Moscow", "Beijing", "Seoul", "Bangkok",
    "Shanghai", "Cape Town", "São Paulo", "Mexico City", "Buenos Aires",
    "Jakarta", "Kuala Lumpur", "Amsterdam", "Vienna", "Cairo"
    ]
    boolean = ['True','False']
    list_challenges = [
        f"sum of{a} and {b} is?",
        f"I Live In {choice(cities)}",
        f"{choice(boolean)}"
    ]
    return choice(list_challenges)