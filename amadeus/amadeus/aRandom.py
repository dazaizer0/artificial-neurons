class RandomModule:
    nr: int

    def __init__(self, number):
        """
        Random is randomness manager for amadeus
        :param number:
        """
        self.nr: int = number

    def __repr__(self):
        print(self.nr)
