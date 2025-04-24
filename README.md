# Clases
## Persona:

- Es la clase base que define los atributos básicos de una persona: nombre y apellido.
- Sirve como punto de partida para heredar estos atributos a otras clases más específicas.
## Cliente:

- Hereda de la clase Persona y agrega atributos específicos de un cliente bancario: número de cuenta y balance.
- Define los métodos para realizar depósitos y retiros, así como un método especial __str__ para imprimir de forma legible la información del cliente.

# Funciones
- crear_cliente():
 Solicita al usuario los datos necesarios para crear un nuevo objeto de tipo Cliente y lo retorna.
- inicio():
Es la función principal que controla el flujo del programa.
Crea un objeto de tipo Cliente, presenta un menú al usuario para realizar operaciones bancarias, y actualiza el balance en consecuencia.

# Explicación Detallada
## Creación de Objetos:

- Se crean objetos de tipo Cliente utilizando el constructor que recibe el nombre, apellido, número de cuenta y un balance inicial opcional.
La herencia permite reutilizar el código de la clase Persona para los atributos nombre y apellido.
## Métodos:

- depositar(): Incrementa el balance del cliente en el monto especificado.
- retirar(): Disminuye el balance del cliente en el monto especificado, siempre y cuando haya suficientes fondos.
- str(): Formatea la información del cliente en una cadena de texto legible para su impresión.
## Interacción con el Usuario:

- La función inicio() proporciona una interfaz de línea de comandos simple para que el usuario interactúe con el sistema.
- El usuario puede realizar depósitos y retiros, y el programa muestra el balance actualizado después de cada operación.

# Ejemplo de Uso
Al ejecutar este código, el programa solicitará al usuario que ingrese sus datos personales y el número de cuenta. Luego, presentará un menú para realizar operaciones bancarias. Por ejemplo:
```
Ingrese su nombre: Jaime Alfonso 
Ingrese su apellido: cisneros chama 
Ingrese su numero de cuenta: 722969070995968732
Cliente: Jaime Alfonso cisneros 
Balance de cuenta 722969070995968732: $100000
Elije: Depositar (d), Retirar (r), o Salir (s)
>> r
Monto a depositar: 320000
Deposito aceptado
Cliente: Jaime Alfonso cisneros chama 
Balance de cuenta 12345: $320000
```
