#include <stdio.h>
#include <stdlib.h>

typedef struct Stack {
  void** data;
  size_t size;
  size_t capacity;
} Stack;

Stack* stack_create(size_t capacity) {
  Stack* stack = malloc(sizeof(Stack));
  stack->data = malloc(capacity * sizeof(void*));
  stack->size = 0;
  stack->capacity = capacity;
  return stack;
}

void stack_destroy(Stack* stack) {
  free(stack->data);
  free(stack);
}

void stack_push(Stack* stack, void* element) {
  if (stack->size == stack->capacity) {
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void*));
  }
  stack->data[stack->size++] = element;
}

void* stack_pop(Stack* stack) {
  if (stack->size == 0) {
    return NULL;
  }
  return stack->data[--stack->size];
}

void* stack_peek(Stack* stack) {
  if (stack->size == 0) {
    return NULL;
  }
  return stack->data[stack->size - 1];
}

int stack_is_empty(Stack* stack) {
  return stack->size == 0;
}
