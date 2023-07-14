# TEE RATKAISUSI TÄHÄN:
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
        
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        games_list = super().list_games()
        new_lst = []
        for game in games_list:
            if game.year < 1990:
                new_lst.append(game)
        return new_lst