import json, random
from item import Item

with open('data/items.json', 'r') as f:
    items = json.load(f)

items_trimmed = []
seed_value = random.randint(0, 2**32 - 1)
print(seed_value)

chest_items = [item.get("chest_item") for item in items]

#seed_value = 42
random.seed(seed_value)
random.shuffle(chest_items)


for idx, item in enumerate(items):
    new_item = Item(item.get("data"), chest_items[idx])
    items_trimmed.append(new_item)

print(items_trimmed)

