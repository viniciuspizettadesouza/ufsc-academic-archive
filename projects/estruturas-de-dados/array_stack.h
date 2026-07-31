/** Copyright [2018] <Vinicius Pizetta de Souza> */
#ifndef STRUCTURES_ARRAY_STACK_H
#define STRUCTURES_ARRAY_STACK_H

#include <cstdint>  // std::size_t
#include <stdexcept>  // C++ exceptions

namespace structures {

/**ArrayStack*/
template<typename T>
class ArrayStack {
 public:
    ArrayStack();

    explicit ArrayStack(std::size_t max);

    ~ArrayStack();

    void push(const T& data);  // empilha

    T pop();  // desempilha

    T& top();

    void clear();  // limpa

    std::size_t size();  // tamanho

    std::size_t max_size();

    bool empty();  // vazia

    bool full();  // cheia

 private:
        T* contents;
        int top_;
        std::size_t max_size_;
};

}  // namespace structures

#endif

/** Construtor */
template<typename T> structures::ArrayStack<T>::ArrayStack(std::size_t max) {	 	  	 	      	  	     	 	      	     	   	 	
    top_ = -1;
    max_size_ = max;
    contents = new T[max_size_];
}

template<typename T> structures::ArrayStack<T>::~ArrayStack() {
    delete[] contents;
}

/** Bota um elemento na stack */
template<typename T> void structures::ArrayStack<T>::push(const T& data) {
    if (full())
        throw std::out_of_range("Lista cheia");
    contents[++top_] = data;
}

/** Tira o component do topo*/
template<typename T> T structures::ArrayStack<T>::pop() {
    if (empty())
        throw std::out_of_range("Lista vazia");
    else
        return contents[top_--];
}

/** Limpa a stack */
template<typename T> void structures::ArrayStack<T>::clear() {
    top_ = -1;
}

/** retorn o tamanho atual da stack */
template<typename T> size_t structures::ArrayStack<T>::size() {
    return top_ + 1;
}

/** retorna o tamanho total da stack */
template<typename T> size_t structures::ArrayStack<T>::max_size() {	 	  	 	      	  	     	 	      	     	   	 	
    return max_size_;
}

/** retorn o component que esta no topo do stack */
template<typename T> T& structures::ArrayStack<T>::top() {
    return contents[top_];
}

/** retorna se a stack esta vazia */
template<typename T> bool structures::ArrayStack<T>::empty() {
    if (top_ == -1)
        return true;
    return false;
}

/** retorn se a a stack esta cheia */
template<typename T> bool structures::ArrayStack<T>::full() {
    if (top_ == max_size_-1)
        return true;
    return false;
}
