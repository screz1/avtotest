import json
from random import choice


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent = 4)


def read(filename):
    with open(filename, 'r', encoding= 'utf-8') as file:
        return json.load(file)


class Item:
    def __init__(self, num_in_collection):
        self.num_in_collection = num_in_collection
        self.description = 'item'
        self.rarity = choice(['Common', 'Rare', 'Epic', 'Legendary'])
        self.type = choice(['Cards', 'Stickers', 'Figures', 'Other'])
        self.coupon_name = f"coupon_name_{str(num_in_collection)}"


data = {}

if __name__ == "__main__":
    for i in range(5001):
        data[f"Item({i})"] = vars(Item(num_in_collection=i))
    print(data)
write(data, 'data.json')