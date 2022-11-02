# Flesch Kincaid

## Prerequisites

This project requires the package [hyphenate](https://pypi.org/project/hyphenate/)


hyphenate can be installed with the folowing command in a terminal (mac / linux) or in a command prompt (windows).

```python,
pip install hyphenate
```
## How it works
[calculation.py](calculation.py) calculates the number of; lines, words, and sylables.

[preperations.py](preperations.py) calculates the Flesch reading ease & Flesch-Kincaid grade level.

To change the file location (default is [text](text.txt)) for the tests replace *text.txt* with the path to your chosen file.

### Example
- (You would replace the example name with your chosen file)

- (This code you need to change is in [preperations.py](preperations.py))
```python
text = r'some_file_name_here_please.something'
```
