from prettytable import PrettyTable

table = PrettyTable()
table.add_column("PokemonName", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)
table.align = "l"
print(table)