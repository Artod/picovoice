# Import the lru_cache function
from lru_cache import lru_cache

def test_return_callable():
  # Test that the function returns a decorator when called with no arguments.

  @lru_cache()
  def get_book_info(isbn):
    return "Book info for ISBN: {}".format(isbn)

  assert callable(get_book_info)

def test_cache():
  # Test that the decorator returned by the function correctly caches the results of the decorated function.
  @lru_cache()
  def get_book_info(isbn):
    return "Book info for ISBN: {}".format(isbn)

  # The first call to get_book_info should not be in the cache, so it should return the book info
  assert get_book_info("1234567890") == "Book info for ISBN: 1234567890"

  # The second call to get_book_info should return the same result, but it should be cached now
  assert get_book_info("1234567890") == "Book info for ISBN: 1234567890"

def test_remove_lru_item():
  # Test that the decorator correctly removes the least recently used entries when the cache is full.

  call_cnt = 0
  @lru_cache(maxsize=3)
  def get_book_info(isbn):
    nonlocal call_cnt
    call_cnt += 1
    return "Book info for ISBN: {} - {}".format(isbn, call_cnt)

  # Add three items to the cache
  get_book_info("1")
  get_book_info("2")
  get_book_info("3")

  # Add a fourth item to the cache
  get_book_info("4")

  # The first item should have been removed from the cache because it was the least recently used
  assert get_book_info("1") == "Book info for ISBN: 1 - 5"

if __name__ == "__main__":
  test_return_callable()
  test_cache()
  test_remove_lru_item()
  
  print("Everything passed!")
