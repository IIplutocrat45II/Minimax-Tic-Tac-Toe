"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for val in row:
            if val == None:
                count += 1
    if count%2 != 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        raise Exception
    actions_list = list() # Tracks all the coordinate pairs of the empty spaces 
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if(board[i][j] == None):
                actions_list.append((i,j))
    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action[0], action[1]
    if board[i][j] != None:
        raise  Exception

    board_duplicate = copy.deepcopy(board)

    player_marker = player(board_duplicate) # Check the who's turn to play
    board_duplicate[i][j] = player_marker

    return board_duplicate


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Base cases
    # 1. All the rows
    # 2. All the columns 
    # 3. Both the diagonals

    col1,col2, col3, principal_diaog, secondary_diaog = [],[],[],[],[]
    flag = 0 # 0 means there is a winner and 1 meaning there is no winner
    for i, row in enumerate(board): 
        # Checking for condition 1
        if (len(set(row)) == 1): 
            if row[0] == X :
                return X
            else:
                return O
                                
        # Checking for condition 2
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])

        # Checking for Condition 3
        principal_diaog.append(row[i])
        secondary_diaog.append(row[len(row)-i-1])

    if flag == 0:
        if (len(set(col1)) == 1):
            if col1[0] == X :
                return X
            else:
                return O

        if (len(set(col2)) == 1):
            if col2[0] == X :
                return X
            else:
                return O

        if (len(set(col3)) == 1):
            if col3[0] == X :
                return X
            else:
                return O
        
        if (len(set(principal_diaog))==1):
            if principal_diaog[0] == X :
                return X
            else:
                return O

        if (len(set(secondary_diaog))==1):
            if secondary_diaog[0] == X :
                return X
            else:
                return O
    else:
        return None

    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
        
    col1,col2, col3, principal_diaog, secondary_diaog = [],[],[],[],[]
    for i, row in enumerate(board): 
        # Checking for condition 1
        if (len(set(row)) == 1 and row[0] != None): 
            return True                                
        # Checking for condition 2
        col1.append(row[0])
        col2.append(row[1])
        col3.append(row[2])

        # Checking for Condition 3
        principal_diaog.append(row[i])
        secondary_diaog.append(row[len(row)-i-1])

    if( len(set(col1))==1 and col1[0] != None or 
        len(set(col2))==1 and col2[0] != None or
        len(set(col3))==1 and col3[0] != None
        ):
        return True

    elif( len(set(principal_diaog))==1 and principal_diaog[0] != None or
          len(set(secondary_diaog))==1 and secondary_diaog[0] != None
        ):
        return True
        
    else:
        count = 0
        for row in board:
            for val in row:
                if val == None:
                    count += 1
        if count == 0:
            return True
        else:
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X: 
        return 1
    elif result == O:
        return -1
    elif result == None: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_ = player(board)

    def max_value(board):
        if terminal(board) == True:
            return None, utility(board)
        v = -math.inf
        action_opt = None

        for action in actions(board):
            (_, cal) = min_value(result(board, action=action))
            if v < cal :
                v = cal
                action_opt = action

        return action_opt, v
    
    def min_value(board):
        if terminal(board) == True:
            return None, utility(board)
        v = math.inf
        action_opt = None

        for action in actions(board): 
            _, cal = max_value(result(board, action=action))
            # print("min: ", cal)
            if v > cal:
                v = cal
                action_opt = action
            
        return action_opt, v 
    
    if player_ == X:
        action, score = max_value(board)
        #print("Score of X player= ", score)
        return action
    else:
        action, score = min_value(board)
        #print("Score of O player= ", score)
        return action
    
