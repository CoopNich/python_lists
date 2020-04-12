planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1,"Venus")
planet_list.insert(2, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[0:4]

del planet_list[8]



# CHALLENGE - Need to figure out how to print satellites on one line with planet (Neptune was visited by X, Y, Z)
spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Wohlie", "Venus"),
   ("Ricky", "Neptune"),
   ("Jerry", "Neptune"),
   ("Larry", "Neptune"),
]

for planet in planet_list:
    has_visited = False
    a = f'{planet} was visited by '
    for el in spacecraft:
        if el[1] == planet:
           a += f'{el[0]}, '
           has_visited = True
    else: 
        a = a[slice(-2)] + f'.'
            
    if has_visited: print (a)
    else:
        print(f'{planet} is very lonely.')