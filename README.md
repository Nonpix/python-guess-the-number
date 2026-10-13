# python-guess-the-number

A simple console game written in Python. The computer picks a random number between 1 and 100, and you try to guess it. After each guess, the program tells you whether your number is too high or too low, and shows how many attempts you needed once you get it right.

## Features

- Random number between 1 and 100
- Hints after each guess ("too high" / "too low")
- Attempt counter
- Limited to 7 attempts

## Requirements

- Python 3

## How to run

```bash
python zahlenraten.py
```

## Example

```
Gib eine Zahl zwischen 1 und 100 ein: 50
zu niedrig
Gib eine Zahl zwischen 1 und 100 ein: 75
zu hoch
Gib eine Zahl zwischen 1 und 100 ein: 63
Erraten! Du hast 3 Versuche gebraucht.
```

## What I practiced

- `input()` and type conversion with `int()`
- `while` loops and `if` / `elif` / `else`
- Using the `random` module
