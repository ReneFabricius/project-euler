#include "pr668.h"
#include "primes.h"
#include "..\AVLTree\avltree.h"
#include <vector>
#include <cmath>

using namespace std;

long long Pr668::solve()
{
    long long c = 1;
    vector<int> P;
    primes(P, int(sqrt(n_)));
    AVLTree<MyLong>* T = new AVLTree<MyLong>();

    long long lim = long long(n_ / P[0]);
    long long cur = P[0];
    while (cur <= lim)
    {
        T->insert(MyLong(cur));
        cur *= P[0];
    }

    long long count_bel = 1;
    c += T->get_size() - count_bel;
    vector<long long> holder;
    

    for (int i = 1; i < P.size(); i++)
    {
        long long pr = P[i];
        long long clim = long long(n_ / pr);
        long long blim = long long(n_ / (pr*pr));

        holder.clear();
        holder.reserve(T->get_size());
        for each(MyLong N in *T)
        {
            if (N.get_number() <= blim)
                holder.push_back(N.get_number());
            else
                break;
        }

        for each(long long N in holder)
        {
            long long cur = N*pr;
            while (cur <= clim)
            {
                T->insert(MyLong(cur));
                cur *= pr;
            }
        }

        long long ccur = pr;
        while (ccur <= clim)
        {
            T->insert(MyLong(ccur));
            ccur *= pr;
        }

        T->remove_above_inclusive(clim + 1);
        count_bel += T->count_between(P[i - 1] + 1, P[i]);
        c += T->get_size() - count_bel;
    }

    return c;
}
