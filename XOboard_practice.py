# # A1 = 'X'
# # A2 = 'O'
# # A3 = 'X'
# # B1 = 'X'
# # B2 = 'X'
# # B3 = 'X'
# # C1 = 'O'
# # C2 = 'O'
# # C3 = 'O'

# # #Creating test for board printing using individual variables for each space on the board

# # Row0 = '       1    2    3 '
# # Row1 = 'A',A1,A2,A3
# # Row2 = 'B',B1,B2,B3,
# # Row3 = 'C',C1,C2,C3,
# # print(Row0)
# # print(Row1)
# # print(Row2)
# # print(Row3)

# #graph of the nodes, with horizontal and verticals
# # #to determine win conditions
# # import math
# # SQ = math.sqrt(11)
# # board_graph = {
# #     'A1' : {'A2':1,'B1':10, 'B2': SQ},
# #     'A2' : {'A1':1, 'A3':1,'B1': SQ,'B2':10,'B3':SQ},
# #     'A3' : {'A2':1, 'B2':SQ, 'B3':10},
# #     'B1' : {'A1':10,'A2':SQ,'B2':1,'C1':10,'C2':SQ},
# #     'B2' : {'A1':SQ,'A2':10,'A3':SQ,'B1':1,'B3':1,'C1':SQ,'C2':10,'C3':SQ},
# #     'B3' : {'A2':SQ,'B2':1,'C2':SQ,'C3':10},
# #     'C1' : {'B1':10,'B2':SQ,},
# #     'C2' : {'C1':1,'C3':1,'B1':SQ,'B2':10,'B3':SQ}
# # }

# # print(SQ + SQ)

# board_list = [[' '],['o'],['o'],['o'],['x'],['o'],['x'],['o'],['x']]
# def printboard(): 
#     print('_________________________'),
#     print('|       |       |       |'),
#     print('|',board_list[0],'|',board_list[1],'|',board_list[2],'|'),
#     print('|       |       |       |'),
#     print('|-----------------------|'),
#     print('|       |       |       |'),
#     print('|',board_list[3],'|',board_list[4],'|',board_list[5],'|'),
#     print('|       |       |       |'),
#     print('|-----------------------|'),
#     print('|       |       |       |'),
#     print('|',board_list[6],'|',board_list[7],'|',board_list[8],'|'),
#     print('|       |       |       |'),
#     print('|-----------------------|')


# printboard()
player_counter = 10
opposite_counter = 20

print(player_counter)
print(opposite_counter)
def swap(a, b):
    a,b = b,a

swap(a = player_counter,b = opposite_counter)
print(player_counter)
print(opposite_counter)


