#include "primes.h"

using namespace std;

void primes(std::vector<int>& P, int n)
{
    P.reserve(n / 7);
    vector<bool> flags = vector<bool>(n + 1);
    for (int i = 2; i < flags.size(); i++)
        flags[i] = true;

    for (int i = 2; i < flags.size(); i++)
    {
        if (flags[i])
        {
            P.push_back(i);
            for (int j = i*i; j < flags.size(); j += i)
            {
                flags[j] = false;
            }
        }
    }
}
