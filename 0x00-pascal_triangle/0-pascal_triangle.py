def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    
    Args:
        n (int): The number of rows of Pascal's triangle to generate.
        
    Returns:
        List[List[int]]: A list of lists representing the rows of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle
    
    for i in range(1, n):
        row = [1]  # First element of the row is always 1
        for j in range(1, i):
            # Each triangle element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element of the row is always 1
        triangle.append(row)
    
    return triangle

