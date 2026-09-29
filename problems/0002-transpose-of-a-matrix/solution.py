def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    tr = []
    n, m = len(a), len(a[0])
    for i in range(m):
        ri = []
        for j in range(n):
            ri.append(a[j][i]);
        tr.append(ri)
    return tr
    