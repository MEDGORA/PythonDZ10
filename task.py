import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = ({'whoAmI':lst})

def function(data) :
    result = data.values()
    key = list(data.keys())
    result = list(data.get(key[0]))
    result = list(set(result))
    table = {}
    for i in result :
        lst1 = []
        lst = list(data.get(key[0]))
        for j in lst :
            if j == i :
                lst1.append(1)
            else :
                lst1.append(0)
        table[i] = lst1
    print(table)

function(data)