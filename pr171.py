from collections import Counter
from math import factorial, sqrt


class Numbers(object):
    def __init__(self, digits_list, dig_num):
        self.digs_ = digits_list
        self.n_dig_ = dig_num
        self.cntrs_ = [None] * self.n_dig_
        self.cntrs_[0] = Counter(self.digs_)
        self.cur_i_ = 0
        self.going_up_ = False
        self.number_ = [None] * dig_num
        self.fact_ = factorial(len(digits_list) - dig_num)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.going_up_:
                if self.cur_i_ < 0:
                    raise StopIteration()

                cdi = list(self.cntrs_[self.cur_i_].keys()).index(self.number_[self.cur_i_])
                if cdi < len(self.cntrs_[self.cur_i_]) - 1:
                    self.going_up_ = False
                    continue
                else:
                    self.cntrs_[self.cur_i_] = None
                    self.number_[self.cur_i_] = None
                    self.cur_i_ -= 1
                    continue

            else:
                if self.number_[self.cur_i_] is None:
                    dts = list(self.cntrs_[self.cur_i_].keys())[0]
                else:
                    cdi = list(self.cntrs_[self.cur_i_].keys()).index(self.number_[self.cur_i_])
                    if cdi < len(self.cntrs_[self.cur_i_]) - 1:
                        dts = list(self.cntrs_[self.cur_i_].keys())[cdi + 1]
                    else:
                        self.going_up_ = True
                        continue

                self.number_[self.cur_i_] = dts

                if self.cur_i_ < self.n_dig_ - 1:
                    nctr = self.cntrs_[self.cur_i_].copy()
                    nctr[dts] -= 1
                    if nctr[dts] == 0:
                        del nctr[dts]
                    self.cntrs_[self.cur_i_ + 1] = nctr
                    self.cur_i_ += 1
                    continue
                else:
                    fin_cntr = self.cntrs_[self.n_dig_ - 1].copy()
                    fin_cntr[self.number_[self.n_dig_ - 1]] -= 1
                    if fin_cntr[self.number_[self.n_dig_ - 1]] == 0:
                        del fin_cntr[self.number_[self.n_dig_ - 1]]

                    count = self.fact_
                    for rd in fin_cntr:
                        if fin_cntr[rd] <= 0:
                            print("aaa")
                        count /= factorial(fin_cntr[rd])

                    return sum([d * 10**i for i, d in enumerate(self.number_)]), int(count)


class Digits(object):
    def __init__(self, dig_num, tar_val):
        self.n_dig_ = dig_num
        self.tar_ = tar_val
        self.rem_ = tar_val
        self.digs_ = [0] * self.n_dig_
        self.__fill_from__(0, 9)
        self.returned_ = False

    def __iter__(self):
        return self

    def __fill_from__(self, ind, max_d):
        cur_d = max_d
        for i in range(ind, self.n_dig_):
            while cur_d ** 2 > self.rem_:
                cur_d -= 1
            self.digs_[i] = cur_d
            self.rem_ -= cur_d ** 2

    def __make_step__(self):
        i = self.n_dig_ - 1
        while self.digs_[i] < 2:
            if self.digs_[i] == 1:
                self.rem_ += 1
                self.digs_[i] = 0
            i -= 1
            if i < 0:
                raise StopIteration

        self.rem_ += self.digs_[i] ** 2
        self.digs_[i] -= 1
        self.rem_ -= self.digs_[i] ** 2
        self.__fill_from__(i + 1, self.digs_[i])

    def __next__(self):
        if self.rem_ == 0:
            if not self.returned_:
                self.returned_ = True
                return self.digs_.copy()

            self.__make_step__()

        while self.rem_ != 0:
            self.__make_step__()

        self.returned_ = True
        return self.digs_.copy()


class AllDigits(object):
    def __init__(self, dig_num):
        self.n_dig_ = dig_num
        self.digs_ = [0] * self.n_dig_
        self.__fill_from__(0, 9)
        self.returned_ = False

    def __iter__(self):
        return self

    def __fill_from__(self, ind, max_d):
        for i in range(ind, self.n_dig_):
            self.digs_[i] = max_d

    def __make_step__(self):
        i = self.n_dig_ - 1
        while self.digs_[i] < 1:
            i -= 1
            if i < 0:
                raise StopIteration

        self.digs_[i] -= 1
        self.__fill_from__(i + 1, self.digs_[i])

    def __next__(self):
        if not self.returned_:
            self.returned_ = True
            return self.digs_.copy()

        self.__make_step__()
        return self.digs_.copy()


def pr171(dig):
    max_sum = dig * 9**2
    res_digs = 6
    mod = 10**res_digs
    res = 0
    i = 1
    while i**2 <= max_sum:
        print("Processing square of {}".format(i))
        goal = i**2
        for dig_list in Digits(dig_num=dig, tar_val=goal):
            for num, count in Numbers(digits_list=dig_list, dig_num=res_digs):
                res += num * count
                res = res % mod

        i += 1

    return res



def digits(nd, tar):
    S = set()
    for i in range(10**nd):
        s = []
        l = i
        while l > 0:
            s.append(l % 10)
            l = l // 10

        sm = sum([k**2 for k in s])
        if sm == tar:
            while len(s) < nd:
                s.append(0)
            s.sort(reverse=True)
            S.add(tuple(s))

    return S


def pr171_1(dig):
    max_sum = dig * 9 ** 2
    res_digs = 6
    mod = 10 ** res_digs
    rem_dig = dig - res_digs
    rem_fact = factorial(rem_dig)
    res = 0
    pos_tars = [i**2 for i in range(int(sqrt(max_sum)) + 1)]
    rem_counts = {}
    for num in range(mod):
        if num % (10**6) == 0:
            print(num)

        digs = []
        m = num
        while m > 0:
            digs.append(m % 10)
            m = m // 10

        dig_sq = sum([di**2 for di in digs])
        for pt in pos_tars:
            rem = pt - dig_sq
            if rem >= 0:
                if rem not in rem_counts:
                    count = 0
                    for dl in Digits(rem_dig, rem):
                        cc = rem_fact
                        dl_C = Counter(dl)
                        for k in dl_C:
                            cc = cc // factorial(dl_C[k])

                        count += cc

                    rem_counts[rem] = count

                res += rem_counts[rem] * num
                res = res % mod

    return res

def pr171_2(dig):
    max_sum = dig * 9 ** 2
    res_digs = 6
    mod = 10 ** res_digs
    rem_dig = dig - res_digs
    rem_fact = factorial(rem_dig)
    dig_ones = sum([10**i for i in range(res_digs)])
    res = 0
    pos_tars = [i ** 2 for i in range(int(sqrt(max_sum)) + 1)]

    for digs in AllDigits(res_digs):
        sqs = sum([d**2 for d in digs])
        count = 0
        for pt in pos_tars:
            rem = pt - sqs
            if rem >= 0:
                for dl in Digits(rem_dig, rem):
                    cc = rem_fact
                    dl_C = Counter(dl)
                    for k in dl_C:
                        cc = cc // factorial(dl_C[k])

                    count += cc

        if count == 0:
            continue

        digs_sum = 0
        ctr = Counter(digs)
        for k in ctr:
            plfc = factorial(res_digs - 1)
            for l in ctr:
                if l == k:
                    plfc //= factorial(ctr[l] - 1)
                else:
                    plfc //= factorial(ctr[l])

            digs_sum += dig_ones*k*plfc

        res += count * digs_sum
        res %= mod

    return res


def pr171_3(dig):
    max_sum = dig * 9 ** 2
    res_digs = 9
    mod = 10 ** res_digs
    rem_dig = dig - res_digs
    rem_fact = factorial(rem_dig)
    dig_ones = sum([10 ** i for i in range(res_digs)])
    res = 0
    pos_tars = [i ** 2 for i in range(int(sqrt(max_sum)) + 1)]
    rem_counts = {}

    for digs in AllDigits(res_digs):
        sqs = sum([d ** 2 for d in digs])
        count = 0
        for pt in pos_tars:
            rem = pt - sqs
            if rem >= 0:
                if rem not in rem_counts:
                    cur_count = 0
                    for dl in Digits(rem_dig, rem):
                        cc = rem_fact
                        dl_C = Counter(dl)
                        for k in dl_C:
                            cc = cc // factorial(dl_C[k])

                        cur_count += cc

                    rem_counts[rem] = cur_count

                count += rem_counts[rem]

        if count == 0:
            continue

        digs_sum = 0
        ctr = Counter(digs)
        for k in ctr:
            plfc = factorial(res_digs - 1)
            for l in ctr:
                if l == k:
                    plfc //= factorial(ctr[l] - 1)
                else:
                    plfc //= factorial(ctr[l])

            digs_sum += dig_ones * k * plfc

        res += count * digs_sum
        res %= mod

    return res


if __name__ == "__main__":
    pr171_2(11)