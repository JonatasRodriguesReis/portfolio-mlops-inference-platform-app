from abc import ABC, abstractmethod

class InferenceModel(ABC):
    """
    Contract for any inference model.
    """

    @abstractmethod
    def predict(self, input_text: str) -> str:
        pass