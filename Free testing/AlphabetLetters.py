import string

#One way to print all upper-case letters in the alphabet
capitalLetters = ['A','B','C', 'D','E','F','G','H', 'I','J', 'K','L','M','N', 'O', 'P','Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
p = []
for i in range(1, 50):
    if i%2 == 0:
        p.append(i)
print(p)        
#Another way to print all the upper letters in the alphabet
# print(list(string.ascii_uppercase))
        
#Print all letters in the alphabet except exclude those with the following unicode
letters = [chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85]]
k = [i if i%2 == 0 else "not even" for i in range (1, 10)]

j = [i if i%2 == 0 else "Un-even and small" if i <5  else "Un-even and large" for i in range(1, 15)]



colors = ['Black', 'White']
size = ['s', 'm', 'l', 'xl']

v = [(i, j) for i in colors for j in size]

soled_out = [('Black', 's'), ('White', 'm')]
b = [(i, j) for i in colors for j in size if(i,j) not in soled_out]