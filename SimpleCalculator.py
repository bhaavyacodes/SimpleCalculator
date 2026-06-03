expression = input("Enter expression: ")

try:
    print(eval(expression))

except ZeroDivisionError:
    print("Invalid Expression: Division by Zero")
    
except Exception:
    print("Invalid Expression")