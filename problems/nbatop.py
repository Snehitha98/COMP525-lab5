"""
nbatop.py
Practice Split-Accumulate-Combine pattern to analyze database table
Mihaela Sabin
Created October 23, 2019; Updated March 10, 2020
"""


class NBATop(object):
    """
    Illustrate the split-accumulate-combine pattern
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def highest_salary_by_pos(self):
        """
        Find the highest NBA player salary for each position.
        Salary and position information is in the dataset attribute.
        Returns: dictionary
            key: string representing position
            value: integer representing highest salary for the position
        """
        # To return the dictionary with positions as keys and highest salary as
        # integer, we define an empty dictionary. which we highest_pos_d
        highest_pos_d = {}

        return highest_pos_d


if __name__ == '__main__':
    dataset = [['tom'], [1000], ['PG']]
    p = NBATop(input)
    result = p.highest_salary_by_pos()
    print(f'Highest salary by position: {result}')
