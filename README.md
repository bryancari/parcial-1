[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7013499&assignment_repo_type=AssignmentRepo)
# Parcial I (A) Algoritmos y Programación

Universidad Metropolitana

Facultad de Ingeniería

Departamento de Gestión de Proyectos y Sistemas

Algoritmos y Programación

Prof. Luis Bello, Antonio Guerra y José Quevedo

---

## Pregunta 1

### 1.A (4 ptos)

Dada una oración, escriba una función en Python para verificar si esa oración es un Pangrama o no.

> Un pangrama es una oración que contiene todas las letras del alfabeto inglés

### 1.B (4 ptos)

Realice una función que además determine cuántas letras se repiten en la oración original (debe tomar las mayusculas y minusculas como un mismo caracter)

**Ejemplo de Input:**

```python
pangrama('El cadaver de Wamba, rey godo de Espana, fue exhumado y trasladado en una caja de zinc que peso un kilo')
```

**Output:**

```shell
A. Si es un Pangrama
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Las letras del output deben ser de la oración del pangrama

B.
{'e': 12, 'l': 3, ' ': 20, 'c': 3, 'a': 13, 'd': 8, 'v': 1, 'r': 3, 'w': 1, 'm': 2, 'b': 1, ',': 2, 'y': 2, 'g': 1, 'o': 6, 's': 3, 'p': 2, 'n': 5, 'f': 1, 'u': 5, 'x': 1, 'h': 1, 't': 1, 'j': 1, 'z': 1, 'i': 2, 'q': 1, 'k': 1}
```

---

## Pregunta 2 (12 ptos)

La empresa de transporte Expresos Saman, ofrece tres destinos diarios a ciudades del país, en vehículos de capacidad de hasta 10 pasajeros. Para cada destino hay 3 vehículos. Estos destinos han sido clasificados de la siguiente forma:

| Código |    Destino     | Precio por Pasajero |
| :----: | :------------: | :-----------------: |
|   V    |    Valencia    |         500         |
|   P    | Puerto la Cruz |         700         |
|   B    |  Barquisimeto  |         800         |

Un cliente puede adquirir un pasaje para 1 o más personas hasta un máximo de 10, por lo que se debe validar que exista disponibilidad hacia el destino solicitado.

Al momento de la compra del pasaje, se le solicita al cliente los siguientes datos:

- Cédula de Identidad
- Número de pasajeros
- Ciudad destino

Cuando el cliente solicita pasajes para más de 4 personas, se le otorga un descuento de 20% sobre el monto total a pagar.

Para cada cliente, el programa deberá desplegar la información del recibo con los siguientes datos: **5 ptos**

- El número de cédula de identidad del cliente
- Cantidad de pasajeros
- Código y nombre del destino solicitado
- Monto bruto a pagar
- Monto de descuento (si no aplica, el programa mostrará cero)
- Monto del impuesto a pagar (IVA 16% del monto bruto menos el descuento)
- Monto neto a pagar

Al final del día el programa deberá calcular: **7 ptos**

- La cantidad de clientes por destino (no pasajeros)
- El Monto Total Neto Facturado por destino
- El Monto Total de Descuentos otorgados por destino
- El Monto Total Neto Facturado por Expresos Saman
- Los datos del cliente que más dinero pagó

**Nota 1**: Al momento de la entrada de datos, el programa deberá validar si hay aún disponibilidad hacia el destino solicitado. Si no la hay deberá indicar un mensaje indicando que no hay disponibilidad hacia el destino solicitado, mostrando adicionalmente cuantos cupos quedan.

**Nota 2**: Si se venden los pasajes para todos los destinos y ya no hay más cupos, el programa deberá emitir un mensaje de que ya no hay cupos disponibles para ningún destino, dando el reporte del final del día y terminando la ejecución del programa.

**Nota 3**: Debe utilizar funciones dentro en caso de no hacerlo se le penalizará
