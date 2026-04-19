def sumCorners(n):
    "Scita rohove prvky v stvorcoch do velkosti n - neparne"
    s = 1
    st = 3
    for l in range(3, n + 1, 2):
        s += 4 * st + 6 * (l - 1)
        st += 3 * (l - 1) + l + 1
    
    return s
