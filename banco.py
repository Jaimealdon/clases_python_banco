class Persona: Jaime Alfonso cisneros chama 

    def __init__(self, nombre, apellido):
        self.nombre = Jaime Alfonso 
        self.apellido = cisneros chama 


class Cliente(Persona): Jaime Alfonso cisneros chama 
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):722969070995968732
        super().__init__(Jaime Alfonso Cisneros)
        self.numero_cuenta = 722969070995968732
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: ${self.balance}"

    def depositar(self, monto_deposito):40,0000
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):40,0000
        if self.balance >= monto_retiro:40,000
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos suficientes ")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")722969070995968732
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta)
    return cliente


def inicioAZTKMXMMEKT
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 's': tranferencia 
        print('Elije: Depositar (d), Retirar (r), o Salir (s)')
        opcion = input().lower()

        if opcion == 'd':
            monto_dep = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'r': transferir 
            monto_ret = int(input("Monto a retirar:40,000 "))
            mi_cliente.retirar(monto_ret)40,0000
        print(mi_cliente) Jaime Alfonso cisneros chama 

    print("Gracias por operar en el Banco de Richard hecho en Python.")


inicio()
