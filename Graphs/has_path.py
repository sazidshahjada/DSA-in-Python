def has_path_depth(graph: dict, src, dst) -> bool:
    if src == dst: return True

    for neigbour in graph[src]:
        if has_path_depth(graph, neigbour, dst):
            return True
        
    return False


if __name__ == '__main__':
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    has_path = has_path_depth(graph, 'f', 'j')
    
    if has_path:
        print('Has Path')
    else:
        print('Has No Path')