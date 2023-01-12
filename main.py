import random
import pygame
import sys

fps = pygame.time.Clock()

def createBoard():
    global board
    board = []
    for row in range(height_cells):
        new_row = []
        for column in range(width_cells):
            new_row.append([])
        board.append(new_row)

def printBoard():
    for y in range(len(board)):
        print()
        print("|", end="")
        for x in range(len(board[y])):
            if len(board[y][x]) > 1:
                print("#", end="")
            else:
                print(" ",end="")
        print("|", end="")
    print()
    print(" ", end="")
    for x in range(len(board[0])):
        print("-", end="")

def gameState():
    if isEmptyState():
        return "emptyState"

def isEmptyState():
    for row in board:
        for element in row:
            if element != "":
                return False
    return True

def generatePiece1():
    """
    ####
    """
    board[0][3] = [True,1,0,[(2,2),(1,-2),(-2,-1),(-1,1)], (0,240,240)]
    board[0][4] = [True,1,0,[(1,1),(0,-1),(-1,0),(0,0)], (0,240,240)]
    board[0][5] = [True,1,0,[(0,0),(-1,0),(0,1),(1,-1)], (0,240,240)]
    board[0][6] = [True,1,0,[(-1,-1),(-2,1),(1,2),(2,-2)], (0,240,240)]

def generatePiece2():
    """
    #
    ###
    """
    board[0][3] = [True,2,0,[(2,1),(0,-2),(-2,0),(0,1)], (0,0,240)]
    board[1][3] = [True,2,0,[(1,2),(0,-1),(0,0),(-1,-1)], (0,0,240)]
    board[1][4] = [True,2,0,[(0,1),(1,0),(-1,-1),(0,0)], (0,0,240)]
    board[1][5] = [True,2,0,[(-1,0),(-1,1),(1,1),(1,-2)], (0,0,240)]

def generatePiece3():
    """
      #
    ###
    """
    board[0][5] = [True,3,0,[(0,-1),(-2,0),(0,2),(2,-1)], (240,160,0)]
    board[1][5] = [True,3,0,[(-1,0),(-1,1),(1,1),(1,-2)], (240,160,0)]
    board[1][4] = [True,3,0,[(0,1),(0,0),(0,0),(0,-1)], (240,160,0)]
    board[1][3] = [True,3,0,[(1,2),(1,-1),(-1,-1),(-1,0)], (240,160,0)]

def generatePiece4():
    """
    ##
    ##
    """
    board[0][4] = [True,4,0,[(0,0),(0,0),(0,0),(0,0)], (240,240,0)]
    board[0][5] = [True,4,0,[(0,0),(0,0),(0,0),(0,0)], (240,240,0)]
    board[1][4] = [True,4,0,[(0,0),(0,0),(0,0),(0,0)], (240,240,0)]
    board[1][5] = [True,4,0,[(0,0),(0,0),(0,0),(0,0)], (240,240,0)]

def generatePiece5():
    """
     ##
    ##
    """
    board[0][5] = [True,5,0,[(0,0),(0,-1),(-1,1),(1,0)], (0,240,0)]
    board[0][6] = [True,5,0,[(-1,-1),(-1,0),(0,2),(2,-1)], (0,240,0)]
    board[1][4] = [True,5,0,[(0,2),(2,-1),(-1,-1),(-1,0)], (0,240,0)]
    board[1][5] = [True,5,0,[(-1,1),(1,0),(0,0),(0,-1)], (0,240,0)]

def generatePiece6():
    """
     #
    ###
    """
    board[0][4] = [True,6,0,[(1,-1),(-1,-1),(-1,1),(1,1)], (160,0,240)]
    board[1][3] = [True,6,0,[(1,1),(1,-1),(-1,-1),(-1,1)], (160,0,240)]
    board[1][4] = [True,6,0,[(0,0),(0,0),(0,0),(0,0)], (160,0,240)]
    board[1][5] = [True,6,0,[(-1,-1),(-1,1),(1,1),(1,-1)], (160,0,240)]

def generatePiece7():
    """
    ##
     ##
    """
    board[0][3] = [True,7,0,[(1,0),(1,-1),(-1,-1),(-1,2)], (240,0,0)]
    board[0][4] = [True,7,0,[(0,-1),(0,0),(0,0),(0,1)], (240,0,0)]
    board[1][4] = [True,7,0,[(-1,0,),(1,1),(1,-1,),(-1,0)], (240,0,0)]
    board[1][5] = [True,7,0,[(-2,-1),(0,2),(2,0),(0,-1)], (240,0,0)]

def getMovingPositions():
    """
    moving_positions = [(x,y), [true, pieceType, rotateState, rotateMovements]
    """
    global moving_positions
    moving_positions = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if len(board[y][x]) > 1:
                if board[y][x][0] == True:
                    moving_positions.append([(x,y),board[y][x]])

def moveDownMovingPositions():
    for object in moving_positions:
        x = object[0][0]
        y = object[0][1]

        object[0] = (x,y+1)

def canMoveDown():
    for object in moving_positions:
        y = object[0][1]
        x = object[0][0]
        if y+1 == height_cells:
            return False
        elif len(board[y+1][x]) > 1:
            if board[y+1][x][0] == False:
                return False
    return True

def MoveDown():
    global state


def canMoveLeft():
    for object in moving_positions:
        y = object[0][1]
        x = object[0][0]
        if x == 0:
            return False
        elif len(board[y][x-1]) > 1:
            if board[y][x-1][0] == False:
                return False
    return True

def moveLeftMovingPositions():
    for object in moving_positions:
        x = object[0][0]
        y = object[0][1]

        object[0] = (x-1,y)

def canMoveRight():
    for object in moving_positions:
        y = object[0][1]
        x = object[0][0]
        if x == width_cells-1:
            return False
        elif len(board[y][x+1]) > 1:
            if board[y][x+1][0] == False:
                return False
    return True

def moveRightMovingPositions():
    for object in moving_positions:
        x = object[0][0]
        y = object[0][1]

        object[0] = (x+1,y)


def canRotate():
    # moving_positions = [(x,y), [true, pieceType, rotateState, rotateMovements]
    for object in moving_positions:
        rotation_state = object[1][2]
        rotation_movement_x = object[1][3][rotation_state][0]
        rotation_movement_y = object[1][3][rotation_state][1]
        y = object[0][1] - rotation_movement_y
        x = object[0][0] + rotation_movement_x
        if (y >= 0 and y + 1 <= height_cells) and (x >= 0 and x + 1 <= width_cells):
            if len(board[y][x]) > 1:
                if board[y][x][0] == False:
                    return False
        else:
            return False
    return True

def rotateMovingPositions():
    # moving_positions = [(x,y), [true, pieceType, rotateState, rotateMovements]
    for object in moving_positions:
        rotation_state = object[1][2]
        rotation_movement_x = object[1][3][rotation_state][0]
        rotation_movement_y = object[1][3][rotation_state][1]
        if object[1][2] == 3:
            object[1][2] = 0
        else:
            object[1][2] = object[1][2] + 1
        y = object[0][1] - rotation_movement_y
        x = object[0][0] + rotation_movement_x
        object[0] = (x,y)

def getSectionToDown(line_deleted):
    # moving_positions = [(x,y), [true, pieceType, rotateState, rotateMovements]
    section_to_down = []
    for y in range(len(board)):
        if y == line_deleted:
            break
        for x in range(len(board[y])):
            section_to_down.append([(x,y), board[y][x]])
    return section_to_down

def moveSectionToDownDown(section_to_down):
    for object in section_to_down:
        x = object[0][0]
        y = object[0][1]
        if y + 2 <= height_cells:
            object[0] = (x,y+1)
    return section_to_down

def moveSectionToDown(line_deleted):
    section_to_down = getSectionToDown(line_deleted)
    print(section_to_down)
    for object in section_to_down:
        x = object[0][0]
        y = object[0][1]
        board[y][x] = []

    section_to_down = moveSectionToDownDown(section_to_down)
    print()
    print(section_to_down)

    for object in section_to_down:
        x = object[0][0]
        y = object[0][1]
        board[y][x] = object[1]
        #board[y][x] = []

def removeCompleteLines():
    removed = False
    line_to_remove = None

    for y in range(len(board)):
        full_line = True
        for x in range(len(board[y])):
            if len(board[y][x]) < 1:
                full_line = False
        if full_line:
            line_to_remove = y
            removed = True
            break

    if removed:
        for x in range(len(board[line_to_remove])):
            board[line_to_remove][x] = []
        moveSectionToDown(line_to_remove)
        return True
    return False



def getDirection():
    return "None"
    global direction
    if str(lastInput) == "a":
        direction = "left"
    elif str(lastInput) == "d":
        direction = "right"
    elif str(lastInput) == " ":
        direction = "rotate"
    else:
        direction = "None"


def paintVoidBoard():
    num_vert_lines = height_cells - 1
    num_hor_lines = (height_cells - 3) - 1

    for i in range(num_hor_lines):
        y = (i+1) * cell_height
        pygame.draw.line(window, (255, 255, 255), (0, y), (screen_width, y))

    for i in range(num_vert_lines):
        x = (i+1) * cell_width
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, screen_height))


def paintFigures():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if len(board[y][x]) > 1:
                pygame.draw.rect(window, board[y][x][4], pygame.Rect(cell_width * (x), cell_height * (y-3), cell_width, cell_height))
    #removeShadows()

def increaseDiff():
    global cooldown
    if cooldown > 2:
        cooldown = cooldown - 1
"""
def getShadowPos():
    # moving_positions = [(x,y), [true, pieceType, rotateState, rotateMovements]
    founded = False
    posibleDownMovements = []
    worst_moves_down = 0
    last_index = len(moving_positions) - 1
    while not founded:
        for object in enumerate(moving_positions):
            object_best = False
            better_obj_pos = 0
            x = object[0][0]
            y = object[0][1]
            while not object_best:
                if board[y][x]:


def getPosibleDownMovements(object):
    movements = 0
    x = object[0][0]
    y = object[0][1]
    founded  = False
    while not founded:
        if y + 1 >= len(board-1) and board[]:
            y_to_check = y + 1
        else:
            movements = 0
    return movements


def addShadow(object):
    #object = [(x,y), [true, pieceType, rotateState, rotateMovements]
    x = object[0][0]
    y = object[0][1]
    if object[1][0] == True:


def removeShadows():
    print()
"""

if __name__ == "__main__":
    height_cells = 23
    width_cells = 10
    board = None
    state = "generate"
    direction = "None"
    rotate = False
    lastInput = "None"
    moving_positions = []
    pygame.init()
    screen_width = 300
    screen_height = 600
    cooldown = 15
    dir_cooldown= 3
    actual_cooldown = cooldown
    dir_actual_cooldown = dir_cooldown

    cell_width = screen_width / width_cells
    cell_height = screen_height / (height_cells-3)

    window = pygame.display.set_mode((screen_width, screen_height))
    screen_rect = window.get_rect()
    createBoard()



    while True:
        dir_actual_cooldown = dir_actual_cooldown - 1
        if direction == "down":
            actual_cooldown = -1
        if dir_actual_cooldown < 0:
            dir_actual_cooldown = dir_cooldown
            if state == "generate":
                number = random.randint(1,7)
                #number = 1
                #number = 4
                if number == 1:
                    generatePiece1()
                elif number == 2:
                    generatePiece2()
                elif number == 3:
                    generatePiece3()
                elif number == 4:
                    generatePiece4()
                elif number == 5:
                    generatePiece5()
                elif number == 6:
                    generatePiece6()
                elif number == 7:
                    generatePiece7()

                getMovingPositions()
                state = "moving"

            elif state == "moving":
                if direction == "left":
                    if canMoveLeft():
                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = []

                        moveLeftMovingPositions()

                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = object[1]
                elif direction == "right":
                    if canMoveRight():
                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = []

                        moveRightMovingPositions()

                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = object[1]
                if rotate:
                    rotate = False
                    if canRotate():
                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = []
                        rotateMovingPositions()
                        for object in moving_positions:
                            y = object[0][1]
                            x = object[0][0]
                            board[y][x] = object[1]

        actual_cooldown = actual_cooldown - 1
        if actual_cooldown < 0:
            actual_cooldown = cooldown
            if canMoveDown():
                for object in moving_positions:
                    y = object[0][1]
                    x = object[0][0]
                    board[y][x] = []

                moveDownMovingPositions()

                for object in moving_positions:
                    y = object[0][1]
                    x = object[0][0]
                    board[y][x] = object[1]
            else:
                for object in moving_positions:
                    y = object[0][1]
                    x = object[0][0]
                    board[y][x][0] = False
                direction = "None"
                state = "generate"
                removed_completed_lines = removeCompleteLines()
                while removed_completed_lines:
                    removed_completed_lines = removeCompleteLines()
                    increaseDiff()

        #lastInput = str(input("\n"))
        #getDirection()
        #printBoard()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Keys controllers
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_a:
                    direction = "left"
                elif event.key == pygame.K_d:
                    direction = "right"
                elif event.key == pygame.K_s:
                    direction = "down"
                elif event.key == pygame.K_SPACE:
                    rotate = True


            keys_pressed = pygame.key.get_pressed()
            if not(keys_pressed[pygame.K_a] or keys_pressed[pygame.K_d] or keys_pressed[pygame.K_s] ):
                direction = "None"



        window.fill((0, 0, 0))
        paintFigures()
        paintVoidBoard()
        pygame.display.flip()
        fps.tick(60)


