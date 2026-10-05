def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows = len(a) # 3 
    cols = len(a[0]) # 2
    result = [] 
    for i in range(cols) : 
        new_row = [] #1st iter - gets created 
        for j in range(rows):
            new_row.append(a[j][i]) 
        result.append(new_row)
    return result
    pass