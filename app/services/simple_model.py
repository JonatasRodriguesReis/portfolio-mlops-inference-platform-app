from core.model import InferenceModel

class SimpleRuleBasedModel(InferenceModel):
    """
    Simple model that simulates inference.
    """

    def predict(self, input_text: str) -> str:
        if "error" in input_text.lower():
            return "Detected potential issue in input"
        return "Input processed successfully"