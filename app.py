from equipomicro.model.equipo import Equipo
from equipomicro.view.ui_console import Console


if __name__ == "__main__":
    # Test data
    data = [(10, "Ronaldo", 3, 1, 0), (7, "Messi", 5, 2, 1), (12, "Pibe", 1, 1, 1),
            (2, "Zlatan", 3, 3, 3), (22, "Ospina", 0, 1, 0)]
    team: Equipo = Equipo()
    for d in data:
        team.agregar_jugador(d[0], d[1])
        team.registrar_goles(d[0], d[2])
        team.registrar_tarjetas_amarillas(d[0], d[3])
        team.registrar_tarjetas_rojas(d[0], d[4])

    ui: Console = Console(team)
    ui.app_loop()
