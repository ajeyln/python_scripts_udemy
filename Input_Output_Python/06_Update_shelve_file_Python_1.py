# base file, you need to run this script first
import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans","bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin on soup"]
pasta = ["pasta","cheese"]

print(blt)
print(beans_on_toast)
print(scrambled_eggs)
print(soup)
print(pasta)

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["soup"] = soup
    recipes["pasta"] = pasta

print(recipes)
