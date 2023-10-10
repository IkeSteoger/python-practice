def isValidChessBoard(board):
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']
    
    allPieces = set(color + piece for piece in pieces for color in colors)
    
    validCounts = {'king': (1, 1),
                   'queen': (0, 1),
                   'rook': (0, 2),
                   'bishop': (0, 2),
                   'knight': (0, 2),
                   'pawn': (0, 8)}
    
    pieceCount = {}
    for value in board.values():
        if value in allPieces:
            pieceCount.setdefault(value, 0)
            pieceCount[value] += 1

    for piece in allPieces:
        count = pieceCount.get(piece, 0)
        low, high = validCounts[piece[1:]]
        if not low <= count <= high:
            if low != high:
                print('There should between {low} and {high} {piece} but there are {count}')
            else: 
                print('There should be {low} {piece} but there are {count}')
            return False
        
    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= 'h')):
            print('Invalid to have {board[location]} at position {location}')
            return False
        
    for location, piece in board.items():
        if piece:
            if not piece in allPieces:
                print('{piece} is not a valid chess piece at position {location}')
                return False
            
    return True