"""
## Pregunta 2

La empresa de transporte Expresos Saman, ofrece tres destinos diarios a ciudades del país, en vehículos de capacidad de hasta 10 pasajeros. Para cada destino hay 3 vehículos. Estos destinos han sido clasificados de la siguiente forma:

| Codigo |    Destino     | Precio por Pasajero |
| :----: | :------------: | :-----------------: |
|   V    |    Valencia    |         500         |
|   P    | Puerto la Cruz |         700         |
|   B    |  Barquisimeto  |         800         |

Un cliente puede adquirir un pasaje para 1 o más personas hasta un máximo de 10, por lo que se debe validar que exista disponibilidad hacia el destino solicitado.

Al momento de la compra del pasaje, se le solicita al cliente los siguientes datos:

- Cédula de Identidad,
- Número de pasajeros,
- Ciudad destino.

Cuando el cliente solicita pasajes para más de 4 personas, se le otorga un descuento de 20% sobre el monto total a pagar.

Para cada cliente, el programa deberá desplegar la información del recibo con los siguientes datos:

- El número de cédula de identidad del cliente
- Cantidad de pasajeros
- Código y nombre del destino solicitado
- Monto bruto a pagar
- Monto de descuento (si no aplica, el programa mostrará cero)
- Monto del impuesto a pagar (IVA 16% del monto bruto menos el descuento)
- Monto neto a pagar

Al final del día el programa deberá calcular:

- La cantidad de clientes por destino (no pasajeros)
- El Monto Total Neto Facturado por destino
- El Monto Total de Descuentos otorgados por destino
- El Monto Total Neto Facturado por Expresos Saman
- Los datos del cliente que más dinero pagó

**Nota 1**: Al momento de la entrada de datos, el programa deberá validar si hay aún disponibilidad hacia el destino solicitado. Si no la hay deberá indicar un mensaje indicando que no hay disponibilidad hacia el destino solicitado, mostrando adicionalmente cuantos cupos quedan.

**Nota 2**: Si se venden los pasajes para todos los destinos y ya no hay más cupos, el programa deberá emitir un mensaje de que ya no hay cupos disponibles para ningún destino, dando el reporte del final del día y terminando la ejecución del programa.
"""

def buy_tickets():
  v_bus_1 = []
  v_bus_2 = []
  v_bus_3 = []
  p_bus_1 = []
  p_bus_2 = []
  p_bus_3 = []
  b_bus_1 = []
  b_bus_2 = []
  b_bus_3 = []
  clients = []
  print('''¿En qué destino está interesado? 
  1 para valencia 
  2 para Puerto La Cruz
  3 para Barquisimeto''')
  ask = input('Ingrese su acción: ')
  while not ask.isnumeric() or 1 < int(ask) > 3: 
    ask = input('Valor inválido, intente nuevamente: ')
  if ask == '1':
    if len(v_bus_1) < 10:
      ci = input('Ingrese su cédula: ')
      destino = input('Ingrese su destino: ').lower()
      disponibles = 10-v_bus_1.count('1')
      print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
      print('¿Cuántos boletos desea llevar?')
      compra = input('Ingrese la cantidad: ')
      while not compra.isnumeric() or int(compra) > disponibles: 
        compra = input('Valor invalido, intente nuevamente: ')
      for i in range(1, int(compra)+1):
        v_bus_1.append('1')
        clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino,'bus': v_bus_1})
        return clients
    if len(v_bus_1) == 10:
      print('No hay boletos disponibles en el primer viaje') 
      
      if len(v_bus_2) < 10:
        ci = input('Ingrese su cédula: ')
        destino = input('Ingrese su destino: ').lower()
        disponibles = 10-v_bus_2.count('1')
        print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
        print('¿Cuántos boletos desea llevar?')
        compra = input('Ingrese la cantidad: ')
        while not compra.isnumeric() or int(compra) > disponibles: 
          compra = input('Valor invalido, intente nuevamente: ')
        for i in range(1, int(compra)+1):
          v_bus_2.append('1')
          clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': v_bus_2})
          return clients 
      if len(v_bus_2) == 10:
        print('No hay boletos disponibles en el segundo viaje')
        
        if len(v_bus_3) < 10:
          ci = input('Ingrese su cédula: ')
          destino = input('Ingrese su destino: ').lower()
          disponibles = 10-v_bus_3.count('1')
          print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
          print('¿Cuántos boletos desea llevar?')
          compra = input('Ingrese la cantidad: ')
          while not compra.isnumeric() or int(compra) > disponibles: 
            compra = input('Valor invalido, intente nuevamente: ')
          for i in range(1, int(compra)+1):
            v_bus_3.append('1')
            clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': v_bus_3})
            return clients 
        if len(v_bus_3) == 10:
          print('No hay boletos disponibles en ningún viaje viaje')
          
          if len(v_bus_1) == 1 and len(v_bus_2) == 10 and len(v_bus_3) == 10:
            print('Ya no hay ningún boleto disponible en ningún viaje') 
  
  if ask == '2':
    if len(p_bus_1) < 10:
      ci = input('Ingrese su cédula: ')
      destino = input('Ingrese su destino: ').lower()
      disponibles = 10-p_bus_1.count('1')
      print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
      print('¿Cuántos boletos desea llevar?')
      compra = input('Ingrese la cantidad: ')
      while not compra.isnumeric() or int(compra) > disponibles: 
        compra = input('Valor invalido, intente nuevamente: ')
      for i in range(1, int(compra)+1):
        p_bus_1.append('1')
        clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': p_bus_1})
        return clients
    if len(p_bus_1) == 10:
      print('No hay boletos disponibles en el primer viaje') 
      
      if len(p_bus_2) < 10:
        ci = input('Ingrese su cédula: ')
        destino = input('Ingrese su destino: ').lower()
        disponibles = 10-p_bus_2.count('1')
        print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
        print('¿Cuántos boletos desea llevar?')
        compra = input('Ingrese la cantidad: ')
        while not compra.isnumeric() or int(compra) > disponibles: 
          compra = input('Valor invalido, intente nuevamente: ')
        for i in range(1, int(compra)+1):
          p_bus_2.append('1')
          clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': p_bus_2})
          return clients 
      if len(p_bus_2) == 10:
        print('No hay boletos disponibles en el segundo viaje')
        
        if len(p_bus_3) < 10:
          ci = input('Ingrese su cédula: ')
          destino = input('Ingrese su destino: ').lower()
          disponibles = 10-p_bus_3.count('1')
          print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
          print('¿Cuántos boletos desea llevar?')
          compra = input('Ingrese la cantidad: ')
          while not compra.isnumeric() or int(compra) > disponibles: 
            compra = input('Valor invalido, intente nuevamente: ')
          for i in range(1, int(compra)+1):
            p_bus_3.append('1')
            clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': p_bus_3})
            return clients 
        if len(p_bus_3) == 10:
          print('No hay boletos disponibles en ningún viaje viaje')
          
          if len(p_bus_1) == 1 and len(p_bus_2) == 10 and len(p_bus_3) == 10:
            print('Ya no hay ningún boleto disponible en ningún viaje') 

  if ask == '3':
    if len(b_bus_1) < 10:
      ci = input('Ingrese su cédula: ')
      destino = input('Ingrese su destino: ').lower()
      disponibles = 10-b_bus_1.count('1')
      print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
      print('¿Cuántos boletos desea llevar?')
      compra = input('Ingrese la cantidad: ')
      while not compra.isnumeric() or int(compra) > disponibles: 
        compra = input('Valor invalido, intente nuevamente: ')
      for i in range(1, int(compra)+1):
        b_bus_1.append('1')
        clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': b_bus_1})
        return clients
    if len(b_bus_1) == 10:
      print('No hay boletos disponibles en el primer viaje') 
      
      if len(b_bus_2) < 10:
        ci = input('Ingrese su cédula: ')
        destino = input('Ingrese su destino: ').lower()
        disponibles = 10-b_bus_2.count('1')
        print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
        print('¿Cuántos boletos desea llevar?')
        compra = input('Ingrese la cantidad: ')
        while not compra.isnumeric() or int(compra) > disponibles: 
          compra = input('Valor invalido, intente nuevamente: ')
        for i in range(1, int(compra)+1):
          b_bus_2.append('1')
          clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': b_bus_2})
          return clients 
      if len(b_bus_2) == 10:
        print('No hay boletos disponibles en el segundo viaje')
        
        if len(b_bus_3) < 10:
          ci = input('Ingrese su cédula: ')
          destino = input('Ingrese su destino: ').lower()
          disponibles = 10-b_bus_3.count('1')
          print(f'Quedan {disponibles} boletos disponibles en el primer viaje')
          print('¿Cuántos boletos desea llevar?')
          compra = input('Ingrese la cantidad: ')
          while not compra.isnumeric() or int(compra) > disponibles: 
            compra = input('Valor invalido, intente nuevamente: ')
          for i in range(1, int(compra)+1):
            b_bus_3.append('1')
            clients.append({'client': 1, 'cedula': ci, 'compra': compra, 'destino':  destino, 'bus': b_bus_3})
            return clients 
        if len(b_bus_3) == 10:
          print('No hay boletos disponibles en ningún viaje viaje')
          
          if len(b_bus_1) == 1 and len(b_bus_2) == 10 and len(b_bus_3) == 10:
            print('Ya no hay ningún boleto disponible en ningún viaje') 

def factura_subtotal(clients):
  price_valencia =  500
  price_puerto = 700
  price_barquisimeto = 800
  subtotal = 0
  for i in clients:
    for i in compra.value():
      if clients['bus'] == v_bus_1 or clients['bus'] == v_bus_2 or clients['bus'] == v_bus_3:
        price
  
    
    
    
              
def main():
  pass
