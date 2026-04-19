#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

template<class T>
void swap_vals(T &, T &);

template<class T>
void quicksort(T[], int, int);

template<class T>
int partition(T[], int, int);

int sumNameScores(string arr[], int size);


int main(int argc, char** argv)
{
    if (argc < 2)
    {
        cout << "Zadaj nazov suboru" << endl;
        return 0;
    }

    ifstream mena(argv[1]);

    if (mena.is_open())
    {
        stringstream ss;
        ss << mena.rdbuf();
        mena.close();
        vector<string> mena_vec;

        string meno;
        while (getline(ss, meno, ','))
        {
            mena_vec.push_back(meno.substr(1, meno.size() - 2));
        }

        quicksort(&mena_vec[0], 0, mena_vec.size() - 1);
        int sum = sumNameScores(&mena_vec[0], mena_vec.size());
        mena_vec.clear();
        cout << sum << endl;
        return sum;
    }
    else
    {
        cout << "Nepodarilo sa otvorit subor: " << argv[1] << endl;
    }

    return 0;
}

template<class T>
void quicksort(T arr[], int start, int end)
{
    if (end <= start)
        return;

    int pivot_pos = partition(arr, start, end);
    quicksort(arr, start, pivot_pos - 1);
    quicksort(arr, pivot_pos + 1, end);
}

template<class T>
int partition(T arr[], int start, int end)
{
    T pivot_val = arr[end];
    int i = start;
    for (int j = start; j < end; j++)
    {
        if (arr[j] < pivot_val)
        {
            swap_vals(arr[j], arr[i]);
            i++;
        }
    }
    swap_vals(arr[i], arr[end]);
    return i;
}

template<class T>
void swap_vals(T &a, T &b)
{
    T c = a;
    a = b;
    b = c;
}

int sumNameScores(string arr[], int size)
{
    if (!arr)
        return 0;

    long int sum = 0;

    for (int i = 0; i < size; i++)
    {
        int name_score = 0;
        for (char ch : arr[i])
        {
            name_score += ch - 64;
        }

        name_score *= i + 1;
        sum += name_score;
    }

    return sum;
}
