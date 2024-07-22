import json

file = open('food_example.json', 'r')
foods = json.load(file)
file.close()


foods.append({
    "id": 999, 
    "category": "food",
    "foodName": "Foo",
    "price": 10
})

file = open('food_example.json', 'w')
json.dump(foods, file, indent=4)
file.close()