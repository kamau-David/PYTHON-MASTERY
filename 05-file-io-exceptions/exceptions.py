"""Exception handling: try/except/else/finally, and custom exceptions."""

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("can't divide by zero")
        return None
    except TypeError as e:
        print(f"bad types passed to divide: {e}")
        return None
    else:
        # runs only if the try block succeeded with no exception
        print("division succeeded")
        return result
    finally:
        # always runs, exception or not - good for cleanup
        print("divide() finished")


print(divide(10, 2))
print(divide(10, 0))
print(divide(10, "two"))


# Custom exceptions - subclass Exception (or a more specific built-in)
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""
    def __init__(self, balance, requested):
        super().__init__(
            f"Cannot withdraw {requested}, only {balance} available"
        )
        self.balance = balance
        self.requested = requested


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


try:
    withdraw(100, 500)
except InsufficientFundsError as e:
    print(f"Caught custom exception: {e}")
