import mock
import unittest

from bin import RandomGen


class RandomGenTests(unittest.TestCase):

    def test_next_num_returns_single_possibility(self):
        """A simple situation in which only 1 number is available to be
        chosen by RandomGen with a probability of 1.
        """
        # Given
        gen = RandomGen(
            random_nums=[1],
            probabilities=[1]
        )
        # When
        num = gen.next_num()
        # Then
        self.assertEquals(num, 1)

    def test_returns_single_possibility_with_2_nums(self):
        """An edge case where 1 random number has 100% probability.
        
        Given we have 2 numbers.
        And they have probability 1 and 0 respectively
        When we call next_num() 
        Then we get the number with probability 1
        """
        gen = RandomGen(
            random_nums=[1, 2],
            probabilities=[1, 0]
        )
        num = gen.next_num()
        self.assertEquals(num, 1)

    def test_returns_single_possibility_with_3_nums(self):
        """An edge case where the last random number has 100% probability.
        
        Given we have 3 numbers.
        And they have probability 0, 0 and 1 respectively
        When we call next_num()
        Then we get the number with probability 1
        """
        gen = RandomGen(
            random_nums=[1, 2, 3],
            probabilities=[0, 0, 1]
        )
        num = gen.next_num()
        self.assertEquals(num, 3)

    def test_returns_correct_num_with_2_equal_probability_nums(self):
        """An edge case where each random number has equal probability.
        
        Given we have 2 numbers.
        And they both have probability 0.5
        And our rand_adapter produces 0.4, 0.6 and 0.1 respectively
        When we call next_num()
        Then we get the first number
        When we call next_num()
        Then we get the second number
        When we call next_num()
        Then we get the first number
        """
        rand_adapter = mock.MagicMock()  # controls random generator
        rand_adapter.side_effect = [0.4, 0.6, 0.1]
        gen = RandomGen(
            random_nums=[1, 2],
            probabilities=[0.5, 0.5],
            rand_adapter=rand_adapter
        )
        num = gen.next_num()
        self.assertEquals(num, 1)
        num = gen.next_num()
        self.assertEquals(num, 2)
        num = gen.next_num()
        self.assertEquals(num, 1)

    def test_edge_case_when_random_gen_equals_probability_limit(self):
        """An edge case where each random number has equal probability and
        the random generator returns an edge value.
        
        Given we have 2 numbers.
        And they both have probability 0.5
        And our rand_adapter produces 0.5
        When we call next_num()
        Then we get the first number
        """
        rand_adapter = mock.MagicMock(return_value=0.5)  # controls random generator
        gen = RandomGen(
            random_nums=[1, 2],
            probabilities=[0.5, 0.5],
            rand_adapter=rand_adapter
        )
        num = gen.next_num()
        self.assertEquals(num, 1)

    def test_returns_correct_num_with_many_probabilities(self):
        """Test a complicated case with many random numbers and 
        probabilities

        Given we have many random numbers -1, 0, 1, 2 and 3.
        And they both have probabilities 0.01, 0.3, 0.58, 0.1 and 0.01
        And our rand_adapter produces 0.4, 0, 0.01, 1, 0.9119233 and 0.2
        When we call next_num()
        Then we get 1
        When we call next_num()
        Then we get -1
        When we call next_num()
        Then we get -1
        When we call next_num()
        Then we get 3
        When we call next_num()
        Then we get 2
        When we call next_num()
        Then we get 0
        """
        rand_adapter = mock.MagicMock()
        rand_adapter.side_effect = [0.4, 0, 0.01, 1, 0.9119233, 0.2]
        gen = RandomGen(
            random_nums=[-1, 0, 1, 2, 3],
            probabilities=[0.01, 0.3, 0.58, 0.1, 0.01],
            rand_adapter=rand_adapter
        )
        num = gen.next_num()  # side_effect -> 0.4
        self.assertEquals(num, 1)
        num = gen.next_num()  # side_effect -> 0
        self.assertEquals(num, -1)
        num = gen.next_num()  # side_effect -> 0.01
        self.assertEquals(num, -1)
        num = gen.next_num()  # side_effect -> 1
        self.assertEquals(num, 3)
        num = gen.next_num()  # side_effect -> 0.9119233
        self.assertEquals(num, 2)
        num = gen.next_num()  # side_effect -> 0.2
        self.assertEquals(num, 0)
