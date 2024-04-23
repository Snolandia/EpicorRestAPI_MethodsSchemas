
Python -> To use many of the objects, youll need to do something similar to this :

obj = apiMethod()
values = obj["values"]
for val in values:
    apiObj = apiObjectClass(val)