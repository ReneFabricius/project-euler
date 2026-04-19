#include "AVLTree.h"
#include <iostream>
#include "..\pr668\primes.h"
#include "..\pr668\pr668.h"

class MyInt
{
    int number;
public:
    MyInt(int num) :
        number(num)
    {

    }
    int compare(MyInt const & other) const
    {
        if (this->number == other.number)
            return 0;
        if (this->number < other.number)
            return -1;

        return 1;
    }

    int get_number() const
    {
        return this->number;
    }
};


int main()
{
    
    /*AVLTree<MyInt>* int_tree = new AVLTree<MyInt>();
    int_tree->insert(MyInt(7));
    int_tree->insert(MyInt(12));
    int_tree->insert(MyInt(4));
    int_tree->insert(MyInt(2));
    int_tree->insert(MyInt(17));
    int_tree->insert(MyInt(25));
    int_tree->insert(MyInt(26));
    int_tree->insert(MyInt(33));
    int_tree->insert(MyInt(37));
    int_tree->insert(MyInt(45));
    int_tree->insert(MyInt(1));
    int_tree->insert(MyInt(44));
    int_tree->insert(MyInt(42));
    int_tree->insert(MyInt(170));
    int_tree->remove(MyInt(4));
    int_tree->insert(MyInt(48));

    for (StructureIterator<MyInt> it = int_tree->begin(); it != int_tree->end(); ++it)
    {
        std::cout << (*it).get_number() << "\n";
    }

    std::cout << "\nBetween 38 and 48:\n";
    for (StructureIterator<MyInt> it = int_tree->iterator_from(MyInt(38)); it != int_tree->iterator_from(MyInt(48 + 1)); ++it)
    {
        std::cout << (*it).get_number() << "\n";
    }
    std::cout << "\nCount between 38 and 48:";
    std::cout << int_tree->count_between(MyInt(38), MyInt(48)) << "\n";

    std::cout << "After removal above 36:\n";
    int_tree->remove_above_inclusive(MyInt(36));
    for (StructureIterator<MyInt> it = int_tree->begin(); it != int_tree->end(); ++it)
    {
        std::cout << (*it).get_number() << "\n";
    }

    std::cout << "\nCount between 38 and 48:";
    std::cout << int_tree->count_between(MyInt(38), MyInt(48)) << "\n";

    delete int_tree;


    std::vector<int> P = std::vector<int>();
    primes(P, 100);
    for (int i = 0; i < P.size(); i++)
    {
        std::cout << P[i] << " ";
    }*/
    long long n;
    while (std::cin >> n)
    {
        Pr668* pr = new Pr668(n);
        std::cout << pr->solve() << "\n";
    }



    return 0;
};