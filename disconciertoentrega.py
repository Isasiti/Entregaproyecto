import random

class Usuario():
    def init(self):
        self.usuarios = []
        self.reservas_palco_vip = 0
        self.reservas_entrada_normal = 0
        self.palcos_disponibles = 40
        self.entradas_normales_disponibles = 200
        self.reportes = []
        self.codigos_reserva = {}
        self.bar = crear_carrito()

    def iniciar_sistema(self):
        while True:
            print("\nBienvenido al Sistema de Reservas")
            print("1. Ingresar como Usuario")
            print("2. Ingresar como Personal")
            print("3. Ver reportes y códigos (Personal)")
            print("4. Verificar compras y dejar reporte (Usuario)")
            print("5. Salir")
            opcion = input("Ingrese su opción: ")

            if opcion == '1':
                self.ingresar_como_usuario()
            elif opcion == '2':
                self.ingresar_como_personal()
            elif opcion == '3':
                self.ver_reportes_y_codigos()
            elif opcion == '4':
                self.verificar_compras_y_dejar_reporte()
            elif opcion == '5':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def ingresar_como_usuario(self):
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        cedula = input("Ingrese su número de cédula: ")

        if edad < 18:
            print("Lo sentimos, debes ser mayor de edad para realizar una reserva.")
            return

        print(f"Bienvenido, {nombre}!")
        codigo = self.elegir_tipo_reserva(nombre)
        self.codigos_reserva[codigo] = nombre

    def elegir_tipo_reserva(self, nombre):
        print("Seleccione el tipo de reserva:")
        print("1. Palco VIP")
        print("2. Entrada Normal")
        tipo_reserva = input("Ingrese su opción: ")

        if tipo_reserva == '1':
            self.reservar_palco_vip(nombre)
        elif tipo_reserva == '2':
            self.reservar_entrada_normal(nombre)
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

    def reservar_palco_vip(self, nombre):
        if self.palcos_disponibles > 0:
            print("¡Reserva de Palco VIP exitosa!")
            self.reservas_palco_vip += 1
            self.palcos_disponibles -= 1
            self.pedir_bebidas(nombre, "VIP")
            return self.generar_codigo_unico(nombre)
        else:
            print("Lo sentimos, todos los palcos VIP están ocupados.")

    def reservar_entrada_normal(self, nombre):
        if self.entradas_normales_disponibles > 0:
            print("¡Reserva de Entrada Normal exitosa!")
            self.reservas_entrada_normal += 1
            self.entradas_normales_disponibles -= 1
            self.pedir_bebidas(nombre, "Normal")
            return self.generar_codigo_unico(nombre)
        else:
            print("Lo sentimos, no quedan entradas normales disponibles.")

    def pedir_bebidas(self, nombre, tipo_usuario):
        while True:
            self.bar.mostrar_bebidas(tipo_usuario)
            bebida = input("Seleccione una bebida del menú (o 'fin' para terminar): ")
            if bebida.lower() == 'fin':
                break
            cantidad = int(input("Ingrese la cantidad: "))
            self.bar.seleccionar_bebida(tipo_usuario, bebida, cantidad)

    def generar_codigo_unico(self, nombre):
        codigo = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3)) + str(random.randint(1, 200))
        print(f"Su código único de reserva es: {codigo}. Guarde este código para referencia.")
        return codigo
class acceder_sistema:
    def verificar_compras_y_dejar_reporte(self):
        codigo = input("Ingrese su código único de reserva: ")
        if codigo in self.codigos_reserva:
            nombre = self.codigos_reserva[codigo]
            print(f"Bienvenido de nuevo, {nombre}!")
            self.pedir_bebidas(nombre, "Normal")
            self.dejar_reporte_experiencia(nombre)
        else:
            print("Código inválido. No se encontró una reserva asociada.")

    def dejar_reporte_experiencia(self, nombre):
        reporte = input("Por favor, deje un reporte sobre su experiencia en el sistema: ")
        self.reportes.append({"nombre": nombre, "reporte": reporte})
        print("¡Gracias por su feedback!")
    def ingresar_como_personal(self):
        usuario = input("Ingrese el usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        if usuario == "isasiti" and contraseña == "mimama":
            print("Acceso como personal concedido.")
            self.ver_reportes_y_codigos()
            self.ver_bebida_mas_pedida()
        else:
            print("Usuario o contraseña incorrectos.")
class Estadisticasyreportes:
    def __init__(self, reportes, codigos_reserva, usuarios):
        self.reportes = reportes
        self.codigos_reserva = codigos_reserva
        self.usuarios = usuarios

    def ver_reportes_y_codigos(self, usuario_autorizado=False):
        if usuario_autorizado:
            print("Reportes de experiencia:")
            for idx, reporte in enumerate(self.reportes):
                print(f"{idx + 1}. Usuario: {reporte['nombre']} - Reporte: {reporte['reporte']}")

            print("\nCódigos de reserva:")
            for codigo, nombre in self.codigos_reserva.items():
                print(f"Código: {codigo} - Usuario: {nombre}")
        else:
            print("Acceso denegado. Se requieren permisos de personal autorizado.")
    def determinar_bebida_mas_pedida(self, usuario_autorizado=False):
        if usuario_autorizado:
            bebidas_seleccionadas = []
            for nombre, bebidas in self.usuarios.items():
                for bebida, cantidad in bebidas.items():
                    bebidas_seleccionadas.extend([bebida] * cantidad)

            if bebidas_seleccionadas:
                from collections import Counter
                contador_bebidas = Counter(bebidas_seleccionadas)
                bebida_mas_pedida = contador_bebidas.most_common(1)[0][0]
                print(f"La bebida más pedida por los usuarios es: {bebida_mas_pedida}")
            else:
                print("No hay suficientes datos para determinar la bebida más pedida.")
        else:
            print("Acceso denegado. Se requieren permisos de personal autorizado.")
class crear_carrito:
    def __init__(self):
        self.bebidas = {
            "alcoholicas": [
                {"nombre": "Cerveza", "precio": 5000},
                {"nombre": "Vino tinto", "precio": 10000},
                {"nombre": "Ron", "precio": 80000},
                {"nombre": "Whisky", "precio": 120000},
                {"nombre": "Gin Tónico", "precio": 70000}
            ],
            "no_alcoholicas": [
                {"nombre": "Agua", "precio": 1000},
                {"nombre": "Refresco de cola", "precio": 3000},
                {"nombre": "Jugo de naranja", "precio": 2000},
                {"nombre": "Limonada", "precio": 2500},
                {"nombre": "Té helado", "precio": 2000}
            ]
        }
    def mostrar_bebidas(self, tipo_usuario):
        print("Bebidas disponibles:")
        for categoria in self.bebidas:
            print(f"{categoria.capitalize()}:")
            for bebida in self.bebidas[categoria]:
                precio = bebida["precio"]
                if tipo_usuario == "VIP":
                    precio *= 0.75  # Aplicar descuento del 25% para usuarios VIP
                print(f"{bebida['nombre']} - ${precio / 1000:.2f}K")

    def seleccionar_bebida(self, tipo_usuario, bebida, cantidad):
        for categoria in self.bebidas:
            for b in self.bebidas[categoria]:
                if bebida == b["nombre"]:
                    precio = b["precio"]
                    if tipo_usuario == "VIP":
                        precio *= 0.75  # Aplicar descuento del 25% para usuarios VIP
                    total = precio * cantidad
                    print(f"{cantidad} {bebida} seleccionada(s) - Total: ${total / 1000:.2f}K")
                    return
        print(f"{bebida} no está en el menú")
sistema = Usuario()
sistema.iniciar_sistema()