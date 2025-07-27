import random

# Nastavenie počiatočných hodnôt
player_hp = 100
monster_hp = 80

print("Vitaj v Dungeon Fighte!")
print("Budeš bojovať s príšerou. Nech vyhrá ten najsilnejší!")

# Hlavný cyklus hry
while player_hp > 0 and monster_hp > 0:
    input("\nStlač Enter pre útok...")

    # Útok hráča
    player_attack = random.randint(10, 20)
    monster_hp -= player_attack
    print(f"💥 Zasiahol si príšeru za {player_attack} bodov. Príšera má {max(monster_hp, 0)} HP.")

    # Príšera zaútočí len ak ešte žije
    if monster_hp > 0:
        monster_attack = random.randint(5, 15)
        player_hp -= monster_attack
        print(f"👹 Príšera zaútočila za {monster_attack} bodov. Tvoje HP: {max(player_hp, 0)}")

# Výsledok hry
if player_hp > 0:
    print("\n🎉 Vyhral si! Príšera je porazená.")
else:
    print("\n💀 Zomrel si. Dungeon ťa pohltil.")
