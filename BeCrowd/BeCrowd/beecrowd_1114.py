password = '2002'
valid_pass = ''
while True:
    x = input()
    valid_pass = str(x)
    if valid_pass == password:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')
             