import random


class RandomGen:

    def __init__(self, random_nums, probabilities, rand_adapter=random.random):
        """RandomGen is a class that returns a weighted random selection
        `next_num()` from a list of numbers and their probability weighting.

        Args:
            random_nums - Should contain a list of numbers. Numbers returned
                by `RandomGen.next_num` will be selected from this list.
            probabilities - Should be a list of probabilities of the occurence
                of any random_num for each element in `random_nums`.
            rand_adapter - Can be used to inject a

        Restrictions:
            - The order of elements in `probabilities` should corrospond to
              the order of elements in `random_nums`.
            - The sum of all elements in `probabilities` should be equal to 1.
            - Each element in `probabilities` must be in the range 0 <= p <= 1.

        As with any Pythonic interface RandomGen does not perform any type or
        value checks on arguement inputs. It is expected that anyone using
        this interface will adhere to the documented restrictions above.
        """
        self.random_nums = random_nums
        self.probabilities = probabilities
        self.rand_adapter = rand_adapter

    def next_num(self):
        """
        Returns one of the random_nums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        random_index = self.rand_adapter()

        for i, random_num in enumerate(self.random_nums):
            probability = self.probabilities[i]
            random_index -= probability
            if random_index <= 0:
                return random_num
