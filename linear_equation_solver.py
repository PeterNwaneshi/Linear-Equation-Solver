import numpy as np
def matrix_solver():
    """Solves linear equation of any n x n, n x m
    [a11, a12, .., a1n] | [ x1 ]   [b(r1)]
    [.     .   ..   . ] | [  . ]   [  .  ]
    [.     .   ..   . ] | [  . ] = [  .  ]
    [.     .   ..   . ] | [  . ]   [  .  ]
    [an1, an2, .., ann] | [ xn ]   [b(rn)]
    """

    try:
        ro = int(input('Matrix Size (No. of columns): = '))
        co = int(input('Matrix Size (No. of Rows): = '))

        r1 = []
        for j in range(co):
            for i in range(ro):
                i=i+1


                r = int(input('a{}{} = '.format(i,j+1)))
                r1.append(r)

        A = []
        for x in range(0, len(r1), ro):  
            A1 = r1[x:x + ro]
            A.append(A1)
        print('A = {}'.format(A))
        print('='*30)

        B = []
        for u in range(co):
            m = int(input('b({}{}) = '.format('r',u+1)))
            B.append(m)
        print('B = {}'.format(B))
        

        # Matrix A
        A = np.array(A)

        # Matrix B
        B = np.array(B)

        ans = np.linalg.solve(A,B)

        
        print('='*30)
        for result in range(len(ans)):
            print('X{} = {:.2f}'.format(result+1, ans[result]))
        print('*'*12,"End",'*'*12)
    except:
        print("There're issues with your supplied information")

###################################################################################################
print(matrix_solver.__doc__)
matrix_solver()
