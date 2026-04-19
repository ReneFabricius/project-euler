
class Node:
    def __init__(self, id):
        self.id_ = id
        self.l_ = []
        self.ld_ = []
        self.proc_ = False
        self.cnctnd_ = False


class Triangle:
    def __init__(self, sz):
        self.sz_ = sz
        self.nodes_ = []
        self.normal_ = [None]*sz
        self.rotated_ = [None]*(sz - 1)
        self.pit_ = 7
        for i in range(sz):
            self.normal_[i] = [None]*(self.pit_ * (i + 1))
            if i < sz - 1:
                self.rotated_[i] = [None]*(self.pit_ * (i + 1))

        # nodes
        gni = 0
        for i in range(sz - 1, -1, -1):
            for ti in range(i + 1):
                ctni = 0
                if i < sz - 1:
                    for ni in range(3):
                        self.normal_[i][ti * self.pit_ + ni] = self.rotated_[i][ti * self.pit_ + (4 - ni)]
                    ctni = 3

                for ni in range(ctni, self.pit_):
                    if ni == 0 and ti > 0:
                        self.normal_[i][ti * self.pit_ + ni] = self.normal_[i][(ti - 1) * self.pit_ + 2]
                    else:
                        self.nodes_.append(Node(gni))
                        self.normal_[i][ti * self.pit_ + ni] = self.nodes_[gni]
                        gni += 1

            if i > 0:
                for ti in range(i):
                    for ni in range(3):
                        self.rotated_[i - 1][ti * self.pit_ + ni] = self.normal_[i][(ti + 1) * self.pit_ + ((6 - ni) % 6)]
                    for ni in range(4, 6):
                        self.rotated_[i - 1][ti * self.pit_ + ni] = self.normal_[i][ti * self.pit_ + (8 - ni)]

                    self.nodes_.append(Node(gni))
                    self.rotated_[i - 1][ti * self.pit_ + 3] = self.nodes_[gni]
                    gni += 1
                    self.nodes_.append(Node(gni))
                    self.rotated_[i - 1][ti * self.pit_ + 6] = self.nodes_[gni]
                    gni += 1

        # connections
        for i in range(sz - 1, -1, -1):
            for ti in range(i + 1):
                for ni in range(self.pit_):
                    if self.normal_[i][ti * self.pit_ + ni].cnctnd_:
                        continue

                    if ni == 0:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(120)
                        s = self.general_set(i, -1, ti, 0, (4, 5), self.normal_, set())
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(150)
                        s = self.general_set(i, -1, ti, 1, (3, 6), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti, 1, (2, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(180)
                        s = self.general_set(i, 0, ti, 1, (1, 2), self.normal_, set())
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        if i < self.sz_ - 1:
                            self.normal_[i][ti * self.pit_ + ni].ld_.append(210)
                            s = self.general_set(i + 1, 1, ti + 1, 2, (2, 6), self.normal_, set())
                            s = self.general_set(i, 1, ti, 2, (1, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(240)
                            s = self.general_set(i + 1, 1, ti, 1, (2, 3), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(270)
                            s = self.general_set(i + 1, 2, ti, 1, (1, 6), self.normal_, set())
                            s = self.general_set(i + 1, 2, ti, 1, (0, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(300)
                            s = self.general_set(i + 1, 1, ti, 0, (0, 5), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            # 330, 360
                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if ni == 2:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(30)
                        s = self.general_set(i, -1, ti, -2, (5, 6), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti - 1, -2, (4, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(60)
                        s = self.general_set(i, -1, ti, -1, (3, 4), self.normal_, set())
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        if ti < i:
                            self.normal_[i][ti * self.pit_ + ni].ld_.append(90)
                            s = self.general_set(i - 1, -2, ti, -1, (4, 6), self.normal_, set())
                            s = self.general_set(i - 1, -2, ti, -1, (3, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(120)
                            s = self.general_set(i, -1, ti + 1, 0, (4, 5), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(150)
                            s = self.general_set(i, -1, ti + 1, 1, (3, 6), self.normal_, set())
                            s = self.general_set(i - 1, -1, ti + 1, 1, (2, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(180)
                            s = self.general_set(i, 0, ti + 1, 1, (1, 2), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            if i < self.sz_ - 1:
                                self.normal_[i][ti * self.pit_ + ni].ld_.append(210)
                                s = self.general_set(i + 1, 1, ti + 2, 2, (2, 6), self.normal_, set())
                                s = self.general_set(i, 1, ti + 1, 2, (1, 6), self.rotated_, s)
                                self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        if i < self.sz_ - 1:
                            self.normal_[i][ti * self.pit_ + ni].ld_.append(240)
                            s = self.general_set(i + 1, 1, ti + 1, 1, (2, 3), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(270)
                            s = self.general_set(i + 1, 2, ti + 1, 1, (1, 6), self.normal_, set())
                            s = self.general_set(i + 1, 2, ti + 1, 1, (0, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            self.normal_[i][ti * self.pit_ + ni].ld_.append(300)
                            s = self.general_set(i + 1, 1, ti + 1, 0, (0, 5), self.normal_, set())
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                            # 330, 360

                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if i == 0 and ni == 4:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(240)
                        s = self.general_set(i, 1, ti, 1, (2, 3), self.normal_, set())
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(270)
                        s = self.general_set(i, 2, ti, 1, (1, 6), self.normal_, set())
                        s = self.general_set(i, 2, ti, 1, (0, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        # 300

                    if ni == 1:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(90)
                        s = self.general_set(i, -2, ti, -1, (4, 6), self.normal_, set())
                        s - self.general_set(i - 2, -2, ti - 1, -1, (3, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(180)
                        s = self.general_set(i, 0, ti, 1, (2,), self.normal_, set())
                        s = self.general_set(i, 0, ti + 1, 1, (1,), self.normal_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if ni == 3:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(60)
                        s = self.general_set(i, -1, ti, -1, (4,), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti - 1, -1, (3,), self.normal_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        if ti < i:
                            self.normal_[i][ti * self.pit_ + ni].ld_.append(150)
                            s = self.general_set(i - 1, -1, ti + 1, 1, (3, 6), self.normal_, set())
                            s = self.general_set(i - 1, -1, ti, 1, (2, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(240)
                        s = self.general_set(i, 1, ti, 1, (2,), self.normal_, set())
                        s = self.general_set(i + 1, 1, ti + 1, 1, (3, ), self.normal_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        # 330

                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if ni == 5:
                        if ti > 0:
                            self.normal_[i][ti * self.pit_ + ni].ld_.append(30)
                            s = self.general_set(i - 1, -1, ti - 2, -2, (5, 6), self.normal_, set())
                            s = self.general_set(i - 1, -1, ti - 1, -2, (4, 6), self.rotated_, s)
                            self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(120)
                        s = self.general_set(i, -1, ti, 0, (4,), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti, 0, (5,), self.normal_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(210)
                        s = self.general_set(i, 1, ti, 2, (2, 6), self.normal_, set())
                        s = self.general_set(i, 1, ti + 1, 2, (1, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        # 300

                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if ni == 6:
                        self.normal_[i][ti * self.pit_ + ni].ld_.append(30)
                        s = self.general_set(i, -1, ti, -2, (5,), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti - 2, -2, (6,), self.normal_, s)
                        s = self.general_set(i - 1, -1, ti - 1, -2, (4, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(90)
                        s = self.general_set(i, -2, ti, -1, (4,), self.normal_, set())
                        s = self.general_set(i - 2, -2, ti - 1, -1, (6,), self.normal_, s)
                        s = self.general_set(i - 2, - 2, ti - 1, -1, (3, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(150)
                        s = self.general_set(i, -1, ti, 1, (3,), self.normal_, set())
                        s = self.general_set(i - 1, -1, ti + 1, 1, (6,), self.normal_, s)
                        s = self.general_set(i - 1, -1, ti, 1, (2, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(210)
                        s = self.general_set(i, 1, ti, 2, (2,), self.normal_, set())
                        s = self.general_set(i + 1, 1, ti + 2, 2, (6,), self.normal_, s)
                        s = self.general_set(i, 1, ti + 1, 2, (1, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        self.normal_[i][ti * self.pit_ + ni].ld_.append(270)
                        s = self.general_set(i, 2, ti, 1, (1,), self.normal_, set())
                        s = self.general_set(i + 2, 2, ti + 1, 1, (6,), self.normal_, s)
                        s = self.general_set(i, 2, ti, 1, (0, 6), self.rotated_, s)
                        self.normal_[i][ti * self.pit_ + ni].l_.append(s)

                        # 330

                        self.normal_[i][ti * self.pit_ + ni].cnctnd_ = True

                    if i < sz - 1 and ni == 6:
                        self.rotated_[i][ti * self.pit_ + ni].ld_.append(30)
                        s = self.general_set(i, -1, ti, -2, (4,), self.rotated_, set())
                        s = self.general_set(i - 1, -1, ti - 2, -2, (6,), self.rotated_, s)
                        s = self.general_set(i, -1, ti - 1, -2, (5, 6), self.normal_, s)
                        self.rotated_[i][ti * self.pit_ + ni].l_.append(s)

                        self.rotated_[i][ti * self.pit_ + ni].ld_.append(90)
                        s = self.general_set(i, - 2, ti, - 1, (3,), self.rotated_, set())
                        s = self.general_set(i - 2, -2, ti - 1, -1, (6,), self.rotated_, s)
                        s = self.general_set(i, -2, ti, -1, (4, 6), self.normal_, s)
                        self.rotated_[i][ti * self.pit_ + ni].l_.append(s)

                        self.rotated_[i][ti * self.pit_ + ni].ld_.append(150)
                        s = self.general_set(i, -1, ti, 1, (2,), self.rotated_, set())
                        s = self.general_set(i - 1, -1, ti + 1, 1, (6,), self.rotated_, s)
                        s = self.general_set(i, -1, ti + 1, 1, (3, 6), self.normal_, s)
                        self.rotated_[i][ti * self.pit_ + ni].l_.append(s)

                        self.rotated_[i][ti * self.pit_ + ni].ld_.append(210)
                        s = self.general_set(i, 1, ti, 2, (1,), self.rotated_, set())
                        s = self.general_set(i + 1, 1, ti + 2, 2, (6,), self.rotated_, s)
                        s = self.general_set(i + 1, 1, ti + 1, 2, (2, 6), self.normal_, s)
                        self.rotated_[i][ti * self.pit_ + ni].l_.append(s)

                        self.rotated_[i][ti * self.pit_ + ni].ld_.append(270)
                        s = self.general_set(i, 2, ti, 1, (0,), self.rotated_, set())
                        s = self.general_set(i + 2, 2, ti + 1, 1, (6,), self.rotated_, s)
                        s = self.general_set(i + 2, 2, ti + 1, 1, (1, 6), self.normal_, s)
                        self.rotated_[i][ti * self.pit_ + ni].l_.append(s)

                        # 330

                        self.rotated_[i][ti * self.pit_ + ni].cnctnd_ = True

    def general_set(self, rsi, rs, tsi, ts, nis, source, s):
        cri = rsi
        cti = tsi
        while -1 < cri < len(source) and -1 < cti <= cri:
            for ni in nis:
                s.add(source[cri][cti * self.pit_ + ni].id_)

            cri += rs
            cti += ts

        return s

    def count_triangles(self):
        triangs = []

        for node in self.nodes_:
            for lai in range(len(node.l_)):
                if 0 < node.ld_[lai] < 180:
                    for pbi in node.l_[lai]:
                        pb = self.nodes_[pbi]
                        for lci in range(len(pb.l_)):
                            if node.ld_[lai] < pb.ld_[lci] < node.ld_[lai] + 180:
                                for lbi in range(len(node.l_)):
                                    if node.ld_[lai] < node.ld_[lbi] <= 180:
                                        pais = pb.l_[lci].intersection(node.l_[lbi])
                                        if len(pais) > 0:
                                            pai = pais.pop()
                                            triangs.append(frozenset([node.id_, pbi, pai]))

        return triangs







