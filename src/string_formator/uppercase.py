from .formator import Formator


class UpperCase(Formator):
    @staticmethod
    def format(text: str) -> str:
        return text.upper()
