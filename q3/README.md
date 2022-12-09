# Question 3
Q3 [C] Design and implement a stack class (i.e. struct with accompanying functions). The
interface should allow storing any data type including complex structures. Describe different
implementation strategies and compare their pros and cons. What is the best approach in an
embedded real-time system? What is the best approach when memory resources are very
limited? You can use “malloc” and “free” functions.

## Answer
The implementation is in the `stack.c` file. To run the tests, use the following commands:
```
gcc stack.c test.c -o test
.\test
```

This implementation uses a dynamic array to store the elements in the stack, and it automatically increases the capacity of the stack when needed. This allows it to store any data type, including complex structures.

The Stack struct has three fields:

`data`: a pointer to the data stored in the stack. By using void* pointers, the stack can hold elements of any type without the need to specify the type of the elements when defining the Stack data structure.
`size`: the number of items currently in the stack.
`capacity`: the maximum number of items the stack can hold before it needs to be resized. 

The `stack_create()` function initializes a new stack with the given `initial_capacity`. It allocates memory for the Stack struct and the underlying data array using `malloc()`, and returns a pointer to the newly created Stack.

The `stack_destroy()` function frees the memory used by the stack, including the memory for the data array. This function should be called when the stack is no longer needed to avoid memory leaks.

The `stack_push()` function adds an item to the top of the stack. If the stack is already at capacity, it doubles the capacity of the stack before adding the new item.

The `stack_pop()` function removes the top item from the stack and returns it. If the stack is empty, it returns NULL.

This implementation uses `malloc()` and `free()` to dynamically allocate and deallocate memory as needed. It also uses `realloc()` to resize the data array when the stack reaches capacity.

## Complexity analysis

This code defines a Stack data structure using a dynamic array. `stack_push` has an amortized complexity of `O(1)`, since it only needs to reallocate the array when the stack reaches capacity, which happens at most once every logarithmic number of `stack_push` operations. All other operations on the stack have a constant time complexity of `O(1)`.

## Alternative implementation strategies

There are many different strategies that can be used to implement a Stack data structure. One common strategy is to use a dynamic array, as in the code example provided. This approach has the advantage of being relatively simple to implement, and allows for constant-time access to the top element of the stack (via the `stack_peek` function). However, it also has the disadvantage of potentially requiring frequent reallocations of the underlying array, which can be expensive in terms of time and memory.

Another common strategy is to use a linked list to implement the stack. This approach avoids the need for reallocations, since new elements can simply be added to the front of the list. However, it has the disadvantage of requiring `O(n)` time to access the top element of the stack, since it may be necessary to traverse the entire list to find it.

A third approach is to use a balanced binary tree, such as a red-black tree or an AVL tree. This allows for efficient insertion and deletion of elements, as well as efficient access to the top element of the stack. However, it requires more complex implementation and may be overkill for a simple stack data structure.

### Real-time system

In an embedded real-time system, where time and memory constraints may be more stringent, the best approach for implementing a Stack data structure would likely be to use a fixed-size array. This avoids the overhead of dynamic memory allocation and reallocation, and allows for constant-time access to the top element of the stack. It does have the disadvantage of having a fixed maximum size, but in many cases this can be determined in advance and accommodated. Additionally, if the stack is expected to frequently reach its maximum capacity, it may be necessary to implement some kind of overflow handling strategy to avoid errors.

### Limited memory resources

When memory resources are very limited, it may be necessary to use a more space-efficient approach for implementing a Stack data structure. One possible approach is to use a singly-linked list, where each node in the list contains a single element and a pointer to the next element in the stack. This approach has the advantage of requiring only a fixed, small amount of memory per element, regardless of the size of the stack. It also allows for constant-time insertion and deletion of elements. However, it has the disadvantage of requiring O(n) time to access the top element of the stack, since it may be necessary to traverse the entire list to find it. Additionally, since the list is singly-linked, it is not possible to efficiently pop elements from the bottom of the stack.
