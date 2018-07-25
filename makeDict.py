a = open('parts.txt','r')
a_message = a.read()

parts = a_message.split('\n')
a.close()

b = open('partno.txt','r')
b_message = b.read()

partno = b_message.split('\n')
b.close()

c = open('manu.txt','r')
c_message = c.read()

manu = c_message.split('\n')
c.close()

searchPart = dict(zip(parts, partno))
searchManu = dict(zip(parts, manu))

print(searchManu)
