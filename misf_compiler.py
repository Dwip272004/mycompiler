import sys
from antlr4 import *
from MISFLexer import MISFLexer
from MISFParser import MISFParser
from MISFVisitor import MISFVisitor
import os

class MISFCustomVisitor(MISFVisitor):
    def __init__(self):
        self.variables = {}

    # Implement visitor methods for each rule
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitAssignmentStatement(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expression())
        self.variables[var_name] = value
        return value

    def visitPrintStatement(self, ctx):
        value = self.visit(ctx.expression())
        print(value)
        return value

    def visitBinaryOperation(self, ctx):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.getChild(1).getText()
        
        try:
            left = int(left)
            right = int(right)
        except ValueError:
            # If conversion fails, treat as strings
            if op == '+':
                return str(left) + str(right)
            raise Exception(f"Invalid operation {op} for strings")

        if op == '+': return left + right
        if op == '-': return left - right
        if op == '*': return left * right
        if op == '/': return left / right

    def visitIntLiteral(self, ctx):
        return int(ctx.INT().getText())

    def visitStringLiteral(self, ctx):
        # Remove the quotes from the string
        return ctx.STRING().getText()[1:-1]

    def visitVariable(self, ctx):
        var_name = ctx.ID().getText()
        if var_name in self.variables:
            return self.variables[var_name]
        raise Exception(f"Variable {var_name} not defined")

def process_misf_file(file_path):
    if not file_path.endswith('.misf'):
        print(f"Error: File {file_path} is not a .misf file")
        return False
    
    try:
        # Create input stream from file
        input_stream = FileStream(file_path)
        
        # Create lexer
        lexer = MISFLexer(input_stream)
        stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = MISFParser(stream)
        tree = parser.program()
        
        # Create and run visitor
        visitor = MISFCustomVisitor()
        visitor.visit(tree)
        
        return True
    
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python misf_compiler.py <file.misf>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    success = process_misf_file(file_path)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()