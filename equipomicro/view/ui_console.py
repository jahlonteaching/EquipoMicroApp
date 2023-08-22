from equipomicro.model.equipo import Equipo

ENTER_NUMBER = "Ingrese el número: "


class Console:

    def __init__(self, equipo: Equipo):
        self.equipo: Equipo = equipo

    @staticmethod
    def show_welcome_msg():
        print(f"{'=':=^40}")
        print(f"{' BIENVENIDO A LA APP DEL EQUIPO ':=^40}")
        print(f"{'=':=^40}")

    @staticmethod
    def show_menu():
        print("\nOPCIONES:")
        print("1. Lista de jugadores")
        print("2. Agregar jugador")
        print("3. Registrar goles")
        print("4. Registrar tarjetas amarillas")
        print("5. Registrar tarjetas rojas")
        print("6. Ver jugadores con más tarjetas que goles")
        print("7. Ver jugadores con más tarjetas rojas que umbral")
        print("8. Informe de jugadores")
        option = int(input("Ingrese una opción: "))
        while option not in range(1, 9):
            print(">>> ERROR: opción inválida. Intente nuevamente")
            option = int(input("Ingrese una opción: "))
        return option

    def app_loop(self):
        Console.show_welcome_msg()
        end_app: bool = False
        while not end_app:
            option: int = Console.show_menu()
            end_app = self.process_user_option(option)

    def process_user_option(self, option: int) -> bool:
        if option == 1:
            self.list_players()
        if option == 2:
            self.add_new_player()
        elif option == 3:
            self.register_goals()
        elif option == 4:
            self.register_yellow_cards()
        elif option == 5:
            self.register_red_cards()
        elif option == 6:
            self.show_players_with_more_cards_than_goals()
        elif option == 7:
            self.show_players_with_more_red_cards_than_threshold()
        elif option == 8:
            self.show_team_report()
        elif option == 9:
            self.exit_app()
            return True

        return False

    def list_players(self):
        print(f"\n{' LISTA DE JUGADORES ':=^40}")
        for player in self.equipo.jugadores.values():
            print(f"> {player.numero} - {player.nombre}")

    def add_new_player(self):
        print(f"\n{' AGREGAR JUGADOR ':=^40}")
        numero: int = int(input(ENTER_NUMBER))
        nombre: str = input("Ingrese el nombre: ")
        jugador = self.equipo.agregar_jugador(numero, nombre)
        if jugador is not None:
            print(f"El jugador {numero} - {nombre} se agregó exitosamente")
        else:
            print(f">>> ERROR: Ya existe un jugador con el número {numero}")

    def register_goals(self):
        print(f"\n{' REGISTRAR GOLES ':=^40}")
        numero: int = int(input(ENTER_NUMBER))
        goles: int = int(input("Ingrese la cantidad de goles: "))
        if self.equipo.registrar_goles(numero, goles):
            print("Goles registrados exitosamente")
        else:
            print(f">>> ERROR: No existe un jugador con el número {numero}")

    def register_yellow_cards(self):
        print(f"\n{' REGISTRAR TARJETAS AMARILLAS ':=^40}")
        numero: int = int(input(ENTER_NUMBER))
        tarjetas_amarillas: int = int(input("Ingrese la cantidad de tarjetas amarillas: "))
        if self.equipo.registrar_tarjetas_amarillas(numero, tarjetas_amarillas):
            print("Tarjetas amarillas registradas exitosamente")
        else:
            print(f">>> ERROR: No existe un jugador con el número {numero}")

    def register_red_cards(self):
        print(f"\n{' REGISTRAR TARJETAS ROJAS ':=^40}")
        numero: int = int(input(ENTER_NUMBER))
        tarjetas_rojas: int = int(input("Ingrese la cantidad de tarjetas rojas: "))
        if self.equipo.registrar_tarjetas_rojas(numero, tarjetas_rojas):
            print("Tarjetas amarillas registradas exitosamente")
        else:
            print(f">>> ERROR: No existe un jugador con el número {numero}")

    def show_players_with_more_cards_than_goals(self):
        print(f"\n{' JUGADORES CON MAS TARJETAS QUE GOLES ':=^40}")
        players = self.equipo.jugadores_con_mas_tarjetas_que_goles()
        for player in players:
            print(player)
            print(f"{'_':_^30}")

    def show_players_with_more_red_cards_than_threshold(self):
        print(f"\n{' JUGADORES CON MAS ROJAS QUE UMBRAL ':=^40}")
        threshold: int = int(input("Ingrese el umbral de rojas: "))
        players = self.equipo.jugadores_con_mas_rojas_que(threshold)
        for player in players:
            print(player)
            print(f"{'_':_^30}")

    def show_team_report(self):
        print(f"\n{' INFORME DEL EQUIPO ':=^40}")
        report = self.equipo.informe_jugadores()
        for num, value in report.items():
            print(f"Player number {num} -> {value}")

    @staticmethod
    def exit_app():
        print(f"{'=':=^40}")
        print(f"{' FIN DE LA APLICACIÓN ':=^40}")
        print(f"{'=':=^40}")
