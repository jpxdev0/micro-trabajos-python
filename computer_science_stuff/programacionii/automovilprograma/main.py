from class_automovil import Automovil

auto1 = Automovil()
print(auto1)

auto = []

for _ in range(10):
    auto.append(Automovil())

for a in auto:
    print(a)