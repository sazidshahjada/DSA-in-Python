def depth_first_traverse(adj_list: dict, first_node):
    print('Depth First Traversal:')

    stack = [first_node]


    while stack:
        current_node = stack.pop()
        print(current_node, end=' ')
        neigbour_node = adj_list[current_node]

        for node in neigbour_node:
            stack.append(node)
            
    print()

def breadth_first_traverse(adj_list: dict, first_node):
    print('Breadth First Traversal:')

    queue = [first_node]

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=' ')
        neigbour_node = adj_list[current_node]

        for node in neigbour_node:
            queue.append(node)

    print()

if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }
    
    depth_first_traverse(graph, 'f')
    breadth_first_traverse(graph, 'f')