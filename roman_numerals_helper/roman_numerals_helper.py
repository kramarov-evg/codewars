class RomanNumerals:

    @staticmethod
    def to_roman(number):
        result = 'M' * (number//1000)
        number %= 1000
        result += 'CM' * min(number//900, 1)
        number %= 900
        result += 'D' * min(number//500, 1)
        number %= 500
        result += 'CD' * min(number//400, 1)
        number %= 400
        result += 'C' * (number//100)
        number %= 100
        result += 'XC' * min(number//90, 1)
        number %= 90
        result += 'L' * min(number//50, 1)
        number %= 50
        result += 'XL' * min(number//40, 1)
        number %= 40
        result += 'X' * (number//10)
        number %= 10
        result += 'IX' * min(number//9, 1)
        number %= 9
        result += 'V' * min(number//5, 1)
        number %= 5
        result += 'IV' * min(number//4, 1)
        number %= 4
        result += 'I' * (number//1)
        return result

    @staticmethod
    def from_roman(number):
        CM = number.count('CM')
        M = number.count('M') - CM
        CD = number.count('CD')
        D = number.count('D') - CD
        XC = number.count('XC')
        C = number.count('C') - XC - CD - CM
        XL = number.count('XL')
        L = number.count('L') - XL
        IX = number.count('IX')
        X = number.count('X') - XC - XL - IX
        IV = number.count('IV')
        V = number.count('V') - IV
        I = number.count('I') - IX - IV
        return M * 1000 + CM * 900 + CD * 400 + D * 500 +\
            XC * 90 + C * 100 + XL * 40 + L * 50 + IX * 9 +\
            X * 10 + IV * 4 + V * 5 + I
