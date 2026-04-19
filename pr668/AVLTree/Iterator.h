#pragma once

template<typename T>
class StructureIterator;

template<typename T>
class Iterator;
    
template<typename T>
class Iterable
{
public:
        
    StructureIterator<T> begin() const;

    StructureIterator<T> end() const;

    StructureIterator<T> begin_lo() const;

    StructureIterator<T> end_lo() const;

    virtual Iterator<T>* get_begin_iterator() const = 0;

    virtual Iterator<T>* get_end_iterator() const = 0;

    virtual Iterator<T>* get_level_ord_begin_iterator() const = 0;

    virtual Iterator<T>* get_level_ord_end_iterator() const = 0;
};

    
template<typename T>
class StructureIterator
{
private:
    Iterator<T>* iterator_;
public:
    StructureIterator(Iterator<T>* iterator);

    virtual ~StructureIterator();

    StructureIterator<T>& operator=(const StructureIterator<T>& other);

    bool operator!=(const StructureIterator<T>& other);

    const T operator*();

    const StructureIterator<T>& operator++();
};

template<typename T>
class Iterator
{
public:
    virtual ~Iterator();

    virtual Iterator<T>& operator=(const Iterator<T>& other) = 0;

    virtual bool operator!=(const Iterator<T>& other) = 0;

    virtual const T operator*() = 0;

    virtual Iterator<T>& operator++() = 0;
};

template<typename T>
inline StructureIterator<T> Iterable<T>::begin() const
{
    return StructureIterator<T>(get_begin_iterator());
}

template<typename T>
inline StructureIterator<T> Iterable<T>::end() const
{
    return StructureIterator<T>(get_end_iterator());
}

template<typename T>
inline StructureIterator<T> Iterable<T>::begin_lo() const
{
    return StructureIterator<T>(get_level_ord_begin_iterator());
}

template<typename T>
inline StructureIterator<T> Iterable<T>::end_lo() const
{
    return StructureIterator<T>(get_level_ord_end_iterator());
}

template<typename T>
inline StructureIterator<T>::StructureIterator(Iterator<T>* iterator) :
    iterator_(iterator)
{
}

template<typename T>
StructureIterator<T>::~StructureIterator()
{
    delete iterator_;
}

template<typename T>
inline StructureIterator<T>& StructureIterator<T>::operator=(const StructureIterator<T>& other)
{
    *iterator_ = *other.iterator_;
    return *this;
}

template<typename T>
inline bool StructureIterator<T>::operator!=(const StructureIterator<T>& other)
{
    return *iterator_ != *other.iterator_;
}

template<typename T>
inline const T StructureIterator<T>::operator*()
{
    return **iterator_;
}

template<typename T>
inline const StructureIterator<T>& StructureIterator<T>::operator++()
{
    Iterator<T>* iterator = &(++*iterator_);
    if (*iterator != *iterator_)
    {
        delete iterator_;
        *iterator_ = *iterator;
    }
    return *this;
}

template<typename T>
inline Iterator<T>::~Iterator()
{
}