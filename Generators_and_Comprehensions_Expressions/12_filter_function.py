import timeit

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

for meal in menu:
    if "spam" not in meal:
        print(meal)

print("*" * 120)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)
print("*" * 120)

def spamless_camp():
    meals = [meal for meal in menu if not_spam(meal)]
    return(meals)

def not_spam(meals_list: list):
    return spam not in meals_list

def spamless_filter():
    spamless_meals = list(filter(not_spam, menu))
    return spamless_meals

if __name__ == "__menu__":
    print(spamless_camp())
    print(spamless_filter())
    print(timeit.timeit(spamless_camp(), number=100000))
    print(timeit.timeit(spamless_filter(), number=100000))