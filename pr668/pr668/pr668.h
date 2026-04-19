#include "..\AVLTree\AVLTree.h"

class MyLong
{
    long long number;
public:
    MyLong(long long num) :
        number(num)
    {

    }
    int compare(MyLong const & other) const
    {
        if (this->number == other.number)
            return 0;
        if (this->number < other.number)
            return -1;

        return 1;
    }

    long long get_number() const
    {
        return this->number;
    }
};

class Pr668
{
private:
    long long n_;
public:
    Pr668(long long n) { this->n_ = n; };
    long long solve();
};
