import numpy as np 
matrix=np.array([[20,17,23,15,2],[10,9,12,7,3],[12,11,14,10,4],[16,16,19,14,4],[11,12,14,12,4]])
b=np.array([18,11,11,17])
def dtr(matrixd,det=0):
    det=det
    for el in range(len(matrix[0])):
        a=matrix[0][el]
        if el%2==0:
            print('четное')
        else:
            print('нечетное')
            a=-a
        newMatrix=np.delete(matrix,0,0)
        newMatrix=np.delete(newMatrix,el,1)
        print(f'a={a}')
        print(newMatrix)
        if len(newMatrix)==3:
            algebraic=triple(newMatrix)*a
            print(algebraic)
            print('')
            print('')
            print('')
            det=det+algebraic
        else:
            dtr(newMatrix,det)

    print(f'det(matrix)={det}')
def triple(matrix):
    sol=f'({matrix[0][0]}*{matrix[1][1]}*{matrix[2][2]})+({matrix[0][1]}*{matrix[1][2]}*{matrix[2][0]})+({matrix[0][2]}*{matrix[1][0]}*{matrix[2][1]})-({matrix[0][2]}*{matrix[1][1]}*{matrix[2][0]})-({matrix[0][1]}*{matrix[1][0]}*{matrix[2][2]})-({matrix[0][0]}*{matrix[1][2]}*{matrix[2][1]})'
    print(f'det(3)={sol}')
    print(f'det(3)={eval(sol)}')
    return eval(sol)
def Kramer(matrix,b):
    for el in range(len(matrix[0])):
        altMatrix=matrix.copy()
        altMatrix=np.transpose(altMatrix)
        altMatrix[el]=b
        altMatrix=np.transpose(altMatrix)
        print(altMatrix)
        print('----------------------------------------------------------------')
        dtr(altMatrix)
        print('                          НОВАЯ МАТРИЦА               ')
dtr(matrix)