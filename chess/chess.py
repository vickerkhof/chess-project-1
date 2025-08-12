import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

SIZE = 100
TEXT = ""
FONT = pygame.font.SysFont(None, SIZE)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
transparant_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

SQUARE_SIZE = 90
X_CO = (SCREEN_WIDTH-8*SQUARE_SIZE)/2
Y_CO = (SCREEN_HEIGHT-8*SQUARE_SIZE)/2

"""promoting pieces shows the positions, color, piece-type and associated img for all pieces that will be displayed as options when a pawn promotes"""

promoting_pieces = {
    "white_queen": ["white-queen.png", "", (0,0), ["white", "queen"]],
    "black_queen": ["black-queen.png", "", (0,0), ["black", "queen"]],
    "white_rook": ["white-rook.png", "", (0,0), ["white", "rook"]],
    "black_rook": ["black-rook.png", "", (0,0), ["black", "rook"]],
    "white_bishop": ["white-bishop.png", "", (0,0), ["white", "bishop"]],
    "black_bishop": ["black-bishop.png", "", (0,0), ["black", "bishop"]],
    "white_knight": ["white-knight.png", "", (0,0), ["white", "knight"]],
    "black_knight": ["black-knight.png", "", (0,0), ["black", "knight"]]
}

"""pieces shows the positions, color, piece-type and associated img for all the pieces"""

pieces = {
    "1": ["black-rook.png", "", (0,0), ["black", "rook"]], "2": ["black-knight.png", "", (0,0), ["black", "knight"]],
    "3": ["black-bishop.png", "", (0,0), ["black", "bishop"]], "4": ["black-queen.png", "", (0,0), ["black", "queen"]],
    "5": ["black-king.png", "", (0,0), ["black", "king"]], "6": ["black-bishop.png", "", (0,0), ["black", "bishop"]],
    "7": ["black-knight.png", "", (0,0), ["black", "knight"]], "8": ["black-rook.png", "", (0,0), ["black", "rook"]],
    "9": ["black-pawn.png", "", (0,0), ["black", "pawn"]], "10": ["black-pawn.png", "", (0,0), ["black", "pawn"]],
    "11": ["black-pawn.png", "", (0,0), ["black", "pawn"]], "12": ["black-pawn.png", "", (0,0), ["black", "pawn"]],
    "13": ["black-pawn.png", "", (0,0), ["black", "pawn"]], "14": ["black-pawn.png", "", (0,0), ["black", "pawn"]],
    "15": ["black-pawn.png", "", (0,0), ["black", "pawn"]], "16": ["black-pawn.png", "", (0,0), ["black", "pawn"]], 
    "49": ["white-pawn.png", "", (0,0), ["white", "pawn"]], "50": ["white-pawn.png", "", (0,0), ["white", "pawn"]],
    "51": ["white-pawn.png", "", (0,0), ["white", "pawn"]], "52": ["white-pawn.png", "", (0,0), ["white", "pawn"]],
    "53": ["white-pawn.png", "", (0,0), ["white", "pawn"]], "54": ["white-pawn.png", "", (0,0), ["white", "pawn"]],
    "55": ["white-pawn.png", "", (0,0), ["white", "pawn"]], "56": ["white-pawn.png", "", (0,0), ["white", "pawn"]], 
    "57": ["white-rook.png", "", (0,0), ["white", "rook"]], "58": ["white-knight.png", "", (0,0), ["white", "knight"]],
    "59": ["white-bishop.png", "", (0,0), ["white", "bishop"]], "60": ["white-queen.png", "", (0,0), ["white", "queen"]],
    "61": ["white-king.png", "", (0,0), ["white", "king"]], "62": ["white-bishop.png", "", (0,0), ["white", "bishop"]],
    "63": ["white-knight.png", "", (0,0), ["white", "knight"]], "64": ["white-rook.png", "", (0,0), ["white", "rook"]]
}


color = [(255, 254, 223), (140, 94, 0)]
pieces_rect = {}
promoting_pieces_rect = {}
squares = {}
coordinates = []
############### FUNCTIONS ###############

"""the write function is a simple function you call when you want to display text on the screen. it takes the message/text you want to display ,the font and the color of the text you want to display"""

def write(text, font, color):
    img = font.render(text, True, color)
    x, y = img.get_size()
    x = abs(x/2-SCREEN_WIDTH/2)
    y = abs(y/2-SCREEN_HEIGHT/2)
    canvas.blit(img, (x, y))

"""the get_*_moves get called when the program needs all the legal moves of a specific piecce. the function doesn't take consideration with a pins and check, that gets handles separatly.
it only takes the number/square the piece is on, except for the king and pawn moves who als take castling rights and en-passants in to consideration"""

def get_rook_moves(number):
    possible_moves = []
    number = int(number)
    E_COLOR = "white"
    O_COLOR = "black"

    if pieces[str(number)][3][0] == "white":
        E_COLOR = "black"
        O_COLOR = "white"

    checking = True
    checking_number = number
    if number%8 != 0:
        while checking:
            checking_number += 1
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 0 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking = True
    checking_number = number
    if number%8 != 1:
        while checking:
            checking_number -= 1
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 1 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking_number = number
    checking = True
    if checking_number+8 < 65:
        while checking:
            checking_number += 8
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number+8 > 64 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking_number = number
    checking = True
    if checking_number-8 > 0:
        while checking:
            checking_number -= 8
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number-8 < 1 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False

    return possible_moves

def get_bishop_moves(number):
    number = int(number)
    possible_moves = []
    E_COLOR = "white"
    O_COLOR = "black"

    if pieces[str(number)][3][0] == "white":
        E_COLOR = "black"
        O_COLOR = "white"

    checking = True
    checking_number = number
    if number%8 != 1 and number+7 < 65:
        while checking:
            checking_number += 7
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 1 or checking_number+7 > 64 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking = True
    checking_number = number
    if number%8 != 0 and number+9 < 65:
        while checking:
            checking_number += 9
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 0 or checking_number+9 > 64 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking = True
    checking_number = number
    if number%8 != 1 and number-9 > 0:
        while checking:
            checking_number -= 9
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 1 or checking_number-9 < 1 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False
    checking = True
    checking_number = number
    if number%8 != 0 and number-7 > 0:
        while checking:
            checking_number -= 7
            if pieces[str(checking_number)][3][0] != O_COLOR:
                possible_moves.append(checking_number)
            else:
                checking = False
            if checking_number%8 == 0 or checking_number-7 < 1 or pieces[str(checking_number)][3][0] == E_COLOR:
                checking = False

    return possible_moves


def get_queen_moves(number):
    straight_moves = get_rook_moves(number=number)
    diagonal_moves = get_bishop_moves(number=number)
    possible_moves = straight_moves + diagonal_moves

    return possible_moves


def get_king_moves(number, castle_short, castle_long):
    possible_moves = []
    number = int(number)
    E_COLOR = "white"
    O_COLOR = "black"
    C_SHORT = 2
    C_LONG = -2
    KING = 5

    if pieces[str(number)][3][0] == "white":
        E_COLOR = "black"
        O_COLOR = "white"
        KING = 61

    diversion_numbers = [1, 7, 8, 9, -1, -7, -8, -9]

    for num in diversion_numbers:
        if 0 < number+num < 65 and not (number%8 == 0 and (number+num)%8 == 1) and not (number%8 == 1 and (number+num)%8 == 0):
            if pieces[str(number+num)][3][0] != O_COLOR:
                possible_moves.append(number+num)
    
    if number == KING and  not is_check(E_COLOR, pieces, number, number, number, "king"):
        if castle_short:
            free_squares = []
            for n in range(2):
                if pieces[str(number+C_SHORT+n-1)][0] == "" and not is_check(E_COLOR, pieces, number, number+C_SHORT+n-1, number+C_SHORT+n-1, "king"):
                    free_squares.append(number+C_SHORT+n-1)
            if len(free_squares) == 2:
                possible_moves.append(number+C_SHORT)
        if castle_long:
            free_squares = []
            for n in range(3):
                if pieces[str(number+C_LONG-n+1)][0] == "" and not is_check(E_COLOR, pieces, number, number+C_SHORT+n-1, number+C_SHORT+n-1, "king"):
                    free_squares.append(number+C_LONG-n+1)
            if len(free_squares) == 3:
                possible_moves.append(number+C_LONG)
    
    return possible_moves


def get_knight_moves(number):
    number = int(number)
    possible_moves = []
    O_COLOR = pieces[str(number)][3][0]

    moves = [15, 17, 6, 10, -6, -10, -15, -17]
    
    if number%8 == 1:
        moves = [17, 10, -6, -15]
    elif number%8 == 2:
        moves = [17, 10, -6, -15, 15, -17]
    elif number%8 == 0:
        moves = [15, 6, -10, -17]
    elif number%8 == 7:
        moves = [15, 6, -10, -17, 17, -15]
    for num in moves:
        if 0 < number+num < 65:
            if pieces[str(number+num)][3][0] != O_COLOR:
                possible_moves.append(number+num)

    return possible_moves


def get_pawn_moves(number, en_passant):
    passed = 0
    number = int(number)
    possible_moves = [] 
    new_en_passant = []
    
    EN_RIGHT = -1
    EN_LEFT = 1
    LEFT = 9
    RIGHT = 7
    FORWARD_1 = 8
    FORWARD_2 = 16
    IS_LEFT = [8, 16, 24, 32, 40, 48, 56, 64]
    IS_RIGHT = [1, 9, 17, 25, 33, 41, 49, 57]
    ENIM_COLOR = "white"

    if pieces[str(number)][3][0] == "black":
        START_VALUES = [9, 17]
    else:

        EN_LEFT *= -1
        EN_RIGHT *= -1
        ENIM_COLOR = "black"
        IS_LEFT = [1, 9, 17, 25, 33, 41, 49, 57]
        IS_RIGHT = [8, 16, 24, 32, 40, 48, 56, 64]
        START_VALUES = [49, 56]
        LEFT *= -1
        RIGHT *= -1
        FORWARD_1 *= -1
        FORWARD_2 *= -1
    
    if 0 < number+FORWARD_1 < 65:
        if START_VALUES[0] <= number <= START_VALUES[1] and pieces[str(number+FORWARD_1)][0] == "" and pieces[str(number+FORWARD_2)][0] == "":
            possible_moves.append(number+FORWARD_2)
            new_en_passant.append(number+FORWARD_2)
        if pieces[str(number+FORWARD_1)][0] == "":
            possible_moves.append(number+FORWARD_1)

        if number not in IS_LEFT:
            if pieces[str(number+LEFT)][3][0] == ENIM_COLOR :
                possible_moves.append(number+LEFT)
            elif pieces[str(number+EN_LEFT)][3][0] != "" and pieces[str(number)][3][0] != pieces[str(number+EN_LEFT)][3][0] and str(number+EN_LEFT) == str(en_passant):
                possible_moves.append(number+LEFT)
                passed = number+LEFT

        if number not in IS_RIGHT:
            if pieces[str(number+RIGHT)][3][0] == ENIM_COLOR:
                possible_moves.append(number+RIGHT)
            elif pieces[str(number+EN_RIGHT)][3][0] != "" and pieces[str(number)][3][0] != pieces[str(number+EN_RIGHT)][3][0] and str(number+EN_RIGHT) == str(en_passant):
                possible_moves.append(number+RIGHT)
                passed = number+RIGHT

    return [possible_moves, new_en_passant, passed]


"""the castle function doesn't handle the entire canstling, it only handles the changing of the rooks position and also only takes a the number/square the rooks is on before castling."""

def castle(number):
    number = int(number)
    if number == 63:
        pieces["62"] = pieces["64"]
        pieces["64"] = ["", "", pieces["64"][2], ["none", "none"]]
    elif number == 59:
        pieces["60"] = pieces["57"]
        pieces["57"] = ["", "", pieces["57"][2], ["none", "none"]]
    elif number == 3:
        pieces["4"] = pieces["1"]
        pieces["1"] = ["", "", pieces["1"][2], ["none", "none"]]
    else:
        pieces["6"] = pieces["8"]
        pieces["8"] = ["", "", pieces["8"][2], ["none", "none"]]


"""the promote function get called when i pawn get moved to the back-rank, and displays the options the user can choose from to change its pawn in to (queen, rook, bishop and knight) as well as a white
rectangle underneath it for visibility. it take the number/square the pawn has been put on and the color (black or white) as inputs"""

def promote(number, color):
    transform_size = SQUARE_SIZE
    coordinates = []
    if color == "white":
        rect_canvas = pygame.Rect(((SCREEN_WIDTH-8*SQUARE_SIZE)/2)+(((int(number)-1)%8)*SQUARE_SIZE), pieces[number][2][1]-SQUARE_SIZE, SQUARE_SIZE, 4*SQUARE_SIZE)
        pygame.draw.rect(canvas, (255, 255, 255, 255), rect_canvas)
        co = [((SCREEN_WIDTH-8*SQUARE_SIZE)/2)+(((int(number)-1)%8)*SQUARE_SIZE), pieces[number][2][1]-SQUARE_SIZE]
    else:
        rect_canvas = pygame.Rect(((SCREEN_WIDTH-8*SQUARE_SIZE)/2)+(((int(number)-1)%8)*SQUARE_SIZE), pieces[number][2][1]-2*SQUARE_SIZE, SQUARE_SIZE, 4*SQUARE_SIZE)
        pygame.draw.rect(canvas, (255, 255, 255, 255), rect_canvas)
        co = [((SCREEN_WIDTH-8*SQUARE_SIZE)/2)+(((int(number)-1)%8)*SQUARE_SIZE), pieces[number][2][1]+SQUARE_SIZE]
        transform_size *= -1
    
    for element in promoting_pieces:
        if promoting_pieces[element][3][0] == color:
            first_piece = pygame.image.load(f"pieces-basic-png/{promoting_pieces[element][0]}")
            new_image = pygame.transform.scale(first_piece, (SQUARE_SIZE, SQUARE_SIZE))
            new_image_rect = new_image.get_rect()
            new_image_rect.topleft = (co[0], co[1])
            canvas.blit(new_image, new_image_rect)
            coordinates.append(co)
            co[1] += transform_size
    
    return coordinates


"""the is_check function determins is a specific move causes a check by returing a boolean, given the color to move,the current position (piece_dict), the number/square the moving piece would go off of,
the number/square it would go to, the location of the moving color's king and the piece-type of the moving piece"""

def is_check(to_move, piece_dict, number, moving, king_loc, piece):
    number = str(number)
    moving = str(moving)
    king_loc = str(king_loc)
    mover = {}
    if piece == "king":
        king_loc = moving
    first_move = piece_dict[moving]
    second_move = piece_dict[number]
    piece_dict[moving] = piece_dict[number]
    piece_dict[number] = ["", "", piece_dict[number][2], ["none", "none"]]
    for element in piece_dict:
        if piece_dict[element][3][0] == to_move:
            if piece_dict[element][3][1] == "pawn":
                all_moves = get_pawn_moves(number=element, en_passant=en_passant)
                mover[element] = all_moves[0]
                passed = all_moves[2]
            elif piece_dict[element][3][1] == "rook":
                mover[element] = get_rook_moves(number=element)
                print(f"rook moves: {piece_dict[element]}")
            elif piece_dict[element][3][1] == "bishop":
                mover[element] = get_bishop_moves(number=element)
            elif piece_dict[element][3][1] == "queen":
                mover[element] = get_queen_moves(number=element)
            elif piece_dict[element][3][1] == "king":
                if piece_dict[element][3][0] == "white":
                    mover[element] = get_king_moves(number=element, castle_short=(not king_moved[1] and not rook_short_moved[1]), castle_long=(not king_moved[1] and not rook_long_moved[1]))
                else:
                    mover[element] = get_king_moves(number=element, castle_short=(not king_moved[0] and not rook_short_moved[0]), castle_long=(not king_moved[0] and not rook_long_moved[0]))
            elif piece_dict[element][3][1] == "knight":
                mover[element] = get_knight_moves(number=element)
            for mover_element in mover[element]:
                if str(mover_element) == king_loc:
                    piece_dict[moving] = first_move
                    piece_dict[number] = second_move
                    return True
    piece_dict[moving] = first_move
    piece_dict[number] = second_move
    return False


############### NON FUNCTIONS ###############


"""the initialize function puts all the squares and pieces in to their starting positions and takes no inputs."""

def initialize():
    images = []
    SQUARE_SIZE = 90
    X_CO = (SCREEN_WIDTH-8*SQUARE_SIZE)/2
    Y_CO = (SCREEN_HEIGHT-8*SQUARE_SIZE)/2
    pieces_rect = {}
    squares = {}
    coordinates = []
    for num in range(64):
        if num%8 == 0 and num != 0:
            X_CO = (SCREEN_WIDTH-8*SQUARE_SIZE)/2
            Y_CO += SQUARE_SIZE
        squares[f"square{num}"] = pygame.Rect((X_CO, Y_CO, SQUARE_SIZE, SQUARE_SIZE))
        images.append([f"square{num}"])
        X_CO += SQUARE_SIZE
        coordinates.append((X_CO, Y_CO))

    for num in range(1, 65):
        num = str(num)
        if num in pieces and pieces[num][0]:
            first_piece = pygame.image.load(f"pieces-basic-png/{pieces[num][0]}")
            pieces[num][1] = pygame.transform.scale(first_piece, (SQUARE_SIZE, SQUARE_SIZE))
            pieces[num][2] = coordinates[int(num)-1]
            pieces_rect[f"{num}_rect"] = pieces[num][1].get_rect()
            pieces_rect[f"{num}_rect"].topright = coordinates[int(num)-1]
        else:
            pieces[num] = ["", "", coordinates[int(num)-1], ["none", "none"]]
    
    return [squares, pieces_rect, images]


############### RUNNING LOOP ###############
moves = {'49': [33, 41], '50': [34, 42], '51': [35, 43], '52': [36, 44], '53': [37, 45], '54': [38, 46], '55': [39, 47], '56': [40, 48], '58': [43, 41], '63': [46, 48]}
last_3_positions = {}
is_drawn = [False, False]
insuficient_material = [{}, {}]
fifty_moves = 0
piece_moves = []
past_moves = []
king_pos = {"black": "5","white": "61"}
check= [None, None]
to_move = ["white", "black"]
cover = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
coordinates = []
in_promotion = False
king_moved = [False, False]
rook_short_moved = [False, False]
rook_long_moved = [False, False]
passed = 0
in_passant = False
in_selection = False
answer = ""
en_passant = None
active_image = None
selected_piece = None
run = True
wait = False
while run:

    screen.fill("#341C00")

    in_list = initialize()
    squares = in_list[0]
    pieces_rect = in_list[1]
    images = in_list[2]
    color = [(255, 254, 223), (140, 94, 0)]

    for n in range(64):
        if n%8 == 0 and n != 0:
            color = color[::-1]
        p = color[n%2]
        pygame.draw.rect(screen, p, squares[f"square{n}"])

    for piece in pieces_rect:
        screen.blit(pieces[piece[:-5]][1], pieces_rect[piece])
    
    screen.blit(transparant_surface, (0, 0))
    screen.blit(canvas, (0, 0))

    if wait:
        write(TEXT, FONT, "#CCA500")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            pos = (mouse_x, mouse_y)
            answer = False
            for element in pieces:
                if (pieces[element][2][0] > mouse_x > pieces[element][2][0]-SQUARE_SIZE and
                    pieces[element][2][1] < mouse_y < pieces[element][2][1]+SQUARE_SIZE):
                    answer = element
            """by checking the wait variable it is checking if the game is still on going or not"""
            if event.button == 1 and not wait:
                """here the program draw transparant cicles above the visible cicles that showed the possible moves of a piece when click"""
                for move in piece_moves:
                        pygame.draw.circle(transparant_surface, (60, 57, 34, 0), (pieces[str(move)][2][0]-SQUARE_SIZE/2, pieces[str(move)][2][1]+SQUARE_SIZE/2,), SQUARE_SIZE/4, SQUARE_SIZE)

                if answer and (pieces[answer][3][0] == to_move[0] or in_selection or in_promotion):
                    """if the choice canvas is still getting displayed, the program shouldn't move anything, but instead look what piece the user chose"""
                    if in_promotion:
                        if answer in coordinates:
                            fifty_moves = 0
                            location = int(answer)%8
                            if location == 0:
                                location = 8
                            if int(answer) <= 32:
                                pieces[str(location)][3][1] = promoting_pieces[f"white_{coordinates[answer]}"][3][1]
                                pieces[str(location)][0] = promoting_pieces[f"white_{coordinates[answer]}"][0]
                            else:
                                pieces[str(location+56)][3][1] = promoting_pieces[f"black_{coordinates[answer]}"][3][1]
                                pieces[str(location+56)][0] = promoting_pieces[f"black_{coordinates[answer]}"][0]
                        pygame.draw.rect(canvas, (255, 255, 255, 0), cover)
                        in_promotion = False
                        """if a piece is getting selected the program must check if user played it and if so, move it there."""
                    elif in_selection:
                        if int(answer) in piece_moves:
                            """if the user selectedd a possible move, the program plays that move together with all the other thing that may be atached to it (rook moves after castling, pawn removal after en-passant, ...)"""
                            en_passant = None
                            if pieces[selected_piece][3][1] == "pawn":
                                fifty_moves = 0
                                if abs(int(selected_piece)-int(answer)) == 16:
                                    en_passant = answer
                                if answer == passed:
                                    if int(selected_piece)-int(answer) in [7, -9]:
                                        pieces[str(int(selected_piece)+1)] =["", "", pieces[str(int(answer)+1)][2], ["none", "none"]]
                                    elif int(selected_piece)-int(answer) in [-7, 9]:
                                        pieces[str(int(selected_piece)-1)] =["", "", pieces[str(int(answer)-1)][2], ["none", "none"]]
                            to_move = to_move[::-1]
                            if pieces[answer][0] != "":
                                fifty_moves = 0
                            pieces[answer] = pieces[selected_piece]
                            pieces[selected_piece] = ["", "", pieces[selected_piece][2], ["none", "none"]]
                            if pieces[answer][3][1] == "king":
                                king_pos[to_move[1]] = answer
                                if pieces[answer][3][0] == "white":
                                    king_moved[1] = True
                                else:
                                    king_moved[0] = True
                                if abs(int(selected_piece)-int(answer)) == 2:
                                    castle(answer)
                                king_pos[to_move[0]] = answer
                            elif pieces[answer][3][1] == "rook":
                                if answer == "1":
                                    rook_long_moved = [True, rook_long_moved[1]]
                                elif answer == "8":
                                    rook_short_moved = [True, rook_short_moved[1]]
                                elif answer == "57":
                                    rook_long_moved = [rook_long_moved[0], True]
                                elif answer == "64":
                                    rook_short_moved = [rook_short_moved[0], True]
                            elif pieces[answer][3][1] == "pawn" and (int(answer) < 9 or int(answer) > 56):
                                promote(answer, pieces[answer][3][0])
                                if pieces[answer][3][0] == "black":
                                    coordinates = {answer: "queen", str(int(answer)-8): "rook", str(int(answer)-16): "bishop", str(int(answer)-24): "knight"}
                                else:
                                    coordinates = {answer: "queen", str(int(answer)+8): "rook", str(int(answer)+16): "bishop", str(int(answer)+24): "knight"}
                                in_promotion = True
                            elif answer == str(passed):
                                if pieces[answer][3][0] == "white":
                                    pieces[str(int(answer)+8)] = ["", "", pieces[str(int(answer)+8)][2], ["none", "none"]]
                                else:
                                    pieces[str(int(answer)-8)] = ["", "", pieces[str(int(answer)-8)][2], ["none", "none"]]
                            
                            """now the program check is the game has ended in a draw of if it is still on going"""
                            positions = {}
                            for play in pieces:
                                positions[play] = pieces[play][3][1]
                            positions["en_passant"] = passed
                            positions["to_move"] = to_move[0]
                            positions["castle"] = [king_moved, rook_short_moved, rook_long_moved]
                            positions = str(positions)
                            
                            is_in = False
                            if positions in last_3_positions:
                                last_3_positions[positions] += 1
                                if last_3_positions[positions] == 3:
                                    TEXT = f"Draw"
                                    wait = True
                                    print("3 pos")
                            else:
                                last_3_positions[positions] = 1

                            fifty_moves += 1
                            if fifty_moves == 100:
                                TEXT = "Draw"
                                wait = True
                                print("50 moves")
                            
                            insuficient_material = [{}, {}]
                            for element in pieces:
                                if pieces[element][3][0] == "white":
                                    if pieces[element][3][1] in insuficient_material[0]:
                                        insuficient_material[0][pieces[element][3][1]][1] += 1
                                    else:
                                        insuficient_material[0][pieces[element][3][1]] = [element, 1]
                                elif pieces[element][3][0] == "black":
                                    if pieces[element][3][1] in insuficient_material[1]:
                                        insuficient_material[1][pieces[element][3][1]][1] += 1
                                    else:
                                        insuficient_material[1][pieces[element][3][1]] = [element, 1]

                            number = 0
                            bishop = None
                            if len(insuficient_material[0]) <= 2:
                                for element in insuficient_material[0]:
                                    if insuficient_material[0][element][1] == 1:
                                        if element != "pawn" and element != "rook" and element != "queen" and element != "bishop":
                                            number += 1
                                        elif element == "bishop":
                                            number += 1
                                            bishop = int(insuficient_material[0][element][0])%2
                            if number == len(insuficient_material[0]):
                                is_drawn[0] = True

                            number = 0
                            if len(insuficient_material[1]) <= 2:
                                for element in insuficient_material[1]:
                                    if insuficient_material[1][element][1] == 1:
                                        if element != "pawn" and element != "rook" and element != "queen" and element != "bishop":
                                            number += 1
                                        elif insuficient_material[1][element][0] == "bishop":
                                            if int(insuficient_material[1][element][0])%2  == bishop:
                                                number += 1
                            if number == len(insuficient_material[1]):
                                is_drawn[1] = True
                            
                            if is_drawn[0] and is_drawn[1]:
                                TEXT = "Draw"
                                wait = True
                                print("material")

                        """here the program feches all the legal moves the player can play before he selects anything"""
                        in_selection = False
                        moves = {}
                        for element in pieces:
                            if pieces[element][3][0] == to_move[0]:
                                if pieces[element][3][1] == "pawn":
                                    all_moves = get_pawn_moves(number=element, en_passant=en_passant)
                                    moves[element] = all_moves[0]
                                    passed = all_moves[2]
                                elif pieces[element][3][1] == "rook":
                                    moves[element] = get_rook_moves(number=element)
                                elif pieces[element][3][1] == "bishop":
                                    moves[element] = get_bishop_moves(number=element)
                                elif pieces[element][3][1] == "queen":
                                    moves[element] = get_queen_moves(number=element)
                                elif pieces[element][3][1] == "king":
                                    if pieces[element][3][0] == "white":
                                        moves[element] = get_king_moves(number=element, castle_short=(not king_moved[1] and not rook_short_moved[1]), castle_long=(not king_moved[1] and not rook_long_moved[1]))
                                    else:
                                        moves[element] = get_king_moves(number=element, castle_short=(not king_moved[0] and not rook_short_moved[0]), castle_long=(not king_moved[0] and not rook_long_moved[0]))
                                elif pieces[element][3][1] == "knight":
                                    moves[element] = get_knight_moves(number=element)
                                moves[element].append(pieces[element][3][1])

                        """in this block the program filters out all the moves that cause a check for the played playing the move (filters out the illigal moves)."""
                        to_remove_moves = []
                        for m in moves:
                            to_remove_move = []
                            for move in moves[m]:
                                if type(move) == int:
                                    check = is_check(to_move[1], pieces, m, move, king_pos[to_move[0]], moves[m][-1])
                                    if check:
                                        to_remove_move.append(move)
                            to_remove_move.append(moves[m][-1])
                            for remove in to_remove_move:
                                moves[m].remove(remove)
                            if len(moves[m]) == 0:
                                to_remove_moves.append(m)
                        for e in to_remove_moves:
                            del moves[e]
                            
                        """when conclusion have been found the program checks if it is a win or a draw."""
                        if len(moves) == 0:
                            print(to_move[1], king_pos[to_move[0]], king_pos[to_move[0]], king_pos[to_move[0]], "king")
                            if is_check(to_move[1], pieces, king_pos[to_move[0]], king_pos[to_move[0]], king_pos[to_move[0]], "king"):
                                TEXT = f"Winner: {to_move[1]}"
                            else:
                                TEXT = f"Draw"
                                print("stalemate")
                            wait = True

                        """if nothing is getting selected or no choice canvas is getting displayed,
                        the program checks if the user selected anything yet and then displays the possible positions."""
                    else:
                        selected_piece = answer
                        if answer in moves:
                            piece_moves = moves[answer]
                        else:
                            piece_moves =[]
                        if len(piece_moves) > 0:
                            in_selection = True
                            for move in piece_moves:
                                pygame.draw.circle(transparant_surface, (60, 57, 34, 100), (pieces[str(move)][2][0]-SQUARE_SIZE/2, pieces[str(move)][2][1]+SQUARE_SIZE/2,), SQUARE_SIZE/5, SQUARE_SIZE)
                    """if the used didn't select a piece, it unselects all the previous pieces"""
                else:
                    in_selection = False
                """when the user click after the game has ended, the game gets terminated"""
            elif wait:
                run = False
                


    pygame.display.update()

pygame.quit()
