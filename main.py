from Classes.driver import Driver


def main():
    print("\nFormula 1 2012 - Gerenciador de Campeonato\n")

    # Lista com os dados brutos dos pilotos
    raw_drivers_data = [
        [1, "Sebastian Vettel", "Red Bull"],
        [2, "Mark Webber", "Red Bull"],
        [3, "Jenson Button", "McLaren"],
        [4, "Lewis Hamilton", "McLaren"],
        [5, "Fernando Alonso", "Ferrari"],
        [6, "Felipe Massa", "Ferrari"],
        [7, "Kimi Räikkönen", "Lotus"],
        [8, "Romain Grosjean", "Lotus"],
        [9, "Bruno Senna", "Williams"],
        [10, "Pastor Maldonado", "Williams"],
        [11, "Nico Hülkenberg", "Force India"],
        [12, "Paul di Resta", "Force India"],
        [14, "Kamui Kobayashi", "Sauber"],
        [15, "Sergio Pérez", "Sauber"],
        [16, "Daniel Ricciardo", "Toro Rosso"],
        [17, "Jean-Éric Vergne", "Toro Rosso"],
        [18, "Michael Schumacher", "Mercedes"],
        [19, "Nico Rosberg", "Mercedes"],
        [20, "Heikki Kovalainen", "Caterham"],
        [21, "Vitaly Petrov", "Caterham"],
        [22, "Pedro de la Rosa", "HRT"],
        [23, "Narain Karthikeyan", "HRT"],
        [24, "Timo Glock", "Marussia"],
        [25, "Charles Pic", "Marussia"]
    ]

    # Lista que vai armazenar os objetos instanciados
    drivers_list = []

    for data in raw_drivers_data:
        # Criando o objeto usando 'num'
        driver_obj = Driver(num=data[0], name=data[1], team=data[2])
        drivers_list.append(driver_obj)

    # Buscar um piloto específico pelo número dele
    search_num = 13
    found_driver = None

    for driver in drivers_list:
        if driver.num == search_num:
            found_driver = driver
            break  # Encontrou, interrompe o laço

    # Executa ações caso o piloto tenha sido encontrado
    if found_driver:
        print(f"Piloto selecionado: {found_driver.name} ({found_driver.team})")
        print(f"Vitórias antigas: {found_driver.wins}")

        found_driver.add_win()

        print(f"{found_driver.name} - {found_driver.wins} Vitórias")
    else:
        print("Piloto não encontrado.")


if __name__ == "__main__":
    main()