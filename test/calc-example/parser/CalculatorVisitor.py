# Generated from ../Calculator.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#Multiplication.
    def visitMultiplication(self, ctx:CalculatorParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Addition.
    def visitAddition(self, ctx:CalculatorParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Subtraction.
    def visitSubtraction(self, ctx:CalculatorParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Number.
    def visitNumber(self, ctx:CalculatorParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Division.
    def visitDivision(self, ctx:CalculatorParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Parentheses.
    def visitParentheses(self, ctx:CalculatorParser.ParenthesesContext):
        return self.visitChildren(ctx)



del CalculatorParser