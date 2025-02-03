import random

SAMPLES = 1_000_000

triangle_cases = 0

for _ in range(1_000_000):
    random_point = random.random()

    stick1 = min(random_point, 1 - random_point)
    longer_part = 1 - stick1

    stick2 = random.random() * longer_part
    stick3 = longer_part - stick2

    is_striangle = (
        (stick1 + stick2 > stick3) and
        (stick2 + stick3 > stick1) and
        (stick1 + stick3 > stick2)
    )

    triangle_cases += 1 if is_striangle else 0

print(f"The prob is {triangle_cases/SAMPLES} after {SAMPLES} tries")
