from itertools import combinations

from line_profiler import profile


def check_cor(prefix, completed):
    parts = []
    comb_len = 0
    cur_part = []
    for d in prefix:
        if d == "b":
            parts.append("".join(cur_part))
            cur_part = []
        else:
            comb_len += 1
            cur_part.append(d)

    if comb_len == 10 and cur_part:
        parts.append("".join(cur_part))

    if parts != completed:
        raise RuntimeError(
            f"Inconsistent parameters. pref: {prefix}, compl: {completed}"
        )


def find_src(num):
    break_cands = list(range(1, 10))
    for num_breaks in range(1, 5):
        for divis in combinations(break_cands, num_breaks):
            parts = []
            i = 0
            for d in divis:
                parts.append(num[i:d])
                i = d
            parts.append(num[i:])

            for n in range(2, 10):
                sours = []
                for prt in parts:
                    prt_i = int(prt)
                    if prt_i % n == 0:
                        sours.append(str(prt_i // n))
                    else:
                        break

                joined = "".join(sours + [str(n)])
                if len(joined) == len(set(joined)) == 10:
                    print((n, sours))


@profile
def pr170():
    all_digs = set([str(n) for n in range(10)])
    BREAK = "b"
    source = ["18", "5470639", "2"]
    greatest_prod_c = "9847150236"

    def search(pref: list[str], completed_parts: list[str], avail_digs: set[str]):
        nonlocal greatest_prod_c
        nonlocal source
        if completed_parts and any(
            [part.startswith("0") for part in completed_parts if len(part) > 1]
        ):
            return

        if len(completed_parts) >= 2:
            prods = []
            left = int(completed_parts[0])
            for right in completed_parts[1:]:
                prods.append(str(left * int(right)))

            prod = "".join(prods)
            if len(prod) > len(all_digs):
                return

            for i, d in enumerate(prod):
                if greatest_prod_c[i] < d:
                    break
                elif greatest_prod_c[i] > d:
                    return
            prod_set = set(prod)
            if len(prod_set) != len(prod):
                return

            if (
                not avail_digs
                and len(prod) == len(all_digs)
                and len(completed_parts) >= 3
            ):
                print(f"assigning gr: {prod}, parts: {completed_parts}")
                greatest_prod_c = prod
                source = completed_parts

        if avail_digs:
            # if len(completed_parts) < 3 and len(avail_digs) == 1 and pref[-1] != BREAK:
            #    # only one number on the right and only one digit left
            #    avail_nxt = {BREAK}
            if pref and pref[-1] != BREAK:
                avail_nxt = avail_digs | {BREAK}
            else:
                avail_nxt = avail_digs

            for nxt in avail_nxt:
                if len(pref) == 1:
                    print(f"pref: {pref}, nxt: {nxt}")

                new_completed = []
                if nxt == BREAK or (nxt != BREAK and len(avail_digs) == 1):
                    last_part = [nxt] if nxt != BREAK else []
                    for dig in pref[::-1]:
                        if dig != BREAK:
                            last_part.append(dig)
                        else:
                            break

                    new_part = "".join(last_part[::-1])
                    new_completed.append(new_part)

                search(
                    pref=pref + [nxt],
                    completed_parts=completed_parts + new_completed,
                    avail_digs=avail_digs - {nxt},
                )

    search(pref=[], completed_parts=[], avail_digs=all_digs)

    return greatest_prod_c, source


if __name__ == "__main__":
    pr170()
