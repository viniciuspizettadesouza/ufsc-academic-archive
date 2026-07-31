from antlr4 import FileStream, CommonTokenStream
from os import path
import argparse
from ast_decompiler import decompile

try:
    from .parser.vjjLexer import vjjLexer
    from .parser.vjjParser import vjjParser
except ImportError:
    # Generate ANTLR parser from g4 file
    from .generate_parser import generate_parser
    generate_parser(path.join(path.dirname(__file__), 'parser/vjj.g4'))

    from .parser.vjjLexer import vjjLexer
    from .parser.vjjParser import vjjParser

# import astVisitor after the try-except
from .astVisitor import astVisitor


def main():

    # Argument parser
    parser_args = argparse.ArgumentParser(prog='vjj', description='C-- interpreter')
    parser_args.add_argument('input', type=str, help='source code')
    parser_args.add_argument('-o', metavar='', type=str, default=None, help='python output')

    args = parser_args.parse_args() 
    #################################

    input_stream = FileStream(args.input)

    lexer = vjjLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = vjjParser(stream)

    tree = parser.start() # Get AST

    # Transverse AST to generate python ast 
    # visitor = astVisitor(args.input)
    # ast = visitor.visitStart(tree)

    # code = compile(source=ast, filename=args.input, mode='exec') 

    # exec(code, globals())
    
    # if args.o:
    #     with open(args.o, 'w') as file:
    #         file.write(decompile(ast))

if __name__ == '__main__':
    main()