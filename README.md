# Watermelon Game

A Suika-style "merge the fruit" game built with pygame: drop fruits down a shaft, and matching fruits are meant to merge into the next size up. Window caption reads "Watermelon game" (the folder used to be named "pasteque", French for watermelon).

**Status:** dropping and collision-circle detection work; the actual merge-on-collision logic is stubbed out (`update()` in `main.py` has a `pass` where the merge would happen), so it's an unfinished prototype rather than a complete game.

## Requirements
```
pip install pygame numpy
```

## Running it
```
python main.py
```
