from data import people, plants_list, plant_dict

if bool(people) and all(person[1] for person in people):
    print("Sending Email")
else:
    print("User must edit the list of receipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This plant contains grass")
else:
    print("no grasses in this pack")

if any([plant.plant_type == "Grass" for plant in plant_dict.values()]):
    print("This dict contains grass")
else:
    print("no grasses in this dict")

if any(plant_dict[key].plant_type == "Grass" for key in plant_dict):
    print("This dict contains grass")
else:
    print("no grasses in this dict")