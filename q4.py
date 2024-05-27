ethiopia_coffe_location = [
    {"Addis Ababa": {"Ambo", "Buta Jirra", "Adama"}},
    {"Ambo": {"Gedo", "Nekemte"}},
    {"Buta Jirra": {"Worabe", "Wolkite"}},
    {"Adama": {"Dire Dawa", "Mojo"}},
    {"Gedo": {"Shambu", "Fincha"}},
    {"Nekemte": {"Gimbi", "Limu"}},
    {"Worabe": {"Hosana", "Durame"}},
    {"Wolkite": {"Benchi Naji", "Tepi"}},
    {"Mojo": {"Dilla", "Kaffa"}},
    {"Dire Dawa": {"Chiro", "Harar"}}
]


terminals = [4, 5, 8, 8, 6, 5, 5, 6, 7, 9, 6, 10]
coffeePlaces = ["Shambu", "Fincha", "Gimbi", "Limu", "Hosana", "Durame", "Benchi Naji", "Tepi", "Kaffa", "Dilla", "Chiro", "Harar"]
is_max = True
ternminals = []
choosen_cities = []

for i in range(0, len(terminals), 2):
    if is_max:
        if terminals[i] > terminals[i + 1]:
            choosen_cities.append(coffeePlaces[i])
        else:
            choosen_cities.append(coffeePlaces[i + 1])
        ternminals.append(max(terminals[i], terminals[i + 1]))

nodes = {
    "Fincha": "Gedo",
    "Limu": "Nekemte",
    "Hosana": "Worabe",
    "Tepi": "Wolkite",
    "Dilla": "Mojo",
    "Harar": "Dire Dawa"
}
is_max = False
choosen_cities_2 = []
terminals_2 = []

for i in range(0, len(ternminals), 2):
    if not is_max:
        if ternminals[i] > ternminals[i + 1]:
            choosen_cities_2.append(nodes[choosen_cities[i + 1]])
        else:
            choosen_cities_2.append(nodes[choosen_cities[i]])
        terminals_2.append(min(ternminals[i], ternminals[i + 1]))

nodes_1 = {
    "Gedo": "Ambo",
    "Worabe": "Buta Jirra",
    "Mojo": "Adama"
}

max_city_ind = 0
if terminals_2[1] > terminals_2[max_city_ind]:
    max_city_ind = 1
if terminals_2[2] > terminals_2[max_city_ind]:
    max_city_ind = 2

second_city = choosen_cities_2[max_city_ind]
first_choosen_city = nodes_1[second_city]
print(first_choosen_city)
print(second_city)
third_city_options = next(city_dict for city_dict in ethiopia_coffe_location if second_city in city_dict)
third_city = next(c for c in third_city_options[second_city] if c in nodes)
print(third_city)
