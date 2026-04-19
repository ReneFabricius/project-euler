#pragma once

template<typename T>
class BSTreeNode
{
private:
    BSTreeNode<T>* father_;
    BSTreeNode<T>* left_son_;
    BSTreeNode<T>* right_son_;
    T data_;

public:
    BSTreeNode(T data);
    virtual BSTreeNode<T>* get_shallow_copy();
    virtual ~BSTreeNode();
    BSTreeNode<T>* get_left_son();
    BSTreeNode<T>* get_right_son();
    BSTreeNode<T>* get_father();
    int compare(T const & data);
    T access_data();
    void set_left_son(BSTreeNode<T>* left_son);
    void set_right_son(BSTreeNode<T>* right_son);
    void reset_father();
    void switch_with(BSTreeNode<T>* node);
    bool has_left_son();
    bool has_right_son();
    bool is_left_child();
    bool is_right_child();
};

template<typename T>
inline BSTreeNode<T>::BSTreeNode(T data) :
    data_(data), father_(nullptr), left_son_(nullptr), right_son_(nullptr)
{
}

template<typename T>
inline BSTreeNode<T>* BSTreeNode<T>::get_shallow_copy()
{
    return new BSTreeNode<T>(this->data_);
}

template<typename T>
inline BSTreeNode<T>::~BSTreeNode()
{
    this->left_son_ = nullptr;
    this->right_son_ = nullptr;
    this->father_ = nullptr;
}

template<typename T>
inline BSTreeNode<T> * BSTreeNode<T>::get_left_son()
{
    return this->left_son_;
}

template<typename T>
inline BSTreeNode<T> * BSTreeNode<T>::get_right_son()
{
    return this->right_son_;
}

template<typename T>
inline BSTreeNode<T> * BSTreeNode<T>::get_father()
{
    return this->father_;
}


template<typename T>
inline int BSTreeNode<T>::compare(T const & data)
{
    return this->data_.compare(data);
}

template<typename T>
inline T BSTreeNode<T>::access_data()
{
    return this->data_;
}

template<typename T>
inline void BSTreeNode<T>::set_left_son(BSTreeNode<T>* left_son)
{
    this->left_son_ = left_son;
    if (left_son != nullptr)
        left_son->father_ = this;
}

template<typename T>
inline void BSTreeNode<T>::set_right_son(BSTreeNode<T>* right_son)
{
    this->right_son_ = right_son;
    if (right_son != nullptr)
        right_son->father_ = this;
}

template<typename T>
inline void BSTreeNode<T>::reset_father()
{
    if (this->father_ != nullptr)
    {
        if (this->father_->left_son_ == this)
            this->father_->left_son_ = nullptr;
        else if (this->father_->right_son_ == this)
            this->father_->right_son_ = nullptr;

        this->father_ = nullptr;
    }

}

template<typename T>
inline void BSTreeNode<T>::switch_with(BSTreeNode<T>* node)
{
    if (node == nullptr)
        return;

    T data = this->data_;
    this->data_ = node->data_;
    node->data_ = data;
}

template<typename T>
inline bool BSTreeNode<T>::has_left_son()
{
    return this->left_son_ != nullptr;
}

template<typename T>
inline bool BSTreeNode<T>::has_right_son()
{
    return this->right_son_ != nullptr;
}

template<typename T>
inline bool BSTreeNode<T>::is_left_child()
{
    if (this->father_ != nullptr)
        return this->father_->left_son_ == this;

    return false;
}

template<typename T>
inline bool BSTreeNode<T>::is_right_child()
{
    if (this->father_ != nullptr)
        return this->father_->right_son_ == this;
    return false;
}
