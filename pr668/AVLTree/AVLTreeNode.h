#pragma once
#include "BSTreeNode.h"

template <typename T>
class AVLTreeNode: public BSTreeNode<T>
{
private:
    int balance_;

public:
    AVLTreeNode(T data);
    virtual BSTreeNode<T>* get_shallow_copy() override;
    int get_balance();
    void increment_balance();
    void decrement_balance();
    void update_balance_by(int change);
};

template<typename T>
inline AVLTreeNode<T>::AVLTreeNode(T data):
    BSTreeNode<T>(data), balance_(0)
{
}

template<typename T>
inline BSTreeNode<T>* AVLTreeNode<T>::get_shallow_copy()
{
    AVLTreeNode<T> * ret = new AVLTreeNode<T>(this->access_data());
    ret->balance_ = this->balance_;
    return ret;
}

template<typename T>
inline int AVLTreeNode<T>::get_balance()
{
    return this->balance_;
}


template<typename T>
inline void AVLTreeNode<T>::increment_balance()
{
    this->balance_++;
}

template<typename T>
inline void AVLTreeNode<T>::decrement_balance()
{
    this->balance_--;
}

template<typename T>
inline void AVLTreeNode<T>::update_balance_by(int change)
{
    this->balance_ += change;
}
