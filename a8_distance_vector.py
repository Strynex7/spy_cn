def update_routing_table(matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix

num_nodes = int(input("Enter the number of nodes: "))
cost_matrix = []

for i in range(num_nodes):
    row_input = input(f"Enter {num_nodes} values for row {i+1} (space separated): ").split()
    row = [float('inf') if x == 'inf' else int(x) for x in row_input]
    cost_matrix.append(row)

final_matrix = update_routing_table(cost_matrix, num_nodes)

print("\nFinal Distance Vector Matrix:")
for row in final_matrix:
    print(row)