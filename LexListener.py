# Generated from Lex.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LexParser import LexParser
else:
    from LexParser import LexParser

# This class defines a complete listener for a parse tree produced by LexParser.
class LexListener(ParseTreeListener):

    # Enter a parse tree produced by LexParser#start.
    def enterStart(self, ctx:LexParser.StartContext):
        pass

    # Exit a parse tree produced by LexParser#start.
    def exitStart(self, ctx:LexParser.StartContext):
        pass


    # Enter a parse tree produced by LexParser#code.
    def enterCode(self, ctx:LexParser.CodeContext):
        pass

    # Exit a parse tree produced by LexParser#code.
    def exitCode(self, ctx:LexParser.CodeContext):
        pass


    # Enter a parse tree produced by LexParser#statement.
    def enterStatement(self, ctx:LexParser.StatementContext):
        pass

    # Exit a parse tree produced by LexParser#statement.
    def exitStatement(self, ctx:LexParser.StatementContext):
        pass


    # Enter a parse tree produced by LexParser#mainStatement.
    def enterMainStatement(self, ctx:LexParser.MainStatementContext):
        pass

    # Exit a parse tree produced by LexParser#mainStatement.
    def exitMainStatement(self, ctx:LexParser.MainStatementContext):
        pass


    # Enter a parse tree produced by LexParser#mainStatementNoNewLine.
    def enterMainStatementNoNewLine(self, ctx:LexParser.MainStatementNoNewLineContext):
        pass

    # Exit a parse tree produced by LexParser#mainStatementNoNewLine.
    def exitMainStatementNoNewLine(self, ctx:LexParser.MainStatementNoNewLineContext):
        pass


    # Enter a parse tree produced by LexParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:LexParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by LexParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:LexParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by LexParser#methodHeader.
    def enterMethodHeader(self, ctx:LexParser.MethodHeaderContext):
        pass

    # Exit a parse tree produced by LexParser#methodHeader.
    def exitMethodHeader(self, ctx:LexParser.MethodHeaderContext):
        pass


    # Enter a parse tree produced by LexParser#methodHeaderVariables.
    def enterMethodHeaderVariables(self, ctx:LexParser.MethodHeaderVariablesContext):
        pass

    # Exit a parse tree produced by LexParser#methodHeaderVariables.
    def exitMethodHeaderVariables(self, ctx:LexParser.MethodHeaderVariablesContext):
        pass


    # Enter a parse tree produced by LexParser#methodHeaderVariable.
    def enterMethodHeaderVariable(self, ctx:LexParser.MethodHeaderVariableContext):
        pass

    # Exit a parse tree produced by LexParser#methodHeaderVariable.
    def exitMethodHeaderVariable(self, ctx:LexParser.MethodHeaderVariableContext):
        pass


    # Enter a parse tree produced by LexParser#methodBody.
    def enterMethodBody(self, ctx:LexParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by LexParser#methodBody.
    def exitMethodBody(self, ctx:LexParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by LexParser#methodStatement.
    def enterMethodStatement(self, ctx:LexParser.MethodStatementContext):
        pass

    # Exit a parse tree produced by LexParser#methodStatement.
    def exitMethodStatement(self, ctx:LexParser.MethodStatementContext):
        pass


    # Enter a parse tree produced by LexParser#methodStatementNoNewLine.
    def enterMethodStatementNoNewLine(self, ctx:LexParser.MethodStatementNoNewLineContext):
        pass

    # Exit a parse tree produced by LexParser#methodStatementNoNewLine.
    def exitMethodStatementNoNewLine(self, ctx:LexParser.MethodStatementNoNewLineContext):
        pass


    # Enter a parse tree produced by LexParser#methodName.
    def enterMethodName(self, ctx:LexParser.MethodNameContext):
        pass

    # Exit a parse tree produced by LexParser#methodName.
    def exitMethodName(self, ctx:LexParser.MethodNameContext):
        pass


    # Enter a parse tree produced by LexParser#methodCall.
    def enterMethodCall(self, ctx:LexParser.MethodCallContext):
        pass

    # Exit a parse tree produced by LexParser#methodCall.
    def exitMethodCall(self, ctx:LexParser.MethodCallContext):
        pass


    # Enter a parse tree produced by LexParser#forDeclaration.
    def enterForDeclaration(self, ctx:LexParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by LexParser#forDeclaration.
    def exitForDeclaration(self, ctx:LexParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by LexParser#forHead.
    def enterForHead(self, ctx:LexParser.ForHeadContext):
        pass

    # Exit a parse tree produced by LexParser#forHead.
    def exitForHead(self, ctx:LexParser.ForHeadContext):
        pass


    # Enter a parse tree produced by LexParser#forBody.
    def enterForBody(self, ctx:LexParser.ForBodyContext):
        pass

    # Exit a parse tree produced by LexParser#forBody.
    def exitForBody(self, ctx:LexParser.ForBodyContext):
        pass


    # Enter a parse tree produced by LexParser#forStatement.
    def enterForStatement(self, ctx:LexParser.ForStatementContext):
        pass

    # Exit a parse tree produced by LexParser#forStatement.
    def exitForStatement(self, ctx:LexParser.ForStatementContext):
        pass


    # Enter a parse tree produced by LexParser#forStatementNoNewLine.
    def enterForStatementNoNewLine(self, ctx:LexParser.ForStatementNoNewLineContext):
        pass

    # Exit a parse tree produced by LexParser#forStatementNoNewLine.
    def exitForStatementNoNewLine(self, ctx:LexParser.ForStatementNoNewLineContext):
        pass


    # Enter a parse tree produced by LexParser#ifDeclaration.
    def enterIfDeclaration(self, ctx:LexParser.IfDeclarationContext):
        pass

    # Exit a parse tree produced by LexParser#ifDeclaration.
    def exitIfDeclaration(self, ctx:LexParser.IfDeclarationContext):
        pass


    # Enter a parse tree produced by LexParser#ifHead.
    def enterIfHead(self, ctx:LexParser.IfHeadContext):
        pass

    # Exit a parse tree produced by LexParser#ifHead.
    def exitIfHead(self, ctx:LexParser.IfHeadContext):
        pass


    # Enter a parse tree produced by LexParser#ifBody.
    def enterIfBody(self, ctx:LexParser.IfBodyContext):
        pass

    # Exit a parse tree produced by LexParser#ifBody.
    def exitIfBody(self, ctx:LexParser.IfBodyContext):
        pass


    # Enter a parse tree produced by LexParser#truePart.
    def enterTruePart(self, ctx:LexParser.TruePartContext):
        pass

    # Exit a parse tree produced by LexParser#truePart.
    def exitTruePart(self, ctx:LexParser.TruePartContext):
        pass


    # Enter a parse tree produced by LexParser#elsePart.
    def enterElsePart(self, ctx:LexParser.ElsePartContext):
        pass

    # Exit a parse tree produced by LexParser#elsePart.
    def exitElsePart(self, ctx:LexParser.ElsePartContext):
        pass


    # Enter a parse tree produced by LexParser#ifStatement.
    def enterIfStatement(self, ctx:LexParser.IfStatementContext):
        pass

    # Exit a parse tree produced by LexParser#ifStatement.
    def exitIfStatement(self, ctx:LexParser.IfStatementContext):
        pass


    # Enter a parse tree produced by LexParser#ifStatementNoNewLine.
    def enterIfStatementNoNewLine(self, ctx:LexParser.IfStatementNoNewLineContext):
        pass

    # Exit a parse tree produced by LexParser#ifStatementNoNewLine.
    def exitIfStatementNoNewLine(self, ctx:LexParser.IfStatementNoNewLineContext):
        pass


    # Enter a parse tree produced by LexParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:LexParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by LexParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:LexParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by LexParser#variableType.
    def enterVariableType(self, ctx:LexParser.VariableTypeContext):
        pass

    # Exit a parse tree produced by LexParser#variableType.
    def exitVariableType(self, ctx:LexParser.VariableTypeContext):
        pass


    # Enter a parse tree produced by LexParser#variableName.
    def enterVariableName(self, ctx:LexParser.VariableNameContext):
        pass

    # Exit a parse tree produced by LexParser#variableName.
    def exitVariableName(self, ctx:LexParser.VariableNameContext):
        pass


    # Enter a parse tree produced by LexParser#pFloatLiteral.
    def enterPFloatLiteral(self, ctx:LexParser.PFloatLiteralContext):
        pass

    # Exit a parse tree produced by LexParser#pFloatLiteral.
    def exitPFloatLiteral(self, ctx:LexParser.PFloatLiteralContext):
        pass


    # Enter a parse tree produced by LexParser#pIntegerLiteral.
    def enterPIntegerLiteral(self, ctx:LexParser.PIntegerLiteralContext):
        pass

    # Exit a parse tree produced by LexParser#pIntegerLiteral.
    def exitPIntegerLiteral(self, ctx:LexParser.PIntegerLiteralContext):
        pass


    # Enter a parse tree produced by LexParser#pStringLiteral.
    def enterPStringLiteral(self, ctx:LexParser.PStringLiteralContext):
        pass

    # Exit a parse tree produced by LexParser#pStringLiteral.
    def exitPStringLiteral(self, ctx:LexParser.PStringLiteralContext):
        pass


    # Enter a parse tree produced by LexParser#pMathOperation.
    def enterPMathOperation(self, ctx:LexParser.PMathOperationContext):
        pass

    # Exit a parse tree produced by LexParser#pMathOperation.
    def exitPMathOperation(self, ctx:LexParser.PMathOperationContext):
        pass


    # Enter a parse tree produced by LexParser#variableInitialization.
    def enterVariableInitialization(self, ctx:LexParser.VariableInitializationContext):
        pass

    # Exit a parse tree produced by LexParser#variableInitialization.
    def exitVariableInitialization(self, ctx:LexParser.VariableInitializationContext):
        pass


    # Enter a parse tree produced by LexParser#condition.
    def enterCondition(self, ctx:LexParser.ConditionContext):
        pass

    # Exit a parse tree produced by LexParser#condition.
    def exitCondition(self, ctx:LexParser.ConditionContext):
        pass


    # Enter a parse tree produced by LexParser#mathOperation.
    def enterMathOperation(self, ctx:LexParser.MathOperationContext):
        pass

    # Exit a parse tree produced by LexParser#mathOperation.
    def exitMathOperation(self, ctx:LexParser.MathOperationContext):
        pass


    # Enter a parse tree produced by LexParser#binaryMathOperation.
    def enterBinaryMathOperation(self, ctx:LexParser.BinaryMathOperationContext):
        pass

    # Exit a parse tree produced by LexParser#binaryMathOperation.
    def exitBinaryMathOperation(self, ctx:LexParser.BinaryMathOperationContext):
        pass


    # Enter a parse tree produced by LexParser#unaryMathOperation.
    def enterUnaryMathOperation(self, ctx:LexParser.UnaryMathOperationContext):
        pass

    # Exit a parse tree produced by LexParser#unaryMathOperation.
    def exitUnaryMathOperation(self, ctx:LexParser.UnaryMathOperationContext):
        pass


    # Enter a parse tree produced by LexParser#argument.
    def enterArgument(self, ctx:LexParser.ArgumentContext):
        pass

    # Exit a parse tree produced by LexParser#argument.
    def exitArgument(self, ctx:LexParser.ArgumentContext):
        pass



del LexParser