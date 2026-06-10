from Classes.driver import Driver
from Classes.team import Team
from Classes.round import Round

def main():
    print("\nFormula 1 2012 - Gerenciador de Campeonato\n")

    rounds_list, drivers_list, teams_list = criar_objetos()

    print("1 - Exibir Corridas")
    print("2 - Exibir Pilotos")
    print("3 - Exibir equipes\n")

    initial_input = input("Digite sua escolha: ")

    match initial_input:
        case "1":
            for r in rounds_list:
                print(f"{r.id} - {r.name}")
        case "2":
            for d in drivers_list:
                print(f"{d.num} - {d.name} - {d.team.name}")
        case "3":
            for t in teams_list:
                print(f"{t.id} - {t.name}")
        case _:
            print("Ops... Opção inválida. Vamos tentar novamente.")
            main()
def criar_objetos():
    # DADOS BRUTOS DOS TIMES
    raw_teams_data = [
        [1, "Red Bull"], [2, "McLaren"], [3, "Ferrari"], [4, "Lotus"],
        [5, "Force India"], [6, "Sauber"], [7, "Toro Rosso"], [8, "Williams"],
        [9, "Mercedes"], [10, "Caterham"], [11, "HRT"], [12, "Marussia"]
    ]

    # Criando o dicionário de objetos das equipes
    teams_dict = {}
    for data in raw_teams_data:
        # Passamos 0 para os pontos, posição e vitórias iniciais da classe Team
        team_obj = Team(id=data[0], name=data[1], points=0, position=0, wins=0)
        teams_dict[data[1]] = team_obj  # Guarda usando o nome como chave (ex: "Ferrari")

    # DADOS BRUTOS DOS PILOTOS
    raw_drivers_data = [
        [1, "Sebastian Vettel", "Red Bull"], [2, "Mark Webber", "Red Bull"],
        [3, "Jenson Button", "McLaren"], [4, "Lewis Hamilton", "McLaren"],
        [5, "Fernando Alonso", "Ferrari"], [6, "Felipe Massa", "Ferrari"],
        [7, "Kimi Räikkönen", "Lotus"], [8, "Romain Grosjean", "Lotus"],
        [9, "Bruno Senna", "Williams"], [10, "Pastor Maldonado", "Williams"],
        [11, "Nico Hülkenberg", "Force India"], [12, "Paul di Resta", "Force India"],
        [14, "Kamui Kobayashi", "Sauber"], [15, "Sergio Pérez", "Sauber"],
        [16, "Daniel Ricciardo", "Toro Rosso"], [17, "Jean-Éric Vergne", "Toro Rosso"],
        [18, "Michael Schumacher", "Mercedes"], [19, "Nico Rosberg", "Mercedes"],
        [20, "Heikki Kovalainen", "Caterham"], [21, "Vitaly Petrov", "Caterham"],
        [22, "Pedro de la Rosa", "HRT"], [23, "Narain Karthikeyan", "HRT"],
        [24, "Timo Glock", "Marussia"], [25, "Charles Pic", "Marussia"]
    ]
    rounds_raw_list = [
        [1, "Melbourne"], [2, "Kalua Lumpur"],
        [3, "Marina Bay"], [4, "Suzuka"],
        [5, "Yeongam"], [6, "Shangai"],
        [7, "New Deli"], [8, "Barcelona"],
        [9, "Monaco"], [10, "Silverstone"],
        [11, "Spa-Francorchamps"], [12, "Hockenheim"],
        [13, "Budapest"], [14, "Monza"],
        [15, "Valencia"], [16, "Montreal"],
        [17, "Austin"], [18, "São Paulo"],
        [19, "Bahrain"], [20, "Abu Dahbi"]
    ]

    # Lista que vai armazenar os objetos das corridas
    rounds_list = []

    for data in rounds_raw_list:
        round_obj = Round(data[0], data[1])
        rounds_list.append(round_obj)

    # Lista que vai armazenar os objetos dos pilotos
    drivers_list = []

    for data in raw_drivers_data:
        team_name = data[2]
        team_obj = teams_dict[team_name]

        # Instancia o piloto passando o objeto do time em 'team_object'
        driver_obj = Driver(num=data[0], name=data[1], team_object=team_obj)
        drivers_list.append(driver_obj)

    # lista que armazena os objetos das equipes
    teams_list = []

    for data in raw_teams_data:
        team_obj = teams_dict[data[1]]
        teams_list.append(team_obj)

    return rounds_list, drivers_list, teams_list

if __name__ == "__main__":
    main()
