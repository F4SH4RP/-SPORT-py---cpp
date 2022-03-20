import os

s = ['' for i in range(7)]
s[1] = '''

'''

s[2] = '''
print(1)
'''

s[3] = '''
a = 3
if a == 3:
    print('yes a == 3')
else:
    print('guys i have bad news')
'''

s[4] = '''
a = 5
if a == 3:
    print('its not an IF test its an ELSE test lol')
else:
    print('test 4 fine ^-^')
'''

s[5] = '''
for i in range(5):
    print((i+7)*3)
for i in range(5, 10):
    print((i+7)*3)
for i in range(5, 15, 2):
    print((i+7)*3)
'''

s[6] = '''
for i in range(1,100,17):
    if i%3==0 or i%4==0:
        print(i*4-1)


if 1:
    print(1)
if 2:
    for i in range(5):
        for j in range(2):
            print(i*j)
'''



os.system('rm answers1 answers2')
for i in s:
    f =  open("input.py", 'w')
    f.write(i)
    f.close
    os.system('python3 tocpp.py > output.cpp ; g++ output.cpp -o a ; ./a >> answers1')
    f2 = open('tempres.py', 'w')
    os.system('python3 input.py >> answers2')

        
