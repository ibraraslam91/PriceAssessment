from .formator import Formator


class AlterCase(Formator):
    @staticmethod
    def format(text: str) -> str:
        return "".join(
            [
                char.lower() if index % 2 == 0 else char.upper()
                for index, char in enumerate(text)
            ]
        )
