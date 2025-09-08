from parser.CalculatorParser import CalculatorParser
from parser.CalculatorListener import CalculatorListener
class EvaluationListener(CalculatorListener):
    def __init__(self):
        self.stack = []

    def exitNumber(self, ctx: CalculatorParser.NumberContext):
        # Push the number onto the stack
        print("exitNumber")
        number = int(ctx.getText())
        self.stack.append(number)
        print(f" Pushed {number}")

    def exitParentheses(self, ctx: CalculatorParser.ParenthesesContext):
        # Evaluate the expression inside the parentheses
        pass  # No action needed; the result will be handled in the parent operation

    def exitMultiplication(self, ctx: CalculatorParser.MultiplicationContext):
        print("exitMultiplication")
        right = self.stack.pop()
        left = self.stack.pop()
        result = left * right
        self.stack.append(result)
        print(f" Pop {right}")
        print(f" Pop {left}")
        print(f" Push {result}")

    def exitDivision(self, ctx: CalculatorParser.DivisionContext):
        print("exitDivision")   
        right = self.stack.pop()
        left = self.stack.pop()
        result = left / right
        self.stack.append(result)
       
        print(f" Pop {right}")
        print(f" Pop {left}")
        print(f" Push {result}")

    def exitAddition(self, ctx: CalculatorParser.AdditionContext):
        print("exitAddition")
        right = self.stack.pop()
        left = self.stack.pop()
        result = left + right
        self.stack.append(result)
        print(f" Pop {right}")
        print(f" Pop {left}")
        print(f" Push {result}")

    def exitSubtraction(self, ctx: CalculatorParser.SubtractionContext):
        print("exitSubtraction")
        right = self.stack.pop()
        left = self.stack.pop()
        result = left - right
        self.stack.append(result)
        print(f" Pop {right}")
        print(f" Pop {left}")
        print(f" Push {result}")
     # Exit a parse tree produced by CalculatorParser#Parentheses.
    def exitParentheses(self, ctx:CalculatorParser.ParenthesesContext):
        print("exitParentheses")

    def getResult(self):
        # The final result will be the last item on the stack
        return self.stack.pop() if self.stack else None