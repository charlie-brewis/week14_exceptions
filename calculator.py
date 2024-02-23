from tkinter import *


class Calculator:
    
    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("400x150")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack()

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result: 0")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblNum1 = Label(self.mainFrame, text="Number 1:")
        lblNum1.pack()

        entryNum1 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num1
        )
        entryNum1.pack()

        lblNum2 = Label(self.mainFrame, text="Number 2:")
        lblNum2.pack()

        entryNum2 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num2
        )
        entryNum2.pack()

        lblResult = Label(
            self.mainFrame,
            textvariable=self.result
        )
        lblResult.pack()

        btnMultiply = Button(
            self.mainFrame,
            text="Multiply",
            command=self.multiply
        )
        btnMultiply.pack(side="left")

        btnDivide = Button(
            self.mainFrame,
            text="Divide",
            command= self.divide
        )
        btnDivide.pack(side="right")

        btnClose = Button(
            self.mainFrame,
            text="Close",
            command=self.win.destroy
        )
        btnClose.pack()

    def multiply(self):
        errors = []
        try:
            num1 = self.num1.get()
        except:
            errors.append("Invalid Number for Num1")
        try:
            num2 = self.num2.get()
        except:
            errors.append("Invalid Number for Num2")
        if len(errors) == 0:
            result = num1 * num2
            self.result.set(f"Result: {result :.4f} (4 d.p.)")
        else:
            self.result.set(f"Errors: {errors}")

    def divide(self):
        errors = []
        try:
            num1 = self.num1.get()
        #TODO: specify exception type
        except:
            errors.append("Invalid Number for Num1")
        try:
            num2 = self.num2.get()
        except:
            errors.append("Invalid Number for Num2")
        if len(errors) == 0:
            result = num1 / num2
            self.result.set(f"Result: {result :.4f} (4 d.p.)")
        else:
            self.result.set(f"Errors: {errors}")


def main():
    calc = Calculator()
    calc.run()


main()