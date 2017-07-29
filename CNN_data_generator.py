"""
This file Aims at Taking a PGN file and generating FEN of it and generating evaluation of it

"""
# https://lichess.org/forum/off-topic-discussion/pgn-to-fen-conversion
import random
import time

import chess
import chess.uci
import chess.pgn
import sys

def pgn_eval():
    # Going through Each game in PGN file
    mega_pgn_obj = open('/home/john/geek_stuff/Chess Project/Chess Data/CCRL-4040.[727811].pgn')
    for offset, headers in chess.pgn.scan_headers(mega_pgn_obj):
        print(int(headers['PlyCount']))
        mega_pgn_obj.seek(offset)
        print(mega_pgn_obj.seek(offset))
        game = chess.pgn.read_game(mega_pgn_obj)
        print("Game: ", game)
        # Going to a Random Position in Game
        rand_pos = random.randint(5, 6)
        count = 0
        while not game.is_end():
            game = game.variations[0]                   # Assigning Child node to game itself
            count += 1
            if count >= rand_pos:
                break
        # Create Board from Game Node
        board = game.board()
        # Get Fen notation of the board
        fen_board_pos = board.fen()
        print('Count ', count)
        print('Move ', game.move)
        print('PGN notation of Board ', game)
        print("Fen Notation of Board ", fen_board_pos)
        print('Its Type ', type(fen_board_pos))

        ## Open Chess Engine and evaluate the board position
        info_handler = chess.uci.InfoHandler()
        engine = chess.uci.popen_engine('/home/john/Downloads/stockfish-8-linux/Linux/stockfish_8_x64')
        engine.info_handlers.append(info_handler)
        engine.position(board)
        # Evaluate Time
        evaltime = 5000  # so 5 seconds
        evaluation = engine.go(movetime=evaltime)

        print("Evaluation ", evaluation)
        print('CP score ', info_handler.info['score'])
        print('\n\n\n')
        time.sleep(20)

        ## Completed : Traversing through each game in a PGN file and selecting some random Board position and evaluate using stockfish
        ## TODO: Convert board position to appropriate feature map and create a data set using feature mapped board position and evaluation

if __name__ == '__main__':
    pgn_eval()