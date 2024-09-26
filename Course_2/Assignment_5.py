# 面向对象(OOP)相关。逻辑⻔与电路。
# 使⽤OOP继承。
# 实现：与门、或门和非门

class LogicGate:

    def __int__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate " + \
                         self.getLabel() + "-->"))
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + \
                         self.getLabel() + "-->"))


class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate " + \
                         self.getLabel() + "-->"))

# 与门
class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# 或门
class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0


# 非门
class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):

        a = self.getPin()
        if a==1:
            return 0
        else:
            return 1
