# write your solution here
def matrix_sum():
    sum = 0
    with open("matrix.txt") as f:
        for line in f:
            line = line.replace("\n","")
            line = line.split(",")
            for i in range(len(line)):
                sum += int(line[i])
    return sum

def matrix_max():
    max = 0
    with open("matrix.txt") as f:
        for line in f:
            line = line.replace("\n","")
            line = line.split(",")
            for i in range(len(line)):
                if int(line[i]) > max:
                    max = int(line[i])
    return max

def row_sums():
    lst = []
    with open("matrix.txt") as f:
        for line in f:
            sum = 0
            line = line.replace("\n","")
            line = line.split(",")
            for i in range(len(line)):
                sum += int(line[i])
            lst.append(sum)
    return lst

# OFFICIAL SOLUTION TIP: USE HELPER FUNCTIONS 
# def read_matrix():
#     with open("matrix.txt") as file:
#         m = []
#         for row in file:
#             mrow = []
#             items = row.split(",")
#             for item in items:
#                 mrow.append(int(item))
#             m.append(mrow)
 
#     return m
 
# # Yhdistää matriisin rivit yhdeksi listaksi
# def combine(matriisi: list):
#     mlist = []
#     for row in matriisi:
#         mlist += row
    
#     return mlist
 
# def matrix_sum():
#     mlist = combine(read_matrix())
#     return sum(mlist)
 
# def matrix_max():
#     mlist = combine(read_matrix())
#     return max(mlist)
 
# def row_sums():
#     matrix = read_matrix()
#     sums = []
#     for row in matrix:
#         sums.append(sum(row))
#     return sums