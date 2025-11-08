# generate graph by the adjecency matrix
def adjacency_matrix(n):
    A = []
    for i in range(n):
        row = [] 
        for j in range(n):
            while True:
                try:
                    value = int(input(f'A[{i + 1}][{j + 1}] = '))
                    if value != 0 and value != 1:
                        print("use only 0 or 1\n")
                        continue
                    row.append(value)
                    break
                except ValueError:
                    print("enter the integer value\n")
        A.append(row) 
    return A

# generate right subgraph on new collection
def right_subgraph(subset, A):
    A_new = []
    n = len(subset)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[subset[i]][subset[j]])
        
        A_new.append(row)
    return A_new

# union
def graphs_union(A, B):
    n1 = len(A) 
    n2 = len(B)  
    cur_size = n1 + n2
    
    R = [[0] * cur_size for _ in range(cur_size)]  
    

    for i in range(n1):
        for j in range(n1):
            R[i][j] = A[i][j]
    
    for i in range(n2):
        for j in range(n2):
            R[i + n1][j + n1] = B[i][j]
    
    return R

# connection
def graphs_connection(A, B):
    n1 = len(A)  
    n2 = len(B) 
    cur_size = n1 + n2
    
    R = [[0] * cur_size for _ in range(cur_size)] 

    for i in range(n1):
        for j in range(n1):
            R[i][j] = A[i][j]
    
  
    for i in range(n2):
        for j in range(n2):
            R[i + n1][j + n1] = B[i][j]
    
    
    for i in range(n1):
        for j in range(n2):
            R[i][j + n1] = 1  
            R[j + n1][i] = 1 
    
    return R

# intersect ( A.size = B.size)
def graphs_intersection(A, B):
    if (len(A) != len(B)):
        print("we're work on this, try later...\n")
        return
    
    n = len(A) 
    
    R = [[0] * n for _ in range(n)]  
    
    for i in range(n):
        for j in range(n):
            if A[i][j] == 1 and B[i][j] == 1:
                R[i][j] = 1
    
    return R

# addition
def graph_addition(A):
    n = len(A)
    complement = []
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                if A[i][j] == 1:
                    row.append(0)
                else:
                    row.append(1)
            else:
                row.append(0)
        complement.append(row)
    return complement


# last operation from screenshot
def remove_vertex(graph, vertex_index):
    n = len(graph)
    
    if vertex_index < 0 or vertex_index >= n:
        raise ValueError("incorrect index")
    
    new_graph = []
    
    for i in range(n):
        if i == vertex_index:
            continue 
        
        new_row = []
        for j in range(n):
            if j == vertex_index:
                continue  
            
            new_row.append(graph[i][j])
        
        new_graph.append(new_row)
    
    return new_graph

def print_graph(graph):
    for row in graph:
        print(row)
    print()
