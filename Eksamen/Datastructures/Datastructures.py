
#List: ordered - Mutable - dynamic - nested indexing - arbitrary depth.
list = []
#Tuple: Ordered - immutable 
list2 = ["q", "u", "u", "x"]
#Dictionary: - Mutable - dynamic - nested - indexing - key access
thisdictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
#Set: Unordered - Unique - Mutable - dynamic 
s = set(list2)
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')

x = thisdictionary["model"]
f = open('text.txt', 'r')
for line in f:
    list.append(line.strip())
 
#List Comprehension
list3 = [i for i in list]
tuple = (i for i in t)
#Printing
print(", ".join(list))
print("Will only print one part: " + x)
print(", ".join(list2))
