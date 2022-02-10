from .base import Output


class Print(Output):
    @staticmethod
    def write(content: str):
        print(content)
