class Mashina:
    def __init__(self, rang, model,tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
gentra = Mashina("qora", "gentra", 200)
damas = Mashina("oq", "damas 1-2", 120)
bmw = Mashina("sariq", "damas M5")

print(f"Gentraning rangi: {gentra.rang}")
print(f"Gentraning rangi: {gentra.model}")
print(f"Gentraning rangi: {gentra.tezlik}")
print("-" *25)
print(f"Damasning rangi: {damas.rang}")
print(f"Damasning rangi: {damas.model}")
print(f"Damasning rangi: {damas.tezlik}")
print("-" *25)
print(f"BMW'ning rangi: {bmw.rang}")
print(f"BMW'ning rangi: {bmw.model}")
print(f"BMW'ning rangi: {bmw.tezlik}")
