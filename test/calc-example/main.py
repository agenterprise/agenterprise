import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from parser.CalculatorLexer import CalculatorLexer as lexer
from parser.CalculatorParser import CalculatorParser as parser
from parser.CalculatorListener import CalculatorListener as listener
from mylistener import EvaluationListener   

def main(input_file):
    # Read the input file
    input_stream = FileStream(input_file)
    # Create lexer and parser
    mylexer = lexer(input_stream)
    stream = CommonTokenStream(mylexer)
    myparser = parser(stream)
    # Parse the input
    tree = myparser.expression()
    print(tree.toStringTree(recog=myparser))
    mylistener = listener()
    mylistener = EvaluationListener()
    walker = ParseTreeWalker()
    walker.walk(mylistener, tree)
    res = mylistener.getResult()
    print(res)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
    else:
        main(sys.argv[1])