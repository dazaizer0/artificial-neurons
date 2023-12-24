import random as rd

class RandomModule:
    def GET_RANDOM_NUMBER(self, from_number: int, to_number: int) -> int:
        return rd.randint(0, 1)  # temporary