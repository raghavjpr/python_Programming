class Banking:
    
    
    def Check(self):
        try:
            file = open('bank.bin','rb')
            while True:
                t = load(file)
        except FileNotFoundError:
            self.a_no = 654321000123
        except EOFError:
            self.a_no = t.a_no + 1
            file.close()

    def Create():
        self.Check()
        file = open('bank.bin','ab+')
