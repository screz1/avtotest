import json
from random import randint as rd, choice as ch


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent = 4)


def read(filename):
    with open(filename, 'r', encoding= 'utf-8') as file:
        return json.load(file)


class Items:
    def __init__(self, num_in_collection):
        self.num_in_collection = num_in_collection

        self.description = 'item'
        self.rarity = ch(['Common', 'Rare', 'Epic', 'Legendary', 'Immortal'])
        self.type = ch(['Cards', 'Stickers', 'Figures', 'Other'])
        self.coupon_name = rd(1, 5000)

data = []


for i in range(5):
    data.append(vars(Items(num_in_collection=i)))
    #data['item2'].append(Items().__dict__)

write(data, 'data.json')



#print(read('data.json'))
#input()