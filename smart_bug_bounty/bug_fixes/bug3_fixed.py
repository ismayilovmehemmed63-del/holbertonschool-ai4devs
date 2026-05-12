import threading

_counter = 0
_counter_lock = threading.Lock()

def add_item(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

def increment_counter(n=1):
    global _counter
    with _counter_lock:
        _counter += n
        return _counter

def reset_counter():
    global _counter
    with _counter_lock:
        _counter = 0

if __name__ == "__main__":
    cart_a = add_item("apple")
    cart_b = add_item("banana")
    assert cart_a == ["apple"]
    assert cart_b == ["banana"]
    print("Test 1 passed")
    my_cart = []
    add_item("milk", my_cart)
    add_item("eggs", my_cart)
    assert my_cart == ["milk", "eggs"]
    print("Test 2 passed")
    reset_counter()
    threads = [threading.Thread(target=increment_counter) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert _counter == 100
    print("Test 3 passed")
    print("All tests passed for bug3_fixed.py")
