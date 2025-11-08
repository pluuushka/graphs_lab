from utils import *

def demonstrate_operations():
    print("Demonstration of operations")
    print("=" * 50)
   

    print("1. Creating graphs")
    print("-" * 30)
    

    A = [
        [0, 1, 1],
        [1, 0, 1], 
        [1, 1, 0]
    ]
    print("Graph A :")
    print_graph(A)
    

    B = [
        [0, 1],
        [1, 0]
    ]
    print("Graph B :")
    print_graph(B)
    
    C = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    print("Graph C :")
    print_graph(C)
    
    # 2. Right subgrapgh
    print("2. Right subgraph")
    print("-" * 30)
    subset = [0, 2]  
    result = right_subgraph(subset, A)

    print(f"Right subgraph A on {subset}:")
    print_graph(result)
    
    # 3. Union
    print("3. A ∪ B")
    print("-" * 30)
    union_result = graphs_union(A, B)
    print("Result of union:")
    print_graph(union_result)
    
    # 4. Connection
    print("4. A + B")
    print("-" * 30)
    connection_result = graphs_connection(A, B)
    print("Result of connection:")
    print_graph(connection_result)
    
    # 5. Intersect
    print("5. A ∩ C")
    print("-" * 30)
    intersection_result = graphs_intersection(A, C)
    print("Result of intersect:")
    print_graph(intersection_result)
    
    # 6. Addition
    print("6. Addition A")
    print("-" * 30)
    
    result_of_add = graph_addition(A)
    print("Graph addition A:")
    print_graph(result_of_add)
    
    # 7. Delete vertex
    print("7. Delete vertex from A")
    print("-" * 30)
    removed_result = remove_vertex(A, 0)
    print("Graph A after deleting 0:")
    print_graph(removed_result)

def demonstrate_with_user_input():
    print("\n" + "=" * 50)
    print("User input: ")
    print("=" * 50)
    

    print("Enter the matrix adjacency:")
    n = int(input("Enter the count of vertex: "))
    user_graph = adjacency_matrix(n)
    
    print("\nCreated graph:")
    print_graph(user_graph)
    
    if n > 0:
        vertex_to_remove = int(input(f"Enter the index to delete (0-{n-1}): "))
        result = remove_vertex(user_graph, vertex_to_remove)
        print(f"\nGraph after deleted {vertex_to_remove}:")
        print_graph(result)

if __name__ == "__main__":
    demonstrate_operations()
    #demonstrate_with_user_input()