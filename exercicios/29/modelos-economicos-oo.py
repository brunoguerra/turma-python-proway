class Vehicle:
    def __init__(self, model, km_per_l):
        self.set_model(model)
        self.set_km_per_l(km_per_l)
    
    def set_model(self, model):
        self._model = model
    
    def get_model(self):
        return self._model

    def set_km_per_l(self, km):
        self._km_per_l = km
    
    def get_km_per_l(self):
        return self._km_per_l

# fusca = Vehicle()
# fusca.set_model('Fusca')
# fusca.set_km_per_l(6)

# gol = Vehicle()
# gol.set_model('GOL')
# gol.set_km_per_l(15)

# vectra = Vehicle()
# vectra.set_model('Vectra')
# vectra.set_km_per_l(14)

# corola = Vehicle()
# corola.set_model('Corola')
# corola.set_km_per_l(18)

# s10 = Vehicle()
# s10.set_model('S10')
# s10.set_km_per_l(12)

# vehicles_tuple = (fusca, gol, vectra, corola, s10)

vehicles_tuple = (
    Vehicle('Fusca', 6),
    Vehicle('Gol', 15),
    Vehicle('Vectra', 14),
    Vehicle('Corola', 18),
    Vehicle('S10', 12),
)

# max_econ = 0
# for vehicle in vehicles_tuple:
#     if vehicle.get_km_per_l() > max_econ:
#         max_econ = vehicle.get_km_per_l()

max_econ = max([vehicle.get_km_per_l() for vehicle in vehicles_tuple])

for vehicle in vehicles_tuple:
    if vehicle.get_km_per_l() == max_econ:
        print('Modelo mais economico', vehicle.get_model())

for vehicle in vehicles_tuple:
    print(vehicle.get_model(), 'consome ', 1000 / vehicle.get_km_per_l(), 'L em 1000km')