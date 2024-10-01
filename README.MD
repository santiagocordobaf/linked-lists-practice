# PRÁCTICA LISTAS ENLAZADAS

## Sistema de Gestión de Reservas de Salas de Conferencias

Eres responsable de desarrollar un sistema de gestión de reservas para las salas de 
conferencias de un edificio corporativo. El sistema debe permitir a los usuarios 
registrar, modificar y cancelar reservas de las salas, así como gestionar la 
disponibilidad de las mismas. Las salas deben estar organizadas de forma contigua 
por tipo de sala (Ejemplo: Pequeña, Mediana, Grande).

### Requisitos:

Crea una clase llamada Sala con los siguientes atributos:

- ID (identificador único)
- Tipo de sala (Ejemplo: Pequeña, Mediana, Grande)
- Capacidad máxima
- Nombre de la sala
- Tarifa por hora de uso
- Estado (Disponible/Reservada)

Cada nodo de la lista enlazada representará una sala en el edificio.

### Operaciones requeridas: 

1. Agregar una sala: Registrar una nueva sala con todos sus atributos.
2. Eliminar una sala: Eliminar una sala específica del sistema.
3. Buscar salas por tipo: Retornar todas las salas de un tipo específico 
(pequeña, mediana, grande), mostrando la información de cada una y su 
disponibilidad.
4. Buscar salas por capacidad: Permitir la búsqueda de salas que puedan 
acomodar un número específico de personas.
5. Listar salas disponibles para reserva: Mostrar todas las salas que están 
disponibles, junto con sus atributos y la tarifa por hora.
6. Listar salas reservadas: Mostrar todas las salas que están actualmente 
reservadas.
7. Reservar una sala por tipo: Permitir reservar una sala de un tipo específico.
8. Modificar una reserva: Cambiar la sala reservada o actualizar la fecha/hora 
de la reserva.
9. Cancelar una reserva: Eliminar una reserva existente, liberando la sala para 
otros usuarios.
10. Aplicar descuento por uso prolongado: Si una sala se reserva por más de 
8 horas, aplicar un 15% de descuento en la tarifa total.
11. Calcular ingresos por reservas: Calcular el total de ingresos obtenidos por 
las reservas de salas hasta el momento.
12. Intercambiar salas en mantenimiento: Permitir intercambiar una sala que 
esté en mantenimiento por otra que cumpla las mismas características 
(capacidad y tipo). Los nodos deben intercambiarse, manteniendo la posición 
en la lista enlazada.
13. Reorganizar las salas por capacidad: Permitir reorganizar las salas en la 
lista enlazada en función de su capacidad máxima, de mayor a menor.
14. Listar salas reservadas por tipo: Mostrar todas las salas reservadas de un 
tipo específico (Ejemplo: Todas las salas grandes reservadas).
