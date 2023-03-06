data = {"color":'red, green, orange ',
        'fruit': 'apple, grapes, mango',
        'pet':'dog, cat',
        'car':"van, sedan"

        }

keys = list(data.keys())
x = 0
while x < len(keys):
        key = keys[x]
        value = data[key]
        print(key + ':' + value )
        x +=1