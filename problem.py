from primes import primeFactDecomp
from gmpy2 import mpq
from itertools import combinations


def createAdepts(l):
    A = {}
    for n in range(2, l + 1):
        D = primeFactDecomp(n)
        a = True
        for p in D.keys():
            if p != 2:
                if p ** D[p] * 2 > l:
                    a = False
                    break
            else:
                if p ** D[p] * 3 > l:
                    a = False
                    break

        if a:
            A[n] = D

    return A


def getNumbersByPrimes(A):
    N = {}
    for a in list(A.keys()):
        for p in A[a]:
            if p ** A[a][p] in N:
                N[p ** A[a][p]] += [a]
            else:
                N[p ** A[a][p]] = [a]

    return N


def createPartialSums(A):
    S = {}
    i = 0
    for a in A:
        ss = 0
        for av in list(A.keys())[i:]:
            ss += 1 / av ** 2
        S[a] = ss
        i += 1

    return S


def problem152(l):
    A = createAdepts(l)
    N = getNumbersByPrimes(A)
    S = createPartialSums(A)
    SolvedStates = set()

    Sols = []

    def findSols(cs, csol, av, req, pres):
        nonlocal Sols
        fs = frozenset(csol)
        if fs in SolvedStates:
            return

        SolvedStates.add(fs)

        if cs > 1 / 2:
            return

        if len(req) > 0:

            rq = req[0]
            pw = 1
            while rq in N:
                for mul in N[rq]:
                    if mul in av:
                        npres = set(pres)
                        nreq = list(req)
                        nav = set(av)
                        nav.remove(mul)

                        for p in A[mul]:
                            ppw = p ** A[mul][p]
                            if ppw not in pres:
                                cur = p
                                while cur < ppw:
                                    if cur in nreq:
                                        nreq.remove(cur)
                                    npres.add(cur)
                                    cur *= cur

                                if ppw in nreq:
                                    nreq.remove(ppw)
                                    npres.add(ppw)

                                else:
                                    nreq.append(ppw)

                        findSols(cs + 1 / mul ** 2, csol + [mul], set(nav), list(nreq), set(npres))

                rq *= rq
                pw += 1

        else:
            if cs == 1 / 2:
                Sols.append(csol)
                return

            for aval in av:
                if cs + S[aval] < 1 / 2:
                    return

                npres = set(pres)
                nreq = list(req)
                nav = set(av)

                for p in A[aval]:
                    ppw = p ** A[aval][p]
                    if ppw not in pres:
                        cur = p
                        while cur < ppw:
                            npres.add(cur)
                            cur *= cur

                        nreq.append(ppw)

                nav.remove(aval)
                findSols(cs + 1 / aval ** 2, csol + [aval], set(nav), list(nreq), set(npres))

    findSols(1 / 4 + 1 / 9, [2, 3], set(list(A.keys())[2:]), [2, 3], set())

    findSols(1 / 4 + 1 / 16, [2, 4], set([3] + list(A.keys())[3:]), [4], set([2]))

    return Sols


def findGroups(l):
    A = createAdepts(l)
    if l <= 80:
        nonsolvable = set([11, 31, 16, 17, 19, 23, 25, 27, 29, 37])
        for adept in list(A.keys()):
            Prim_pows = set()
            for p in A[adept]:
                Prim_pows.add(p ** A[adept][p])

            if len(Prim_pows & nonsolvable) > 0:
                del A[adept]

    N = getNumbersByPrimes(A)
    N[2] = N[2][1:]
    G = {}
    for p in N:
        G[p] = {}

    for k in list(N.keys())[:0:-1]:
        LA = []
        pw = A[k][list(A[k].keys())[0]]

        for nu in N[k]:
            LA += [tuple([mpq(1, nu ** 2), set([nu])])]

        k2 = k * list(A[k].keys())[0]
        while k2 in N:
            if 2 * pw in G[k2]:
                for comb in G[k2][2 * pw]:
                    LA += [tuple([comb[0], comb[1]])]

            if 2 * pw - 1 in G[k2]:
                for comb in G[k2][2 * pw - 1]:
                    LA += [tuple([comb[0], comb[1]])]

            k2 *= list(A[k].keys())[0]

        print(k, len(LA))
        Cache = {0: mpq(0, 1), 1: LA[-1][0]}
        for ss in range(2, 2 ** len(LA)):
            bi = bin(ss)[2:]
            su = mpq(0, 1)
            if k == 2:
                su = mpq(1, 4)

            found = bi.find('1')
            if found < len(bi) - 1:
                rest = int(bi[found + 1:], 2)
                su += Cache[rest]
            su += LA[found - len(bi)][0]

            Cache[ss] = su

            cur_pw = 2 * pw - 2
            if k == 2:
                cur_pw = 1

            base = list(A[k].keys())[0]

            while cur_pw >= 0:
                if su.denominator % (base ** (cur_pw + 1)) != 0 and su.denominator % (base ** cur_pw) == 0:
                    st = set()
                    ind = -1
                    for b in bi[::-1]:
                        if b == '1':
                            st = st | LA[ind][1]
                        ind -= 1

                    if cur_pw in G[k]:
                        G[k][cur_pw].append(tuple([su, st]))
                    else:
                        G[k][cur_pw] = [tuple([su, st])]

                cur_pw -= 1

    return G, A


def find93(G, A):
    to_be_avoided = set([9, 18, 72])
    for sol in G[3][0]:
        Found = False
        for e in sol[1]:
            if 3 in A[e] and A[e][3] == 2:
                if len(sol[1] & to_be_avoided) == 0:
                    print(sol)
                else:
                    break


def buildCombinations(G, A):
    Groups = []
    ignored = set([2, 4, 8])

    def tryBuildGroup(startGroup, resolved, resolved_nines=set()):
        nonlocal Groups
        M = {}
        for member in startGroup:
            M[member] = A[member]
        Prime_pows = getNumbersByPrimes(M)
        unresolved = set(Prime_pows.keys()) - resolved - ignored
        if len(unresolved) == 0:
            Groups.append(startGroup)

        else:
            unres_M = max(unresolved)
            must_be_incl = set(Prime_pows[unres_M])
            if unres_M == 9:
                must_be_incl = set(Prime_pows[unres_M]) - resolved_nines

            if 0 in G[unres_M]:
                for potential_addition in G[unres_M][0]:
                    if (potential_addition[1] & must_be_incl) == must_be_incl:
                        addible = True
                        for pot_add in potential_addition[1] - must_be_incl:
                            if len(set(
                                    [pot_add_p ** A[pot_add][pot_add_p] for pot_add_p in A[pot_add]]) & resolved) > 0:
                                addible = False
                                break

                        if addible:
                            n_start_g = startGroup | potential_addition[1]
                            n_resolved = resolved | set([unres_M])
                            tryBuildGroup(n_start_g, n_resolved, resolved_nines)

    for sol3 in G[3][0]:
        contains9 = False
        res_9 = set()
        for elem3 in sol3[1]:
            if A[elem3][3] == 2:
                contains9 = True
                res_9.add(elem3)

        if contains9:
            tryBuildGroup(sol3[1], set([3]), res_9)
        else:
            tryBuildGroup(sol3[1], set([3]))

    Sol4 = []
    for rem4 in G[4]:
        Sol4 += G[4][rem4]

    for sol4 in Sol4:
        if 4 not in sol4[1]:
            continue

        feasible = True
        for elem4 in sol4[1]:
            if 3 in A[elem4] and A[elem4][3] == 1:
                feasible = False
                break

        if feasible:
            tryBuildGroup(sol4[1], set([3]))

        '''tryBuildGroup(sol4[1], set())'''

    return Groups


def buildCombinations_n(G, A):
    Groups = []
    ignored = set([2, 4, 8, 3, 9])

    def tryBuildGroup_n(startGroup, resolved):
        nonlocal Groups
        M = {}
        for member in startGroup:
            M[member] = A[member]
        Prime_pows = getNumbersByPrimes(M)
        unresolved = set(Prime_pows.keys()) - resolved - ignored
        if len(unresolved) == 0:
            Groups.append(startGroup)

        else:
            unres_M = max(unresolved)
            must_be_incl = set(Prime_pows[unres_M])

            if 0 in G[unres_M]:
                for potential_addition in G[unres_M][0]:
                    if (potential_addition[1] & must_be_incl) == must_be_incl:
                        addible = True
                        for pot_add in potential_addition[1] - must_be_incl:
                            if len(set(A[pot_add].keys()) & resolved) > 0:
                                addible = False
                                break

                        if addible:
                            n_start_g = startGroup | potential_addition[1]
                            n_resolved = resolved | set([unres_M])
                            tryBuildGroup_n(n_start_g, n_resolved)

    for pr_pw in G:
        if pr_pw in ignored:
            continue

        if 0 in G[pr_pw]:
            for start_sol in G[pr_pw][0]:
                tryBuildGroup_n(start_sol[1], set([pr_pw]))

    return Groups


def testCombinations(GR):
    potential_additions = [tuple([mpq(0, 1), set()]), tuple([mpq(1, 4 ** 2), set([4])]),
                           tuple([mpq(1, 8 ** 2), set([8])]), tuple([mpq(1, 4 ** 2) + mpq(1, 8 ** 2), set([4, 8])])]
    GRf = []

    for gr in GR:
        sm = mpq(1, 4)
        for mem in gr:
            sm += mpq(1, mem ** 2)

        for pot_add in potential_additions:
            if sm + pot_add[0] == mpq(1, 2):
                GRf.append(gr | pot_add[1] | set([2]))

    return GRf


def testCombinations_n(GR):
    potential_additions = [2, 4, 8, 3, 9]
    GRf = []

    for gr in GR:
        sm = mpq(1, 4)
        for mem in gr:
            sm += mpq(1, mem ** 2)

        for pot_add_len in range(len(potential_additions) + 1):
            for pot_add in combinations(potential_additions, pot_add_len):
                pot_add_frac = mpq(0, 1)
                for add_elem in pot_add:
                    pot_add_frac += mpq(1, add_elem ** 2)

                if sm + pot_add_frac == mpq(1, 2):
                    GRf.append(gr | set(pot_add) | set([2]))

    return GRf


def tryFilterDuplicates(GRf):
    GRff = set()
    for grf in GRf:
        GRff.add(frozenset(grf))

    return GRff


def problem152n(l):
    return tryFilterDuplicates(testCombinations(buildCombinations(*findGroups(l))))


def problem152_n_n(l):
    return tryFilterDuplicates(testCombinations_n(buildCombinations_n(*findGroups(l))))



GR = problem152n(80)



