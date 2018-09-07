class PrintOddNumber:  
    def __init__(self):
            self.word=""
    def enter_input(self):
        self.word =input("Enter a String: ")
        
    def print_odd_index(self):
        output = self.word[1::2]
        print(output)

    test = PrintOddNumber()
    test.enter_input()
    test.print_odd_index()
        