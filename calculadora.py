class Calculadora:
      def __init__(self,numero_uno,numero_dos):
          self.numero_uno = numero_uno
          self.numero_dos = numero_dos
      def suma(self):
        return self.numero_uno + self.numero_dos
      def resta(self):
        return self.numero_uno - self.numero_dos
      def mult(self):
        return self.numero_uno * self.numero_dos
      def div(self):
        return  self.numero_dos  / self.numero_uno

numerouno = int(input("Indicame el primer numero:"))
numerodos = int(input("Indicame el segundo numero:"))
calc = Calculadora(numerouno,numerodos)
print("Elige el tipo de operacion que deseas hacer:\n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division\nsi eliges otra opcion se saldra del sistema y no me puedes dividir entre 0:")
opcion= int(input())
if(opcion == 1):
    print(f"El resultado de la suma es:{calc.suma()}")
elif(opcion == 2):
    print(f"El resultado de la resta es:{calc.resta()}")
elif(opcion == 3):
    print(f"El resultado de la multiplicacion es:{calc.mult()}")
elif(opcion == 4) and numerouno != 0:
    print(f"El resultado de la division es:{calc.div()}")
else:
    print(f"Te dije que saldria de las operaciones pero esos numeros {numerouno}  y {numerodos} son buenos numeros")