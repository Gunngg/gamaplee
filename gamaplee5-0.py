import random
import math

version = "5.0"
# major - backwards incompatible
# minor - backwards compatible

# TODO:
# nothing?

'''
    (dd.m.yyyy)
    1.0 (31.5.2021?) - the
    2.0 (01.6.2021?) - stuff like A. and A, / changed <'' and >'' into <, and >, / added the t command / added copying and pasting / added the [] thing
    2.1 (01.6.2021?) - replaced <, and >, with <. and >. / added the {} and {}' (this version is actually backwards incompatible but nobody cares about this anywys)
    2.2 (02.6.2021?) - z12 and Z12
    3.0 (02.6.2021?/05.6.2021?) - added &' / added ['] / replaced {}' with {'}
    4.0 (05.6.2021~06.6.2021) - changed z12 and Z12 to 1z2 and 1Z2 / you can now put {} and 12 inside other ones (it doesnt always work properly because i suck at coding) / removed @ / added f, F, x, +., -. / changed intro message / added text generator
    5.0 (10.6.2021) - changed {} and {' } to {. } and {, } / added [. ]; [, ]; {. }; {, }; m; M; m'/M'
    '''

# this is an esolang
# The Greatest And Most Awesomest Programming Language To Ever Exist - GAMAPLEE
'''
    Data is stored in an infinite square grid. Each cell holds a number (0 by default)

    -- COMMANDS --
    # - text until the end of the line is ignored
    <>^v - move the pointer in a specific direction
    ()AV - move the value of the current cell in the shown direction, while current cell's value becomes 0
    ('/)'/A'/V' - copies the current value in the shown direction
    (./)./A./V. - ()AV but moves the value 2 tiles
    (,/),/A,/V, - ('/)'/A'/V' but copies the value 2 tiles
    + - adds one to the cell
    - - subtracts one from the cell
    f - if current value is 0 it gets turned into 1 and gets saved below; if current value isnt 0 its becomes 0 and gets saved below
    ~ - ends the program
    m - moves in a random direction horizontally/vertically
    M - moves in a random direction diagonally
    m'/M' - moves in any direction horizontally/vertically/diagonally
    : - copies current cell's value
    ; - pastes copied value while keeping it "copied" (if you didnt copy anything, the value is 0)
    +. - adds 1 to the copied value
    -. - subtracts 1 from the copied value
    x - set copied value to 0
    F - f but for the copied value
    _ - sets current cells value to 0
    ? - sets current cells value to a random ascii character value (between 33 and 126 inclusive)
    [ ] - if current cell's value isnt 0, does whats inside the brackets, otherwise skips them
    [' ] - if current cell's value IS 0, does whats inside the brackets, otherwise skips them
    [. ] - if copied value isnt 0, does whats inside the brackets, otherwise skips them
    [, ] - if copied value IS 0, does whats inside the brackets, otherwise skips them
    { } - repeats whats inside the brackets n times where n is the current cell's value 
    {' } - same as above but sets current value to 0 before repeating
    {. } - repeats whats inside the brackets n times where n is the currently copied value and doesnt delete it (see ":" and ";")
    {, } - same as above but sets copied value to 0
    (1 IS LIKE LEFT BRACKET 2 IS RIGHT BRACKET) im sorry
    1z 2 - loops stuff inside the brackets until "finds" a cell whose value is zero
    1Z 2 - loops stuff inside the brackets until CURRENT cell's value is 0
    n - gets users input which is a number and stores it in the current cell
    N - same as above but stores the ascii value of the number
    i - same as n but can also get strings as input - (numbers saved as themselves, symbols as ascii)
    I - stores all characters as ascii
    o - outputs the current cells value [opposite of n]
    O - o without newline
    o'/O' - o without newline but with space
    q - outputs the ascii character with the cells value [opposite of I]
    Q - q without newline
    q'/Q' - q without newline but with space
    c - outputs numbers 0-9 as themselves, everything else as ascii [opposite of i]
    C - c without newline
    c'/C' - c without newline but with space
    = - [eq] if current value is equal to value above then value below is set to 1, otherwise its 0
    =' - [not eq] if current value is NOT equal to value above then value below is set to 1, otherwise its 0
    >' - [greater] if current value is greater than value above then value below is 1, otherwise is 0
    >. - [greater or eq] if current value is greater or equals the value above then value below is 1, otherwise 0
    <' - [less] if current value is less than value above then value below is 1 otherwise 0
    <. - [less or eq] if current value is less or equals value above then value below is 1 otherwise 0
    & - [and] if current value and value above arent 0, value below becomes 1, otherwise 0
    &' - [nor] if current value and value above ARE both 0, value below gets set to 1, otherwise it gets set to 0
    | - [or] if current value OR value above arent zero, value below is 1, otherwise 0
    |' - [xor] same as above but there should but its only 1-0 or 0-1 (it cant be 1-1)
    * - multiplies current cell's value by the value of the cell above and saves it into cell below
    / - divides current value by value of cell above and saves into cell below
    -' - subtracts cell above from current cell and saves below
    +' - adds current cell to cell above and saves below
    ^' - raises current cell to the power of cell above and saves below
    s - squares current cell and save below
    t - raises current cell to the power of itself and saves below
    r - finds the nth root of the current cell, where n is the cell above and saves below
    R - finds square root of current cell and saves below
    % - finds modulo between current cell and cell above and saves below
    ! - calculates factorial of current cell and saves below
    '''
''' cancelled and not coded (probably)
    [CANCELLED] r - flips the current nonzero row (09504 -> 04059)
    [CANCELLED] R - flips current column            ^^^^     ^^^^
    -- SPECIAL COMMANDS --
    [ALL CANCELLED LOL!!!]

    [] - moves the pointer, {} - doesnt
    [zDIRECTIONS] - repeats the DIRECTIONS until the current cell value is 0 (EXAMPLE: [z>], [z)], [mz>?A])
    [n , N , i , I , o , ODIRECTIONS] - same as n, N, i, I, o, O but inputs/outputs multiple symbols following DIRECTIONS (but what about 3505 - itll output 35)(EXAMPLE:
    000
    120
    if pointer is at 1: [o>] outputs 12, pointer is at 2; [i>] replaces 1,2,0  etc with inputted stuff)
    {same as above} - same as above but pointer stays in place
    [dDIRECTIONS] - duplicates current cell's value into the cell in DIRECTIONS
    {above}
    [DDIRECTIONS] - duplicates in DIRECTIONS until value of cell is 0
    {above}
    -- MAYBE WILL ADD --
    [*DIRECTIONS] - multiplies current cell by the cell that you get to if you do DIRECTIONS
    [+ , - , / , %DIRECTIONS] - same as above but addition, subtraction, division and modulo
    Stuff like [i>] - [i3>] - same as [i3>] but input is only 3 chars long
    '''
''' CANCELLED
    [CANCELLED] ()AV - move the pointer in a specific direction, then move the row/column in the opposite direction (with the pointer), so the pointer stays in place and the only thing that moves is the row/column
    r and R (reverse) are cancelled because too hard
    [not the if != 0 stuff] stuff with [] too hard fjeijfe
    [I] cancelled bruh (multiple character inputrtdjkafkj;

    elif i == '(' and level == 0:
        # 0 3 5  pointer moves  0 3 5
        # 2>0<7                 0>2<0
        # current row moves to the right
        jin = 0
        isj0 = False
        for j0 in data:
            if j.startswith(str(ccol+1)+':'+str(crow)+':'):
                isj0 = True
                ccol += 1
                break
        if isj0 == False:
            for j in data:
                if j.startswith(cur):
                        data[jin] = str(int(data[jin].split(':')[1])+1)+':'+data[jin].split(':')[1]+':'+data[jin].split(':')[2]
                jin += 1
            cval = getvalue(ccol,crow)
    
    elif i == ')' and level == 0:
        jin = 0
        for j in data:
            if j.startswith(cur):
                data[jin] = str(int(data[jin].split(':')[1])-1)+':'+data[jin].split(':')[1]+':'+data[jin].split(':')[2]
            jin += 1
        cval = getvalue(ccol,crow)
    
    elif i == 'A' and level == 0:
        jin = 0
        for j in data:
            if j.startswith(cur):
                data[jin] = data[jin].split(':')[0]+':'+str(int(data[jin].split(':')[1])-1)+':'+data[jin].split(':')[2]
            jin += 1
        cval = getvalue(ccol,crow)
    
    elif i == 'V' and level == 0:
        jin = 0
        for j in data:
            if j.startswith(cur):
                data[jin] = data[jin].split(':')[0]+':'+str(int(data[jin].split(':')[1])+1)+':'+data[jin].split(':')[2]
            jin += 1
        cval = getvalue(ccol,crow)
    
    NEWER VERSION
    elif i == '(' and level == 0:
            jin = 0
            for j in data:
                if j.split(':')[1] == crow:
                    data[jin] = str(int(data[jin].split(':')[0])+1)+':'+data[jin].split(':')[1]+':'+data[jin].split(':')[2]
                else:
                    jin += 1
    '''
''' scrapped {} thing
    #{
    elif i == '{':
        level += 1
        badbrac = 0
        leftin = iin
        isfound = False
        win = 0
        for w in S[iin+1:]:
            if w == '}' and badbrac == 0:
                #if (str(iin)+':'+str(win+iin+1)+':'+str(copy)) not in bracs:
                bracs.append(str(iin)+':'+str(win+iin+1)+':'+str(copy))
                rightin = win+iin+1
                isfound = True
                break
            elif w == '{':
                badbrac += 1
            elif w == '}' and badbrac != 0:
                badbrac -= 1
            win += 1
        if isfound == False:
            rightin = len(S)-1
            S = S+'}'
        curvy = S[leftin+1:rightin]
        Sl = list(S)
        aain = 0
        for aa in Sl:
            if leftin <= aain <= rightin:
                Sl.pop(aain)
            aain+=1
        Sl.insert(leftin+1,curvy*copy)
        S = ''.join(Sl)
        print(S)
        if S[iin+1] == "'":
            copy = 0
    '''


def convert(D,P='Q'):
    asc = []
    ain = 0
    out = ''
    if type(D) == str:
        for dd in D:
            asc.append(ord(dd))
    elif type(D) == list:
        asc = D
    for a in asc:
        if ain == 0:
            out = out+(a*'+') + P
        else:
            #[30,35]
            #    ^^
            # five minuses is shorter than 35 pluses and 1 underscore
            if a-asc[ain-1] == 0:
                out = out + P
            elif abs(a-asc[ain-1]) <= (1+asc[ain-1]):
                if a > asc[ain-1]:
                    out = out + '+'*(a-asc[ain-1]) + P
                elif a < asc[ain-1]:
                    out = out + '-'*(asc[ain-1]-a) + P
            else:
                out = out + '_' + (a*'+') + P
        ain += 1
    return out


# column:row:value

data = ['0:0:0']
ccol = 0
crow = 0
cval = 0
cur = str(ccol)+':'+str(crow)+':'
copy = 0
bracs = []

print('Welcome to The Greatest And Most Awesomest Programming Language To Ever Exist (or GAMAPLEE) interpreter')

def getvalue(C, R):
    global ccol, crow, cval, cur
    jin=0
    isfound = False
    for j in data:
        if j.startswith(str(C)+':'+str(R)+':'):
            isfound = True
            return int(float(j.split(':')[2]))
        else:
            jin+=1
    if isfound == False:
        return 0

def updval():
    global cval
    jin = 0
    for j in data:
        if j.startswith(cur):
            cval = int(float(j.split(':')[2]))
        else:
            jin += 1
        
def reset():
    global data, ccol, crow, cval, cur, copy, bracs
    data = ['0:0:0']
    ccol = 0
    crow = 0
    cval = 0
    cur = str(ccol)+':'+str(crow)+':'
    copy = 0
    bracs = []

def add():
    global data, ccol, crow, cval, cur
    jin = 0
    isin = False
    if cur+str(cval) in data:
        isin = True
    else:
        for j in data:
            if j.startswith(cur):
                isin = True
            else:
                isin = False
    if isin == False:
        data.append(cur+str(cval))

    
def gamaplee(S):
    global ccol, crow, cval, cur, copy, bracs
    level = 0 #how many brackets deep
    brac = 0 #level but less strict?
    badbrac = 0
    iin = 0
    tild = False
    LEFT = 0
    RIGHT = 0
    # this is for comments
    line = S.split('\n')
    kin = 0
    Kin = 0
    tagid = 0
    for k in line:
        if '#' in k:
            for K in k:
                if K == '#':
                    tagid = Kin
                    Kin = 0
                    break
                Kin += 1
            line[kin] = line[kin][:tagid]
        kin += 1
    S = '\n'.join(line)
    # this is to prevent "string index out of range"
    prime = ['o','O','q','Q','c','C','=','>','<','|','-','+','^','(',')','A','V','[','{','m'] # can have a character after them
    special = ['z','Z']
    if len(S) >= 1:
        if S[-1] in prime:
            S = S+'\n  '
    elif len(S) >= 2:
        if S[-1] in prime or S[-2] in prime:
            S = S+'\n  '

    for i in S:

        if tild == False:

            cur = str(ccol)+':'+str(crow)+':'

            if cur+str(cval) not in data:
                add()
            updval()

            #<
            if i == '<' and S[iin+1] != "'" and S[iin+1] != "." and level == brac:
                # IF POINTER ALWAYS POINTS AT (0,0)
                # 0 3 5  pointer moves  0 3 5
                # 2>0<7                >2<0 7
                #   ^ if this 0         ^ now this 0
                # ^ this is -1            ^ and this 1
                # all columns move to the right, all columns +1
                ccol += 1
                cval = int(getvalue(ccol,crow))

            #>
            elif i == '>' and S[iin+1] != "'" and S[iin+1] != "." and level == brac:
                ccol -= 1
                cval = int(getvalue(ccol,crow))
            
            #^
            elif i == '^' and S[iin+1] != "'" and level == brac:
                crow -= 1
                cval = int(getvalue(ccol,crow))

            #v
            elif i == 'v' and level == brac:
                crow += 1
                cval = int(getvalue(ccol,crow))

            #(
            elif i == '(' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol+1)+':'+str(crow)+':'):
                        data[jin] = str(ccol+1)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol+1)+':'+str(crow)+':'+str(cval))
                cval = 0
            
            #)
            elif i == ')' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol-1)+':'+str(crow)+':'):
                        data[jin] = str(ccol-1)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol-1)+':'+str(crow)+':'+str(cval))
                cval = 0
            
            #A
            elif i == 'A' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow-1)+':'):
                        data[jin] = str(ccol)+':'+str(crow-1)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow-1)+':'+str(cval))
                cval = 0
            
            #V
            elif i == 'V' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval))
                cval = 0

            #('
            elif i == '(' and S[iin+1] == "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol+1)+':'+str(crow)+':'):
                        data[jin] = str(ccol+1)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol+1)+':'+str(crow)+':'+str(cval))

            #)'
            elif i == ')' and S[iin+1] == "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol-1)+':'+str(crow)+':'):
                        data[jin] = str(ccol-1)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol-1)+':'+str(crow)+':'+str(cval))
            
            #A'
            elif i == 'A' and S[iin+1] == "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow-1)+':'):
                        data[jin] = str(ccol)+':'+str(crow-1)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow-1)+':'+str(cval))
            
            #V'
            elif i == 'V' and S[iin+1] == "'" and S[iin+1] != "." and S[iin+1] != "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval))
            
            #(.
            elif i == '(' and S[iin+1] != "'" and S[iin+1] == "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol+2)+':'+str(crow)+':'):
                        data[jin] = str(ccol+2)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol+2)+':'+str(crow)+':'+str(cval))
                cval = 0
            
            #).
            elif i == ')' and S[iin+1] != "'" and S[iin+1] == "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol-2)+':'+str(crow)+':'):
                        data[jin] = str(ccol-2)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol-2)+':'+str(crow)+':'+str(cval))
                cval = 0
            
            #A.
            elif i == 'A' and S[iin+1] != "'" and S[iin+1] == "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow-2)+':'):
                        data[jin] = str(ccol)+':'+str(crow-2)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow-2)+':'+str(cval))
                cval = 0
            
            #V.
            elif i == 'V' and S[iin+1] != "'" and S[iin+1] == "." and S[iin+1] != "," and level == brac:
                jin = 0
                didfind = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                    else:
                        jin +=1
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+2)+':'):
                        data[jin] = str(ccol)+':'+str(crow+2)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+2)+':'+str(cval))
                cval = 0
            
            #(,
            elif i == '(' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] == "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol+2)+':'+str(crow)+':'):
                        data[jin] = str(ccol+2)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol+2)+':'+str(crow)+':'+str(cval))

            #),
            elif i == ')' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] == "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol-2)+':'+str(crow)+':'):
                        data[jin] = str(ccol-2)+':'+str(crow)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol-2)+':'+str(crow)+':'+str(cval))
            
            #A,
            elif i == 'A' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] == "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow-2)+':'):
                        data[jin] = str(ccol)+':'+str(crow-2)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow-2)+':'+str(cval))
            
            #V,
            elif i == 'V' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] == "," and level == brac:
                didfind = False
                jin = 0
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+2)+':'):
                        data[jin] = str(ccol)+':'+str(crow+2)+':'+str(cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+2)+':'+str(cval))

            #+
            elif i == '+' and S[iin+1] != "'" and S[iin+1] != "." and level == brac:
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(cval+1)
                        cval += 1
                    else:
                        jin += 1
            
            #-
            elif i == '-' and S[iin+1] != "'" and S[iin+1] != "." and level == brac:
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(cval-1)
                        cval -= 1
                    else:
                        jin += 1
            
            #f
            elif i == 'f' and level == brac:
                if cval == 0:
                    fvalue = '1'
                else:
                    fvalue = '0'
                jin = 0
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+fvalue
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+fvalue)

            #~
            elif i == '~' and level == brac:
                tild = True
            
            #m
            elif i == 'm' and S[iin+1] != "'" and level == brac:
                mr = random.choice([0,1,2,3])
                if mr == 0:
                    #left
                    ccol += 1
                elif mr == 1:
                    #right
                    ccol -= 1
                elif mr == 2:
                    #up
                    crow -= 1
                elif mr == 3:
                    #down
                    crow += 1
                cval = int(getvalue(ccol,crow))
            
            #M
            elif i == 'M' and S[iin+1] != "'" and level == brac:
                mr = random.choice([0,1,2,3])
                if mr == 0:
                    #up left
                    ccol += 1
                    crow -= 1
                elif mr == 1:
                    #up right
                    ccol -= 1
                    crow -= 1
                elif mr == 2:
                    #down left
                    ccol += 1
                    crow += 1
                elif mr == 3:
                    #down right
                    ccol -= 1
                    crow += 1
                cval = int(getvalue(ccol,crow))
            
            #m'/M'
            elif (i == 'm' and S[iin+1] == "'") or (i == 'm' and S[iin+1] == "'") and level == brac:
                mr = random.choice([0,1,2, 3,4, 5,6,7])
                if mr == 0:
                    #up left
                    ccol += 1
                    crow -= 1
                elif mr == 1:
                    #up
                    crow -= 1
                elif mr == 2:
                    #up right
                    ccol -= 1
                    crow -= 1
                elif mr == 3:
                    #left
                    ccol += 1
                elif mr == 4:
                    #right
                    ccol -= 1
                elif mr == 5:
                    #down left
                    ccol += 1
                    crow += 1
                elif mr == 6:
                    #down
                    crow += 1
                elif mr == 7:
                    #down right
                    ccol -= 1
                    crow += 1
                cval = int(getvalue(ccol,crow))
            
            #:
            elif i == ':' and level == brac:
                copy = cval
            
            #;
            elif i == ';' and level == brac:
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(copy)
                        cval = copy
                    else:
                        jin += 1
            
            #+.
            elif i == '+' and S[iin+1] != "'" and S[iin+1] == "." and level == brac:
                copy += 1
            
            #-.
            elif i == '-' and S[iin+1] != "'" and S[iin+1] == "." and level == brac:
                copy -= 1

            #x
            elif i == 'x' and level == brac:
                copy = 0
            
            #F
            elif i == 'F' and level == brac:
                if copy == 0:
                    copy = 1
                else:
                    copy = 0
            
            #[
            elif i == '[' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != ",":
                brac += 1
                if cval != 0:
                    #i feel like a fucking genius rn
                    level += 1
            
            #['
            elif i == '[' and S[iin+1] == "'" and S[iin+1] != "." and S[iin+1] != ",":
                brac += 1
                if cval == 0:
                    level += 1
            
            #[.
            elif i == '[' and S[iin+1] != "'" and S[iin+1] == "." and S[iin+1] != ",":
                brac += 1
                if copy != 0:
                    level += 1
            
            #[,
            elif i == '[' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] == ",":
                brac += 1
                if copy == 0:
                    level += 1
            
            #]
            elif i == ']':
                brac -= 1
                level -= 1
                if brac < 0:
                    brac = 0
                if level < 0:
                    level = 0
            
            #{
            elif i == '{' and S[iin+1] != "'" and S[iin+1] != "." and S[iin+1] != ",":
                brac += 1
                badbrac = 0
                win = 0
                for w in S[iin+1:]:
                    if w == '}' and badbrac == 0:
                        if (str(iin)+':'+str(win+iin+1)+':'+str(cval)) not in bracs:
                            bracs.append(str(iin)+':'+str(win+iin+1)+':'+str(cval))
                        break
                    elif w == '{':
                        badbrac += 1
                    elif w == '}' and badbrac != 0:
                        badbrac -= 1
                    win += 1

            #{'
            elif i == '{' and S[iin+1] == "'":
                brac += 1
                badbrac = 0
                win = 0
                for w in S[iin+1:]:
                    if w == '}' and badbrac == 0:
                        if (str(iin)+':'+str(win+iin+1)+':'+str(cval)) not in bracs:
                            bracs.append(str(iin)+':'+str(win+iin+1)+':'+str(cval))
                        break
                    elif w == '{':
                        badbrac += 1
                    elif w == '}' and badbrac != 0:
                        badbrac -= 1
                    win += 1
                cval = 0
            
            #{. {,
            elif i == '{' and (S[iin+1] == "." or S[iin+1] == ","):
                brac += 1
                badbrac = 0
                win = 0
                for w in S[iin+1:]:
                    if w == '}' and badbrac == 0:
                        if (str(iin)+':'+str(win+iin+1)+':'+str(copy)) not in bracs:
                            bracs.append(str(iin)+':'+str(win+iin+1)+':'+str(copy))
                        break
                    elif w == '{':
                        badbrac += 1
                    elif w == '}' and badbrac != 0:
                        badbrac -= 1
                    win += 1
                if S[iin+1] == ",":
                    copy = 0

            #}
            if i == '}':
                brac -= 1
                zin = 0
                z2found = False
                for z in bracs:
                    if iin == int(z.split(':')[1]):
                        LEFT = int(z.split(':')[0])
                        RIGHT = int(z.split(':')[1])
                        REPEAT = int(z.split(':')[2])
                        break
                    zin += 1
                for z2 in bracs:
                    # whywhywhywhywhywhywhywhywhywhywhywhywhywhywhywhywhywhywhy
                    if int(z2.split(':')[0]) < LEFT and int(z2.split(':')[1]) > RIGHT:
                        z2found = True
                    else:
                        z2found = False
                if REPEAT != 0 and z2found == False:
                    while REPEAT >= 1:
                        #<><>{{}} - left is 4 right is 7
                        #    4567
                        #     ??
                        #^^^^^ - 5; aka left (4) + 1
                        gamaplee(' '*(LEFT+1)+S[LEFT+1:RIGHT])
                        REPEAT -= 1
            
            #1
            elif i == '1':
                brac += 1
                if S[iin+1] == 'z':
                    badbrac = 0
                    win = 0
                    for w in S[iin+1:]:
                        if w == '2' and badbrac == 0:
                            bracs.append(str(iin)+':'+str(win+iin+1)+':z')
                            break
                        elif w == '1':
                            badbrac += 1
                        elif w == '2' and badbrac != 0:
                            badbrac -= 1
                        win += 1
                elif S[iin+1] == 'Z':
                    badbrac = 0
                    win = 0
                    for w in S[iin+1:]:
                        if w == '2' and badbrac == 0:
                            bracs.append(str(iin)+':'+str(win+iin+1)+':Z:'+str(ccol)+':'+str(crow))
                            break
                        elif w == '1':
                            badbrac += 1
                        elif w == '2' and badbrac != 0:
                            badbrac -= 1
                        win += 1
            
            #2
            elif i == '2':
                brac -= 1
                zin = 0
                for z in bracs:
                    if iin == int(z.split(':')[1]):
                        LEFT = int(z.split(':')[0])
                        RIGHT = int(z.split(':')[1])
                        BRTYPE = z.split(':')[2]
                        break
                    zin += 1
                if BRTYPE == 'z':
                    while cval != 0:
                        gamaplee(S[LEFT+1:RIGHT])
                elif BRTYPE == 'Z':
                    ZCOL = int(bracs[zin].split(':')[3])
                    ZROW = int(bracs[zin].split(':')[4])
                    while getvalue(ZCOL,ZROW) != 0:
                        gamaplee(S[LEFT+1:RIGHT])

            #n
            elif i == 'n' and level == brac:
                ninp = int(input('n:>'))
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(ninp)
                        cval = ninp
                    else:
                        jin += 1
            
            #N
            elif i == 'N' and level == brac:
                Ninp = int(input('N:>'))
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(ord(str(Ninp)))
                        cval = ord(str(Ninp))
                    else:
                        jin += 1
            
            #i
            elif i == 'i' and level == brac:
                iinp = input('i:>')
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        try:
                            data[jin] = cur+str(int(iinp))
                        except:
                            data[jin] = cur+str(ord(iinp))
                    else:
                        jin += 1

            #I
            elif i == 'I' and level == brac:
                Iinp = input('I:>')
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(ord(Iinp))
                    else:
                        jin += 1

            #o
            elif i == 'o' and S[iin+1] != "'" and level == brac:
                is0 = True
                for j in data:
                    if j.startswith(cur):
                        print(j.split(':')[2])
                        is0 = True
                        break
                    else:
                        is0 = False
                if is0 == False:
                    print('0')
            
            #O
            elif i == 'O' and S[iin+1] != "'" and level == brac:
                for j in data:
                    if j.startswith(cur):
                        print(j.split(':')[2],end='')
                        is0 = True
                        break
                    else:
                        is0 = False
                if is0 == False:
                    print('0',end='')
            
            #o' O'
            elif (i == 'o' and S[iin+1] == "'" and level == brac) or (i == 'O' and S[iin+1] == "'" and level == brac):
                for j in data:
                    if j.startswith(cur):
                        print(j.split(':')[2],end=' ')
                        is0 = True
                        break
                    else:
                        is0 = False
                if is0 == False:
                    print('0',end=' ')
            
            #q
            elif i == 'q' and S[iin+1] != "'" and level == brac:
                for j in data:
                    if j.startswith(cur):
                        print(chr(int(j.split(':')[2])))

            #Q
            elif i == 'Q' and S[iin+1] != "'" and level == brac:
                for j in data:
                    if j.startswith(cur):
                        print(chr(int(j.split(':')[2])),end='')
            
            #q' Q'
            elif (i == 'q' and S[iin+1] == "'" and level == brac) or (i == 'Q' and S[iin+1] == "'" and level == brac):
                for j in data:
                    if j.startswith(cur):
                        print(chr(int(j.split(':')[2])),end=' ')
            
            #c
            elif i == 'c' and S[iin+1] != "'" and level == brac:
                for j in data:
                    if j.startswith(cur):
                        if int(j.split(':')[2]) >= 0 and int(j.split(':')[2]) <= 9:
                            print(int(j.split(':')[2]))
                        elif int(j.split(':')[2]) >= 10:
                            print(chr(int(j.split(':')[2])))
            
            #C
            elif i == 'C' and S[iin+1] != "'" and level == brac:
                for j in data:
                    if j.startswith(cur):
                        if int(j.split(':')[2]) >= 0 and int(j.split(':')[2]) <= 9:
                            print(int(j.split(':')[2]),end='')
                        elif int(j.split(':')[2]) >= 10:
                            print(chr(int(j.split(':')[2])),end='')
            
            #c' C'
            elif (i == 'c' and S[iin+1] == "'" and level == brac) or (i == 'C' and S[iin+1] == "'" and level == brac):
                for j in data:
                    if j.startswith(cur):
                        if int(j.split(':')[2]) >= 0 and int(j.split(':')[2]) <= 9:
                            print(int(j.split(':')[2]),end=' ')
                        elif int(j.split(':')[2]) >= 10:
                            print(chr(int(j.split(':')[2])),end=' ')
            
            #_
            elif i == '_' and level == brac:
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+'0'
                        cval = 0
                    else:
                        jin += 1

            #?
            elif i == '?' and level == brac:
                ran = random.randint(33,126)
                jin = 0
                for j in data:
                    if j.startswith(cur):
                        data[jin] = cur+str(ran)
                        cval = ran
                    else:
                        jin += 1
            
            #=
            elif i == '=' and S[iin+1] != "'" and level == brac:
                didfind = False
                iseq = False
                if cval == getvalue(ccol,crow-1):
                    iseq = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    iseq = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and iseq == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and iseq == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #='
            elif i == '=' and S[iin+1] == "'" and level == brac:
                didfind = False
                iseq = False
                if cval == getvalue(ccol,crow-1):
                    iseq = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                else:
                    iseq = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and iseq == True:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
                elif didfind == False and iseq == False:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
            
            #>'
            elif i == '>' and S[iin+1] == "'" and S[iin+1] != "," and level == brac:
                didfind = False
                isgr = False
                if cval > getvalue(ccol,crow-1):
                    isgr = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    isgr = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isgr == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isgr == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #>.
            elif i == '>' and S[iin+1] != "'" and S[iin+1] == "." and level == brac:
                didfind = False
                isgr = False
                if cval >= getvalue(ccol,crow-1):
                    isgr = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    isgr = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isgr == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isgr == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #<'
            elif i == '<' and S[iin+1] == "'" and S[iin+1] != "," and level == brac:
                didfind = False
                isls = False
                if cval < getvalue(ccol,crow-1):
                    isls = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    isls = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isls == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isls == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #<.
            elif i == '<' and S[iin+1] != "'" and S[iin+1] == "." and level == brac:
                didfind = False
                isls = False
                if cval <= getvalue(ccol,crow-1):
                    isls = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    isls = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isls == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isls == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')

            #&
            elif i == '&' and S[iin+1] != "'" and level == brac:
                didfind = False
                bothnot0 = False
                if cval != 0 and getvalue(ccol,crow-1) != 0:
                    bothnot0 = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    bothnot0 = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and bothnot0 == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and bothnot0 == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #&'
            elif i == '&' and S[iin+1] == "'" and level == brac:
                didfind = False
                both0 = False
                if cval == 0 and getvalue(ccol,crow-1) == 0:
                    both0 = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                else:
                    both0 = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and both0 == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and both0 == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #|
            elif i == '|' and S[iin+1] != "'" and level == brac:
                didfind = False
                isor = False
                if (cval != 0 and getvalue(ccol,crow-1) != 0) or (cval != 0 and getvalue(ccol,crow-1) == 0) or (cval == 0 and getvalue(ccol,crow-1) != 0):
                    isor = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                elif (cval == 0 and getvalue(ccol,crow-1) == 0):
                    isor = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isor == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isor == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
            #|'
            elif i == '|' and S[iin+1] == "'" and level == brac:
                didfind = False
                isor = False
                if (cval != 0 and getvalue(ccol,crow-1) == 0) or (cval == 0 and getvalue(ccol,crow-1) != 0):
                    isor = True
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':1'
                            didfind = True
                        else:
                            jin += 1
                elif (cval == 0 and getvalue(ccol,crow-1) == 0) or (cval != 0 and getvalue(ccol,crow-1) != 0):
                    isor = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                            data[jin] = str(ccol)+':'+str(crow+1)+':0'
                            didfind = True
                        else:
                            jin += 1
                if didfind == False and isor == True:
                    data.append(str(ccol)+':'+str(crow+1)+':1')
                elif didfind == False and isor == False:
                    data.append(str(ccol)+':'+str(crow+1)+':0')
            
                ''' : is replaced with A'
                    elif i == ':' and level == 0:
                    didfind = False
                    jin = 0
                    for j in data:
                        if j.startswith(str(ccol)+':'+str(crow-1)+':'):
                            data[jin] = str(ccol)+':'+str(crow-1)+':'+str(cval)
                            didfind = True
                        else:
                            jin += 1
                    if didfind == False:
                        data.append(str(ccol)+':'+str(crow-1)+':'+str(cval))
                    '''
            
            #*
            elif i == '*' and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval*above)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval*above))
            
            #/
            elif i == '/' and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                if float(cval/above) == int(cval/above):
                    eq = True
                else:
                    eq = False
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        if eq == False:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval/above)
                        else:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(int(float(cval/above)))
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    if eq == False:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(cval/above))
                    else:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(int(float(cval/above))))
            
            #-'
            elif i == '-' and S[iin+1] == "'" and S[iin+1] != "." and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval-above)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval-above))
            
            #+'
            elif i == '+' and S[iin+1] == "'" and S[iin+1] != "." and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval+above)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval+above))
            
            #^'
            elif i == '^' and S[iin+1] == "'" and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval**above)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval**above))
            
            #s
            elif i == 's' and level == brac:
                jin = 0
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval**2)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval**2))
            
            #t
            elif i == 't' and level == brac:
                jin = 0
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval**cval)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval**cval))
            
            #r
            elif i == 'r' and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                if float(math.pow(cval,1/above)) == int(math.pow(cval,1/above)):
                    eq = True
                else:
                    eq = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        if eq == True:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(int(float(math.pow(cval,1/above))))
                        else:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(math.pow(cval,1/above))
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    if eq == True:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(int(float(math.pow(cval,1/above)))))
                    else:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(math.pow(cval,1/above)))
            
            #R
            elif i == 'R' and level == brac:
                jin = 0
                didfind = False
                if float(math.pow(cval,1/2)) == int(math.pow(cval,1/2)):
                    eq = True
                else:
                    eq = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        if eq == True:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(int(float(math.pow(cval,1/2))))
                        else:
                            data[jin] = str(ccol)+':'+str(crow+1)+':'+str(math.pow(cval,1/2))
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    if eq == True:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(int(float(math.pow(cval,1/2)))))
                    else:
                        data.append(str(ccol)+':'+str(crow+1)+':'+str(math.pow(cval,1/2)))

            #%
            elif i == '%' and level == brac:
                jin = 0
                above = getvalue(ccol,crow-1)
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(cval%above)
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(cval%above))
            
            #!
            elif i == '!' and level == brac:
                jin = 0
                didfind = False
                for j in data:
                    if j.startswith(str(ccol)+':'+str(crow+1)+':'):
                        data[jin] = str(ccol)+':'+str(crow+1)+':'+str(math.factorial(cval))
                        didfind = True
                    else:
                        jin += 1
                if didfind == False:
                    data.append(str(ccol)+':'+str(crow+1)+':'+str(math.factorial(cval)))
            
            iin += 1
            
            '''elif i == '[' and level == 0:
                level = 1
                if S[S.index(i)+1] == 'I':
                    if S[S.index(i)+2] == '>':
                        Iinp = input('I.>')
                        yin = 0
                        for y in Iinp:
                            jin = 0
                            for j in data:
                                if j.startswith(cur):
                                    data[jin] = cur+str(ord(Iinp[yin]))
                                else:
                                    jin += 1
                            ccol -= 1
                            cval = int(getvalue(ccol,crow))
                            yin += 1
                            

            
                elif i == '[' and level == 0:
                level = 1
                if S[Sid+1] == 'z':
                    while cval != 0:
                        gin = Sid+2
                        for g in S[Sid+2:]:
                            if g != ']':
                                if g == '>':
                                    ccol -= 1
                                    cval = int(getvalue(ccol,crow))
                                    cur = str(ccol)+':'+str(crow)+':'
                                    if cur+str(cval) not in data:
                                        add()
                                    updval()
                Sid += 1'''




while True:
    print('Type "c" to start coding (then type "exit" or "~~" to exit); type "o" to open a file; type "t" to use the text generator ("~~" to exit)')
    og = str(input())
    if og == 'c':
        kod = input()
        while kod != 'exit' and kod != '~~':
            gamaplee(kod)
            print('/---\\')
            reset()
            kod = input()
    elif og == 'o':
        print('Enter file path')
        pat = input()
        fil = open(pat, "r")
        cod = fil.read()
        fil.close()
        gamaplee(cod)
        print('/---\\')
        reset()
    elif og == 't':
        tex = input('Enter text>')
        if tex == '~~':
            continue
        prn = input('Enter the output command>')
        while tex != '~~' and prn != '~~':
            print(convert(tex,prn))
            tex = input('Enter text>')
            prn = input('Enter the output command>')


