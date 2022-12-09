#include <stddef.h>
#include <stdio.h>
#include <assert.h>
#include "stack.h"

int main() {
  // Test stack_create()
  Stack* stack = stack_create(1);
  assert(stack != NULL);
  assert(stack->size == 0);
  assert(stack->capacity == 1);

  // Test stack_push()
  stack_push(stack, (void*)1);
  assert(stack->size == 1);
  assert(stack->capacity == 1);

  // Test stack_peek()
  void* element = stack_peek(stack);
  assert(element == (void*)1);

  // Test stack_pop()
  element = stack_pop(stack);
  assert(element == (void*)1);
  assert(stack->size == 0);
  assert(stack->capacity == 1);

  // Test stack_is_empty()
  assert(stack_is_empty(stack) == 1);

  // Test stack_destroy()
  stack_destroy(stack);

  printf("Everything passed!");

  return 0;
}
