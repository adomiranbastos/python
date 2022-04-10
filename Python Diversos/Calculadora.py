from functools import reduce

entrada = ''

def pega_inputs():
    entrada = input("Por favor digite o calculo que deseja fazer:\n")
    print(calc(str(entrada)))
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calc(expr):
    if is_number(expr):
        return float(expr)    
    arr = expr.split('+')
    if len(arr) > 1:
        return sum(map(calc, arr))
    arr = expr.split('-')
    if len(arr) > 1:
        return reduce(lambda x,y: x-y, map(calc, arr))
    arr = expr.split('*')
    if len(arr) > 1:
        return reduce(lambda x,y: x*y, map(calc, arr), 1)
    arr = expr.split('/')
    if len(arr) > 1:
        return reduce(lambda x,y: x/y, map(calc, arr))
    
def menu():
    mop = input("Selecione a opção desejada\n\n1 - Calcular\n2 - Sair\n\n Opção: ")
    if(mop == '1'):
        pega_inputs()
    else:
        quit()

if __name__ == "__main__":
    menu()