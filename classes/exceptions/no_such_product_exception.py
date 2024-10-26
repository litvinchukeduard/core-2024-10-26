

class NoSuchProductException(ValueError):
    def __init__(self, id: int):
        error_text = f"No such product: {id}"
        super().__init__(error_text)

        