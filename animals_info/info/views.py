from django.shortcuts import render

def animals(request):
    animals = [
    {
        "id" :1,
        "name": "Dog",
        "legs": 4,
        "weight": 5.67,
        "height":4.2,
        "speed": 34,
        "family": 2
    },
    {
        "id": 2,
        "name": "Domestic Cat",
        "legs": 2,
        "weight": 5.67,
        "height":4.2,
        "speed": 34,
        "family": 1
    },
            
    {
        "id": 3,
        "name": "Panther",
        "legs": 2,
        "weight": 5.67,
        "height":4.2,
        "speed": 34,
        "family": 1 
    }
]
    return render(request, "info/animals.html", {"animals":animals})
    
    
def familles(request):
    familles = [
    {
        "id": 1,
        "name": "Felidae"
    },
    {
        "id": 2,
        "name": "Caninae"
    }
]
    return render(request, "info/familles.html", {"familles":familles})
