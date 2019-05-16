# Queues

- the first element could be accessible
- First in First out policy —> seems like the queue in supermarket
- Insert —> enqueue  Delete —>dequeue
- Elementes are added to the tail and are extracted from the head

## Basic

- enqueue()

- dequeue()

  

## Enqueue method

- check if the queue is full
- if the queue is full, produce overflow error
- if the queue is not full increment **rear** pointer to point the next empty space.
- Add data element to the queue location, where the rear is pointing.

>last=last+1
>
>queue[last]=data
>
>

## Dequeue method

- check if the queue is empty
- if the queue is empty,produce underflow error
- if the queue is not empty,access the data where the first is pointing
- Increment **front** pointer to point to the next available data element.

>data=queue[first]
>
>first=first+1

## runtime of queue

all queue operation take time O(1)