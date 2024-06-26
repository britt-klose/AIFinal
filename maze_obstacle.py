
############################################################
#### Maze structure with obstacle:
### if you use this maze and search for oncology it will
### return error that path cannot be found
############################################################
maze = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 4, 4, 1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 4, 4, 1, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 4, 4, 4, 4, 4, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 5, 5, 5, 5, 5, 1, 3, 3, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 9, 1, 1, 1, 1, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 5, 5, 1, 1, 1, 1, 3, 3, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 9, 9, 9, 1, 4, 4, 4, 4, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1, 4, 1, 1, 1, 0, 0, 0, 0, 5, 5, 5, 5, 1, 3, 3, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 1, 9, 9, 9, 1, 4, 4, 4, 4, 1, 4, 4, 4, 1, 4, 4, 4, 1, 4, 1, 1, 1, 1, 4, 4, 4, 9, 9, 1, 0, 0, 0, 5, 5, 5, 5, 5, 1, 3, 3, 1, 1],
[1, 1, 1, 9, 0, 0, 0, 1, 1, 9, 9, 9, 1, 4, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 1, 4, 4, 4, 4, 1, 4, 4, 4, 9, 9, 1, 0, 0, 1, 5, 5, 5, 5, 5, 1, 3, 3, 1, 1],
[1, 1, 1, 9, 0, 0, 0, 1, 9, 9, 9, 9, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 1, 1, 1, 4, 1, 1, 1, 1, 4, 4, 1, 1, 9, 1, 0, 0, 1, 1, 1, 1, 5, 5, 1, 3, 3, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 1, 9, 0, 1, 1, 1, 1, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 5, 5, 5, 1, 9, 0, 0, 0, 1, 5, 5, 5, 5, 5, 3, 3, 3, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 4, 1, 1, 1, 1, 4, 4, 1, 5, 5, 5, 9, 9, 9, 0, 0, 1, 5, 5, 5, 5, 5, 3, 3, 3, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 4, 1, 1, 4, 4, 4, 4, 1, 5, 5, 9, 1, 1, 1, 0, 0, 1, 5, 5, 5, 5, 5, 3, 3, 3, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 4, 4, 11, 1, 4, 4, 4, 1, 4, 4, 4, 4, 4, 5, 5, 9, 9, 9, 9, 0, 0, 1, 5, 5, 5, 5, 5, 3, 3, 3, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1, 7, 7, 7, 7, 1, 11, 4, 4, 11, 1, 4, 4, 11, 1, 4, 4, 1, 1, 1, 1, 1, 4, 1, 1, 5, 1, 1, 1, 1, 0, 0, 1, 5, 5, 5, 5, 5, 3, 3, 3, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1, 7, 7, 1, 1, 1, 11, 11, 11, 11, 1, 11, 11, 11, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 5, 5, 7, 5, 5, 1, 0, 0, 1, 8, 8, 3, 3, 3, 3, 3, 3, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1, 7, 7, 7, 7, 1, 11, 1, 11, 11, 1, 11, 11, 11, 1, 1, 1, 1, 1, 1, 1, 1, 4, 5, 5, 5, 7, 5, 5, 0, 0, 0, 1, 8, 8, 3, 3, 1, 3, 3, 3, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 1, 7, 1, 7, 7, 1, 11, 1, 11, 11, 1, 11, 11, 11, 11, 11, 11, 4, 4, 4, 1, 9, 9, 1, 1, 1, 7, 1, 1, 1, 0, 0, 1, 8, 8, 3, 3, 1, 1, 1, 1, 1, 1],
[0, 0, 1, 1, 1, 0, 0, 1, 7, 1, 7, 7, 7, 11, 1, 11, 11, 1, 1, 1, 11, 1, 11, 11, 4, 4, 4, 1, 9, 9, 9, 9, 1, 7, 7, 7, 1, 0, 0, 1, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1],
[0, 0, 1, 1, 1, 0, 0, 1, 7, 1, 7, 7, 7, 1, 1, 11, 11, 11, 11, 11, 11, 1, 4, 4, 4, 4, 4, 1, 9, 9, 9, 9, 1, 7, 7, 7, 1, 0, 0, 1, 8, 8, 8, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 9, 1, 1, 1, 0, 1, 0, 0, 1, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 8, 8, 8, 8, 8, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 12, 0, 12, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 8, 8, 8, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 1, 3, 1, 3, 3, 3, 1, 12, 12, 1, 12, 12, 12, 1, 0, 0, 1, 6, 6, 6, 6, 6, 1, 7, 1, 7, 7, 7, 1, 8, 8, 8, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 7, 7, 1, 7, 1, 3, 1, 3, 3, 3, 1, 12, 12, 12, 12, 12, 12, 1, 0, 0, 0, 6, 6, 6, 6, 6, 1, 7, 1, 7, 7, 7, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 7, 7, 7, 7, 1, 7, 7, 3, 3, 3, 3, 3, 1, 12, 12, 12, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 6, 6, 1, 7, 1, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 7, 7, 1, 1, 1, 1, 1, 12, 12, 12, 1, 10, 0, 0, 0, 0, 1, 6, 6, 6, 6, 6, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 7, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 10, 10, 1, 0, 0, 1, 6, 6, 6, 6, 6, 1, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 7, 7, 7, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 1, 1, 1, 10, 10, 1, 0, 0, 1, 1, 1, 6, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 7, 7, 7, 7, 1, 10, 10, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1, 1, 0, 0, 1, 6, 6, 6, 1, 6, 1, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 7, 7, 7, 7, 7, 7, 1, 10, 10, 1, 10, 10, 1, 10, 1, 1, 10, 10, 10, 1, 0, 0, 1, 6, 6, 6, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 10, 10, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 1, 6, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 6, 1, 6, 1, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 10, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 10, 0, 6, 1, 0, 6, 1, 1, 6, 6, 6, 1, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 7, 7, 1, 10, 10, 1, 10, 10, 1, 10, 10, 1, 10, 10, 1, 10, 10, 10, 1, 10, 1, 10, 10, 6, 1, 6, 6, 6, 1, 6, 6, 6, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 1, 7, 7, 1, 10, 10, 1, 10, 10, 1, 10, 10, 1, 10, 10, 10, 10, 1, 10, 10, 10, 1, 10, 10, 6, 1, 6, 6, 6, 1, 1, 1, 13, 1, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1],
[1, 1, 1, 1, 1, 0, 0, 0, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 10, 10, 1, 1, 10, 10, 6, 1, 1, 1, 6, 13, 13, 13, 13, 13, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1],
[1, 1, 1, 1, 1, 9, 9, 9, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 1, 1, 1, 6, 6, 6, 13, 13, 13, 13, 13, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1],
[1, 1, 1, 1, 1, 9, 9, 9, 10, 10, 10, 10, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 6, 6, 6, 6, 6, 13, 13, 13, 13, 13, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
