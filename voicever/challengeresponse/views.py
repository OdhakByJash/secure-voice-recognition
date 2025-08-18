from rest_framework.decorators import api_view
from challengeresponse.models import Challenge
from random import choice,randint
def challenge():
    cities = [
    "New York", "London", "Paris", "Tokyo", "Mumbai",
    "Los Angeles", "Chicago", "Toronto", "Berlin", "Sydney",
    "Dubai", "Singapore", "Hong Kong", "Rome", "Barcelona",
    "Istanbul", "Moscow", "Beijing", "Seoul", "Bangkok",
    "Shanghai", "Cape Town", "São Paulo", "Mexico City", "Buenos Aires",
    "Jakarta", "Kuala Lumpur", "Amsterdam", "Vienna", "Cairo"
    ]
    boolean = ['True','False']
    a = randint(10,30)
    b = randint(10,30)
    city = choice(cities)
    boolean_value = choice(boolean)
    list_challenges = [
        [f"Say The Result Of This Expression: sum of{a} and {b} is?",a+b],
        [f"Say: I Live In {city}",city],
        [f"Say: {boolean_value}",boolean_value]
    ]
    return choice(list_challenges)
@api_view(['POST'])
def challenege(request):
    