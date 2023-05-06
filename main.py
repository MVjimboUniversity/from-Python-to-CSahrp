import sys
import os
from antlr4 import *
from LexLexer import LexLexer
from LexParser import LexParser
from CSharpListener import CSharpListener


def main(file_name):
    input = FileStream(file_name)
    lexer = LexLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LexParser(stream)
    tree = parser.start()

    if os.path.isfile(file_name[:-2] + "cs"):
        os.remove(file_name[:-2] + "cs")
    output = open(file_name[:-2] + "cs","w")
    
    htmlChat = CSharpListener(output)
    walker = ParseTreeWalker()
    walker.walk(htmlChat, tree)
      
if __name__ == '__main__':
    main("example/input.py")
