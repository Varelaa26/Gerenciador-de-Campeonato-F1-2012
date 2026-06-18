from Classes.driver import Driver


class Round:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.results = []
        self.fast_lap = None
        self.already_happened = False

    # Alterado para receber apenas a lista de objetos dos pilotos
    def set_results(self, drivers_list):
        print(f"\nDefinindo Resultados - {self.name}\n")

        for i in range(1, 11):
            nome_piloto = input(f"Digite o nome do {i}° Colocado: ")

            piloto_encon_obj = None
            for d in drivers_list:
                if d.name == nome_piloto:
                    piloto_encon_obj = d
                    break

            if piloto_encon_obj is not None:
                piloto_encon_obj.add_result(i)
                # Guarda o objeto do piloto no histórico de resultados do GP
                self.results.append(piloto_encon_obj)
            else:
                print("Aviso: Piloto com esse nome não foi encontrado. Tente novamente para esta posição.")

        self.already_happened = True