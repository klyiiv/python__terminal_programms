def draw_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()
 
 
def matrix_horizontal_reflection(matrix):
    for i in matrix:
        for j in reversed(i):
            print(j, end=' ')
        print()
 
 
def matrix_vertical_reflection(matrix):
    for i in reversed(matrix):
        for j in i:
            print(j, end=' ')
        print()
 
 
def matrix_tranpone(matrix):
    for i in list(zip(*matrix)):
        for j in i:
            print(j, end=' ')
        print()
