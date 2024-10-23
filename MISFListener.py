# Generated from MISF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MISFParser import MISFParser
else:
    from MISFParser import MISFParser

# This class defines a complete listener for a parse tree produced by MISFParser.
class MISFListener(ParseTreeListener):

    # Enter a parse tree produced by MISFParser#program.
    def enterProgram(self, ctx:MISFParser.ProgramContext):
        pass

    # Exit a parse tree produced by MISFParser#program.
    def exitProgram(self, ctx:MISFParser.ProgramContext):
        pass


    # Enter a parse tree produced by MISFParser#statement.
    def enterStatement(self, ctx:MISFParser.StatementContext):
        pass

    # Exit a parse tree produced by MISFParser#statement.
    def exitStatement(self, ctx:MISFParser.StatementContext):
        pass


    # Enter a parse tree produced by MISFParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:MISFParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by MISFParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:MISFParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by MISFParser#printStatement.
    def enterPrintStatement(self, ctx:MISFParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by MISFParser#printStatement.
    def exitPrintStatement(self, ctx:MISFParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by MISFParser#ifStatement.
    def enterIfStatement(self, ctx:MISFParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MISFParser#ifStatement.
    def exitIfStatement(self, ctx:MISFParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MISFParser#whileStatement.
    def enterWhileStatement(self, ctx:MISFParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MISFParser#whileStatement.
    def exitWhileStatement(self, ctx:MISFParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MISFParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:MISFParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by MISFParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:MISFParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by MISFParser#functionCall.
    def enterFunctionCall(self, ctx:MISFParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MISFParser#functionCall.
    def exitFunctionCall(self, ctx:MISFParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MISFParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:MISFParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by MISFParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:MISFParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by MISFParser#stringLiteral.
    def enterStringLiteral(self, ctx:MISFParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by MISFParser#stringLiteral.
    def exitStringLiteral(self, ctx:MISFParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by MISFParser#intLiteral.
    def enterIntLiteral(self, ctx:MISFParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by MISFParser#intLiteral.
    def exitIntLiteral(self, ctx:MISFParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by MISFParser#variable.
    def enterVariable(self, ctx:MISFParser.VariableContext):
        pass

    # Exit a parse tree produced by MISFParser#variable.
    def exitVariable(self, ctx:MISFParser.VariableContext):
        pass


    # Enter a parse tree produced by MISFParser#binaryOperation.
    def enterBinaryOperation(self, ctx:MISFParser.BinaryOperationContext):
        pass

    # Exit a parse tree produced by MISFParser#binaryOperation.
    def exitBinaryOperation(self, ctx:MISFParser.BinaryOperationContext):
        pass



del MISFParser