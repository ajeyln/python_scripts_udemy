menu = [
    [ "egg", "spam", "bacon"],
    [ "egg", "sausage", "bacon"],
    [ "egg", "spam"],
    [ "egg", "bacon", "spam"],
    [ "egg", "bacon", "sausage", "spam"],
    [ "spam", "bacon", "sausage", "spam"],
    [ "spam", "egg", "spam", "spam", "bacon","spam"],
    [ "spam", "egg", "sausage", "spam"],
    [ "chicken", "chips"]
]

# normal method
meals = []
for meal in menu:
    if "spam" not in meal:
        meals.append(meal)
    else:
        meals.append("a meal was skipped")
print(meals)
print("*" * 120)

# for comprehension with basic conditional comprehension
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)
print("*" * 120)

# for comprehension with two conditional comprehension
fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal
               if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
print("*" * 120)

fussy_meals =[meal for meal in menu if
              ("spam" in meal or "eggs" in meal) and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)