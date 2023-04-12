import json

my_array = [str(i) for i in range(1, 101)]

for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        my_array[i - 1] = "BIGBANG"
    elif i % 3 == 0:
        my_array[i - 1] = "BIG"
    elif i % 5 == 0:
        my_array[i - 1] = "BANG"

jsonStr = json.dumps(my_array)
jsonFile = open("output.json", "w")
jsonFile.write(jsonStr)
jsonFile.close()
