/** Copyright [2018] <Vinicius Pizetta de Souza> */
#ifndef STRUCTURES_ARRAY_QUEUE_H
#define STRUCTURES_ARRAY_QUEUE_H

#include <cstdint>  // std::size_t
#include <stdexcept>  // C++ Exceptions

namespace structures {

/**  ArrayQueue  */
template<typename T>
class ArrayQueue {
 public:
    ArrayQueue();

    explicit ArrayQueue(std::size_t max);

    ~ArrayQueue();

    void enqueue(const T& data);

    T dequeue();

    T& back();

    void clear();

    std::size_t size();

    std::size_t max_size();

    bool empty();

    bool full();

 private:
    T* contents;
    std::size_t size_;
    std::size_t max_size_;
};

}  // namespace structures

#endif

/** construtor com parametro  */
template<typename T> structures::ArrayQueue<T>::ArrayQueue(std::size_t max) {	 	  	 	      	  	     	 	      	     	   	 	
    size_ = 0;
    max_size_ = max;
    contents = new T[max_size_];
}

/** destrutor  */
template<typename T> structures::ArrayQueue<T>::~ArrayQueue() {
    delete[] contents;
}

/** bota na fila */
template<typename T> void structures::ArrayQueue<T>::enqueue(const T& data) {
    if (full())
        throw std::out_of_range("Lista cheia");
    else
        contents[size_++] = data;
}

/** tira da fila  */
template<typename T> T structures::ArrayQueue<T>::dequeue() {
    if (empty()) {
        throw std::out_of_range("Lista vazia");
    } else {
        auto temp = contents[0];
        size_--;
        for (int i = 0; i < size_; i++)
            contents[i] = contents[i+1];
            return temp;
    }
}

/** remove o ultimo da fila  */
template<typename T> T& structures::ArrayQueue<T>::back() {
    if (empty())
        throw std::out_of_range("Lista vazia");
    return contents[size_ - 1];
}	 	  	 	      	  	     	 	      	     	   	 	

/** esvazia a fila  */
template<typename T> void structures::ArrayQueue<T>::clear() {
    size_ = 0;
}

/** retorna o tamanho atual da fila  */
template<typename T> std::size_t structures::ArrayQueue<T>::size() {
    return size_;
}

/** retorna o tamanho maximo da fila  */
template<typename T> std::size_t structures::ArrayQueue<T>::max_size() {
    return max_size_;
}

/** retorna se esta vazio  */
template<typename T> bool structures::ArrayQueue<T>::empty() {
    return size_ == 0;
}

/** retorna se esta cheio  */
template<typename T> bool structures::ArrayQueue<T>::full() {
    return size_ == max_size_;
}
	 	  	 	      	  	     	 	      	     	   	 	
