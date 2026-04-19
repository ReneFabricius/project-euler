#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <math.h>
#include <numeric>

using namespace std;

void primes(vector<int> &prim, unsigned int n);
void findAbundant(vector<int> &potential, vector<int> &abundant);
int sumPropDivisors(int n);
void findSumsOfTwoAbundants(vector<int> &abundant, set<int> &sums);

int const LIMIT = 28123;

int main(int argc, char** argv)
{
    
    int integers_range[LIMIT - 1];
    for (int i = 0; i < LIMIT - 1; i++)
    {
        integers_range[i] = i + 1;
    }

    vector<int> prim;
    primes(prim, LIMIT - 1);
    vector<int> potential_abundant(LIMIT - 1);
    vector<int>::iterator it = set_difference(integers_range, (integers_range + (LIMIT - 1)), &prim[0], (&prim[0] + prim.size()), potential_abundant.begin());
    potential_abundant.resize(it - potential_abundant.begin());
    prim.clear();

    vector<int> abundants;
    findAbundant(potential_abundant, abundants);
    potential_abundant.clear();

    set<int> twoAbundantsSums;
    findSumsOfTwoAbundants(abundants, twoAbundantsSums);
    abundants.clear();

    long int sum_of_sums_of_two_abundants = accumulate(twoAbundantsSums.begin(), twoAbundantsSums.end(), 0);
    twoAbundantsSums.clear();

    long int sum_of_all_positive_integers_which_cannot_be_written_as_sum_of_two_abundants = (LIMIT * (LIMIT - 1)) / 2 - sum_of_sums_of_two_abundants;

    cout << sum_of_all_positive_integers_which_cannot_be_written_as_sum_of_two_abundants << endl;

    return 0;
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


    for (size_t l = 2; l < n + 1; l++)
    {
        if (sie[l])
        {
            prim.push_back(l);
        }
    }

    delete[] sie;
}

void findAbundant(vector<int> &potential, vector<int> &abundant)
{
    for (int pot : potential)
    {
        if (sumPropDivisors(pot) > pot)
            abundant.push_back(pot);
    }
}

int sumPropDivisors(int n)
{
    if (n == 1)
        return 0;

    int sum = 1;
    int sqr = int(sqrt(n));
    for (int i = 2; i < sqr; i++)
    {
        if (n % i == 0)
        {
            sum += i + n/i;
        }
    }
    if (n % sqr == 0)
    {
        if (sqr * sqr == n)
            sum += sqr;
        else
            sum += sqr + n / sqr;
    }

    return sum;
}

void findSumsOfTwoAbundants(vector<int> &abundant, set<int> &sums)
{
    for (int i = 0; i < abundant.size(); i++)
    {
        for (int j = i; j < abundant.size(); j++)
        {
            int sum = abundant[i] + abundant[j];
            if (sum < LIMIT)
                sums.insert(sum);
            else
                break;
        }
    }
}
