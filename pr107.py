
def removeEdges():
    f = open("p107_network.txt")
    M = []
    for l in f:
        L = [int(e) if e != '-' else '-' for e in l[:-1].split(',')]
        M.append(L)
    
    removed = 0
    while True:
        c = findCycle(M)
        if c is None:
            return removed
        
        m_A = -1
        m_B = -1
        m_v = 0
        for i in range(len(c)):
            if M[c[i]][c[(i + 1) % len(c)]] > m_v:
                m_A = c[i]
                m_B = c[(i + 1) % len(c)]
                m_v = M[m_A][m_B]
        
        removed += m_v
        M[m_A][m_B] = '-'
        M[m_B][m_A] = '-'
    
def findCycle(M):
    def visitNeighbours(V):
        c = 0
        for n in M[V[-1]]:
            if n != '-':
                if len(V) > 2 and c != V[-2] and c in V:
                    return V[V.index(c)::]
                
                if len(V) == 1 or (len(V) > 1 and c != V[-2]):
                    res = visitNeighbours(list(V) + [c])
                    if res is not None:
                        return res
            c += 1
        return None
    
    return visitNeighbours([0])
                
    
