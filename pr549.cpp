#include <iostream>
#include <sstream>
#include <math.h>
#include <time.h>

using namespace std;

typedef unsigned long int ulint;

ulint find_m(ulint n, int e);
ulint S(ulint n);


ulint find_m(ulint n, int e)   // n - prvocislo; najde najmensie cislo, ktoreho faktorial bude delitelny cislom n**e
{
    ulint m = 0;

    while (e / n >= 1 && e > 0)
    {
        e -= n + 1;
        m += n * n;
        ulint c = m / (n*n);
        if (c >= n)
        {
            while (c % n == 0 && c > 0)
            {
                e -= 1;
                c = c / n;
            }
        }
    }

    if (e > 0)
        m += e * n;

    return m;
}

ulint S(ulint n)    // suma najmensich cisel takych, ze ich faktorial je delitelny cislom k, pre k 2...n
{
    ulint *array_s = new ulint[n + 1];
    if (!array_s)
        return 0;

    for (ulint i = 2; i < n + 1; i++)
        array_s[i] = 0;

    for (ulint i = 2; i < n + 1; i++)
    {
        if (array_s[i] == 0)
        {
            ulint pow = i;
            unsigned int exp = 1;

            do {
                ulint m = find_m(i, exp);
                for (ulint j = pow; j < n + 1; j += pow)
                {
                    if (array_s[j] < m)
                        array_s[j] = m;
                }
                pow *= i;
                exp += 1;
            } while (pow <= n);
        }
    }

    unsigned long long int sum = 0;
    for (ulint i = 2; i < n + 1; i++)
        sum += array_s[i];

    delete[] array_s;
    return sum;

}


int main(int argc, char *argv[])
{
    if (argc >= 2)
    {
        istringstream iss(argv[1]);
        ulint n;

        if (iss >> n)
        {
            struct timespec start, finish;
            double elapsed;

            clock_gettime(CLOCK_MONOTONIC, &start);

            cout << "S(" << n << ") = " << S(n) << "\n";

            clock_gettime(CLOCK_MONOTONIC, &finish);

            elapsed = (finish.tv_sec - start.tv_sec);
            elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0;
            
            cout << "Time elapsed: " << elapsed << endl;
        }

    }
    else
        std::cout << "Zadaj jeden cisleny argument" << "\n";
    

    return 0;
}
