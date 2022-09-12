from random import randint


class Calculate:
    
    def __init__(self: object, level: int, /) -> None:
        self.__level: int = level
        self.__value1: int = self._make_value
        self.__value2: int = self._make_value
        self.__operation: int = randint(1, 3)  # 1 = sum, 2 = subtract, 3 = multiply
        self.__result: int = self._make_result

    @property
    def level(self: object) -> int:
        return self.__level
        
    @property
    def value1(self: object) -> int:
        return self.__value1
    
    @property
    def value2(self: object) -> int:
        return self.__value2
    
    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result
    
    
    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Sum'
        elif self.operation == 2:
            op = 'Subtract'
        elif self.operation == 3:
            op = 'Multiply'
        else:
            op = 'Unknown Operation'
        return f'Value 1: {self.value1} \nValue 2: {self.value2} \nLevel: {self.level} \nOperation: {op}'

    @property
    def _make_value(self: object) -> int:
        if self.level == 1:
            return randint(0, 10)
        elif self.level == 2:
            return randint(0, 100)
        elif self.level == 3:
            return randint(0, 1000)
        elif self.level == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def _make_result(self: object) -> int:
        if self.operation == 1:
            return self.value1 + self.value2
        elif self.operation == 2:
            return self.value1 - self.value2
        else:
            return self.value1 * self.value2

    @property
    def _op_simbol(self: object) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'
    
    def check_result(self: object, answer: int) -> bool:
        ok: bool = False

        if self.result == answer:
            print('uHUhuhuuhh! Right Answer!')
            ok = True
        else:
            print('Wrong Answer!')
        print(f'{self.value1} {self._op_simbol} {self.value2} = {self.result}')
        return ok

    def show_operation(self: object) -> None:
        print(f'{self.value1} {self._op_simbol} {self.value2} = ?')