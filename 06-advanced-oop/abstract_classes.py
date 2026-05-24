"""Abstract base classes enforce that subclasses implement certain methods."""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float) -> str:
        """Subclasses MUST implement this."""

    def receipt(self, amount: float) -> str:
        # Concrete method shared by all subclasses
        return f"Receipt: processed {amount} via {self.process(amount)}"


class MpesaProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"M-Pesa (KES {amount})"


class CardProcessor(PaymentProcessor):
    def process(self, amount: float) -> str:
        return f"Card (KES {amount})"


for processor in [MpesaProcessor(), CardProcessor()]:
    print(processor.receipt(1500))

try:
    PaymentProcessor()   # can't instantiate an ABC directly
except TypeError as e:
    print(f"can't instantiate abstract class: {e}")
