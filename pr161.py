from functools import reduce
import operator
import copy


def contains_shape(L, shp):
    for l in L:
        if (l[0] == shp[0] and l[1] == shp[1]) or (l[0] == shp[1] and l[1] == shp[0]):
            return True

    return False


def rotate_base(BS_SHAPES, BS_ROTATED):
    for bs_shp in BS_SHAPES:
        rttd = bs_shp
        for r in range(4):
            if not contains_shape(BS_ROTATED, rttd):
                BS_ROTATED.append(rttd)
            rttd = [[rttd[0][1], -rttd[0][0]], [rttd[1][1], -rttd[1][0]]]


class AdvShape:
    def __init__(self, **kwargs):
        PWRS3 = kwargs['PWRS3']
        PWRS2 = kwargs['PWRS2']

        if 'M' in kwargs:
            M = kwargs['M']
            self.M_ = copy.deepcopy(M)
            self.h_ = len(M)
            self.w_ = len(M[0])
            self.bin_r_ = [0] * (self.w_ - 2) * 4  # top, left, down, right: cw
            self.in_s_ = self.h_ - 2
            self.sum_ = 0
            for r in M:
                self.sum_ += sum(r)

            mov_ind = [1, 1]
            fxd_ind = [[1, 0], [self.in_s_, self.in_s_ + 1]]
            bin_r_ind = 0
            for side in range(4):
                mov = 1 - side % 2
                fxd = side % 2
                fxd_l_ind = (side % 2 + side // 2) % 2
                change = 1 - (side // 2) * 2

                for i in range(self.in_s_):
                    inn = [-1, -1]
                    out = [-1, -1]
                    [inn[fxd], out[fxd]] = fxd_ind[fxd_l_ind]
                    inn[mov] = out[mov] = mov_ind[mov]

                    if i < self.in_s_ - 1:
                        mov_ind[mov] += change

                    if reduce(operator.getitem, inn, M) == 0:
                        self.bin_r_[bin_r_ind] = -1
                    elif reduce(operator.getitem, out, M) == 1:
                        self.bin_r_[bin_r_ind] = 1

                    bin_r_ind += 1

            self.hash_ = 0
            for i in range(len(self.bin_r_)):
                self.hash_ += (self.bin_r_[i] + 1) * PWRS3[i]

            self.sides_hashes_ = [[0, 0] for i in range(4)]  # top, right, down, left: increasing powers
            # from left to right and from top down, on first index irregularities inside, on second outside
            for side in range(4):
                dir = 1 - (side // 2) * 2
                start_ind = side * self.in_s_ + (side // 2) * (self.in_s_ - 1)
                for i in range(self.in_s_):
                    if self.bin_r_[start_ind + dir * i] < 0:
                        self.sides_hashes_[side][0] += PWRS2[i]
                    elif self.bin_r_[start_ind + dir * i] > 0:
                        self.sides_hashes_[side][1] += PWRS2[i]

        else:
            AS1 = kwargs['AS1']
            AS2 = kwargs['AS2']
            self.h_ = 2 * (len(AS1.M_) - 1)
            self.w_ = len(AS1.M_[0])
            self.in_w_ = self.w_ - 2
            self.M_ = [[0 for wi in range(self.w_)] for hi in range(self.h_)]
            for ri in range(len(AS1.M_)):
                for ci in range(len(AS1.M_[ri])):
                    self.M_[ri][ci] = AS1.M_[ri][ci]

            offset = len(AS1.M_) - 2
            for ri in range(len(AS2.M_)):
                for ci in range(len(AS2.M_[ri])):
                    if AS2.M_[ri][ci] == 1:
                        self.M_[offset + ri][ci] = AS2.M_[ri][ci]

            self.bin_r_ = [0 for i in range(2 * (self.h_ + self.w_ - 2 * 2))]
            for i in range(3 * self.in_w_):
                self.bin_r_[i + (i // (2 * self.in_w_)) * 3 * self.in_w_] = AS1.bin_r_[
                    i + (i // (2 * self.in_w_)) * self.in_w_]

            for i in range(3 * self.in_w_):
                self.bin_r_[i + 2 * self.in_w_] = AS2.bin_r_[i + self.in_w_]

            if self.bin_r_[2 * self.in_w_ - 1] < 1:
                self.bin_r_[2 * self.in_w_ - 1] = -1 if self.M_[self.in_w_][self.in_w_] == 0 else 0

            if self.bin_r_[2 * self.in_w_] < 1:
                self.bin_r_[2 * self.in_w_] = -1 if self.M_[self.in_w_ + 1][self.in_w_] == 0 else 0

            if self.bin_r_[5 * self.in_w_ - 1] < 1:
                self.bin_r_[5 * self.in_w_ - 1] = -1 if self.M_[self.in_w_ + 1][1] == 0 else 0

            if self.bin_r_[5 * self.in_w_] < 1:
                self.bin_r_[5 * self.in_w_] = -1 if self.M_[self.in_w_][1] == 0 else 0

            self.hash_ = 0
            for i in range(len(self.bin_r_)):
                self.hash_ += (self.bin_r_[i] + 1) * PWRS3[i]

            self.sides_hashes_ = [[0, 0] for i in range(4)]  # top, right, down, left: increasing powers
            # from left to right and from top down, on first index irregularities inside, on second outside
            side_lens = [self.in_w_, 2 * self.in_w_, self.in_w_, 2*self.in_w_]
            for side in range(4):
                dir = 1 - (side // 2) * 2
                start_ind = sum(side_lens[:side]) + (side // 2) * (side_lens[side] - 1)
                for i in range(side_lens[side]):
                    if self.bin_r_[start_ind + dir * i] < 0:
                        self.sides_hashes_[side][0] += PWRS2[i]
                    elif self.bin_r_[start_ind + dir * i] > 0:
                        self.sides_hashes_[side][1] += PWRS2[i]


def change_pick(P):
    if len(P) == 1:
        return False

    sum = P[-1]
    P[-1] = 0
    i = 2
    while P[-i] == 0:
        if i == len(P):
            return False
        i += 1

    P[-i] -= 1
    P[-i + 1] = sum + 1
    return True


def increment_group(G, m):
    if len(G) == 0:
        return False

    i = 1
    while G[-i] == m - i:
        i += 1
        if i > len(G):
            return False

    G[-i] += 1
    j = len(G) - i + 1
    while j < len(G):
        G[j] = G[j - 1] + 1
        j += 1

    return True


def assign_base_location(l):
    for i in range(len(l)):
        l[i] = i


def increment_locations(L, m):
    i = 1
    while not increment_group(L[-i], m):
        i += 1
        if i > len(L):
            return False
    j = len(L) - i + 1
    while j < len(L):
        assign_base_location(L[j])
        j += 1

    return True


def valid_loc(L, M, SHAPES):
    s_sz = len(M) - 2
    for ri in range(len(M)):
        for ci in range(len(M[ri])):
            M[ri][ci] = 0

    for si in range(len(L)):
        for spos in L[si]:
            r = (spos // s_sz) + 1
            c = (spos % s_sz) + 1
            for sqr in SHAPES[si] + [[0, 0]]:
                if M[r + sqr[0]][c + sqr[1]] != 0:
                    return False
                M[r + sqr[0]][c + sqr[1]] = 1

    if M[(s_sz + 1) // 2][(s_sz + 1) // 2] != 1:
        return False

    return True


def rotate_M(M, rot):
    rot_pos = (rot + 4) % 4
    M_temp = None
    M_rot = copy.deepcopy(M)
    SZ = len(M)
    for r in range(rot_pos):
        M_temp = copy.deepcopy(M_rot)
        for row in range(SZ):
            for col in range(SZ):
                M_rot[col][SZ - row - 1] = M_temp[row][col]

    return M_rot


def get_req(PW2, n):
    return ((n % PW2[9]) << 9) | (n // PW2[9])


def process_M(M, PWRS3):
    h = len(M) - 2
    w = len(M[0]) - 2
    SZ = [w, h]
    START_POINTS = [[[0, 1], [1, 1]], [[1, w + 1], [1, w]], [[h + 1, w], [h, w]], [[h, 0], [h, 1]]]
    abs_i = 0
    for s in range(4):
        ch = (1 - s//2)*2 - 1
        co = (s + 1) % 2
        lim_i = s % 2
        COORD_CH = [0, 0]
        for pi in range(SZ[lim_i]):
            COORD = START_POINTS[s]
    bin_r_ = [0] * (h + w) * 2  # top, left, down, right: cw

    hash_ = 0
    for i in range(len(bin_r_)):
        hash_ += (bin_r_[i] + 1) * PWRS3[i]


def find_adv_shapes(BASE_ROT, PWRS2, PWRS3):
    MAX_PLACED = 6
    POSs = 9
    M = [[0 for i in range(5)] for j in range(5)]
    PICKS = [0 for i in range(POSs)]
    SHP_C = len(BASE_ROT)
    RES = {}
    while True:
        placed_count = sum([i > 0 for i in PICKS])
        if 0 < placed_count <= MAX_PLACED:
            for i in range(len(M)):
                for j in range(len(M[i])):
                    M[i][j] = 0

            valid = True
            for pl in range(len(PICKS)):
                if PICKS[pl] > 0:
                    pos_r = pl // 3 + 1
                    pos_c = pl % 3 + 1
                    for occ in BASE_ROT[PICKS[pl] - 1] + [[0, 0]]:
                        if M[pos_r + occ[0]][pos_c + occ[1]] != 0:
                            valid = False
                            break
                        else:
                            M[pos_r + occ[0]][pos_c + occ[1]] = 1

                if not valid:
                    break

            if M[2][2] != 1:
                valid = False

            if valid:
                adv_shp = AdvShape(M=M, PWRS3=PWRS3, PWRS2=PWRS2)
                if adv_shp.hash_ in RES:
                    RES[adv_shp.hash_][1] += 1
                else:
                    RES[adv_shp.hash_] = [adv_shp, 1]

        fin = False
        ppos = -1
        while PICKS[ppos] == SHP_C:
            ppos -= 1
            if ppos < -len(PICKS):
                fin = True
                break

        if fin:
            break

        norm_ppos = len(PICKS) + ppos
        if norm_ppos >= 0:
            if norm_ppos < 3:
                print(PICKS)
            PICKS[norm_ppos] += 1
            for i in range(norm_ppos + 1, len(PICKS)):
                PICKS[i] = 0

    return RES


def pr161():
    GRID_SZ = [9, 12]
    SP_SIZE = 3
    MAX_PICK_N = 5
    POS_COUNT = SP_SIZE * SP_SIZE
    BS_SHAPES = [[[0, -1], [0, 1]],
                 [[-1, 0], [0, 1]]]
    BS_ROTATED = []

    PWRS2 = [2 ** i for i in range(4 * 2 * SP_SIZE)]
    PWRS3 = [3 ** i for i in range(4 * 2 * SP_SIZE)]
    ADV_SHAPES = {}

    rotate_base(BS_SHAPES, BS_ROTATED)

    M = [[0 for j in range(SP_SIZE + 2)] for i in range(SP_SIZE + 2)]
    for pick_n in range(1, MAX_PICK_N + 1):
        P = [0] * len(BS_ROTATED)
        P[0] = pick_n
        not_fin = True
        while not_fin:

            # print(P)

            L = []
            for p in P:
                if p == 0:
                    L.append([])
                else:
                    Lp = []
                    for pi in range(p):
                        Lp.append(pi)

                    L.append(Lp)

            all_locs_tested = False
            while not all_locs_tested:
                while not all_locs_tested and not valid_loc(L, M, BS_ROTATED):
                    # print("\t" + str(L))

                    all_locs_tested = not increment_locations(L, POS_COUNT)

                if all_locs_tested:
                    break

                adv_shp = AdvShape(M=M, PWRS3=PWRS3, PWRS2=PWRS2)
                if adv_shp.hash_ in ADV_SHAPES:
                    ADV_SHAPES[adv_shp.hash_][1] += 1
                else:
                    ADV_SHAPES[adv_shp.hash_] = [adv_shp, 1]

                # print("\t" + str(L))

                all_locs_tested = not increment_locations(L, POS_COUNT)

            not_fin = change_pick(P)

    ADV_ADV_SHAPES = {}
    for k1 in ADV_SHAPES:
        S1 = ADV_SHAPES[k1][0]
        if S1.sides_hashes_[0][1] != 0 or (S1.sides_hashes_[0][0] & PWRS2[1] == PWRS2[1]):
            continue
        for k2 in ADV_SHAPES:
            S2 = ADV_SHAPES[k2][0]

            if S1.sides_hashes_[2][1] | S2.sides_hashes_[0][0] == S2.sides_hashes_[0][0] and\
                S1.sides_hashes_[2][0] | S2.sides_hashes_[0][1] == S1.sides_hashes_[2][0] and\
                    ((S1.sides_hashes_[2][0] & PWRS2[1] == 0 and S2.sides_hashes_[0][0] & PWRS2[1] == 0) or\
                     S1.sides_hashes_[2][1] & PWRS2[1] == PWRS2[1] or S2.sides_hashes_[0][1] & PWRS2[1] == PWRS2[1]):
                AS = AdvShape(AS1=S1, AS2=S2, PWRS3=PWRS3, PWRS2=PWRS2)
                AS_count = ADV_SHAPES[k1][1] * ADV_SHAPES[k2][1]
                if AS.hash_ in ADV_ADV_SHAPES:
                    ADV_ADV_SHAPES[AS.hash_][1] += AS_count
                else:
                    ADV_ADV_SHAPES[AS.hash_] = [AS, AS_count]

    CORNERS = [{} for i in range(4)]  # start top right, then cw
    for h in ADV_ADV_SHAPES:
        AS = ADV_ADV_SHAPES[h][0]
        for corner in range(4):
            s1 = corner
            s2 = (corner + 1) % 4
            if AS.sides_hashes_[s1][1] == 0 and \
                    AS.sides_hashes_[s2][1] == 0 and \
                    AS.sides_hashes_[s1][0] in [0, PWRS2[(s1//2)*((1 + s1 % 2)*AS.in_w_ - 1)]] and \
                    AS.sides_hashes_[s2][0] in \
                    [0, PWRS2[(1 - (corner % 2 + corner // 2) % 2)*((1 + s2 % 2)*AS.in_w_ - 1)]]:
                CORNERS[corner][h] = ADV_ADV_SHAPES[h]

    SIDES = [{} for i in range(4)]  # start top, then cw
    for h in ADV_ADV_SHAPES:
        AS = ADV_ADV_SHAPES[h][0]
        for side in range(4):
            if AS.sides_hashes_[side][1] == 0 and \
                    AS.sides_hashes_[side][0] in [0, PWRS2[0], PWRS2[(1 + side % 2)*AS.in_w_ - 1],
                                                  PWRS2[0] | PWRS2[(1 + side % 2)*AS.in_w_ - 1]]:
                SIDES[side][h] = ADV_ADV_SHAPES[h]

    HALVES = {}
    count = 0
    c0c = 0
    for kc0 in CORNERS[0]:
        c0c += 1
        print("C0: " + str(c0c) + "/" + str(len(CORNERS[0])))
        C0 = CORNERS[0][kc0][0]
        for ks0 in SIDES[0]:
            S0 = SIDES[0][ks0][0]
            if C0.sides_hashes_[3][1] | S0.sides_hashes_[1][0] == S0.sides_hashes_[1][0] and \
                C0.sides_hashes_[3][0] | S0.sides_hashes_[1][1] == C0.sides_hashes_[3][0] and \
                    (C0.sides_hashes_[3][1] | PWRS2[5]) & S0.sides_hashes_[1][0] == S0.sides_hashes_[1][0] and \
                    (S0.sides_hashes_[1][1] | PWRS2[5]) & C0.sides_hashes_[3][0] == C0.sides_hashes_[3][0]:
                for kc3 in CORNERS[3]:
                    C3 = CORNERS[3][kc3][0]
                    if C3.sides_hashes_[1][1] | S0.sides_hashes_[3][0] == S0.sides_hashes_[3][0] and \
                        C3.sides_hashes_[1][0] | S0.sides_hashes_[3][1] == C3.sides_hashes_[1][0] and \
                            (C3.sides_hashes_[1][1] | PWRS2[5]) & S0.sides_hashes_[3][0] == S0.sides_hashes_[3][0] and \
                            (S0.sides_hashes_[3][1] | PWRS2[5]) & C3.sides_hashes_[1][0] == C3.sides_hashes_[1][0]:
                        count += 1
                        half_bin_repr = [0] * 9
                        for i in range(3):
                            half_bin_repr[i] = C3.bin_r_[11 - i]
                            half_bin_repr[3 + i] = S0.bin_r_[11 - i]
                            half_bin_repr[6 + i] = C0.bin_r_[11 - i]

                        if C3.bin_r_[8] == 1:
                            half_bin_repr[3] = 0
                        if S0.bin_r_[12] == 1:
                            half_bin_repr[2] = 0
                        if S0.bin_r_[8] == 1:
                            half_bin_repr[6] = 0
                        if C0.bin_r_[12] == 1:
                            half_bin_repr[5] = 0

                        hash = 0

                        for i in range(9):
                            if half_bin_repr[i] < 0:
                                hash += PWRS2[i]
                            elif half_bin_repr[i] > 0:
                                hash += PWRS2[9 + i]

                        half_count = CORNERS[0][kc0][1] * CORNERS[3][kc3][1] * SIDES[0][ks0][1]
                        if hash in HALVES:
                            HALVES[hash] += half_count
                        else:
                            HALVES[hash] = half_count

                        if count < 0:
                            for i in range(8):
                                print(str(C3.M_[i]) + " " + str(S0.M_[i]) + " " + str(C0.M_[i]))
                            print("\n")
                            print(str(half_bin_repr))
                            print("\n")

    result_count = 0
    for kh in HALVES:
        req_kh = get_req(PWRS2, kh)
        if req_kh in HALVES:
            result_count += HALVES[kh]*HALVES[req_kh]

    print(str(count))
    return result_count


def pm(M):
    for l in M:
        print(l)
    print("\n\n")


def pmf(M, f):
    for l in M:
        f.write(str(l) + "\n")
    f.write("\n\n")


def test():
    S, C = pr161()
    S1 = C[0][236317][0]
    S2 = C[1][442879][0]
    P2 = [2**i for i in range(50)]
    P3 = [3**i for i in range(50)]
    AS = AdvShape(AS1=S1, AS2=S2, PWRS3=P3, PWRS2=P2)

    print('S1')
    pm(S1.M_)
    print('S2')
    pm(S2.M_)
    print('AS')
    pm(AS.M_)

    return S1, S2, AS


def try_increment(r, c, SHPS, M, MP):
    if MP[r][c] >= 0:
        M[r + 1][c + 1] = 0
        for cl in SHPS[MP[r][c]]:
            M[r + 1 + cl[0]][c + 1 + cl[1]] = 0

    if MP[r][c] == len(SHPS) - 1:
        MP[r][c] = -1
        return False

    inc = 1
    while MP[r][c] + inc < len(SHPS):
        valid = M[r + 1][c + 1] == 0
        if valid:
            for cl in SHPS[MP[r][c] + inc]:
                if M[r + 1 + cl[0]][c + 1 + cl[1]] == 1:
                    valid = False
                    break

        if valid:
            MP[r][c] += inc
            M[r + 1][c + 1] = 1
            for cl in SHPS[MP[r][c]]:
                M[r + 1 + cl[0]][c + 1 + cl[1]] = 1

            return True

        inc += 1

    MP[r][c] = -1
    return False


def build_tiles(w, h, SHPS, P2, FS):
    # Creates all possible tiles with width w and height h from shapes SHPS which have position at fr, fc filled
    # Tiles are characterized by dents and protrusions, all possible dents and protrusions starting on the left
    # of the top side going to the left, then the right side from top down, then bottom side from left to the right,
    # then left side from top down are characterized by respective powers of 2. Dents first, then protrusions.
    # Whole tile is uniquely characterized by the sum of these powers.
    TILES = {}  # Keys are binary characterizations, values are numbers of ways in which tile can be built
    M = [[0 for i in range(w + 2)] for j in range(h + 2)]
    MP = [[-1 for i in range(w)] for j in range(h)]
    var_is = [1 - s % 2 for s in range(4)]
    start_i_i = [[1, 1], [1, w], [h, 1], [1, 1]]
    start_i_o = [[0, 1], [1, w + 1], [h + 1, 1], [1, 0]]
    lims = [w, h, w, h]
    cur_i = w*h - 1
    while cur_i >= 0:
        if try_increment(cur_i // w, cur_i % w, SHPS, M, MP):
            cur_i = w*h - 1
            # check, save
            forced_filled = True
            for fcoor in FS:
                if M[fcoor[0] + 1][fcoor[1] + 1] != 1:
                    forced_filled = False
                    break

            if forced_filled:
                key = 0
                p2_pos = 0
                # dents
                for s in range(4):
                    for inc in range(lims[s]):
                        cp_r = start_i_i[s][0] + (1 - var_is[s])*inc
                        cp_c = start_i_i[s][1] + var_is[s]*inc
                        if M[cp_r][cp_c] == 0:
                            key += P2[p2_pos]

                        p2_pos += 1

                # protrusions
                for s in range(4):
                    for inc in range(lims[s]):
                        cp_r = start_i_o[s][0] + (1 - var_is[s]) * inc
                        cp_c = start_i_o[s][1] + var_is[s] * inc
                        if M[cp_r][cp_c] == 1:
                            key += P2[p2_pos]

                        p2_pos += 1

                if key in TILES:
                    TILES[key] += 1
                else:
                    TILES[key] = 1
                    # pm(M)

        else:
            cur_i -= 1

    return TILES


def visualize_tile(tile, w, h, P2):
    M = [[0 for c in range(w + 2)] for r in range(h + 2)]
    for ir in range(1, h + 1):
        for ic in range(1, w + 1):
            M[ir][ic] = 1

    var_is = [1 - s % 2 for s in range(4)]
    start_i_i = [[1, 1], [1, w], [h, 1], [1, 1]]
    start_i_o = [[0, 1], [1, w + 1], [h + 1, 1], [1, 0]]
    lims = [w, h, w, h]

    p2_pos = 0
    # dents
    for s in range(4):
        for inc in range(lims[s]):
            cp_r = start_i_i[s][0] + (1 - var_is[s]) * inc
            cp_c = start_i_i[s][1] + var_is[s] * inc
            if tile & P2[p2_pos] == P2[p2_pos]:
                M[cp_r][cp_c] = 0

            p2_pos += 1

    # protrusions
    for s in range(4):
        for inc in range(lims[s]):
            cp_r = start_i_o[s][0] + (1 - var_is[s]) * inc
            cp_c = start_i_o[s][1] + var_is[s] * inc
            if tile & P2[p2_pos] == P2[p2_pos]:
                M[cp_r][cp_c] = 1

            p2_pos += 1

    return M


def visualise_half(half, w, P2):
    M = [[1 - j for i in range(3*w)] for j in range(2)]
    for di in range(3*w):
        if half & P2[di] == P2[di]:
            M[0][di] = 0
    for pi in range(3*w):
        if half & P2[3*w + pi] == P2[3*w + pi]:
            M[1][pi] = 1

    return M


def build_double_tiles(TILES, tw, th, P2):
    # Offsets of powers of 2 for specific top and bottom features
    prots_offset = 2*(tw + th)
    top_dents_offset = 0
    bottom_dents_offset = tw + th
    top_prots_offset = prots_offset + top_dents_offset
    bottom_prots_offset = prots_offset + bottom_dents_offset

    bottom_prots_mask = 0
    bottom_dents_mask = 0
    top_prots_mask = 0
    top_dents_mask = 0

    DTILES = {}

    for i in range(tw):
        bottom_prots_mask |= P2[bottom_prots_offset + i]
        bottom_dents_mask |= P2[bottom_dents_offset + i]
        top_prots_mask |= P2[top_prots_offset + i]
        top_dents_mask |= P2[top_dents_offset + i]

    full_top_prot = top_prots_mask

    top_middle_dent = P2[top_dents_offset + tw//2]
    bottom_middle_dent = P2[bottom_dents_offset + tw//2]
    top_middle_prot = P2[top_prots_offset + tw//2]
    bottom_middle_prot = P2[bottom_prots_offset + tw//2]

    top_tile_first_part_dents_mask = 0
    top_tile_first_part_prots_mask = 0
    top_tile_second_part_dents_mask = 0
    top_tile_second_part_prots_mask = 0
    btm_tile_first_part_dents_mask = 0
    btm_tile_first_part_prots_mask = 0
    btm_tile_second_part_dents_mask = 0
    btm_tile_second_part_prots_mask = 0

    top_t_fp_d_shift = 0
    top_t_fp_p_shift = 2*th
    top_t_sp_d_shift = th
    top_t_sp_p_shift = 3*th
    btm_t_fp_d_shift = th
    btm_t_fp_p_shift = 3*th
    btm_t_sp_d_shift = 2*th
    btm_t_sp_p_shift = 4*th

    for i in range(tw + th - 1):
        top_tile_first_part_dents_mask |= P2[top_dents_offset + i]
        top_tile_first_part_prots_mask |= P2[prots_offset + i]

        btm_tile_first_part_dents_mask |= P2[top_dents_offset + tw + 1 + i]
        btm_tile_first_part_prots_mask |= P2[prots_offset + tw + 1 + i]

    for i in range(th - 1):
        top_tile_second_part_dents_mask |= P2[2*tw + th + i]
        top_tile_second_part_prots_mask |= P2[prots_offset + 2*tw + th + i]

        btm_tile_second_part_dents_mask |= P2[top_dents_offset + 2*tw + th + 1 + i]
        btm_tile_second_part_prots_mask |= P2[prots_offset + 2*tw + th + 1 + i]

    TOP_T_M = [top_tile_first_part_dents_mask, top_tile_first_part_prots_mask,
               top_tile_second_part_dents_mask, top_tile_second_part_prots_mask]
    BTM_T_M = [btm_tile_first_part_dents_mask, btm_tile_first_part_prots_mask,
               btm_tile_second_part_dents_mask, btm_tile_second_part_prots_mask]
    TOP_T_S = [top_t_fp_d_shift, top_t_fp_p_shift, top_t_sp_d_shift, top_t_sp_p_shift]
    BTM_T_S = [btm_t_fp_d_shift, btm_t_fp_p_shift, btm_t_sp_d_shift, btm_t_sp_p_shift]

    R_S_TOP_T_IN = [2*tw + th - 1, 4*tw + 3*th - 1, 3*tw + 3*th - 1]
    R_S_BTM_T_IN = [tw - 1, 3*tw + 2*th - 1, 3*tw + 2*th]
    R_S_OUT = [tw + th - 1, tw+ th, 3*tw + 5*th - 1, 3*tw + 5*th]
    L_S_TOP_T_IN = [tw + th, 3*tw + 3*th, 4*tw + 4*th - 1]
    L_S_BTM_T_IN = [0, 2*tw + 2*th, 4*tw + 3*th]
    L_S_OUT = [2*tw + 3*th - 1, 2*tw + 3*th, 4*tw + 7*th - 1, 4*tw + 7*th]

    TOP_T_INS = [R_S_TOP_T_IN, L_S_TOP_T_IN]
    BTM_T_INS = [R_S_BTM_T_IN, L_S_BTM_T_IN]
    OUTS = [R_S_OUT, L_S_OUT]
    for i in range(len(OUTS)):
        for j in range(len(TOP_T_INS[i])):
            TOP_T_INS[i][j] = P2[TOP_T_INS[i][j]]
        for k in range(len(BTM_T_INS[i])):
            BTM_T_INS[i][k] = P2[BTM_T_INS[i][k]]
        for l in range(len(OUTS[i])):
            OUTS[i][l] = P2[OUTS[i][l]]

    for top_t in TILES:
        if full_top_prot & top_t != 0:
            # protrusions on top
            continue
        if top_middle_dent & top_t != 0:
            # dent in the middle on top
            continue

        required_dents = (top_t & bottom_prots_mask) >> (bottom_prots_offset - top_dents_offset)
        allowed_prots = (top_t & bottom_dents_mask) << (top_prots_offset - bottom_dents_offset)

        required_prots = 0
        forbidden_dents = 0

        if top_t & bottom_middle_dent == bottom_middle_dent:
            required_prots = top_middle_prot
        elif top_t & bottom_middle_prot == 0:
            forbidden_dents = top_middle_dent

        for btm_t in TILES:
            accepted = True
            if btm_t & required_dents != required_dents:
                accepted = False
            if accepted and ((btm_t & top_prots_mask) | allowed_prots != allowed_prots):
                accepted = False
            if accepted and (btm_t & required_prots != required_prots):
                accepted = False
            if accepted and (btm_t & forbidden_dents != 0):
                accepted = False

            if not accepted:
                # file.write("Rejected btm:\n")
                # pm(visualize_tile(btm_t, tw, th, P2), file)
                continue

            # file.write("Top:\n")
            # pm(visualize_tile(top_t, tw, th, P2), file)
            # file.write("Accepted btm:\n")
            # pm(visualize_tile(btm_t, tw, th, P2), file)

            dtile = 0
            for i in range(len(TOP_T_M)):
                dtile |= (top_t & TOP_T_M[i]) << TOP_T_S[i]
                dtile |= (btm_t & BTM_T_M[i]) << BTM_T_S[i]

            for i in range(len(OUTS)):
                if TOP_T_INS[i][2] & top_t == TOP_T_INS[i][2]:
                    dtile |= OUTS[i][2]
                if BTM_T_INS[i][2] & btm_t == BTM_T_INS[i][2]:
                    dtile |= OUTS[i][3]
                if (TOP_T_INS[i][0] & top_t == TOP_T_INS[i][0]) and (BTM_T_INS[i][1] & btm_t == 0):
                    dtile |= OUTS[i][0]
                if (BTM_T_INS[i][0] & btm_t == BTM_T_INS[i][0]) and (TOP_T_INS[i][1] & top_t == 0):
                    dtile |= OUTS[i][1]

            count = TILES[top_t] * TILES[btm_t]
            if dtile in DTILES:
                DTILES[dtile] += count
            else:
                DTILES[dtile] = count

            # file.write("Resulting dtile:\n")
            # pm(visualize_tile(dtile, tw, 2*th, P2), file)

    return DTILES


def filter_invalid_dtiles(DTILES, P2):
    tw = 3
    th = 3
    prots_offset = 2 * (tw + 2*th)
    top_dents_offset = 0
    top_prots_offset = prots_offset + top_dents_offset

    top_prots_mask = 0
    top_dents_mask = 0

    for i in range(tw):
        top_prots_mask |= P2[top_prots_offset + i]
        top_dents_mask |= P2[top_dents_offset + i]

    top_middle_dent = P2[top_dents_offset + tw // 2]

    VDTILES = {}
    for dtile in DTILES:
        if dtile & top_prots_mask != 0:
            continue
        if dtile & top_middle_dent != 0:
            continue

        VDTILES[dtile] = DTILES[dtile]

    return VDTILES


def sort_dtiles(DTILES, tw, th, P2):
    right_prots = 0
    left_prots = 0
    right_dents = 0
    left_dents = 0
    r_hash_d_mask = 0
    r_hash_p_mask = 0
    r_hash_d_shift = tw
    r_hash_p_shift = 2*(tw + th) + tw - (th - 1)

    for i in range(th):
        right_prots |= P2[2*(tw + th) + tw + i]
        left_prots |= P2[2*(tw + th) + 2*tw + th + i]

    for i in range(tw + th - 2):
        right_dents |= P2[1 + i]

    for i in range(tw - 1):
        left_dents |= P2[i]
    for i in range(th - 1):
        left_dents |= P2[2*tw + th + i]

    for i in range(th - 1):
        r_hash_d_mask |= P2[tw + i]
        r_hash_p_mask |= P2[2*(tw + th) + tw + i]

    R = {}
    M = {}
    L = {}

    for dtile in DTILES:
        r_hash = ((dtile & r_hash_d_mask) >> r_hash_d_shift) | ((dtile & r_hash_p_mask) >> r_hash_p_shift)
        if r_hash in M:
            M[r_hash].append([dtile, DTILES[dtile]])
        else:
            M[r_hash] = [[dtile, DTILES[dtile]]]

        if dtile & right_dents == 0 and dtile & right_prots == 0:
            R[dtile] = DTILES[dtile]

        if dtile & left_dents == 0 and dtile & left_prots == 0:
            if r_hash in L:
                L[r_hash].append([dtile, DTILES[dtile]])
            else:
                L[r_hash] = [[dtile, DTILES[dtile]]]

    return L, M, R


def build_halves(L, M, R, tw, th, P2):
    l_hash_d_mask = 0
    l_hash_p_mask = 0
    l_hash_d_shift = 2*tw + th - (th - 1)
    l_hash_p_shift = 2*(tw + th) + 2*tw + th

    for i in range(th - 1):
        l_hash_d_mask |= P2[2*tw + th + i]
        l_hash_p_mask |= P2[2*(tw + th) + 2*tw + th + i]

    lt_out_d_mask = 0
    lt_out_p_mask = 0
    mt_out_d_mask = 0
    mt_out_p_mask = 0
    rt_out_d_mask = 0
    rt_out_p_mask = 0
    lt_out_d_shift = tw + th                        # to right
    lt_out_p_shift = 2*(tw + th) + tw + th - 3*tw   # to right
    mt_out_d_shift = tw + th - tw                   # to right
    mt_out_p_shift = 2*(tw + th) + tw + th - 4*tw   # to right
    rt_out_d_shift = tw + th - 2*tw                 # to right
    rt_out_p_shift = 2*(tw + th) + tw + th - 5*tw   # to right

    LT_OUT_COMB = [P2[tw + th - 1], P2[2*(tw + th) + tw + th - 1], P2[2*(tw + th) + 2*tw + th - 1]]
    MT_OUT_L_COMB = [P2[2*(tw + th) - 1], P2[4*(tw + th) - 1], P2[2*(tw + th) + tw + th]]
    MT_OUT_R_COMB = [P2[tw + th - 1], P2[2*(tw + th) + tw + th - 1], P2[2*(tw + th) + 2*tw + th - 1]]
    RT_OUT_COMB = [P2[2*(tw + th) - 1], P2[4*(tw + th) - 1], P2[2*(tw + th) + tw + th]]
    HALF_IN_COMB = [P2[tw - 1], P2[tw], P2[2*tw - 1], P2[2*tw],
                    P2[3*tw + tw - 1], P2[3*tw + tw], P2[3*tw + 2*tw - 1], P2[3*tw + 2*tw]]

    for i in range(tw - 1):
        lt_out_d_mask |= P2[tw + th + i]
        lt_out_p_mask |= P2[2*(tw + th) + tw + th + i]
        rt_out_d_mask |= P2[tw + th + 1 + i]
        rt_out_p_mask |= P2[2*(tw + th) + tw + th + 1 + i]

    for i in range(tw - 2):
        mt_out_d_mask |= P2[tw + th + 1 + i]
        mt_out_p_mask |= P2[2*(tw + th) + tw + th + 1 + i]

    HALVES = {}
    for rdtile in R:
        rdt_req_r_hash = ((rdtile & l_hash_d_mask) >> l_hash_d_shift) | ((rdtile & l_hash_p_mask) >> l_hash_p_shift)
        if rdt_req_r_hash in M:
            rdt_req_dent = 0
            rdt_forb_prot = 0
            if rdtile & RT_OUT_COMB[1] == RT_OUT_COMB[1]:
                rdt_req_dent = MT_OUT_R_COMB[0]
            if rdtile & RT_OUT_COMB[0] != RT_OUT_COMB[0]:
                rdt_forb_prot = MT_OUT_R_COMB[1]

            for mdtile_l in M[rdt_req_r_hash]:
                mdtile = mdtile_l[0]

                if mdtile & rdt_req_dent != rdt_req_dent:
                    continue
                if mdtile & rdt_forb_prot != 0:
                    continue

                mdt_req_r_hash = ((mdtile & l_hash_d_mask) >> l_hash_d_shift) | ((mdtile & l_hash_p_mask) >> l_hash_p_shift)
                if mdt_req_r_hash in L:
                    mdt_req_dent = 0
                    mdt_forb_prot = 0
                    if mdtile & MT_OUT_L_COMB[1] == MT_OUT_L_COMB[1]:
                        mdt_req_dent = LT_OUT_COMB[0]
                    if mdtile & MT_OUT_L_COMB[0] != MT_OUT_L_COMB[0]:
                        mdt_forb_prot = LT_OUT_COMB[1]

                    for ldtile_l in L[mdt_req_r_hash]:
                        ldtile = ldtile_l[0]

                        if ldtile & mdt_req_dent != mdt_req_dent:
                            continue
                        if ldtile & mdt_forb_prot != 0:
                            continue

                        half_hash = ((ldtile & lt_out_d_mask) >> lt_out_d_shift) | \
                                    ((ldtile & lt_out_p_mask) >> lt_out_p_shift) | \
                                    ((mdtile & mt_out_d_mask) >> mt_out_d_shift) | \
                                    ((mdtile & mt_out_p_mask) >> mt_out_p_shift) | \
                                    ((rdtile & rt_out_d_mask) >> rt_out_d_shift) | \
                                    ((rdtile & rt_out_p_mask) >> rt_out_p_shift)

                        if ldtile & LT_OUT_COMB[2] == LT_OUT_COMB[2]:
                            half_hash |= HALF_IN_COMB[4]
                        if mdtile & MT_OUT_L_COMB[2] == MT_OUT_L_COMB[2]:
                            half_hash |= HALF_IN_COMB[5]
                        if mdtile & MT_OUT_R_COMB[2] == MT_OUT_R_COMB[2]:
                            half_hash |= HALF_IN_COMB[6]
                        if rdtile & RT_OUT_COMB[2] == RT_OUT_COMB[2]:
                            half_hash |= HALF_IN_COMB[7]

                        if (ldtile & LT_OUT_COMB[0] == LT_OUT_COMB[0]) and (mdtile & MT_OUT_L_COMB[1] == 0):
                            half_hash |= HALF_IN_COMB[0]
                        if (mdtile & MT_OUT_L_COMB[0] == MT_OUT_L_COMB[0]) and (ldtile & LT_OUT_COMB[1] == 0):
                            half_hash |= HALF_IN_COMB[1]
                        if (mdtile & MT_OUT_R_COMB[0] == MT_OUT_R_COMB[0]) and (rdtile & RT_OUT_COMB[1] == 0):
                            half_hash |= HALF_IN_COMB[2]
                        if (rdtile & RT_OUT_COMB[0] == RT_OUT_COMB[0]) and (mdtile & MT_OUT_R_COMB[1] == 0):
                            half_hash |= HALF_IN_COMB[3]

                        half_coutn = R[rdtile] * mdtile_l[1] * ldtile_l[1]

                        '''print("Combined L:")
                        pm(visualize_tile(ldtile, tw, th, P2))
                        print("M:")
                        pm(visualize_tile(mdtile, tw, th, P2))
                        print("R:")
                        pm(visualize_tile(rdtile, tw, th, P2))
                        print("Result:")
                        pm(visualise_half(half_hash, tw, P2))'''

                        if half_hash in HALVES:
                            HALVES[half_hash] += half_coutn
                        else:
                            HALVES[half_hash] = half_coutn

    return HALVES


def combine_halves(HALVES, hw, P2):
    dents_mask = 0
    prots_mask = 0

    for i in range(hw):
        dents_mask |= P2[i]
        prots_mask |= P2[hw + i]

    count = 0
    for half in HALVES:
        req_pair = ((half & dents_mask) << hw) | ((half & prots_mask) >> hw)
        if req_pair in HALVES:
            count += HALVES[half]*HALVES[req_pair]
            '''print("Pairing:")
            pm(visualise_half(half, 3, P2))
            pm(visualise_half(req_pair, 3, P2))'''

    return count


def pr161_new():
    GRID_SZ = [9, 12]
    SP_SIZE = 3
    POS_COUNT = SP_SIZE * SP_SIZE
    BS_SHAPES = [[[0, -1], [0, 1]],
                 [[-1, 0], [0, 1]]]
    BS_ROTATED = []

    PWRS2 = [2 ** i for i in range(4 * 2 * SP_SIZE * 10)]

    rotate_base(BS_SHAPES, BS_ROTATED)

    TILES = build_tiles(3, 3, BS_ROTATED, PWRS2, [[1, 1]])

    # t_file = open("G:\Euler\pr161_dtile_test.txt", "w")
    DTILES = build_double_tiles(TILES, 3, 3, PWRS2)

    '''print("Brute forcing dtiles")
    DTILES_BF = build_tiles(3, 6, BS_ROTATED, PWRS2, [[1, 1], [2, 1], [3, 1], [4, 1]])
    print("Filtering bfced dtiles")
    VDTILES_BF = filter_invalid_dtiles(DTILES_BF, PWRS2)
    print("Comparing dtiles")

    if len(DTILES) != len(VDTILES_BF):
        print("DTILES number: " + str(len(DTILES)))
        print("VDTILES number: " + str(len(VDTILES_BF)))

    for vdtile in VDTILES_BF:
        if vdtile not in DTILES:
            print("vdtile not in dtiles:")
            pm(visualize_tile(vdtile, 3, 6, PWRS2))
        elif VDTILES_BF[vdtile] != DTILES[vdtile]:
            print("Different count: BF: " + str(VDTILES_BF[vdtile]) + ", N: " + str(DTILES[vdtile]))

    return DTILES, VDTILES_BF'''

    L, M, R = sort_dtiles(DTILES, 3, 6, PWRS2)
    HALVES = build_halves(L, M, R, 3, 6, PWRS2)
    return combine_halves(HALVES, 9, PWRS2)
