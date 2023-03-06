data = {"color":'red, green, orange ',
        'fruit': 'apple, grapes, mango',
        'pet':'dog, cat',
        'car':"van, sedan"

        }

# for loop


for  key in data:
    value = data[key]
    print(key + ":" + str(value))