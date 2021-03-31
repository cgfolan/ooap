A1 = 'X'
A2 = 'O'
A3 = 'X'
B1 = 'X'
B2 = 'X'
B3 = 'X'
C1 = 'O'
C2 = 'O'
C3 = 'O'

#Creating test for board printing using individual variables for each space on the board

Row0 = '       1    2    3 '
Row1 = 'A',A1,A2,A3
Row2 = 'B',B1,B2,B3,
Row3 = 'C',C1,C2,C3,
print(Row0)
print(Row1)
print(Row2)
print(Row3)


import math
SQ = math.sqrt(11)
board_graph = {
    'A1' : {'A2':1,'B1':10, 'B2': SQ},
    'A2' : {'A1':1, 'A3':1,'B1': SQ,'B2':10,'B3':SQ},
    'A3' : {'A2':1, 'B2':SQ, 'B3':10},
    'B1' : {'A1':10,'A2':SQ,'B2':1,'C1':10,'C2':SQ},
    'B2' : {'A1':SQ,'A2':10,'A3':SQ,'B1':1,'B3':1,'C1':SQ,'C2':10,'C3':SQ},
    'B3' : {'A2':SQ,'B2':1,'C2':SQ,'C3':10},
    'C1' : {'B1':5,'B2':SQ,},
    'C2' : {'C1':1,'C3':1,'B1':SQ,'B2':10,'B3':SQ}
}

print(SQ + SQ)
