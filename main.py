import enum

class Parser:
    def __init__(self, exp: str):
        self.exp = exp
        self.pos = 0
        self.length = len(exp)
        self.ch  = self.read_ch()

    def read_ch(self) -> str|None:
        if self.pos >= self.length:
            return None

        self.ch = self.exp[self.pos]
        self.pos += 1

        return self.ch

    def parse(self) -> bool:
        if self.ch == "(":

            self.ch = self.read_ch()
            self.parse()

            if self.ch == ")":
                self.ch = self.read_ch()
                return self.parse_1()

            else: return False

        elif self.ch == "[":

            self.ch = self.read_ch()
            self.parse()

            if self.ch == "]":
                self.ch = self.read_ch()
                return self.parse_2()

            else: return False

        elif self.ch is None: return True

        else: return False

    def parse_1(self) -> bool:
        if self.ch == "[":

            self.ch = self.read_ch()
            self.parse()

            if self.ch == "]":
                self.ch = self.read_ch()
                return self.parse_2()

            else: return False

        elif self.ch is None: return True

        else: return False

    def parse_2(self) -> bool:
        if self.ch == "(":

            self.ch = self.read_ch()
            self.parse()

            if self.ch == ")":
                self.ch = self.read_ch()
                return self.parse_1()

            else: return False

        elif self.ch is None: return True

        else: return False

class States(enum.Enum):
    PRINT_PROBLEM = 0
    INPUT = 1

def main() -> None:
    state = States.PRINT_PROBLEM
    while True:
        match state:
            case States.PRINT_PROBLEM:
                print("""
                    Правильная скобочная запись с двумя видами скобок. Скобки одного вида не могут стоять рядом. \n
                    Пример:	\n
                        Правильная запись: [(()[])](()[()])[()[[]()]] \n
                        Неправильная запись [()([]([]()))] \n
                """)
                state = States.INPUT
            case States.INPUT:
                exp = input("Введите выражение: ")
                if exp == "q":
                    print("Выход")
                    break

                res = Parser(exp).parse()

                if res: print("Распознано")
                else:   print("Не распознано")

if __name__ == "__main__":
    main()
