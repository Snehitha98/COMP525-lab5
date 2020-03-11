## Lab5: Practice with _split-accumulate-combine_ Pattern
Design, implement, and test __highest_salary_by_pos()__ method in __NBATop__ class in __nbatop.py__ module of __problems__ Python package of __lab5__ repository.

The directory/file structure of the __lab5__ is:
```bash
├── README.md
├── problems
│   ├── __init__.py
│   ├── __pycache__
│   └── split_accumulate_combine.py
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_highest_salary_by_pos.py
```

Method signature and docstring
```python
    def highest_salary_by_pos(self, data):
        """
        Find the highest NBA player salary for each position.
        data: list of three parallel lists
            1st list has players names as strings, 2nd list has their salaries
            as integers, 3rd list has their positions as strings
        Returns: dictionary
            key: string representing position
            value: integer representing highest salary for the position
        """
```

### Top-Level Design Approach
We break down the problem into three subproblems:
To apply the ___split_accumulate_combine___ pattern, we should:
1. ___Split___ salaries by position to get the list of salaries corresponding to each position
2. ___Accumulate___ the maximum salary of the list of salaries for each position
3. ___Combine___ the position and max salary pairs in a data structure that gets returned.

To solve each subproblem, we ask guiding questions that help us figure out the computational steps of the problem solution.

#### 1. Split salaries by position to get the list of the salaries corresponding to each position

_Question 1.1_: What input data are needed?

_Answer_: From the ```data``` parameter, we need:
* the 2nd list, which has the players' salaries, and
* the 3rd list that has the players's positions.

___Computational Step 1___:
* Define and initialize local variable ```salaries``` with the 2nd list in ```data```
* Define and initialize local variable ```positions``` with the 3rd list in ```data```

_Question 1.2_: What do we know about the input data we'll be using?

_Answer_: ```salaries``` and ```positions``` are two __parallel__ lists. This means that, for example, ```salaries[3]``` (the 4th element in ```salaries``` list) is the salary for ```positions[3]``` in the ``` positions``` list.

_Questioni 1.3_: What does it mean to __split__ salaries by position to get a list of salaries corresonding to each position? Is there a specific data structure that woudl model this kind of grouping?

_Answer_: YES! Splitting or associating things with something else is best represented by a __dictionary__ data structure. In our case, each position is a __key__ and the list of corresonding salaries to that position is a __value__. What we want to get from the grouping computation is something like:
```python
{'C': [27977689, 27739975, 26011913, 25976111], 'PF': [18622514, 18622514], ...}
```

___Computational Step 2___: To get a dictionary out of the splitting computations:
* We define and initialize with empty dictionary the local variable ```salaries_by_pos```
* This dictionary has positions as keys and lists of salaries as values.

_Question 1.4_: How do we process the two __parallel__ lists ```salaries``` and ```positions``` to get the splitting by position into the ```salaries_by_pos``` dictionary?
_Answer_: Because of the lists' parallelism, it's important to have the __position__
or __index__ of each element in both lists.

_Question 1.5_: How do we go about creating ```salaries_by_pos``` dictionary  from indexing the two  parallel lists? To figure this out, we consider a very simple, made-up example of the two parallel lists, in which we show their common indices and values corresonding to those indices.

 index | 0 | 1 | 2 | 3
-------| - | - | - | -
salaries | 8M | 2M | 1M | 12M
positions | PG | C |  PF | PG

The output ```salaries_by_pos``` dictionary will be:
```
{'PG': [8M, 12M], 'C': [2M], 'PF': [1M]}
```

__HINT__: Try do it by hand, using pencil and paper, as if you are a machine that gets instructions...

_Answer_: We apply the __accumulation__ pattern to iterate over the sequence of indices in the two lists and accumulate in ```salaries_by_pos``` dictionary the output.  

___Computational Step 3___:
To apply the __accumulation__ pattern, we use a ```for ... in ...``` statement:
* The iterable we iterate through is the sequence ```range(salaries)``` OR ```range(len(positions))```. It doesn't matter which one we pick. Either of them we'll give us the sequence of indices of both lists.
* The loop variable is __index__ of type integer with values from 0, 1, ...
* The accumulator is ```salaries_by_pos``` dictionary data structure

1. At each iteration, we check if the position at current index, ```positions[index]```, is a key in the dictionary ```salaries_by_pos```
2. If the dictionary already has the key, it means that the key already has associated with it a list of salaries
    * Thus, we append the salary at the current index, ```salaries[index]```, to the value associated with the key ```position[index]```
3. Otherwise the dictionary does not have that key
    * So we create a new pair that has the key ```position[index]``` and as value a list with one element, ```salaries[index]```

With these three computation steps we solve the first subproblem.

We note that the 3rd computation step is the most complext. I suggest that we create additional local variables to simplify the implementation of the 3rd step.

Inside the loop, before we do the checking:
* Define variable ```key``` and initialize it with ```positions[index]```
* Define variable ```a_salary``` and initialize it with ```salaries[index]```

We use the variable ```key``` to check if it is in ```salaries_by_pos``` dictionary.
The value corresponding to ```key``` in the dictionary is ```salaries_by_pos[key]```. This value the list of salaries.

#### 2. Accumulate the maximum salary of the list of salaries for each position
_Question 2.1_: How do we accumulate the maximum salary of the list of salaries for each key in the dictionary ```salaries_by_pos```?

_Answer_: We apply the __accumulation__ pattern to iterate through the dictionary.

___Computational Step 4___:
To apply the __accumulation__ pattern, we use ```for ... in ...``` statement:
* The iterable we iterate through is the dictionary ```salaries_by_pos```:
* The loop variable is ```key``` of type string that represents a player's position
* The accumulator is the output dictionary ```result```
    * the keys are the same keys as in ```salaries_by_pos```
    * the values are integers that represent the max salary

1. At each iteration we access the dictionary value corresponding to ```key```, that is, ```salaries_by_pos[key]```. This is the list of salaries corresonding to ```key```.
2. We compute the max with builtin function ```max()``` applied to the salary list value, ```salaries_by_pos[key]```, and store it in some local variable ```max_salary```
3. We add this new pair, ```key``` and ```max_salary``` to the ```result``` dictionary.

#### 3. Combine the position and max salary pairs in a data structure that gets returned
The dictionary ```result``` already contains position and max salary pairs.
___Computational Step 5___:
Return ```result```.
