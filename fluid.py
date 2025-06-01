
def fluid(matrix : list[list[int]]) -> tuple[list[list[int]] , list[list[int]]]: 
    n = len(matrix)
    p = [[0 for _ in range(n)] for _ in range(n)]

    for k in range(n) : 
        for i in range(n) :
            for j in range(n):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j] 
                    p[i][j] = k
    return matrix,p
                    
def get_all_intermediate_verticles(p : list[list[int]],
                                   i : int,
                                   j : int):
    if p[i][j] != 0 :
        get_all_intermediate_verticles(p,i,p[i][j]) 
        print(p[i][j])
        get_all_intermediate_verticles(p,p[i][j],j)

def main():
    INF = float('inf')
    adj_matrix = [[0,5,INF,INF],
                  [50,0,15,5],
                  [30,INF,0,15],
                  [15,INF,5,0]]
    m , p = fluid(adj_matrix)
    get_all_intermediate_verticles(p,0,2)

main()