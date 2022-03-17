
s='''
if 1 == 0:
    print(1)
if 1:
    print(2) 


print(2,end='')
print(2, end = '') 
print(2, end='')
print(2, end ='qwer') 
print(3)
for i in range(10):
    print(6)
    print(6)

for i in range(2, 5):
    print(6)
    
for i in range(2, 10, 3):
    print(6)

for kkk in range(4):
    print(111)
'''

def remspaces(cs): # do not use with empty strings
    idx = 0
    idy = 0
    for i in range(-1, -len(cs)-1, -1):
        if cs[i] == ' ':
            idx+=1
        else:
            break
        
    for i in range(len(cs)):
        if cs[i] == ' ':
            idy += 1
        else:
            break
    if idx==0:
        return cs
    return cs[idy:-idx]
    
def findlvl(cs):
    currlvl = 0
    for i in cs:
        if i == ' ':
            cs = cs[1:]
            currlvl += 1
        else:
            break
    return currlvl, cs


print('#include <iostream>')
print('using namespace std;')
print('int main() {')
currlvl = 0
prevlvl = 0
s += '\n ;'
for cs in s.split('\n'):
    currlvl, cs = findlvl(cs)
    cs = remspaces(cs)
    if cs == '':
        continue
    if currlvl == prevlvl:
        print(';')
    elif currlvl < prevlvl:
        print(';  } ;')
    else:
        print()

    
    if cs[:5] == 'print':
        csp = cs.split('end')
        cs = 'cout << ' + csp[0][6:-1]
        if len(csp) == 1:
            cs += ' << endl'
        else:
            if cs[-1] == ',':
                cs = cs[:-1]
            cspp = str(csp[1]).split("'")[1]
            if cspp != '':
                cs += ' << ' + '\"' + cspp + '\"'

        
    if cs[:2] == 'if':
        cs = 'if (' + cs[3:-1] + ') {'
    
    if cs[:3] == 'for':
        var_name = cs.split(' ')[1]
        addr = 5 + len(var_name)
        if cs[addr:addr+8] == 'in range':
            addr2 = addr + 8
            csp = cs[addr2+1:-2]
            cspp = csp.split(',')
            print(cspp)
            if len(cspp) == 1:
                range_lim = cspp[0]
                cs = 'for ( int ' + var_name + '=0; ' + var_name + '<' + str(range_lim) + '; ' + var_name + '++) {' # yeah
            elif len(cspp) == 2:
                range_lim = cspp[1]
                range_beg = cspp[0]
                cs = 'for ( int ' + var_name + '=' + str(range_beg) + '; ' + var_name + '<' + str(range_lim) + '; ' + var_name + '++) {' # YEEEEAAAAAAH
            elif len(cspp) == 3:
                range_beg = cspp[0]
                range_lim = cspp[1]
                range_step = cspp[2]
                cs = 'for ( int ' + var_name + '=' + str(range_beg) + '; ' + var_name + '<' + str(range_lim) + '; ' + var_name + '+=' + str(range_step) + ') {' # YOOOOOOOOOOOOO
    
    print(' '*currlvl, cs, end = '')
    prevlvl = currlvl
    currlvl = 0

print(' ;')
print('}')


print()
print()
print()
