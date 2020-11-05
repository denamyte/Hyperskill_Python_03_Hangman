def div_by_0(operand):
    return "Division by 0!" if operand == 0 else None


fundic = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: div_by_0(b) or a / b,
    '*': lambda a, b: a * b,
    'mod': lambda a, b: div_by_0(b) or a % b,
    'pow': lambda a, b: a ** b,
    'div': lambda a, b: div_by_0(b) or a // b
}
num1, num2, operation = float(input()), float(input()), input()

operation in fundic and print(fundic[operation](num1, num2))
