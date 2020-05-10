
list = [1, 2, 3]
list2 = []
tupleList = ("Den", "her", "liste", "kan", "ikke", "ændres")
set = ["1", "2", "3"]
thisdictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdictionary["model"]
print(x)

#List Comprehension
list2 = [i for i in [1, 2, 3, 4]]
tuple = (i for i in tupleList)
print(list2)
print(next(tuple))
print("Tuple below:")
