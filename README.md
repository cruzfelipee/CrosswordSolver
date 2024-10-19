# Crossword Solver Algorithm

The algorithm generates a crossword board given a matrix of "." and "?", where "." represents an unfillable space and "?" represents a letter of a word.

The 11, 15 and 25 test cases were taken from the [Words Up?](https://wordsup.co.uk/) website and the list of possible words were taken from [another website](https://xd.saul.pw/data) that contains data regarding over 6000 crosswords on The New York Times since 1965.

## Algorithm

After scanning all word slots on the matrix, they are stored into an Array of words.
Each word stores its adjacent words, creating an undirected graph.
The algorithm then proceeds to loop through every invalid word and randomize their text using the ``lista_palavras.txt`` file.
The process is repeated until every word is valid or if the current valid words make the board impossible.
If the board is considered impossible, it is then reset and the algorithm runs again.
If all words on the board are considered valid, then it rebuilds the crossword matrix from the words graph and shows it on the screen.

## Dependencies
Before running the code, make sure you have tkinter installed by doing

```bash
python -m tkinter
```

## Running the code

The code uses the example boards from the "tests" folder.
You can add new test boards by following the same pattern as the other ones.
By default, the code always run the 11x11 case, you can change that by altering the ``CHOSEN_CASE`` constant at line 9 of ``Main.py``.

```python
CHOSEN_CASE = 11 # edit this
```

## Colaborators
The code was written and thought of in colaboration with [@LavieWinter](https://github.com/LavieWinter) and [@LGMarques9963](https://github.com/LGMarques9963)
