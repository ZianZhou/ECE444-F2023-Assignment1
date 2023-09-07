class utils:
    def reversed(self, num):
        reversed = 0
        if not isinstance(num, int) or num < 0:
            return -1
        while num > 0:
            reversed *= 10
            reversed += num % 10
            num //= 10
        return reversed

    def formatter(self, num):
        if not isinstance(num, int) or num < 0:
            return -1, -1
        binary = bin(num)
        octal = oct(num)
        return binary, octal
