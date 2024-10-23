# Generated from MISF.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,5,5,63,8,5,10,5,12,5,66,9,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,96,8,8,1,8,1,8,1,8,5,
        8,101,8,8,10,8,12,8,104,9,8,1,8,0,1,16,9,0,2,4,6,8,10,12,14,16,0,
        1,1,0,11,14,109,0,21,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,37,1,0,
        0,0,8,43,1,0,0,0,10,56,1,0,0,0,12,69,1,0,0,0,14,82,1,0,0,0,16,95,
        1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,
        21,22,1,0,0,0,22,1,1,0,0,0,23,21,1,0,0,0,24,31,3,4,2,0,25,31,3,6,
        3,0,26,31,3,8,4,0,27,31,3,10,5,0,28,31,3,12,6,0,29,31,3,14,7,0,30,
        24,1,0,0,0,30,25,1,0,0,0,30,26,1,0,0,0,30,27,1,0,0,0,30,28,1,0,0,
        0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,5,15,0,0,33,34,5,1,0,0,34,35,
        3,16,8,0,35,36,5,2,0,0,36,5,1,0,0,0,37,38,5,3,0,0,38,39,5,4,0,0,
        39,40,3,16,8,0,40,41,5,5,0,0,41,42,5,2,0,0,42,7,1,0,0,0,43,44,5,
        6,0,0,44,45,5,4,0,0,45,46,3,16,8,0,46,47,5,5,0,0,47,51,5,7,0,0,48,
        50,3,2,1,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,
        0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,8,0,0,55,9,1,0,0,0,56,57,5,
        9,0,0,57,58,5,4,0,0,58,59,3,16,8,0,59,60,5,5,0,0,60,64,5,7,0,0,61,
        63,3,2,1,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,
        0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,8,0,0,68,11,1,0,0,0,69,70,
        5,10,0,0,70,71,5,15,0,0,71,72,5,4,0,0,72,73,5,5,0,0,73,77,5,7,0,
        0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,
        1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,80,81,5,8,0,0,81,13,1,0,0,0,
        82,83,5,15,0,0,83,84,5,4,0,0,84,85,5,5,0,0,85,86,5,2,0,0,86,15,1,
        0,0,0,87,88,6,8,-1,0,88,96,5,16,0,0,89,96,5,17,0,0,90,96,5,15,0,
        0,91,92,5,4,0,0,92,93,3,16,8,0,93,94,5,5,0,0,94,96,1,0,0,0,95,87,
        1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,96,102,1,0,0,0,
        97,98,10,5,0,0,98,99,7,0,0,0,99,101,3,16,8,6,100,97,1,0,0,0,101,
        104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,17,1,0,0,0,104,102,
        1,0,0,0,7,21,30,51,64,77,95,102
    ]

class MISFParser ( Parser ):

    grammarFileName = "MISF.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'print'", "'('", "')'", 
                     "'if'", "'{'", "'}'", "'while'", "'function'", "'+'", 
                     "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignmentStatement = 2
    RULE_printStatement = 3
    RULE_ifStatement = 4
    RULE_whileStatement = 5
    RULE_functionDeclaration = 6
    RULE_functionCall = 7
    RULE_expression = 8

    ruleNames =  [ "program", "statement", "assignmentStatement", "printStatement", 
                   "ifStatement", "whileStatement", "functionDeclaration", 
                   "functionCall", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    INT=16
    STRING=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MISFParser.StatementContext)
            else:
                return self.getTypedRuleContext(MISFParser.StatementContext,i)


        def getRuleIndex(self):
            return MISFParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MISFParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34376) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(MISFParser.AssignmentStatementContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(MISFParser.PrintStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MISFParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MISFParser.WhileStatementContext,0)


        def functionDeclaration(self):
            return self.getTypedRuleContext(MISFParser.FunctionDeclarationContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MISFParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return MISFParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MISFParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.printStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.functionDeclaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 29
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MISFParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MISFParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MISFParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = MISFParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(MISFParser.ID)
            self.state = 33
            self.match(MISFParser.T__0)
            self.state = 34
            self.expression(0)
            self.state = 35
            self.match(MISFParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MISFParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MISFParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStatement" ):
                return visitor.visitPrintStatement(self)
            else:
                return visitor.visitChildren(self)




    def printStatement(self):

        localctx = MISFParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MISFParser.T__2)
            self.state = 38
            self.match(MISFParser.T__3)
            self.state = 39
            self.expression(0)
            self.state = 40
            self.match(MISFParser.T__4)
            self.state = 41
            self.match(MISFParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MISFParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MISFParser.StatementContext)
            else:
                return self.getTypedRuleContext(MISFParser.StatementContext,i)


        def getRuleIndex(self):
            return MISFParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MISFParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MISFParser.T__5)
            self.state = 44
            self.match(MISFParser.T__3)
            self.state = 45
            self.expression(0)
            self.state = 46
            self.match(MISFParser.T__4)
            self.state = 47
            self.match(MISFParser.T__6)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34376) != 0):
                self.state = 48
                self.statement()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(MISFParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MISFParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MISFParser.StatementContext)
            else:
                return self.getTypedRuleContext(MISFParser.StatementContext,i)


        def getRuleIndex(self):
            return MISFParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MISFParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MISFParser.T__8)
            self.state = 57
            self.match(MISFParser.T__3)
            self.state = 58
            self.expression(0)
            self.state = 59
            self.match(MISFParser.T__4)
            self.state = 60
            self.match(MISFParser.T__6)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34376) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(MISFParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MISFParser.ID, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MISFParser.StatementContext)
            else:
                return self.getTypedRuleContext(MISFParser.StatementContext,i)


        def getRuleIndex(self):
            return MISFParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDeclaration" ):
                return visitor.visitFunctionDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def functionDeclaration(self):

        localctx = MISFParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_functionDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MISFParser.T__9)
            self.state = 70
            self.match(MISFParser.ID)
            self.state = 71
            self.match(MISFParser.T__3)
            self.state = 72
            self.match(MISFParser.T__4)
            self.state = 73
            self.match(MISFParser.T__6)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34376) != 0):
                self.state = 74
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(MISFParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MISFParser.ID, 0)

        def getRuleIndex(self):
            return MISFParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MISFParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MISFParser.ID)
            self.state = 83
            self.match(MISFParser.T__3)
            self.state = 84
            self.match(MISFParser.T__4)
            self.state = 85
            self.match(MISFParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MISFParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesizedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MISFParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MISFParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class StringLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MISFParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MISFParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MISFParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MISFParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MISFParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MISFParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOperationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MISFParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MISFParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MISFParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOperation" ):
                listener.enterBinaryOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOperation" ):
                listener.exitBinaryOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOperation" ):
                return visitor.visitBinaryOperation(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MISFParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                localctx = MISFParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 88
                self.match(MISFParser.INT)
                pass
            elif token in [17]:
                localctx = MISFParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(MISFParser.STRING)
                pass
            elif token in [15]:
                localctx = MISFParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 90
                self.match(MISFParser.ID)
                pass
            elif token in [4]:
                localctx = MISFParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 91
                self.match(MISFParser.T__3)
                self.state = 92
                self.expression(0)
                self.state = 93
                self.match(MISFParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MISFParser.BinaryOperationContext(self, MISFParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 97
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 98
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30720) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.expression(6) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




