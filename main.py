from classes.board import Graph
from utils.parser import parse_arguments

parsed_args = parse_arguments()
board = Graph(file_path=parsed_args.FILE)
print(board.find_all_complete_extensions())