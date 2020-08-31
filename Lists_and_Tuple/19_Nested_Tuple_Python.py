albums = [("Welcome to Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))

# method 1
print("method 1")
for album in albums:
    print("Album :{0:20} Artist :{1:15} Year :{2:4}"
          .format(album[0],album[1],album[2]))
print()

#method 2
print("method 2")
for album in albums:
    name,artist,year = album
    print("Album :{0:20} Artist :{1:15} Year :{2:4}"
          .format(name,artist,year))
