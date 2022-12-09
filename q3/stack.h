#ifndef STACK_H
#define STACK_H

typedef struct Stack {
  void** data;
  size_t size;
  size_t capacity;
} Stack;

Stack* stack_create(size_t capacity);
void stack_destroy(Stack* stack);
void stack_push(Stack* stack, void* element);
void* stack_pop(Stack* stack);
void* stack_peek(Stack* stack);
int stack_is_empty(Stack* stack);

#endif