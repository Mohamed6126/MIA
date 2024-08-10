import pygame as py
py.init()
width=900
height=800
screen= py.display.set_mode([width,height])
timer=py.time.Clock()
fps=60
font = py.font.SysFont('Arial', 60)
heroes=['bat','flash','lantern','super','wonder','lantern', 'flash','bat','cyborg','cyborg','cyborg','cyborg','cyborg','cyborg','cyborg','cyborg']
heroes_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
villains=['z','joker','quin','lex','dark','quin', 'joker','z','wing','wing','wing','wing','wing','wing','wing','wing']
villans_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_hero=[]
captured_villain=[]
valid_moves=[]
# 0=heroes turn no selection   1=heroes turn with selection   2=villans turn no selection   3=villans turn with selection
turn_step=0
selection= 100
# pieces images
# 1-heroes

super= py.transform.scale( py.image.load('R.png'),(80,80))
wonder= py.transform.scale( py.image.load('R (1).png'),(80,80))
flash= py.transform.scale(py.image.load('R (2).png'),(80,80))
lantern= py.transform.scale( py.image.load('Green-Lantern-PNG-Images-HD.png'),(80,80))
bat= py.transform.scale( py.image.load('winkidz-batman-jascon-food-4.png'),(80,80))
cyborg= py.transform.scale( py.image.load('Cyborg-PNG-Image.png'),(80,80))
heroes_imgs = [super, wonder,flash,lantern,bat,cyborg]
piece_list=['super', 'wonder','flash','lantern','bat','cyborg']
# 2-Villains
lex= py.transform.scale( py.image.load('R (3).png'),(80,80))
dark= py.transform.scale( py.image.load('R (4).png'),(80,80))
quin= py.transform.scale( py.image.load('R (5).png'),(80,80))
joker= py.transform.scale( py.image.load('joker-png-images-free-download-free-png-archive-14148.png'),(80,80))
z= py.transform.scale(py.image.load('TheDeathstroke.webp'),(80,80))
wing= py.transform.scale( py.image.load('R (6).png'),(80,80))
villains_imgs=[lex, dark,quin,joker,z,wing]
piece2_list=['lex', 'dark','quin','joker','z','wing']
counter = 0
winner = ''
game_over = False
#gameboard
def drawboard():
    for i in range(32):
        column=i%4
        row=i//4
        if row %2==0:
            py.draw.rect(screen,'light gray',[600-(column*195), row*90 , 90 , 90])
        else :
            py.draw.rect(screen,'light gray',[700-(column*195), row*90 , 90 , 90])
        py.draw.rect(screen, 'gray', [0,720,width,100])
        py.draw.rect(screen, 'gold', [0,720,width,100],5)
        py.draw.rect(screen, 'gold', [790,0,200,height],5)

        status_text =['Heroes: Select a piece to move!','heroes: Select a destination','villans: Select a piece to move!','villans: Select a destination']
        status_surface = font.render(status_text[turn_step], True, 'black')
        screen.blit(status_surface, (10, 730))
        screen.blit(font.render('FORFEIT', True, 'black'), (810, 830))

#gamepieces
def drawpieces():
 for i in range(len(heroes)):
        index = piece_list.index(heroes[i])
        if heroes[i] == 'cyborg':
            screen.blit(cyborg, (heroes_locations[i][0] * 100 +15, heroes_locations[i][1] * 100 ))
        else:
            screen.blit(heroes_imgs[index], (heroes_locations[i][0] * 100 +10, heroes_locations[i][1] * 100 + 10))
        if turn_step < 2:
            if selection == i:
                py.draw.rect(screen, 'red', [heroes_locations[i][0] * 100 + 1, heroes_locations[i][1] * 100 + 1, 100, 100], 2)

 for i in range(len(villains)):
        index = piece2_list.index(villains[i])
        if villains[i] == 'wing':
            screen.blit(wing, (villans_locations[i][0] * 100 +15, villans_locations[i][1] * 90 ))
        else:
            screen.blit(villains_imgs[index], (villans_locations[i][0] * 100 +10, villans_locations[i][1] * 90 + 0))
        if turn_step < 2:
            if selection == i:
                py.draw.rect(screen, 'red', [villans_locations[i][0] * 50 + 1, villans_locations[i][1] * 50 + 1, 100, 100], 2) 

def check_options(pieces, locations, turn):
    moves_list = []
    all_moves_list = []
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'pawn':
            moves_list = check_pawn(location, turn)
        elif piece == 'rook':
            moves_list = check_rook(location, turn)
        elif piece == 'knight':
            moves_list = check_knight(location, turn)
        elif piece == 'bishop':
            moves_list = check_bishop(location, turn)
        elif piece == 'queen':
            moves_list = check_queen(location, turn)
        elif piece == 'king':
            moves_list = check_king(location, turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_king(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = villans_locations
        friends_list = heroes_locations
    else:
        friends_list = villans_locations
        enemies_list = heroes_locations
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_queen(position, color):
    moves_list = check_bishop(position, color)
    second_list = check_rook(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list

def check_bishop(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = villans_locations
        friends_list = heroes_locations
    else:
        friends_list = villans_locations
        enemies_list = heroes_locations
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_rook(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = villans_locations
        friends_list = heroes_locations
    else:
        friends_list = villans_locations
        enemies_list = heroes_locations
    for i in range(4):  # down, up, right, left
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in friends_list and \
                    0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemies_list:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list

def check_pawn(position, color):
    moves_list = []
    if color == 'white':
        if (position[0], position[1] + 1) not in heroes_locations and \
                (position[0], position[1] + 1) not in villans_locations and position[1] < 7:
            moves_list.append((position[0], position[1] + 1))
        if (position[0], position[1] + 2) not in heroes_locations and \
                (position[0], position[1] + 2) not in villans_locations and position[1] == 1:
            moves_list.append((position[0], position[1] + 2))
        if (position[0] + 1, position[1] + 1) in villans_locations:
            moves_list.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in villans_locations:
            moves_list.append((position[0] - 1, position[1] + 1))
    else:
        if (position[0], position[1] - 1) not in heroes_locations and \
                (position[0], position[1] - 1) not in villans_locations and position[1] > 0:
            moves_list.append((position[0], position[1] - 1))
        if (position[0], position[1] - 2) not in heroes_locations and \
                (position[0], position[1] - 2) not in villans_locations and position[1] == 6:
            moves_list.append((position[0], position[1] - 2))
        if (position[0] + 1, position[1] - 1) in heroes_locations:
            moves_list.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in heroes_locations:
            moves_list.append((position[0] - 1, position[1] - 1))
    return moves_list

def check_knight(position, color):
    moves_list = []
    if color == 'white':
        enemies_list = villans_locations
        friends_list = heroes_locations
    else:
        friends_list = villans_locations
        enemies_list = heroes_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list

def check_valid_moves():
    if turn_step < 2:
        options_list = heroes_options
    else:
        options_list = villains_options
    valid_options = options_list[selection]
    return valid_options

def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        py.draw.circle(screen, color, (moves[i][0] * 90 + 50, moves[i][1] * 90 + 50), 5)
def draw_captured():
    for i in range(len(captured_hero)):
        captured_piece = captured_hero[i]
        index = piece_list.index(captured_piece)
        screen.blit(villains_imgs[index], (825, 5 + 50 * i))
    for i in range(len(captured_villain)):
        captured_piece = captured_villain[i]
        index = piece_list.index(captured_piece)
        screen.blit(heroes_imgs[index], (925, 5 + 50 * i))

def draw_captured():
    for i in range(len(captured_hero)):
        captured_piece = captured_hero[i]
        index = piece_list.index(captured_piece)
        screen.blit(villains_imgs[index], (825, 5 + 50 * i))
    for i in range(len(captured_villain)):
        captured_piece = captured_villain[i]
        index = piece_list.index(captured_piece)
        screen.blit(heroes_imgs[index], (925, 5 + 50 * i))
        
def draw_check():
    if turn_step < 2:
        if 'king' in heroes:
            king_index = heroes.index('king')
            king_location = heroes_locations[king_index]
            for i in range(len(villains_options)):
                if king_location in villains_options[i]:
                    if counter < 15:
                        py.draw.rect(screen, 'dark red', [heroes_locations[king_index][0] * 100 + 1,
                                                              heroes_locations[king_index][1] * 100 + 1, 100, 100], 5)
    else:
        if 'king' in villains:
            king_index = villains.index('king')
            king_location = villans_locations[king_index]
            for i in range(len(heroes_options)):
                if king_location in heroes_options[i]:
                    if counter < 15:
                        py.draw.rect(screen, 'dark blue', [villans_locations[king_index][0] * 100 + 1,
                                                               villans_locations[king_index][1] * 100 + 1, 100, 100], 5)
def draw_game_over():
    py.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} won the game!', True, 'white'), (210, 210))
    screen.blit(font.render(f'Press ENTER to Restart!', True, 'white'), (210, 240))

villains_options = check_options(villains, villans_locations, 'black')
heroes_options = check_options(heroes, heroes_locations, 'white')
run = True
while run:
    timer.tick(fps)
    if counter < 30:
        counter += 1
    else:
        counter = 0
    screen.fill('dark gray')
    drawboard()
    drawpieces()
    draw_captured()
    draw_check()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
    # event handling
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1 and not game_over:
            x_coord = event.pos[0] // 100
            y_coord = event.pos[1] // 100
            click_coords = (x_coord, y_coord)
            if turn_step <= 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'black'
                if click_coords in heroes_locations:
                    selection = heroes_locations.index(click_coords)
                    if turn_step == 0:
                        turn_step = 1
                if click_coords in valid_moves and selection != 100:
                    heroes_locations[selection] = click_coords
                    if click_coords in villans_locations:
                        villain = villans_locations.index(click_coords)
                        captured_hero.append(villains[villain])
                        if villains[villain] == 'king':
                            winner = 'white'
                        villains.pop(villain)
                        villans_locations.pop(villain)
                    villains_options = check_options(villains, villans_locations, 'black')
                    heroes_options = check_options(heroes, heroes_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click_coords == (8, 8) or click_coords == (9, 8):
                    winner = 'white'
                if click_coords in villans_locations:
                    selection = villans_locations.index(click_coords)
                    if turn_step == 2:
                        turn_step = 3
                if click_coords in valid_moves and selection != 100:
                    villans_locations[selection] = click_coords
                    if click_coords in heroes_locations:
                        hero = heroes_locations.index(click_coords)
                        captured_villain.append(heroes[hero])
                        if heroes[hero] == 'king':
                            winner = 'black'
                        heroes.pop(hero)
                        heroes_locations.pop(hero)
                    villains_options = check_options(villains, villans_locations, 'black')
                    heroes_options = check_options(heroes, heroes_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
        if event.type == py.KEYDOWN and game_over:
            if event.key == py.K_RETURN:
                game_over = False
                winner = ''
                heroes = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                heroes_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
                villains = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
                villains_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                captured_hero = []
                captured_villain = []
                turn_step = 0
                selection = 100
                valid_moves = []
                villans_options = check_options(villains, villans_locations, 'black')
                heroes_options = check_options(heroes, heroes_locations, 'white')

    if winner != '':
        game_over = True
        draw_game_over()

    py.display.flip()
py.quit()

