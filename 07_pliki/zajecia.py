# f = open('txt.txt')
# print(f.readlines())
# f.close()

#with open('txt.txt') as f:
    #content = f.readlines()

#print(content)
#for line in content:
    #print(line)

# with open('txt.txt', 'w') as f:
    # f.write('Pan Tadeusz')
'''
with open('txt.txt') as fopen:
    content = fopen.readlines()

print(content)
for l in content:
    print(l)
'''
'''
with open('save.txt', 'w') as f:
  f.write('Line 1')
  f.write('Line 2')
  f.write('Line 3')
  f.write('Line 4')
'''
'''
sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
sweets_str = '\n'.join(sweets_list)

with open('save.txt', 'w') as f:
    f.write(sweets_str)
'''