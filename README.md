# Watermelon Game

A "merge the fruit" game built with pygame, in the style of Suika: you drop fruits down a shaft, and matching fruits are meant to merge into the next size up. The window caption reads "Watermelon game" (the folder used to be named "pasteque", French for watermelon).

**Status:** dropping and circle based collision detection both work; the actual merging logic on collision is stubbed out (`update()` in `main.py` has a `pass` where the merge would happen), so this is an unfinished prototype rather than a complete game.

## Requirements
```
pip install pygame numpy
```

## Running it
```
python main.py
```
