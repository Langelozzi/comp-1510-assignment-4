# 1510-Assignment-4

```angular2html
 _______  _______ _________ _______  _          _______  _______    _______ _________ _______  _______
(  ____ )(  ____ \__   __/(  ____ \( (    /|  (  ___  )(  ____ \  (  ____ \__   __/(  ____ )(  ____  \
| (    )|| (    \/   ) (   | (    \/|  \  ( |  | (   ) || (    \/  | (    \/   ) (   | (    )|| (    \/
| (____)|| (__       | |   | |      |   \ | |  | |   | || (__      | (__       | |   | (____)|| (__
|     __)|  __)      | |   | | ____ | (\ \) |  | |   | ||  __)     |  __)      | |   |     __)|  __)
| (\ (   | (         | |   | | \_  )| | \   |  | |   | || (        | (         | |   | (\ (   | (
| ) \ \__| (____/\___) (___| (___) || )  \  |  | (___) || )        | )      ___) (___| ) \ \__| (____/\
|/   \__/(_______/\_______/(_______)|/    )_)  (_______)|/         |/       \_______/|/   \__/(_______/
```

## Game Description
We have created a text based adventure game called 'Reign of Fire'. This game takes place in the dungeon of a 
medieval castle based in the 14th century. Your goal is to defeat the God Kind Thompson and rekindle the fire of 
humanity. We wish you the best of luck on your quest!

## Game details
- The game includes a variety of challenges, from enemy battles, to riddles, to room roadblocks
- In order to complete the game and defeat the king, you must first defeat both of his royal subordinates, indicated 
  on the map by red X's
- The kinds royal subordinates each possess a powerful relic that you must acquire before facing the God King Thompson
- If you die during your quest, you will not lose any items you have gained, but you will be returned to level 1, 
  and you must restart from position (1, 1)

## Game map

##### Legend
  - |#| - Your character
  - |?| - Unvisited location
  - | | - Visited location
  - |X| - Mini boss
  - |👑| - Final boss

##### Map
```
---------------------------|👑|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||X||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||X||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|#||?||?||?||?||?||?||?||?||?|
| |---------------------------
```


## Your names:

* Lucas Angelozzi
* Amir Eskandari

## Your student numbers:

* A01270381
* A01187752

## Your GitHub account IDs:

* Langelozzi
* am-eskandari

## Any important comments you'd like to make about your work:

* In some doctests, such as make_character in character.py, the tests fail unless it is all one line, therefore
  forcing us to disobey the pycharm syntax warning for line length

## Code Requirements

| Required Element                  | Location (Line Number)                                |
|:----------------------------------|:------------------------------------------------------|
| Tuple                             | character.py -- lines 199-200                         |
| List                              | character.py -- line 194                              |
| List/Dict comprehension           | helpers.py -- line 120 <br/> character.py -- line 58  |
| Selection using if                | actions.py -- line 554 <br/> character.py -- line 126 |
| Repetition with for or while loop | character.py -- line 232 <br/> helpers.py -- line 111 |
| The membership operator (in)      | helpers.py -- line 111                                |
| The range function                | board.py -- line 83                                   |
| One or more itertools functions   | board.py -- line 81 <br/> actions.py -- line 767      |
| The enumerate function            | actions.py -- line 634                                |
| The filter or map function        | helpers.py -- line 104                                |
| The random module                 | actions.py -- line 745 <br/> actions.py -- line 772   |
