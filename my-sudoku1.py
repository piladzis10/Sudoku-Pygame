import pygame, time, copy
pygame.font.init()

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
board_solved = copy.deepcopy(board)

def valid(sudoku,number, position):
    #validation for column
    for i in range(len(sudoku)):
        if sudoku[i][position[1]] == number and position[0] != i:
            return False
        
    #validation for rows
    for i in range(len(sudoku[0])):
        if sudoku[position[0]][i] == number and position[1] != i:
            return False
    
    #validation for box
    box_position_x = position[0] // 3 * 3
    box_position_y = position[1] // 3 * 3

    for i in range(box_position_x, box_position_x + 3):
        for j in range(box_position_y, box_position_y+3):
            if sudoku[i][j] == number and (i != position[0] and j != position[1]):
                return False

    return True

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j)
    return None

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(sudoku, i, (row, col)):
            sudoku[row][col] = i

            if solve(sudoku):
                return True
            
            sudoku[row][col] = 0
    return False
   

solve(board_solved)

    




# Initialize the screen
WIDTH, HEIGHT = 500,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

class Grid:
    def __init__(self,block_count):
        self.block_count = block_count

        
    def draw_empty_grid(self,window):
        # Draw vertical lines
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(window,(0,0,0),(25 + 50*i,125),(25 + 50*i,575),4)
            else:
                pygame.draw.line(window,(0,0,0),(25 + 50*i,125),(25 + 50*i,575),1)
        
        # Draw horizontal lines
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(window,(0,0,0),(25,125 + 50*i),(475,125 + 50*i),4)
            else:
                pygame.draw.line(window,(0,0,0),(25,125 + 50*i),(475,125 + 50*i),1)
 

class Box:
    def draw(self,win):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != 0:
                    main_font = pygame.font.SysFont("comicsans", 40)
                    text = main_font.render(str(board[i][j]), True, (0,0,0))
                    pos_x = round((50 - text.get_width()) /2) + 25 + j*50
                    pos_y = round((50 - text.get_height()) /2) + 125 + i*50
                    win.blit(text, (pos_x,pos_y))

            


def format_time(secs):
    sec = secs%60
    minute = secs//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def draw_mistakes(win, mistake_count):

    for i in range(mistake_count):
        pygame.draw.line(win,(255,0,0), (30 + 30*i,50),(50+ 30*i,70))
        pygame.draw.line(win,(255,0,0), (50+ 30*i,50),(30+ 30*i,70))




    


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    grid = Grid(3)
    box = Box()
    click = False
    key = None
    board_row = 0
    board_col = 0
    mistake_count = 0
    start = time.time()


    def redraw_screen(time):
        WIN.fill((255,255,255))

        fnt = pygame.font.SysFont("comicsans",40)
        text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
        WIN.blit(text, (10, 10))

        grid.draw_empty_grid(WIN)

        box.draw(WIN)

        draw_mistakes(WIN,mistake_count)



        if click:
            pygame.draw.rect(WIN,(255,0,0),(pos_box_x,pos_box_y,50,50),4)

        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_screen(round(time.time()- start))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_1:
                    key = 1


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_box_x = (pos[0] - 25) // 50 * 50 + 25
                pos_box_y = (pos[1] - 125) // 50 * 50 + 125
                board_row = (pos[0] - 25) // 50
                board_col = (pos[1] - 125) // 50
                click = True
        if key != None:
            if board_solved[board_col][board_row] == key:
                board[board_col][board_row] = key
            else:
                mistake_count += 1
            key = None
main()
