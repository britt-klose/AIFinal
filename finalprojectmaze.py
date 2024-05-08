#######################################################
#### Final Project Hospital Floorplan
#### pathfinding using A*.
####
#### AI, Spring 2024
#######################################################
import tkinter as tk
from PIL import ImageTk, Image, ImageOps
from queue import PriorityQueue
import heapq
import time


######################################################
#### A cell stores f(), g() and h() values
#### A cell is either open or part of a wall
######################################################

class Cell:
    #### Initially, maze cells have g() = inf and h() = 0
    def __init__(self, x, y, is_wall=False):
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.g = float("inf")
        self.h = 0
        self.f = float("inf")
        self.parent = None

    #### Compare two cells based on their evaluation functions
    def __lt__(self, other):
        return self.f < other.f


######################################################
# A maze is a grid of size rows X cols
######################################################
class MazeGame:
    def __init__(self, root, maze):
        self.root = root
        self.maze = maze

        self.rows = len(maze)
        self.cols = len(maze[0])

    ##########################
    ## Goal states & Ward Key:
    ##########################
        locations={
            "emergency":(1,(23,33)),
            "admissions":(5,(19,46)),
            "pediatric":(3,(36,18)),
            "general":(5,(18, 15)),
            "burn":(1,(26, 16)),
            "maternity":(3,(5, 10)),
            "surgical":(2,(31, 33)),
            "medical":(1,(46, 36)),
            "isolation":(5,(14, 9)),
            "oncology":(1,(33, 38)),
            "icu":(1,(27, 42)),
            "hematology":(3,(31, 23))
            }

        self.cells = [[Cell(x, y, maze[x][y] == 1) for y in range(self.cols)] for x in range(self.rows)]
        # ==1 means anything that's not 1 is open
        
    ########################################################
    ## Start State: User inputs start location in form (x, y)
    ########################################################
        check=1
        while check:
            try:
                print("Enter my start state: ")
                I1 = int(input())
                I2 = int(input())
                self.agent_pos = (I1, I2)
                if not self.cells[self.agent_pos[0]][self.agent_pos[1]].is_wall:
                    self.agent_pos = self.agent_pos
                # Returns error if start state is a wall
                else:
                    raise ValueError("Error, illegal start position")
            except ValueError as e:
                print(e)
            else:
                check=0
                
    ##############################
    ### User inputs wards to hit
    #############################
        check=1
        while check:
            try:

                print(f"You are currently at {self.agent_pos}")
                Ginput= input("Enter ward destinations separated by a comma: ").split(',')
                print(f"Wards to hit:  ({len(Ginput)}) {Ginput}")

                #Create Priority Queue to store all goal locations
                pg=PriorityQueue()
                for i in [locations[x.strip()] for x in Ginput]:
                    pg.put((i[0], i[1]))
            #Returns error if input doesn't match any goal states above
            except:
                print(f"Invalid input! Please renter:")
            else:
                check=0

        self.cell_size = 15
        self.canvas = tk.Canvas(root, width=self.cols * self.cell_size, height=self.rows * self.cell_size, bg='white')
        self.canvas.pack()
        self.draw_maze()

    #############################################
    ### User inputs which search algorithm to use
    ############################################
        algo = input("Which algorithm should I use? Enter 'A' for A* and 'D' for Djikstra's: ").lower()
        print(algo)
        ### A*
        if algo == 'a':
            print("Using A*")
            while not pg.empty():
                self.goal_pos=pg.get()[1]
                #### Start state's initial values for f(n) = g(n) + h(n)
                self.cells[self.agent_pos[0]][self.agent_pos[1]].g = 0
                self.cells[self.agent_pos[0]][self.agent_pos[1]].h = self.heuristic(self.agent_pos)
                self.cells[self.agent_pos[0]][self.agent_pos[1]].f = self.heuristic(self.agent_pos)
                print("Locating ward")
                print("Start location: ", self.agent_pos)
                print("Goal: ", self.goal_pos)
                self.find_path()
                self.agent_pos=self.goal_pos
                for cell in self.cells:
                    for c in cell:
                        c.g=float('inf')
        ### Dijkstra
        if algo == 'd':
            print("Using Djikstra's")
            while not pg.empty():
                self.goal_pos=pg.get()[1]
                #### Start state's initial values for f(n) = g(n)
                self.cells[self.agent_pos[0]][self.agent_pos[1]].g = 0
                self.cells[self.agent_pos[0]][self.agent_pos[1]].f = self.agent_pos
                print("Locating ward")
                print("Start location: ", self.agent_pos)
                print("Goal: ", self.goal_pos)
                self.find_path_D()
                self.agent_pos=self.goal_pos
                for cell in self.cells:
                    for c in cell:
                        c.g=float('inf')


        if pg.empty():
            print("All tasks completed successfully!")


    ############################################################
    #### GUI part. Colors maze by ward, hallway space, and walls
    ############################################################
    def draw_maze(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.maze[x][y] == 1: # Walls
                    color= 'black'
                if self.maze[x][y] == 0: # Open hallways
                    color= 'white'

                ########################
                # Ward Color Key
                ########################
                if self.maze[x][y] == 2: # Maternity
                    color= 'lightblue'
                if self.maze[x][y] == 3: # Admissions
                    color= 'lightgray'
                if self.maze[x][y] == 4: # General Ward
                    color= 'red'
                if self.maze[x][y] == 5: # Emergency
                    color= 'yellow'
                if self.maze[x][y] == 6: # Surgical Ward
                    color= 'pink'
                if self.maze[x][y] == 7: # Oncology
                    color= 'green'
                if self.maze[x][y] == 8: # ICU
                    color= 'orange'
                if self.maze[x][y] == 9: # Isolation Ward
                    color= 'violet'
                if self.maze[x][y] == 10: # Pediatric Ward
                    color= 'lightgreen'
                if self.maze[x][y] == 11: # Burn Ward
                    color= 'purple'
                if self.maze[x][y] == 12: # Hematology
                    color= 'darkorange'
                if self.maze[x][y] == 13: # Medical Ward
                    color= 'chartreuse'

                self.canvas.create_rectangle(y * self.cell_size, x * self.cell_size, (y + 1) * self.cell_size, (x + 1) * self.cell_size, fill=color)



    ############################################################
    #### Manhattan distance
    ############################################################
    def heuristic(self, pos):
        return (abs(pos[0] - self.goal_pos[0]) + abs(pos[1] - self.goal_pos[1]))



    ############################################################
    #### A* Algorithm
    ############################################################
    def find_path(self):
        open_set = PriorityQueue()

        #### Add the start state to the queue
        open_set.put((0, self.agent_pos))

        #### Continue exploring until the queue is exhausted
        while not open_set.empty():

            current_cost, current_pos = open_set.get_nowait()
            current_cell = self.cells[current_pos[0]][current_pos[1]]

            #### Stop if goal is reached
            if current_pos == self.goal_pos:
                print(self.goal_pos)
                self.reconstruct_path()
                print('Ward Found!')
                break


            #### Agent goes E, W, N, and S, whenever possible
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current_pos[0] + dx, current_pos[1] + dy)

                if 0 <= new_pos[0] < self.rows and 0 <= new_pos[1] < self.cols and not self.cells[new_pos[0]][new_pos[1]].is_wall:

                    #### The cost of moving to a new position is 1 unit
                    new_g = current_cell.g + 1


                    if new_g < self.cells[new_pos[0]][new_pos[1]].g:
                        ### Update the path cost g()
                        self.cells[new_pos[0]][new_pos[1]].g = new_g

                        ### Update the heurstic h()
                        self.cells[new_pos[0]][new_pos[1]].h = self.heuristic(new_pos)

                        ### Update the evaluation function for the cell n: f(n) = g(n) + h(n)
                        self.cells[new_pos[0]][new_pos[1]].f = (2 * new_g) + (3 * self.cells[new_pos[0]][new_pos[1]].h)
                        self.cells[new_pos[0]][new_pos[1]].parent = current_cell

                        #### Add the new cell to the priority queue
                        open_set.put((self.cells[new_pos[0]][new_pos[1]].f, new_pos))

        if open_set.empty() and current_pos != self.goal_pos:
            print("Failure, no path found to ward")

    ############################################################
    #### Djikstra's Algorithm
    ############################################################
    def find_path_D(self):
        open_set = PriorityQueue()

        #### Add the start state to the queue
        open_set.put((0, self.agent_pos))

        #### Continue exploring until the queue is exhausted
        while not open_set.empty():
            current_cost, current_pos= open_set.get()
            current_cell = self.cells[current_pos[0]][current_pos[1]]

            #### Stop if goal is reached
            if current_pos == self.goal_pos:
                self.reconstruct_path()
                print('Ward Found!')
                break


            #### Agent goes E, W, N, and S, whenever possible
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current_pos[0] + dx, current_pos[1] + dy)

                if 0 <= new_pos[0] < self.rows and 0 <= new_pos[1] < self.cols and not self.cells[new_pos[0]][new_pos[1]].is_wall:

                    #### The cost of moving to a new position is 1 unit
                    new_g = current_cell.g + 1


                    if new_g < self.cells[new_pos[0]][new_pos[1]].g:
                        ### Update the path cost g()
                        self.cells[new_pos[0]][new_pos[1]].g = new_g

                        ### Update the evaluation function for the cell where f(n) is equal to updated g(n)
                        ### This is equivalent to an algorithm that finds the path based solely on path cost
                        self.cells[new_pos[0]][new_pos[1]].f = new_g
                        self.cells[new_pos[0]][new_pos[1]].parent = current_cell

                        #### Add the new cell to the priority queue
                        open_set.put((new_g, new_pos))

        if open_set.empty() and current_pos != self.goal_pos:
            print("Failure, no path found to ward")

    ############################################################
    #### GUI for visual: Goal is gold, start is grey, path is blue
    ############################################################
    def reconstruct_path(self):
        print("Reconstructing Path...")
        current_cell = self.cells[self.goal_pos[0]][self.goal_pos[1]]
        x, y = current_cell.x, current_cell.y
        self.canvas.create_rectangle(y * self.cell_size, x * self.cell_size, (y + 1) * self.cell_size, (x + 1) * self.cell_size, fill='gold')

        current_cell=current_cell.parent
        while current_cell.parent:
            x, y = current_cell.x, current_cell.y
            self.canvas.create_rectangle(y * self.cell_size, x * self.cell_size, (y + 1) * self.cell_size, (x + 1) * self.cell_size, fill='blue')
            temp=current_cell
            current_cell = current_cell.parent
            temp.parent=None
            ## Delay method to show drawing of maze
            self.root.update()
            time.sleep(0.1)

        x, y = current_cell.x, current_cell.y
        self.canvas.create_rectangle(y * self.cell_size, x * self.cell_size, (y + 1) * self.cell_size, (x + 1) * self.cell_size, fill='brown')


    ############################################################
    #### Moveable positions of agent go right, left, up, down
    ############################################################
    def move_agent(self, event):

        #### Move right, if possible
        if event.keysym == 'Right' and self.agent_pos[1] + 1 < self.cols and not self.cells[self.agent_pos[0]][self.agent_pos[1] + 1].is_wall:
            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] + 1)


        #### Move Left, if possible
        elif event.keysym == 'Left' and self.agent_pos[1] - 1 >= 0 and not self.cells[self.agent_pos[0]][self.agent_pos[1] - 1].is_wall:
            self.agent_pos = (self.agent_pos[0], self.agent_pos[1] - 1)

        #### Move Down, if possible
        elif event.keysym == 'Down' and self.agent_pos[0] + 1 < self.rows and not self.cells[self.agent_pos[0] + 1][self.agent_pos[1]].is_wall:
            self.agent_pos = (self.agent_pos[0] + 1, self.agent_pos[1])

        #### Move Up, if possible
        elif event.keysym == 'Up' and self.agent_pos[0] - 1 >= 0 and not self.cells[self.agent_pos[0] - 1][self.agent_pos[1]].is_wall:
            self.agent_pos = (self.agent_pos[0] - 1, self.agent_pos[1])

        #### Erase agent from the previous cell at time t
        self.canvas.delete("agent")


        ### Redraw the agent in color navy in the new cell position at time t+1
        self.canvas.create_rectangle(self.agent_pos[1] * self.cell_size, self.agent_pos[0] * self.cell_size,
                                    (self.agent_pos[1] + 1) * self.cell_size, (self.agent_pos[0] + 1) * self.cell_size,
                                    fill='navy', tags="agent")



############################################################
#### Maze structure:
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
[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 12, 0, 12, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 8, 8, 8, 8, 1, 1],
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

############################################################
#### The mainloop activates the GUI:
############################################################
root = tk.Tk()
root.title("Robot Nurse")

game = MazeGame(root, maze)
root.bind("<KeyPress>", game.move_agent)

root.mainloop()

