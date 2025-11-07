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
            row.append(A[subset[i], subset[j]])
        
        A_new.append(row)
    return A_new

