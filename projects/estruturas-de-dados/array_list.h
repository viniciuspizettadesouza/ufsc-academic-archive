/** Copyright [2018] <Vinicius Pizetta de Souza> */
#ifndef STRUCTURES_ARRAY_LIST_H
#define STRUCTURES_ARRAY_LIST_H

#include <cstdint>  // std::size_t
#include <stdexcept>  // C++ exceptions
#include <algorithm>

namespace structures {

/**ArrayList*/
template<typename T>
class ArrayList {
 public:
    ArrayList();
    explicit ArrayList(std::size_t max_size);
    ~ArrayList();

    void clear();
    void push_back(const T& data);
    void push_front(const T& data);
    void insert(const T& data, std::size_t index);
    void insert_sorted(const T& data);
    T pop(std::size_t index);
    T pop_back();
    T pop_front();
    void remove(const T& data);
    bool full() const;
    bool empty() const;
    bool contains(const T& data) const;
    std::size_t find(const T& data) const;
    std::size_t size() const;
    std::size_t max_size() const;
    T& at(std::size_t index);
    T& operator[](std::size_t index);
    const T& at(std::size_t index) const;
    const T& operator[](std::size_t index) const;

 private:
    T* contents;
    std::size_t size_;
    std::size_t max_size_;
    static const auto DEFAULT_MAX = 10u;
};

}  // namespace structures

#endif

/** Construtor sem parâmetro */
template<typename T>
structures::ArrayList<T>::ArrayList() {	 	  	 	      	  	     	 	      	     	   	 	
    size_ = 0;
    max_size_ = DEFAULT_MAX;
    contents = new T[DEFAULT_MAX];
}

/** Construtor com parâmetro */
template<typename T>
structures::ArrayList<T>::ArrayList(std::size_t max_size) {
    size_ =  0;
    max_size_ = max_size;
    contents = new T[max_size_];
}

/** Destrutor */
template<typename T>
structures::ArrayList<T>::~ArrayList() {
    delete[] contents;
}

/** Limpa a lista */
template<typename T>
void structures::ArrayList<T>::clear() {
    size_ = 0;
}

/** Bota um elemento no final */
template<typename T>
void structures::ArrayList<T>::push_back(const T& data) {
    insert(data, size_);
}

/** Bota um elemento no início */
template<typename T>
void structures::ArrayList<T>::push_front(const T& data) {
    insert(data, 0);
}	 	  	 	      	  	     	 	      	     	   	 	

/** Bota um elemento na posição */
template<typename T>
void structures::ArrayList<T>::insert(const T& data, std::size_t index) {
    if (full())
        throw std::out_of_range("Lista cheia");
    if (index > size_)
        throw std::out_of_range("Indice nao valido");
    for (int i = size_; i > index; i--) {
        contents[i] = contents[i-1];
    }
    contents[index] = data;
    size_++;
}

/** Bota um elemento em ordem alfabética */
template<typename T>
void structures::ArrayList<T>::insert_sorted(const T& data) {
    if (full())
        throw std::out_of_range("Lista cheia");
    for (int i = 0 ; i < size_ ; i++) {
        if (data < contents[i]) {
            insert(data, i);
            return;
        }
    }
    push_back(data);
}

/** Tira o elemento na posição */
template<typename T>
T structures::ArrayList<T>::pop(std::size_t index) {
    if (empty())
       throw std::out_of_range("Lista vazia");
    if (index >= size_)
        throw std::out_of_range("Indice nao valido");
    auto data = contents[index];
    for (int i = index; i < size_; i++)
        contents[i - 1] = contents[i];
    size_--;
    return data;
}	 	  	 	      	  	     	 	      	     	   	 	
/** Tira o último elemento */
template<typename T>
T structures::ArrayList<T>::pop_back() {
    if (empty())
       throw std::out_of_range("Lista vazia");
    auto data = contents[--size_];
    contents[size_] = 0;
    return data;
}

/** Tira o primeiro elemento */
template<typename T>
T structures::ArrayList<T>::pop_front() {
    if (empty())
        throw std::out_of_range("Lista vazia");
    auto data = contents[0];
    for (int i = 1; i < max_size_; i++)
        contents[i - 1] = contents[i];
    size_--;
    return data;
}

/** Remove um elemento específico */
template<typename T>
void structures::ArrayList<T>::remove(const T& data) {
    int index = find(data);
    if (index > -1) {
        contents[index] = 0;
        for (int i = index; i < max_size_; i++)
            contents[i - 1] = 1;
        size_--;
    }
}

/** Retorna se está cheia */
template<typename T>
bool structures::ArrayList<T>::full() const {	 	  	 	      	  	     	 	      	     	   	 	
    return size_ == max_size_;
}

/** Retorna se está vazio */
template<typename T>
bool structures::ArrayList<T>::empty() const {
    return size_ == 0;
}

/** Retorna se contem o elemento parametro */
template<typename T>
bool structures::ArrayList<T>::contains(const T& data) const {
    for (int i = 0; i < size_; i++) {
        if (contents[i] == data)
            return true;
    }
    return false;
}

/** Retorna o índica do elemento parametro */
template<typename T>
std::size_t structures::ArrayList<T>::find(const T& data) const {
    for (int i = 0; i < size_; i++) {
        if (contents[i] == data)
            return i;
    }
    return size_;
}

/** Retorna o tamanho atual da lista */
template<typename T>
std::size_t structures::ArrayList<T>::size() const {
    return size_;
}

/** Retorna o tamanho máximo da lista */
template<typename T> std::size_t structures::ArrayList<T>::max_size() const {	 	  	 	      	  	     	 	      	     	   	 	
    return max_size_;
}

/** Retorna o elemento do índice parametro */
template<typename T> T& structures::ArrayList<T>::at(std::size_t index) {
    if (index > size_)
        throw std::out_of_range("Lista vazia");
    return contents[index];
}

/** Retorna o elemento na posição parametro */
template<typename T>
T& structures::ArrayList<T>::operator[](std::size_t index) {
    if (index > size_)
        throw std::out_of_range("Lista vazia");
    return contents[index];
}

/** Retona o elemento na posicação parametro */
template<typename T>
const T& structures::ArrayList<T>::at(std::size_t index) const {
    if (index > size_)
        throw std::out_of_range("Lista vazia");
    return contents[index];
}
/** Retorna o elemento da poisção parametro */
template<typename T>
const T& structures::ArrayList<T>::operator[](std::size_t index) const {
    if (index > size_)
        throw std::out_of_range("Lista vazia");
    return contents[index];
}
	 	  	 	      	  	     	 	      	     	   	 	
