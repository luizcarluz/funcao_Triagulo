class Triangulo:
    ''' retorna caracteristiscas de um triangulo
    '''
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def verifica_triangulo(self): # condição de existencia
        if self.a + self.b > self.c and self.b + self.c > self.a \
           and self.c + self.a > self.b:# Verifica se é um triangulo
            return True
        else:
            return False


    def perimetro_triangulo(self): # retorna o perimetro
        return (self.a + self.b + self.c)
    
    def triangulo_retangulo(self): # verifica se é triangulo retangulo    
        
        if self.c > self.a and self.c > self.b and self.c ** 2 == self.a ** 2 + self.b ** 2:
            return True
        if self.a > self.b and self.a > self.c and self.a ** 2 == self.b ** 2 + self.c ** 2:
            return True
    

    def tipo_lado(self): # verifica tipo do triangulo
        if (self.a == self.b) and (self.b == self.c):
            return "equilátero"
        elif (self.a == self.b) or (self.b == self.c) or (self.a == self.c):
            return "isósceles"
        else :
            if Triangulo.triangulo_retangulo(self):
            
                return "Escaleno e triagulo retangulo"
            else:
                return "Escaleno"
        
    
    def area_triangulo(self): # Usa formula de heron para a area
        import math
        p = (self.a + self.b + self.c)/2
        x = p*(p - self.a)*(p - self.b)*(p - self.c)
        area = math.sqrt(x)
        return round(area,4)

      
        
    def calcular_angulos(self):
        # Calcula os ângulos do triângulo
        import math
        # Usando a lei dos cossenos para encontrar o ângulo oposto ao lado c
        cos_A = (self.b**2 + self.c**2 - self.a**2) / (2 * self.b * self.c)
        rad_A = math.acos(cos_A)
        angulo_A = math.degrees(rad_A)
        
        # Usando a lei dos cossenos para encontrar o ângulo oposto ao lado a
        cos_B = (self.c**2 + self.a**2 - self.b**2) / (2 * self.c * self.a)
        rad_B = math.acos(cos_B)
        angulo_B = math.degrees(rad_B)
        
        # O ângulo C será a diferença entre 180° e a soma dos outros dois ângulos
        angulo_C = 180 - angulo_A - angulo_B
        
        return f'{angulo_A:.2f}, {angulo_B:.2f}, {angulo_C:.2f}'


