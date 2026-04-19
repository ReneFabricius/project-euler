from math import ceil

def countPositionsCrossGrid(m, n, k, l):
    """Spocita pocet moznych umiestneni obdlznika kxl do sikmej mriezky obdlznika mxn, m >= n, k >= l"""
    if k + l > 2*n:
        return 0
    
    symet = (n - ceil(k/2) - ceil(l/2) + 1)*(n + ceil(k/2) - ceil(l/2) - k + 1)
    limited = (int((m - n)/2) - 1 + ceil(l/2) - int((l - ((m - n) % 2))/2))*(2*n - l - k +1)
    if limited > 0 or m == n:
        symet += limited 
    symet *= 2
    
    if (m - n + 1) % 2 != l % 2:
        return symet + 2*n - l - k + 1
    
    return symet
    
def countPositionsNormalGrid(m, n, k, l):
    if k > m or l > n:
        return 0
    
    return (m - k + 1)*(n - l + 1)
    
def computeForSingleRectangle(m, n):
    normal_grid_c = 0
    for k in range(1, m + 1):
        for l in range(1, n + 1):
            normal_grid_c += countPositionsNormalGrid(m, n, k, l)
    
    cross_grid_c = 0
    c_m, c_n = m, n
    if n > m:
        c_m, c_n = n, m
        
    for k in range(1, 2*n):
        l = 1
        while l <= k and k + l <= 2*n:
            c_count = countPositionsCrossGrid(c_m, c_n, k, l)
            if k != l:
                c_count *= 2
            cross_grid_c += c_count
            l += 1
    
    return normal_grid_c, cross_grid_c
    
def computeAllSubrectangles(M, N):
    count = 0
    for m in range(1, M + 1):
        for n in range(1, N + 1):
            count += sum(computeForSingleRectangle(m, n))
            
    return count
    
