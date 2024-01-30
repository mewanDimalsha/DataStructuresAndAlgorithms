def energy(orb1, orb2):
    count = 0

    while orb1 > 0:
        i = 0
        energy_drain = orb2
        while (1 << i) + energy_drain <= orb1:
            i += 1

        if i == 0:
            return -1

        orb1 -= (1 << i) + energy_drain
        count += 1

    return count


orb1 = int(input())
orb2 = int(input())

print(energy(orb1, orb2))
