#pragma once
#include "AVLTreeNode.h"
#include "BSTree.h"
#include "Iterator.h"
#include <stdexcept>

template<typename T>
class AVLTree : public BSTree<T>
{
private:
    void rotate_right(AVLTreeNode<T>* node);
    void rotate_left(AVLTreeNode<T>* node);
public:
    AVLTree();
    AVLTree(AVLTree<T> const & other);
    virtual void insert(T data) override;
    virtual T remove(T const & key) override;
};

template<typename T>
inline void AVLTree<T>::rotate_right(AVLTreeNode<T>* node)
{
    if (node->get_left_son() == nullptr)
        return;

    AVLTreeNode<T>* left_son = dynamic_cast<AVLTreeNode<T>*>(node->get_left_son());
    AVLTreeNode<T>* father = dynamic_cast<AVLTreeNode<T>*>(node->get_father());

    if (node->is_left_child())
        father->set_left_son(left_son);
    else if (node->is_right_child())
        father->set_right_son(left_son);
    else
    {
        left_son->reset_father();
        this->set_root(left_son);
    }
        
    node->set_left_son(left_son->get_right_son());

    left_son->set_right_son(node);

    node->update_balance_by(1 - (left_son->get_balance() < 0 ? left_son->get_balance() : 0));

    left_son->update_balance_by(1 + (node->get_balance() > 0 ? node->get_balance() : 0));
}

template<typename T>
inline void AVLTree<T>::rotate_left(AVLTreeNode<T>* node)
{
    if (node->get_right_son() == nullptr)
        return;

    AVLTreeNode<T>* father = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
    AVLTreeNode<T>* right_son = dynamic_cast<AVLTreeNode<T>*>(node->get_right_son());

    if (node->is_left_child())
        father->set_left_son(right_son);
    else if (node->is_right_child())
        father->set_right_son(right_son);
    else
    {
        right_son->reset_father();
        this->set_root(right_son);
    }

    node->set_right_son(right_son->get_left_son());

    right_son->set_left_son(node);

    node->update_balance_by(-1 - (right_son->get_balance() > 0 ? right_son->get_balance() : 0));

    right_son->update_balance_by(-1 + (node->get_balance() < 0 ? node->get_balance() : 0));
}

template<typename T>
inline AVLTree<T>::AVLTree():
    BSTree()
{
}

template<typename T>
inline AVLTree<T>::AVLTree(AVLTree<T> const & other)
{
    *this = other;
}

template<typename T>
inline void AVLTree<T>::insert(T data)
{
    if (this->get_root() == nullptr)
    {
        this->set_root(new AVLTreeNode<T>(data));
        this->increment_size();
        return;
    }

    bool found = false;
    AVLTreeNode<T>* node = dynamic_cast<AVLTreeNode<T>*>(this->find_node(data, found));
    if (found)
    {
        throw std::logic_error("Trying to insert item with duplicate key into AVLTree.");
    }

    bool from_left = false;
    if (node->compare(data) < 0)
    {
        node->set_right_son(new AVLTreeNode<T>(data));
        from_left = false;
    }
    else
    {
        node->set_left_son(new AVLTreeNode<T>(data));
        from_left = true;
    }
    this->increment_size();

    bool cont = true;
    while (node != nullptr && cont)
    {
        if (from_left)
        {
            node->decrement_balance();
        }
        else
        {
            node->increment_balance();
        }

        if (node->get_balance() == 0)
            break;
        else if (node->get_balance() == 2)
        {
            if (dynamic_cast<AVLTreeNode<T>*>(node->get_right_son())->get_balance() == 1)
            {
                this->rotate_left(node);
                cont = false;
            }
            else
            {
                this->rotate_right(dynamic_cast<AVLTreeNode<T>*>(node->get_right_son()));
                this->rotate_left(node);
                cont = false;
            }
        }
        else if (node->get_balance() == -2)
        {
            if (dynamic_cast<AVLTreeNode<T>*>(node->get_left_son())->get_balance() == -1)
            {
                this->rotate_right(node);
                cont = false;
            }
            else
            {
                this->rotate_left(dynamic_cast<AVLTreeNode<T>*>(node->get_left_son()));
                this->rotate_right(node);
                cont = false;
            }
        }
        else
        {
            AVLTreeNode<T>* father = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
            if (father != nullptr)
            {
                if (node == father->get_left_son())
                    from_left = true;
                else
                    from_left = false;
            }
            node = father;
        }

    }
}

template<typename T>
inline T AVLTree<T>::remove(T const & key)
{
    bool found;
    AVLTreeNode<T>* node = dynamic_cast<AVLTreeNode<T>*>(this->find_node(key, found));

    if (!found)
        throw std::logic_error("Trying to remove item non-existent in the AVLTree.");

    T data = node->access_data();
    if (node->has_left_son() && node->has_right_son())
    {
        AVLTreeNode<T>* cur_node = dynamic_cast<AVLTreeNode<T>*>(node->get_right_son());
        while (cur_node->has_left_son())
            cur_node = dynamic_cast<AVLTreeNode<T>*>(cur_node->get_left_son());
        node->switch_with(cur_node);
        node = cur_node;
    }

    this->decrement_size();
    if (node == this->get_root())
    {
        if (node->has_left_son())
            this->set_root(node->get_left_son());
        else if (node->has_right_son())
            this->set_root(node->get_right_son());
        else
            this->set_root(nullptr);

        if (this->get_root() != nullptr)
            this->get_root()->reset_father();

        delete node;
        return data;
    }

    bool from_left = node->is_left_child();
    AVLTreeNode<T>* father = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
    if (node->has_left_son())
    {
        if (node->is_left_child())
            node->get_father()->set_left_son(node->get_left_son());
        else
            node->get_father()->set_right_son(node->get_left_son());
    }
    else if (node->has_right_son())
    {
        if (node->is_left_child())
            node->get_father()->set_left_son(node->get_right_son());
        else
            node->get_father()->set_right_son(node->get_right_son());
    }
    else
    {
        if (node->is_left_child())
            node->get_father()->set_left_son(nullptr);
        else
            node->get_father()->set_right_son(nullptr);
    }

    node->set_left_son(nullptr);
    node->set_right_son(nullptr);
    delete node;
    node = father;
    bool cont = true;
    while (node != nullptr && cont)
    {
        if (node->get_balance() == 0)
        {
            cont = false;
        }
        if (from_left)
            node->increment_balance();
        else
            node->decrement_balance();

        if (node->get_balance() == 2)
        {
            if (dynamic_cast<AVLTreeNode<T>*>(node->get_right_son())->get_balance() == -1)
            {
                this->rotate_right(dynamic_cast<AVLTreeNode<T>*>(node->get_right_son()));
                this->rotate_left(node);
            }
            else
            {
                if (dynamic_cast<AVLTreeNode<T>*>(node->get_right_son())->get_balance() == 0)
                    cont = false;
                this->rotate_left(node);
            }
            node = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
        }
        else if (node->get_balance() == -2)
        {
            if (dynamic_cast<AVLTreeNode<T>*>(node->get_left_son())->get_balance() == 1)
            {
                this->rotate_left(dynamic_cast<AVLTreeNode<T>*>(node->get_left_son()));
                this->rotate_right(node);
            }
            else
            {
                if (dynamic_cast<AVLTreeNode<T>*>(node->get_left_son())->get_balance() == 0)
                    cont = false;
                this->rotate_right(node);
            }
            node = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
        }

        AVLTreeNode<T>* father = dynamic_cast<AVLTreeNode<T>*>(node->get_father());
        if (father != nullptr)
        {
            if (father->get_left_son() == node)
                from_left = true;
            else
                from_left = false;
        }
        node = father;
    }

    return data;
}
