/* http://mathworld.wolfram.com/DecimalExpansion.html */

#include <map>
#include <vector>
#include <math.h>
#include <iostream>
#include <sstream>

using namespace std;

void primes(vector<int> &prim, unsigned int n);
void primeFactDecomp(map<int, int> &decomp, int n);
int multiplicativeOrder10(int m);
int totient(int n);
int powMod(int a, int e, int m);

vector<int> P;

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        cout << "Enter one integer argument" << endl;
        return 0;
    }

    int N;
    if (!(istringstream(argv[1]) >> N))
        cout << "Entered not valid integer" << endl;

    primes(P, int(sqrt(N)) + 1);
    int maxOrd = 0;
    int maxI;

    for (int i = 1; i < N; i++)
    {
        int c = i;
        while (c % 2 == 0)
            c /= 2;
        while (c % 5 == 0)
            c /= 5;
        int mulOrd = multiplicativeOrder10(c);
        if (mulOrd > maxOrd)
        {
            maxOrd = mulOrd;
            maxI = i;
        }
    }

    cout << maxI << endl;

    return 0;
}

void primeFactDecomp(map<int, int> &decomp, int n)
{
    for (int p : P)
    {
        while (n % p == 0)
        {
            decomp[p] += 1;
            n /= p;
        }

        if (n == 1)
            return;

        if (p > sqrt(n))
            break;
    }
    decomp[n] += 1;
}

int totient(int n)
{
    map<int, int> decomp;
    primeFactDecomp(decomp, n);
    int tot = 1;
    for (pair<int, int> p : decomp)
    {
        tot *= p.first - 1;
        if (p.second > 1)
            tot *= pow(p.first, p.second - 1);
    }

    return tot;
}

int multiplicativeOrder10(int m)
{
    if (m == 1)
        return 1;

    int tot = totient(m);
    int exp = 2;
    int highOrd = tot;
    while (exp*exp <= tot)
    {
        if (tot % exp == 0)
        {
            if (powMod(10, exp, m) == 1)
                return exp;

            if (powMod(10, tot / exp, m) == 1)
                highOrd = tot / exp;
        }
        exp += 1;
    }

    return highOrd;
}

int powMod(int a, int e, int m)
{
    int res = 1;
    while (e)
    {
        if (e & 1)
            res = (res * a) % m;

        a = (a*a) % m;
        e >>= 1;
    }
    return res;
}

void primes(vector<int> &prim, unsigned int n)
{
    if (n == 1)
        return;

    bool *sie = new bool[n + 1];

    for (size_t i = 2; i < n + 1; i++)
    {
        sie[i] = true;
    }

    sie[0] = false;
    sie[1] = false;

    for (size_t j = 2; j < sqrt(n) + 1; j++)
    {
        if (sie[j])
        {
            for (size_t k = j*j; k < n + 1; k += j)
                sie[k] = false;
        }
    }

    for (int i = 2; i < n + 1; i++)
    {
        if (sie[i])
            prim.push_back(i);
    }

    delete[] sie;
}
