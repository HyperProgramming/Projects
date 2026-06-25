import random

# turn based battle; asks for p1 'n p2 names; both starts at 8k hp;
# game has max 20 rounds. every round both gets a random card (atk, def, heal);
# each card receives random value (1, 100, 200, 300, 400, 500, 1000);
# p gains a skill point (sp) depending on card value;
# 1 = 0, 100 = 1, 200 = 2, 300 = 3, 400 = 4, 500 = 5, 1000 = 10; max sp you can hold = 20

# atk vs atk = both deal damage to each other
# atk vs def = cmp atk val to def val; 
  # if atk > def: subtract defender hp; 
  # if atk < def: subtract attackers hp; 
  # if atk == def: no dmg;
# def vs def = nothing happens;
# heal vs heal = both heal
# heal vs atk = heal has priority over atk
# heal vs def = p heals while def is useless

# special skills; unique skill (10 sp) = deals random dmg between 1k-3k, prompts everytime if p has 10 sp
# ult skill (20 sp) = deals random dmg between 3k-5k, prompts everytime if p has 20 sp

# end game conditions;
# game ends when either p1 or p2 reaches 0 hp or when 20 rounds has passed
  # if p1 p2 still alive after 20 rounds:
    # cmp remaining hp; if p1 hp > p2 hp: p1 wins; elif p1 hp == p2 hp: draw;

# after every round display:
  # round number; each p card type and value; skill points gained;
  # current skill point total; dmg, heal or def calculations; remaining hp of both players;
# after game ends display:
  # total rounds played; final hp of both players; winner;


while True:
    print("1 on 1 turn based game")
    print("[1] Start\n[2] Mechanics")
    c = int(input("Choice: "))
    # introduction
    if c == 2:
        print("Welcome to my turn based 1 on 1 game!")
        print("The game has a max of 20 rounds and each round you draw 3 random cards")
        print("\tATK, DEF, and HEAL")
        print("Each card receives a random value")
        print("\t1, 100, 200, 300, 400, 500, and 1000")
        print("A player gains a skill point (SP) depending on the card's value")
        print("\t1 = 0, 100 = 1, 200 = 2, 300 = 3, 400 = 4, 500 = 5, 1000 = 10")
        print("The max SP a player can hold is 20\n")
        print("Card phases")
        print("\tatk vs atk = both deal damage to each other")
        print("\tatk vs def = compare atk value to def value")
        print("\t\tif atk > def: subtract defender hp")
        print("\t\tif atk < def: subtract attacker's hp")
        print("\t\tif atk == def: no damage")
        print("\tdef vs def = nothing happens")
        print("\theal vs heal = both heal")
        print("\theal vs atk = heal has priority over atk")
        print("\theal vs def = player heals while def is useless\n")
        print("special skills:")
        print("\tunique skill (10 sp) = deals random dmg between 1k-3k, prompts everytime if player has 10 sp")
        print("\tult skill (20 sp) = deals random dmg between 3k-5k, prompts everytime if player has 20 sp\n")
    elif c == 1:
        print("")
        break
    else:
        print("Invalid Input")

# ask each p name
p1N = input("Enter Player 1 Name: ")   
p2N = input("Enter Player 2 Name: ")   

# player stats
p1hp = 8000
p1sp = 0
p1spG = 0
p2hp = 8000
p2sp = 0
p2spG = 0
# for game
cards = ["atk", "def", "heal"]
cVal = [1, 100, 200, 300, 400, 500, 1000]

for round in range(1, 21):
    print("")
    print("=" * 40)
    print("\t\tROUND", round)
    print("=" * 40)
    # special skills
    if p1sp == 20:
        while True:
            print(p1N, "has 20 SP")
            ult = input("Use ULT? [Y/N]: ")
            if ult == "Y":
                p1sd = random.randint(3000, 5000)
                p1sp = 0
                p2hp -= p1sd
                print(p1N, "used ULT and deals", p1sd, "damage to", p2N)
                print("")
                break
            elif ult == "N":
                print("")
                break
            else:
                print("Invalid Choice, only [Y/N]")
    if p1sp >= 10:
        while True:
            print(p1N, "has", p1sp, "SP")
            uS = input("Use Unique Skill? [Y/N]: ")
            if uS == "Y":
                p1sd = random.randint(1000, 3000)
                p1sp -= 10
                p2hp -= p1sd
                print(p1N, "used Unique Skill and deals", p1sd, "damage to", p2N)
                print("")
                break
            elif uS == "N":
                print("")
                break
            else:
                print("Invalid Choice, only [Y/N]")
    if p2hp <= 0:
        break
    if p2sp == 20:
        while True:
            print(p2N, "has 20 SP")
            ult = input("Use ULT? [Y/N]: ")
            if ult == "Y":
                p2sd = random.randint(3000, 5000)
                p2sp = 0
                p1hp -= p2sd
                print(p2N, "used ULT and deals", p2sd, "damage to", p1N)
                print("")
                break
            elif ult == "N":
                print("")
                break
            else:
                print("Invalid Choice, only [Y/N]")
    if p2sp >= 10:
        while True:
            print(p2N, "has", p2sp, "SP")
            uS = input("Use Unique Skill? [Y/N]: ")
            if uS == "Y":
                p2sd = random.randint(1000, 3000)
                p2sp -= 10
                p1hp -= p2sd
                print(p2N, "used Unique Skill and deals", p2sd, "damage to", p1N)
                print("")
                break
            elif uS == "N":
                print("")
                break
            else:
                print("Invalid Choice, only [Y/N]")
    if p1hp <= 0:
        break
    # card draw
    p1C = random.choice(cards)
    p1V = random.choice(cVal)
    p2C = random.choice(cards)
    p2V = random.choice(cVal)
    # sp gain
    if p1V == 1:
        p1spG = 0
    else:
        p1spG = p1V // 100
        p1sp += p1spG
        if p1sp > 20:
            p1sp = 20
    if p2V == 1:
        p2spG = 0
    else:
        p2spG = p2V // 100
        p2sp += p2spG
        if p2sp > 20:
            p2sp = 20
    
    print(p1N, "drew", p1C, "card, with value", p1V, "\n  SP gained:", p1spG, ",", p1N, "has a total of", p1sp, "skill points!\n")
    print(p2N, "drew", p2C, "card, with value", p2V, "\n  SP gained:", p2spG, ",", p2N, "has a total of", p2sp, "skill points!\n")

    # card phase
    if p1C == "atk" and p2C == "atk":
        p1hp -= p2V
        p2hp -= p1V
        print("Both players hit each other!", p1N, "takes", p2V, "damage,", p2N, "takes", p1V, "damage!\n")
    elif p1C == "atk" and p2C == "def":
        if p1V > p2V: # 200 vs 100
            dmg = p1V - p2V # 200 - 100 = 100
            p2hp -= dmg # p2 hp = 8000 - 100
            print(p1N, "has higher stat!", p2N, "negated", p2V, "damage and took", dmg, "damage\n")
        elif p1V < p2V: # 100 vs 200
            dmg = p2V - p1V # 200 - 100 = 100
            p1hp -= dmg  # p1 hp = 8000 - 100
            print(p2N, "has higher stat and took no damage!", p1N, "took", dmg, "recoil damage\n")
        elif p1V == p2V:
            print("Both values are equal, no damage taken for both sides\n")
    elif p1C == "def" and p2C == "atk": 
        if p1V > p2V: # 200 vs 100
            dmg = p1V - p2V # 200 - 100 = 100
            p2hp -= dmg # p2 hp = 8000 - 100
            print(p1N, "has higher stat and took no damage!", p2N, "took", dmg, "recoil damage\n")
        elif p1V < p2V:
            dmg = p2V - p1V
            p1hp -= dmg
            print(p2N, "has higher stat!", p1N, "negated", p1V, "took", dmg, "damage\n")
        elif p1V == p2V:
            print("Both values are equal, no damage taken for both sides\n")
    elif p1C == "def" and p2C == "def":
        print("Both took defensive stances, nothing happens\n")
    elif p1C == "heal" and p2C == "heal":
        p1hp += p1V
        p2hp += p2V
        print(p1N, "healed", p1V, "hp and", p2N, "healed", p2V, "hp\n")
    elif p1C == "heal" and p2C == "atk":
        p1hp += p1V
        print("Heal has priority over atk!")
        print(p1N, "healed", p1V, "hp")
        p1hp -= p2V
        print(p2N, "dealt", p2V, "damage to", p1N)
        print("")
    elif p1C == "atk" and p2C == "heal":
        p2hp += p2V
        print("Heal has priority over atk!")
        print(p2N, "healed", p2V, "hp")
        p2hp -= p1V
        print(p1N, "dealt", p1V, "damage to", p2N)
        print("")
    elif p1C == "heal" and p2C == "def":
        p1hp += p1V
        print(p1N, "healed", p1V, "hp")
        print(p2N, "defends\n\nNothing happens..\n")
    elif p1C == "def" and p2C == "heal":
        p2hp += p2V
        print(p2N, "healed", p2V, "hp")
        print(p1N, "defends\n\nNothing happens..\n") 
    
    print("--- Remaining HP ---")
    print(p1N, ":", p1hp, "|", p2N, ":", p2hp)

    if p1hp <= 0 or p2hp <= 0:
        break
    input("Press enter to continue..")

# game over screen
print("\n=== GAME OVER ===")
print("Played a total of", round, "rounds\n")
print("--- Remaining HP ---")
print(p1N, ":", p1hp)
print(p2N, ":", p2hp)

if p1hp <= 0 and p2hp <= 0:
    print("Both players are down, the match is a draw")
elif p1hp <= 0:
    print("The winner is", p2N)
elif p2hp <= 0:
    print("The winner is", p1N) 
else:
    if p1hp > p2hp:
        print("20 rounds has passed, the winner is", p1N)
    elif p2hp > p1hp:
        print("20 rounds has passed, the winner is", p2N)
    else:
        print("20 rounds has passed, both have equal standing.. It's a draw!")
input("\nGame over, press enter to exit..")
