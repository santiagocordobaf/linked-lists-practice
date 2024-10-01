class Node:
    __slots__ = 'sala', 'next'

    def __init__(self, sala):
        self.sala = sala
        self.next = None

    def __str__(self):
        return str(self.sala)


class Sala:
    __slots__ = 'ID', 'tipo', 'capacidad', 'nombre', 'tarifa_por_hora', 'estado', 'reserva_detalles'

    def __init__(self, ID, tipo, capacidad, nombre, tarifa_por_hora, estado='Disponible', reserva_detalles=None):
        self.ID = ID
        self.tipo = tipo
        self.capacidad = capacidad
        self.nombre = nombre
        self.tarifa_por_hora = tarifa_por_hora
        self.estado = estado
        self.reserva_detalles = reserva_detalles

    def __str__(self):
        return f"Sala {self.nombre} ({self.tipo}) - Capacidad: {self.capacidad}, Tarifa: ${self.tarifa_por_hora}/hr, Estado: {self.estado}"


class SalaLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __iter__(self):
        curr_node = self.head
        while curr_node:
            yield curr_node.sala
            curr_node = curr_node.next

    def __str__(self):
        return ' -> '.join([str(sala) for sala in self])

    def agregar_sala(self, sala):
        new_node = Node(sala)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        self.length += 1
        print(f"Sala {sala.nombre} agregada.")

    def eliminar_sala(self, ID):
        if self.head is None:
            print("No hay salas para eliminar.")
            return False

        if self.head.sala.ID == ID:
            self.head = self.head.next
            self.length -= 1
            print(f"Sala con ID {ID} eliminada.")
            return True

        curr_node = self.head
        while curr_node.next and curr_node.next.sala.ID != ID:
            curr_node = curr_node.next

        if curr_node.next is None:
            print(f"Sala con ID {ID} no encontrada.")
            return False
        else:
            curr_node.next = curr_node.next.next
            self.length -= 1
            print(f"Sala con ID {ID} eliminada.")
            return True

    def buscar_por_tipo(self, tipo):
        if self.head is None:
            print(f"No hay salas del tipo {tipo}.")
            return
        
        curr_node = self.head
        encontrado = False
        while curr_node:
            if curr_node.sala.tipo == tipo:
                print(curr_node.sala)
                encontrado = True
            curr_node = curr_node.next

        if not encontrado:
            print(f"No se encontraron salas del tipo {tipo}.")

    def buscar_por_capacidad(self, capacidad_minima):
        if self.head is None:
            print(f"No hay salas con capacidad mínima de {capacidad_minima}.")
            return

        curr_node = self.head
        encontrado = False
        while curr_node:
            if curr_node.sala.capacidad >= capacidad_minima:
                print(curr_node.sala)
                encontrado = True
            curr_node = curr_node.next

        if not encontrado:
            print(f"No se encontraron salas con capacidad mínima de {capacidad_minima}.")

    def listar_salas_disponibles(self):
        if self.head is None:
            print("No hay salas disponibles.")
            return

        curr_node = self.head
        encontrado = False
        while curr_node:
            if curr_node.sala.estado == 'Disponible':
                print(curr_node.sala)
                encontrado = True
            curr_node = curr_node.next

        if not encontrado:
            print("No hay salas disponibles en este momento.")

    def listar_salas_reservadas(self):
        if self.head is None:
            print("No hay salas reservadas.")
            return

        curr_node = self.head
        encontrado = False
        while curr_node:
            if curr_node.sala.estado == 'Reservada':
                print(curr_node.sala)
                encontrado = True
            curr_node = curr_node.next

        if not encontrado:
            print("No hay salas reservadas en este momento.")

    def reservar_sala_por_tipo(self, tipo, reserva_detalles):
        if self.head is None:
            print(f"No hay salas disponibles para reservar de tipo {tipo}.")
            return False

        curr_node = self.head
        while curr_node:
            if curr_node.sala.tipo == tipo and curr_node.sala.estado == 'Disponible':
                curr_node.sala.estado = 'Reservada'
                curr_node.sala.reserva_detalles = reserva_detalles
                print(f"Sala {curr_node.sala.nombre} reservada exitosamente.")
                return True
            curr_node = curr_node.next

        print(f"No hay salas disponibles para reservar de tipo {tipo}.")
        return False

    def modificar_reserva(self, ID, nueva_sala_id=None, nuevos_detalles=None):
        if self.head is None:
            print(f"No hay reservas para modificar.")
            return False

        curr_node = self.head
        sala_reservada = None
        while curr_node:
            if curr_node.sala.ID == ID and curr_node.sala.estado == 'Reservada':
                sala_reservada = curr_node.sala
                break
            curr_node = curr_node.next

        if not sala_reservada:
            print(f"No se encontró una reserva con ID {ID}.")
            return False

        if nueva_sala_id:
            # Cambiar a una nueva sala
            nueva_sala = self.buscar_sala_por_id(nueva_sala_id)
            if nueva_sala and nueva_sala.estado == 'Disponible':
                nueva_sala.estado = 'Reservada'
                nueva_sala.reserva_detalles = sala_reservada.reserva_detalles
                sala_reservada.estado = 'Disponible'
                sala_reservada.reserva_detalles = None
                print(f"La reserva fue cambiada a la sala {nueva_sala.nombre}.")
            else:
                print(f"No se pudo encontrar una sala disponible con ID {nueva_sala_id}.")
                return False

        if nuevos_detalles:
            # Cambiar los detalles de la reserva
            sala_reservada.reserva_detalles = nuevos_detalles
            print(f"Los detalles de la reserva en la sala {sala_reservada.nombre} fueron actualizados.")

        return True

    def cancelar_reserva(self, ID):
        if self.head is None:
            print(f"No hay reservas para cancelar.")
            return False

        curr_node = self.head
        while curr_node:
            if curr_node.sala.ID == ID and curr_node.sala.estado == 'Reservada':
                curr_node.sala.estado = 'Disponible'
                curr_node.sala.reserva_detalles = None
                print(f"La reserva de la sala {curr_node.sala.nombre} ha sido cancelada.")
                return True
            curr_node = curr_node.next

        print(f"No se encontró una reserva con ID {ID}.")
        return False
    
    def aplicar_descuento_por_uso_prolongado(self):
        curr_node = self.head
        while curr_node:
            if curr_node.sala.estado == 'Reservada' and curr_node.sala.reserva_detalles:
                horas_reserva = curr_node.sala.reserva_detalles.get('horas', 0)
                if horas_reserva > 8:
                    tarifa_descuento = curr_node.sala.tarifa_por_hora * 0.85
                    total_con_descuento = tarifa_descuento * horas_reserva
                    print(f"Sala {curr_node.sala.nombre} tiene un descuento aplicado. Total con descuento: ${total_con_descuento:.2f}")
                else:
                    total = curr_node.sala.tarifa_por_hora * horas_reserva
                    print(f"Sala {curr_node.sala.nombre} tiene un total de ${total:.2f} sin descuento.")
            curr_node = curr_node.next

    def calcular_ingresos(self):
        ingresos_totales = 0
        curr_node = self.head
        while curr_node:
            if curr_node.sala.estado == 'Reservada' and curr_node.sala.reserva_detalles:
                horas_reserva = curr_node.sala.reserva_detalles.get('horas', 0)
                tarifa = curr_node.sala.tarifa_por_hora
                if horas_reserva > 8:
                    tarifa *= 0.85  # Aplicar descuento del 15%
                ingresos_totales += tarifa * horas_reserva
            curr_node = curr_node.next
        print(f"Ingresos totales por reservas: ${ingresos_totales:.2f}")
        return ingresos_totales

    def intercambiar_salas_en_mantenimiento(self, sala_mantenimiento_id):
        if self.head is None:
            print("No hay salas disponibles.")
            return False

        # Buscar la sala en mantenimiento
        curr_node = self.head
        sala_mantenimiento = None
        while curr_node:
            if curr_node.sala.ID == sala_mantenimiento_id and curr_node.sala.estado == 'Mantenimiento':
                sala_mantenimiento = curr_node
                break
            curr_node = curr_node.next

        if not sala_mantenimiento:
            print(f"No se encontró una sala en mantenimiento con ID {sala_mantenimiento_id}.")
            return False

        # Buscar otra sala con las mismas características
        curr_node = self.head
        while curr_node:
            if curr_node != sala_mantenimiento and curr_node.sala.capacidad == sala_mantenimiento.sala.capacidad and curr_node.sala.tipo == sala_mantenimiento.sala.tipo:
                # Intercambiar las salas
                print(f"Intercambiando la sala {sala_mantenimiento.sala.nombre} con la sala {curr_node.sala.nombre}.")
                sala_mantenimiento.sala, curr_node.sala = curr_node.sala, sala_mantenimiento.sala
                return True

        print("No se encontró una sala con las mismas características para el intercambio.")
        return False

    def reorganizar_por_capacidad(self):
        if self.head is None:
            print("No hay salas para reorganizar.")
            return

        # Convertir la lista enlazada a una lista regular para ordenarla
        nodos = []
        curr_node = self.head
        while curr_node:
            nodos.append(curr_node)
            curr_node = curr_node.next

        # Ordenar los nodos por capacidad (de mayor a menor)
        nodos.sort(key=lambda x: x.sala.capacidad, reverse=True)

        # Reconstruir la lista enlazada
        self.head = nodos[0]
        curr_node = self.head
        for i in range(1, len(nodos)):
            curr_node.next = nodos[i]
            curr_node = curr_node.next
        curr_node.next = None
        print("Las salas han sido reorganizadas por capacidad.")

    def listar_salas_reservadas_por_tipo(self, tipo):
        curr_node = self.head
        salas_reservadas = []
        while curr_node:
            if curr_node.sala.tipo == tipo and curr_node.sala.estado == 'Reservada':
                salas_reservadas.append(curr_node.sala)
            curr_node = curr_node.next

        if salas_reservadas:
            print(f"Salas reservadas del tipo {tipo}:")
            for sala in salas_reservadas:
                print(sala)
        else:
            print(f"No hay salas reservadas del tipo {tipo}.")

# Ejemplo de cómo usar el sistema de gestión de salas
if __name__ == "__main__":
    # Crear lista de salas
    lista_salas = SalaLinkedList()

    # Agregar salas
    lista_salas.agregar_sala(Sala(1, 'Pequeña', 10, 'Sala A', 100))
    lista_salas.agregar_sala(Sala(2, 'Mediana', 20, 'Sala B', 200))
    lista_salas.agregar_sala(Sala(3, 'Grande', 30, 'Sala C', 300, 'Reservada'))

    # Buscar salas por capacidad
    print("\nBuscar salas por capacidad (mínimo 15):")
    lista_salas.buscar_por_capacidad(15)

    # Listar salas disponibles
    print("\nListar salas disponibles:")
    lista_salas.listar_salas_disponibles()

    # Listar salas reservadas
    print("\nListar salas reservadas:")
    lista_salas.listar_salas_reservadas()

    # Reservar una sala
    print("\nReservar una sala tipo Mediana:")
    lista_salas.reservar_sala_por_tipo('Mediana', {'fecha': '2024-10-01', 'hora': '10:00 AM'})

    # Modificar una reserva
    print("\nModificar la reserva de la sala con ID 2:")
    lista_salas.modificar_reserva(2, nuevos_detalles={'fecha': '2024-10-02', 'hora': '11:00 AM'})

    # Cancelar una reserva
    print("\nCancelar la reserva de la sala con ID 3:")
    lista_salas.cancelar_reserva(3)

    # Aplicar descuento
    print("\nAplicar descuento por uso prolongado:")
    lista_salas.aplicar_descuento_por_uso_prolongado()

    # Calcular ingresos
    print("\nCalcular ingresos por reservas:")
    lista_salas.calcular_ingresos()

    # Intercambiar sala en mantenimiento
    print("\nIntercambiar sala en mantenimiento:")
    lista_salas.intercambiar_salas_en_mantenimiento(1)

    # Reorganizar salas por capacidad
    print("\nReorganizar salas por capacidad:")
    lista_salas.reorganizar_por_capacidad()

    # Listar salas reservadas por tipo
    print("\nListar salas reservadas de tipo Mediana:")
    lista_salas.listar_salas_reservadas_por_tipo('Mediana')