
import itertools
#inefficient
msg = 'line1\n'
msg += 'line2\n'
msg += 'line3\n'
#Efficient

msg = ['line1', 'line2', 'line3']
'\n'.join(msg)

#inefficient
cube_numbers = []
for n in range(0,10):
    if n % 2 == 1:
      cube_numbers.append(n**3)

#Efficient
cube_numbers = [n**3 for n in range(1,10) if n%2 == 1]      

oldlist = {"Hello", "World", "Internet"}
#inefficient
newlist = []
for word in oldlist:
    newlist.append(word.upper())

#Efficient
newlist = map(str.upper, oldlist)

