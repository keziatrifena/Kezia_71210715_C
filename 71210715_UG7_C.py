class PrefixConverter:
    def __init__(self):
        self.stackList = ['?']

    # method untuk menambahkan data baru
    def push(self,data):
        self.stackList.append(data)

    # method untuk melihat data paling atas
    def peek(self):
        if self.stackList:
            return self.stackList[-1]
        else:
            return "Isi Stack Kosong"

    # method untuk menghapus data palin atas
    def pop(self):
        if self.stackList:
            data = self.stackList.pop(-1)
            return data
        else:
            return "Isi Stack Kosong"
    
    def cekValidExpression(self,expression):
        if self.stackList == str or self.stackList == "()" :
            print("Ekspresi Infix yang anda masukkan tidak valid !!")
        

    def infixToPrefix(self,expression):
        operand = []
        operator = []
        stack = PrefixConverter()
        stack.push(')')
        for i in range(len(expression)):
            if expression[i] == "-" or expression[i] == "+" or expression[i] == "*" or expression[i] == "/":
                stack.push(expression[i])
                if expression[i] == "/" or expression[i] == "*":
                    stack.push(expression[i])
                elif (expression[i]) != str:
                    stack.push(expression[i][-1])
        return (i)
            
   
if __name__ == '__main__':
    expresi1 = PrefixConverter()
    print(expresi1.infixToPrefix("1+2+3*4/2-1"))
    print(expresi1.infixToPrefix("A * (B + C) / D"))
    print(expresi1.infixToPrefix("(1+2)*3"))
    print(expresi1.infixToPrefix("20 * 3 - 10 + 289"))
    print(expresi1.infixToPrefix("100 * 30 / 600 - 30 + 100 * 777"))