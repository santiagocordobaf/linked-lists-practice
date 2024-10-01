# src/gestion_salas.py

class Node:
    __slots__ = 'sala', 'next'

    def __init__(self, sala):
        self.sala = sala
        self.next = None

    def __str__(self):
        return str(self.sala)


class Sala:
    __slots__ = 'ID', 'tipo', 'capacidad', 'nombre', 'tarifa_por_hora', 'estado'

    def __init__(self, ID, tipo, capacidad, nombre, tarifa_por_hora, estado='Disponible'):
        self.ID = ID
        self.tipo = tipo
        self.capacidad = capacidad
        self.nombre = nombre
        self.tarifa_por_hora = tarifa_por_hora
        self.estado = estado

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
