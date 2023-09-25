def image_filter(pixels, i, j):
    r, g, b = pixels[i, j]
    r1, g1, b1 = pixels[i - 1, j - 1]
    r2, g2, b2 = pixels[i + 1, j + 1]
    n1 = (r1 * g1 * b1) ** (1 / 3)
    n2 = (r2 * g2 * b2) ** (1 / 3)
    n = (n1 + n2) // 2
    r, g, b = r + n, g + n, b + n
    return r, g, b
