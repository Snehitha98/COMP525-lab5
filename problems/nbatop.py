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

    def highest_salary_by_pos(self, nba_data):
        """
        Find the highest NBA player salary for each position.
        Salary and position information is in the dataset attribute.
        Returns: dictionary
            key: string representing position
            value: integer representing highest salary for the position
        """
        # To return the dictionary with positions as keys and highest salary as
        # integer, we define an empty dictionary. which we highest_pos_d
        salaries = nba_data[1]
        positions = nba_data[2]
        salaries_by_pos = {}
        for index in range(len(salaries)):
            key = positions[index]
            a_salary = salaries[index]
            if key in salaries_by_pos:
                salaries_by_pos[key] += [a_salary]
            else:
                salaries_by_pos[key] = [a_salary]
        result = {}
        for key in salaries_by_pos:
            values = salaries_by_pos[key]
            max_salary = max(values)
            result[key] = max_salary
        return result


if __name__ == '__main__':
    nba_data = [['tom'], [1000], ['PG']]
    p = NBATop()
    result = p.highest_salary_by_pos(nba_data)
    print(f'Highest salary by position: {result}')
