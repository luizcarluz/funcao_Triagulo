
from tipo_triangulo import*
def resposta():
    ''' 
    função para continuar verificando triangulos até usuario interromper
    '''
    resp = input('Quer ver outro tringulo? [S/N] ').upper()
    if resp not in[ 'S','N']:
        print(' Por favor, S ou N')
        resposta()
    if resp == 'S':
        return True
    if resp == 'N':
        return False
    

print('='*50)
print(f'{"Vamos Calcular triangulos":^50}')
print('='*50)

while True: # enquanto resposta for sim
    try:
        a = float(input(" Entre com o lado A: ")) # verificação do tipo
    except:
        print('Por favor somene numero')
        continue
    try:
        b = float(input(" Entre com o lado B: "))
    except:
        print('Por favor somene numero')
        continue
    try:
        c = float(input(" Entre com o lado C: "))
    except:
        print('Por favor somene numero')
        continue
    triangulo = Triangulo(a,b,c)
    if not triangulo.verifica_triangulo(): # checa condição de existencia
        print('Por favor, digite medidas válidas para um triangulo')
        continue
    print(f'Area: {triangulo.area_triangulo()}') # chama os métodos da classe
    print(f'Perimetro: {triangulo.perimetro_triangulo()}')
    print(f'Angulos: {triangulo.calcular_angulos()}')
    print(f'Tipo do triangulo: {triangulo.tipo_lado()}')
    if not resposta(): # verifica se desejar continuar
        break
