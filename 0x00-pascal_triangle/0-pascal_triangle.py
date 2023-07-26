def pascal_triangle(n):
    if n <= 0:
        return []

    triangles = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = triangles[-1]
        for j in range(1, i):
            row.append(prev_row[j-1] + prev_row[j])
        row.append(1)
        triangles.append(row)
    return triangles