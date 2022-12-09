# Question 1
[C, Python] Assume we have a function get_book_info(isbn) that takes a string ISBN argument
and retrieves an object containing the Title, Author, and Language of a book (each represented as
a string) that takes a nontrivial amount of time to run (perhaps because it’s making a call to a
database). Write a wrapper function that increases performance by keeping results in memory for
quick lookup. To prevent memory from growing unbounded, we only want to store a maximum of
N book records. At any given time, we should be storing the N books that we accessed most
recently. Assume that N can be a large number when choosing data structure(s) and
algorithm(s).

## Answer

The implementation of the wrapper function can be found in **`lru_cache.py`**. To run the tests, use the following command:
```
python test.py
```

This implementation uses an `OrderedDict` to store the results in a cache. The `OrderedDict` automatically removes the oldest entries when it reaches its maximum size, so we don't need to worry about removing items manually. When the `get_book_info` function is called with an ISBN, we check if the ISBN is already in the cache. If it is, we move it to the end of the cache to indicate that it was recently accessed. If it's not in the cache, we retrieve the book info using the original `get_book_info` function, add it to the cache, and return it.

Note that the `lru_cache` function is a decorator, which means that it takes a function as an argument and returns a modified version of that function. In the example above, the get_book_info function is passed to `lru_cache` as an argument, and the return value of `lru_cache` (which is a wrapper function) is used as a decorator for `get_book_info`. This means that whenever `get_book_info` is called, the wrapper function will be executed instead, which implements the LRU cache.

To use this implementation, you can simply decorate the `get_book_info` function with the `@lru_cache` decorator, specifying the maximum size of the cache as an argument. When the `get_book_info` function is called, the decorator will automatically handle caching the results in memory and returning them quickly if they're already in the cache.

```
from lru_cache import lru_cache

# Use the decorator to wrap the get_book_info function
@lru_cache(maxsize=1024)
def get_book_info(isbn):
  # Original implementation of the get_book_info function goes here
  pass
```

## Complexity analysis

The time complexity of the `lru_cache` function is `O(1)` for both insertion and lookup because the `OrderedDict` data structure is implemented using a doubly-linked list, which allows for constant-time insertion and lookup. The space complexity is `O(n)` where n is the maximum size of the cache specified by the `maxsize` parameter.