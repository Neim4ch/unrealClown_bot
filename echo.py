class echoGame:
    def __init__(self):
        self.echoFlag = False

    def echo_func(self, arg):
            if (arg == 'on'): self.echoFlag = True
            elif (arg == 'off'): self.echoFlag = False
            return self.echoFlag
