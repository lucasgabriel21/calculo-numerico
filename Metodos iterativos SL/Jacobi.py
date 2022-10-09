a = [[3.252, -0.04571, 0.3966],
     [-0.02214, 1.662, 0.06004],
     [0.6193, -0.5575, 2.857]]
b = [1, 1, 1]

def gauss_seidel(a, b, ite):
    """Retorna uma matriz com todas as soluções iteradas pelo método
    de Gauss-Seidel para um sistema linear 3x3"""
    x1 = 0
    x2 = 0
    x3 = 0
    solutions = []
    for i in range(ite):
        x1 = (b[0] - a[0][1]*x2 - a[0][2]*x3) / a[0][0]
        x2 = (b[1] - a[1][0]*x1 - a[1][2]*x3) / a[1][1]
        x3 = (b[2] - a[2][0]*x1 - a[2][1]*x2) / a[2][2]
        X = [x1, x2, x3]
        solutions.append(X)
    return solutions

def jacobi(a, b, ite):
    """Retorna uma matriz com todas as soluções iteradas pelo método
        de Jacobi para um sistema linear 3x3"""
    x1 = 0
    x2 = 0
    x3 = 0
    solutions = []
    for i in range(ite):
        x1_o = x1
        x2_o = x2
        x1 = (b[0] - a[0][1] * x2 - a[0][2] * x3) / a[0][0]
        x2 = (b[1] - a[1][0] * x1_o - a[1][2] * x3) / a[1][1]
        x3 = (b[2] - a[2][0] * x1_o - a[2][1] * x2_o) / a[2][2]
        X = [x1, x2, x3]
        solutions.append(X)
    return solutions

def diferencial_jacgauss(it):
    """Apresenta as diferenças a cada iteração da resolução de um sistema linear
    entre a solução obtida pelo método de Jacobi e o de Gauss-Seidel"""
    for i in range(it):
        print('\nIteração {}:\n'.format(i+1))
        for j in range(3):
            print(jacobi(a, b, it)[i][j] - gauss_seidel(a, b, it)[i][j])
