import random

rucksack = ["Waterflask", "Cheese","Gold coins","Handkerchief", "Tinderbox", "Scrolls","Dagger", "Rope", "Nuts","Pipe", "Tobacco", "Wine skin",
"Herbs", "Axe"]

rucksack.sort()
print(rucksack)

print("Number of Items in the list: ", len(rucksack))

a = ["Gem", "Necklace"]
for i in range(len(a)):
    rucksack.append(a[i])
print(sorted(rucksack))
rucksack.pop(random.randrange(len(rucksack)))

select_items = random.sample(rucksack, k=5)
for n_items in select_items:
    rucksack.remove(n_items)
print(rucksack)
