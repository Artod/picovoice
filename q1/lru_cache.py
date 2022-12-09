from collections import OrderedDict

def lru_cache(maxsize=128):
  # Inner function to be used as a decorator
  def decorator(get_book_info):
    # Create an OrderedDict to store the results in
    # The OrderedDict will automatically remove the oldest entries when it reaches its maxsize
    cache = OrderedDict()

    # Wrapper function to implement the LRU cache
    def wrapper(isbn):
      # Check if the ISBN is already in the cache
      if isbn in cache:
        # If it is, move it to the end of the cache to indicate it was recently accessed
        book_info = cache.pop(isbn)
        cache[isbn] = book_info
      else:
        # If it's not in the cache, retrieve the book info using the original get_book_info function
        book_info = get_book_info(isbn)

        # If the cache is full, remove the oldest entry
        if len(cache) >= maxsize:
          cache.popitem(last=False)          

        # Add the new book info to the cache
        cache[isbn] = book_info

      # Return the book info
      return book_info

    # Return the wrapper function
    return wrapper

  # Return the inner function to be used as a decorator
  return decorator
