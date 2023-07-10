class Solution:
    
        
    def evalRPN(self, tokens: List[str]) -> int:
        operand=[]
        for i in tokens:
            if i.isnumeric():
                operand.append(i)
            else:
                if i == "+":
                    s=operand.pop()
                    f=operand.pop()
                    k= f+i+s
                    k=eval(k)
                elif i == "-":
                    s=operand.pop()
                    f=operand.pop()
                    k= f+i+s
                    k=eval(k)
                elif i == "*":
                    s=operand.pop()
                    f=operand.pop()
                    k= f+i+s
                    k=eval(k)
                elif i == "/":
                    s=operand.pop()
                    f=operand.pop()
                    k= f+i+s
                    k=int(eval(k))
                else:
                    k= i
                operand.append(str(k))
        return int(operand.pop())
    
    