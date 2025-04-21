from collections import deque


def tree_by_levels(node):

    if node is None:
        return []

    sorted_nodes = []
    queue = deque([node])

    while queue:

        current = queue.popleft()
        sorted_nodes.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sorted_nodes
