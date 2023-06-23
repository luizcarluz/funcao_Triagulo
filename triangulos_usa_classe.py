
from tipo_triangulo import*
def resposta():
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

while True:
    try:
        a = float(input(" Entre com o lado A: "))
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
    if not triangulo.verifica_triangulo():
        print('Por favor, digite medidas válidas para um triangulo')
        continue
    print(f'Area: {triangulo.area_triangulo()}')
    print(f'Perimetro: {triangulo.perimetro_triangulo()}')
    print(f'Angulos: {triangulo.calcular_angulos()}')
    print(f'Tipo do triangulo: {triangulo.tipo_lado()}')
    if not resposta():
        break