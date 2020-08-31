welcome = "Welcome to Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
print()
# If want to change the item in metallica, we need to convert from Tuple to Lists

metallica2 = list(metallica) # Coversion from Tuple to list
print(metallica2)

metallica2[0] = "Master of puppets"
print(metallica2)





