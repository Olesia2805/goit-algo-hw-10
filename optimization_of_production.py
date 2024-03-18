import pulp

model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

Lemonades = pulp.LpVariable('Lemonades', lowBound=0, cat='Integer')
Fruit_juices = pulp.LpVariable('Fruit-juices', lowBound=0, cat='Integer')

# Функція цілі (Максимізація прибутку)
model += Lemonades + Fruit_juices, "Profit"

# Додавання обмежень
model += 2 * Lemonades + 1 * Fruit_juices <= 100  # Water
model += 1 * Lemonades <= 50 # Sugar
model += 1 * Lemonades <= 30  # Lemon
model += 2 * Fruit_juices <= 40  # Fruit

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Make Lemonades:", Lemonades.varValue)
print("Produce Fruit-juices:", Fruit_juices.varValue)

# Make Lemonades: 30.0
# Produce Fruit-juices: 20.0