#pragma once
#include <queue>
#include "BSTreeNode.h"
#include "Iterator.h"

template<typename T>
class BSTree: public Iterable<T>
{
private:
    BSTreeNode<T>* root_;
    int size_;
    
protected:
    BSTreeNode<T>* find_node(T const & key, bool & found) const;
    BSTreeNode<T>* get_root() const;
    void set_root(BSTreeNode<T>* root);
    void increment_size();
    void decrement_size();
    static BSTreeNode<T>* get_in_order_follower(BSTreeNode<T>* node);

public:
    BSTree();
    BSTree(BSTree<T> const & other);
    BSTree<T>& operator=(BSTree<T> const & other);
    ~BSTree();
    void clear();
    virtual void insert(T data);
    bool try_find(T const & key, T & data);
    bool contains_data(T const & key);
    T operator[](T const & key);
    virtual T remove(T const & key);
    int get_size() const;
    StructureIterator<T> iterator_from(T const & key) const;
    long count_between(T const & min, T const & max) const;
    void remove_above_inclusive(T const & from);

    class InOrderIterator : public Iterator<T>
    {
    private:
        BSTreeNode<T>* cur_node_;
    public:
        InOrderIterator(BSTreeNode<T>* const start, bool exact = false);
        Iterator<T>& operator=(Iterator<T> const & other);
        bool operator!=(Iterator<T> const & other);
        T const operator*();
        Iterator<T>& operator++();
    };

    class LevelOrderIterator : public Iterator<T>
    {
    private:
        std::queue<BSTreeNode<T>*> que_;
    public:
        LevelOrderIterator(BSTreeNode<T>* const start);
        Iterator<T>& operator=(Iterator<T> const & other);
        bool operator!=(Iterator<T> const & other);
        T const operator*();
        Iterator<T>& operator++();
    };

    Iterator<T>* get_begin_iterator() const;
    Iterator<T>* get_end_iterator() const;
    Iterator<T>* get_level_ord_begin_iterator() const;
    Iterator<T>* get_level_ord_end_iterator() const;
};

template<typename T>
inline BSTreeNode<T>* BSTree<T>::find_node(T const & key, bool & found) const
{
    if (this->root_ == nullptr)
    {
        found = false;
        return nullptr;
    }

    BSTreeNode<T>* cur_node = this->root_;
    BSTreeNode<T>* next_node = this->root_;
    found = false;
    do
    {
        cur_node = next_node;
        int comp = cur_node->compare(key);
        if (comp == 0)
        {
            next_node = nullptr;
            found = true;
        }
        else if (comp < 0)
        {
            next_node = cur_node->get_right_son();
        }
        else
        {
            next_node = cur_node->get_left_son();
        }
    } while (next_node != nullptr);

    return cur_node;
}

template<typename T>
inline BSTreeNode<T>* BSTree<T>::get_root() const
{
    return this->root_;
}

template<typename T>
inline void BSTree<T>::set_root(BSTreeNode<T>* root)
{
    this->root_ = root;
}

template<typename T>
inline void BSTree<T>::increment_size()
{
    this->size_++;
}

template<typename T>
inline void BSTree<T>::decrement_size()
{
    this->size_--;
}

template<typename T>
inline BSTreeNode<T>* BSTree<T>::get_in_order_follower(BSTreeNode<T>* node)
{
    if (node == nullptr)
        return node;

    BSTreeNode<T>* cur_node = node;

    if (cur_node->has_right_son())
    {
        cur_node = cur_node->get_right_son();
        while (cur_node->has_left_son())
            cur_node = cur_node->get_left_son();

        return cur_node;
    }

    while (!(cur_node->get_father() == nullptr || cur_node->is_left_child()))
    {
        cur_node = cur_node->get_father();
    }

    cur_node = cur_node->get_father();

    return cur_node;
}

template<typename T>
inline BSTree<T>::BSTree() :
    root_(nullptr), size_(0)
{
}

template<typename T>
inline BSTree<T>::BSTree(BSTree<T> const & other):
    BSTree()
{
    *this = other;
}

template<typename T>
inline BSTree<T>& BSTree<T>::operator=(BSTree<T> const & other)
{
    if (this != &other)
    {
        this->clear();
        if (other.size_ == 0)
            return *this;

        std::queue<BSTreeNode<T>*> que_other;
        que_other.push(other.root_);
        this->root_ = other.root_->get_shallow_copy();
        std::queue<BSTreeNode<T>*> que_this;
        que_this.push(this->root_);

        while (que_other.size() > 0)
        {
            BSTreeNode<T>* cur_other = que_other.front();
            que_other.pop();
            BSTreeNode<T>* cur_this = que_this.front();
            que_this.pop();

            if (cur_other->has_left_son())
            {
                cur_this->set_left_son(cur_other->get_left_son()->get_shallow_copy());
                que_other.push(cur_other->get_left_son());
                que_this.push(cur_this->get_left_son());
            }

            if (cur_other->has_right_son())
            {
                cur_this->set_right_son(cur_other->get_right_son()->get_shallow_copy());
                que_other.push(cur_other->get_right_son());
                que_this.push(cur_this->get_right_son());
            }
        }

        this->size_ = other.size_;
    }

    return *this;
}

template<typename T>
inline BSTree<T>::~BSTree()
{
    this->clear();
}

template<typename T>
inline void BSTree<T>::clear()
{
    if (this->root_ == nullptr)
        return;

    std::vector<BSTreeNode<T>*> to_delete;
    to_delete.resize(this->size_);
    to_delete[0] = this->root_;
    int insert_index = 1;
    for (int i = 0; i < this->size_; i++)
    {
        if (to_delete[i]->has_left_son())
            to_delete[insert_index++] = to_delete[i]->get_left_son();

        if (to_delete[i]->has_right_son())
            to_delete[insert_index++] = to_delete[i]->get_right_son();

        delete to_delete[i];
        to_delete[i] = nullptr;
    }

    this->root_ = nullptr;
    this->size_ = 0;
}

template<typename T>
inline void BSTree<T>::insert(T data)
{
    if (this->root_ == nullptr)
    {
        this->root_ = new BSTreeNode<T>(data);
        this->size_++;
        return;
    }

    bool found = false;
    BSTreeNode<T>* node = this->find_node(data, found);
    if (found)
    {
        throw std::logic_error("Trying to insert item with duplicate key into AVLTree.");
    }

    if (node->compare(data) < 0)
    {
        node->set_right_son(new BSTreeNode<T>(data));
    }
    else
    {
        node->set_left_son(new BSTreeNode<T>(data));
    }
    this->size_++;
}

template<typename T>
inline bool BSTree<T>::try_find(T const & key, T & data)
{
    bool found = false;
    BSTreeNode<T>* node = this->find_node(key, found);
    if (found)
    {
        data = node->access_data();
    }

    return found;
}

template<typename T>
inline bool BSTree<T>::contains_data(T const & key)
{
    bool found = false;
    this->find_node(key, found);
    return found;
}

template<typename T>
inline T BSTree<T>::operator[](T const & key)
{
    bool found = false;
    BSTreeNode<T>* node = this->find_node(key, found);
    if (!found)
    {
        throw std::out_of_range("Called operator [] on AVLTree with key non-existent in the Tree");
    }

    return node->access_data();
}

template<typename T>
inline T BSTree<T>::remove(T const & key)
{
    bool found;
    BSTreeNode<T>* node = this->find_node(key, found);

    if (!found)
        throw std::logic_error("Trying to remove item non-existent in the BSTree.");

    T data = node->access_data();
    if (node->has_left_son() && node->has_right_son())
    {
        BSTreeNode<T>* cur_node = node->get_right_son();
        while (cur_node->has_left_son())
            cur_node = cur_node->get_left_son();
        node->switch_with(cur_node);
        node = cur_node;
    }

    this->size_--;
    if (node == this->root_)
    {
        if (node->has_left_son())
            this->root_ = node->get_left_son();
        else if (node->has_right_son())
            this->root_ = node->get_right_son();
        else
            this->root_ = nullptr;

        if (this->root_ != nullptr)
            this->root_->reset_father();

        delete node;
        return data;
    }

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
    return data;
}

template<typename T>
inline int BSTree<T>::get_size() const
{
    return this->size_;
}

template<typename T>
inline StructureIterator<T> BSTree<T>::iterator_from(T const & key) const
{
    if (this->get_size() == 0)
        return StructureIterator<T>(new BSTree<T>::InOrderIterator(nullptr));

    bool found;
    BSTreeNode<T>* node = this->find_node(key, found);
    if (!found && node->access_data().compare(key) < 0)
        node = get_in_order_follower(node);

    return StructureIterator<T>(new BSTree<T>::InOrderIterator(node, true));
}

template<typename T>
inline long BSTree<T>::count_between(T const & min, T const & max) const
{
    long count = 0;
    StructureIterator<T> it = this->iterator_from(min);
    while (it != this->end())
    {
        if ((*it).compare(max) > 0)
            break;

        count++;
        ++it;
    }

    return count;
}

template<typename T>
inline void BSTree<T>::remove_above_inclusive(T const & from)
{
    StructureIterator<T> it = this->iterator_from(from);
    while (it != this->end())
    {
        this->remove(*it);
        it = this->iterator_from(from);
    }
}

template<typename T>
inline Iterator<T>* BSTree<T>::get_begin_iterator() const
{
    return new BSTree<T>::InOrderIterator(this->root_);
}

template<typename T>
inline Iterator<T>* BSTree<T>::get_end_iterator() const
{
    return new BSTree<T>::InOrderIterator(nullptr);
}

template<typename T>
inline Iterator<T>* BSTree<T>::get_level_ord_begin_iterator() const
{
    return new BSTree<T>::LevelOrderIterator(this->root_);
}

template<typename T>
inline Iterator<T>* BSTree<T>::get_level_ord_end_iterator() const
{
    return new BSTree<T>::LevelOrderIterator(nullptr);
}

template<typename T>
inline BSTree<T>::InOrderIterator::InOrderIterator(BSTreeNode<T>* const start, bool exact) :
    cur_node_(start)
{
    if (!exact)
    {
        if (this->cur_node_ != nullptr)
        {
            while (this->cur_node_->has_left_son())
                this->cur_node_ = this->cur_node_->get_left_son();
        }
    }
}

template<typename T>
inline Iterator<T>& BSTree<T>::InOrderIterator::operator=(Iterator<T> const & other)
{
    if (this != &other)
    {
        this->cur_node_ = dynamic_cast<BSTree<T>::InOrderIterator const &>(other).cur_node_;
    }
    return *this;
}

template<typename T>
inline bool BSTree<T>::InOrderIterator::operator!=(Iterator<T> const & other)
{
    return this->cur_node_ != dynamic_cast<BSTree<T>::InOrderIterator const &>(other).cur_node_;
}

template<typename T>
inline T const BSTree<T>::InOrderIterator::operator*()
{
    if (this->cur_node_ == nullptr)
        throw std::logic_error("Dereferencing Iterator pointing out of structure.");

    return this->cur_node_->access_data();
}

template<typename T>
inline Iterator<T>& BSTree<T>::InOrderIterator::operator++()
{
    this->cur_node_ = get_in_order_follower(this->cur_node_);

    return *this;
}

template<typename T>
inline BSTree<T>::LevelOrderIterator::LevelOrderIterator(BSTreeNode<T>* const start)
{
    if (start != nullptr)
    {
        this->que_.push(start);
    }
}

template<typename T>
inline Iterator<T>& BSTree<T>::LevelOrderIterator::operator=(Iterator<T> const & other)
{
    if (this != &other)
    {
        this->que_ = dynamic_cast<BSTree<T>::LevelOrderIterator const &>(other).que_;
    }

    return *this;
}

template<typename T>
inline bool BSTree<T>::LevelOrderIterator::operator!=(Iterator<T> const & other)
{
    if (this->que_.size() == 0 && dynamic_cast<BSTree<T>::LevelOrderIterator const &>(other).que_.size() == 0)
        return false;
    if (this->que_.size() == 0 || dynamic_cast<BSTree<T>::LevelOrderIterator const &>(other).que_.size() == 0)
        return true;

    return this->que_ != dynamic_cast<BSTree<T>::LevelOrderIterator const &>(other).que_;
}

template<typename T>
inline T const BSTree<T>::LevelOrderIterator::operator*()
{
    if (this->que_.size() == 0)
        throw std::logic_error("Dereferencing Iterator pointing out of structure.");

    return this->que_.front()->access_data();
}

template<typename T>
inline Iterator<T>& BSTree<T>::LevelOrderIterator::operator++()
{
    if (this->que_.size() > 0)
    {
        BSTreeNode<T>* node = this->que_.front();
        this->que_.pop();
        if (node->has_left_son())
            this->que_.push(node->get_left_son());
        if (node->has_right_son())
            this->que_.push(node->get_right_son());
    }

    return *this;
}
