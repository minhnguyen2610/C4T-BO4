while True:
    Pokemon = {
        "Onix":''':bad-ass rock Python-like creature who is surprisingly can be defeated using a water bucket''',
        "Pikachu":''':known as the main pokemon travels by the side of Ash-ketchup(yummy)-who is also very aggressive''',
        "Lugia":''':have the defense of a nokia and hit like a flying nokia''',
    }
    n = input("please enter the pokemon you want to search: ")
    n = n.lower()
    n = n.capitalize()
    print(n, Pokemon[n])