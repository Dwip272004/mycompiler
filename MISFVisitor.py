# Generated from MISF.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MISFParser import MISFParser
else:
    from MISFParser import MISFParser

# This class defines a complete generic visitor for a parse tree produced by MISFParser.

class MISFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MISFParser#program.
    def visitProgram(self, ctx:MISFParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#statement.
    def visitStatement(self, ctx:MISFParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#assignmentStatement.
    def visitAssignmentStatement(self, ctx:MISFParser.AssignmentStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#printStatement.
    def visitPrintStatement(self, ctx:MISFParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#ifStatement.
    def visitIfStatement(self, ctx:MISFParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#whileStatement.
    def visitWhileStatement(self, ctx:MISFParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:MISFParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#functionCall.
    def visitFunctionCall(self, ctx:MISFParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:MISFParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#stringLiteral.
    def visitStringLiteral(self, ctx:MISFParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#intLiteral.
    def visitIntLiteral(self, ctx:MISFParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#variable.
    def visitVariable(self, ctx:MISFParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MISFParser#binaryOperation.
    def visitBinaryOperation(self, ctx:MISFParser.BinaryOperationContext):
        return self.visitChildren(ctx)



del MISFParser