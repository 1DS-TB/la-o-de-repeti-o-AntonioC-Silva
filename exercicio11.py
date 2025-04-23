import random

hp_inicial = random.randint(200, 1000)
jogador1_hp = hp_inicial
jogador2_hp = hp_inicial
jogador1_hp_max = hp_inicial
jogador2_hp_max = hp_inicial

jogador1_ataque = random.randint(1, 50)
jogador1_defesa = random.randint(1, 50)
jogador2_ataque = random.randint(1, 50)
jogador2_defesa = random.randint(1, 50)

itens_usados1 = False
itens_usados2 = False
status_usado1 = {"Buffer Overflow": False, "Loop Infinito": False, "Tela Azul": False, "Cache Hit": False}
status_usado2 = {"Buffer Overflow": False, "Loop Infinito": False, "Tela Azul": False, "Cache Hit": False}
skip_turn1 = False
skip_turn2 = False

buff_atk1_turns = 0
buff_def1_turns = 0
buff_atk2_turns = 0
buff_def2_turns = 0

original_def1 = jogador1_defesa
original_def2 = jogador2_defesa

modo = input("[1] Multiplayer ou [2] vs CPU? ")

turno = 1
while jogador1_hp > 0 and jogador2_hp > 0:
    if buff_atk1_turns == 0 and buff_def1_turns == 0:
        jogador1_ataque = max(1, jogador1_ataque)
        jogador1_defesa = original_def1
    if buff_atk2_turns == 0 and buff_def2_turns == 0:
        jogador2_ataque = max(1, jogador2_ataque)
        jogador2_defesa = original_def2

    print(f"--- Turno {turno} ---")
    print(f"Jogador 1: HP {jogador1_hp}/{jogador1_hp_max} ATQ {jogador1_ataque} DEF {jogador1_defesa}")
    print(f"{'CPU' if modo == '2' else 'Jogador 2'}: HP {jogador2_hp}/{jogador2_hp_max} ATQ {jogador2_ataque} DEF {jogador2_defesa}")

    if skip_turn1:
        print("Jogador 1 perde a vez por Loop Infinito!")
        skip_turn1 = False
    else:
        print("Jogador 1: [1] Atacar [2] Curar [3] Itens [4] Status")
        acao = input()
        if acao == "1":
            critico = random.randint(1, 10) == 1
            dano = max(0, jogador1_ataque - jogador2_defesa)
            if critico:
                dano *= 2
                print(f"CRÍTICO! Causa {dano} de dano.")
            else:
                print(f"Ataca! Inimigo perde {dano} HP.")
            jogador2_hp -= dano
        elif acao == "2":
            cura = random.randint(10, 50)
            jogador1_hp += cura
            print(f"Curou {cura} HP.")
        elif acao == "3" and not itens_usados1:
            print("Itens: [1] Poção de Força (+10 ATQ por 2 turnos) [2] Poção de Cura (+20-80 HP) [3] Poção de Defesa (+10 DEF por 2 turnos) [4] Poção de Ataque (+10 ATQ por 2 turnos)")
            escolha = input()
            if escolha == "1":
                jogador1_ataque += 10
                buff_atk1_turns = 2
            elif escolha == "2":
                jogador1_hp += random.randint(20, 80)
            elif escolha == "3":
                jogador1_defesa += 10
                buff_def1_turns = 2
            elif escolha == "4":
                jogador1_ataque += 10
                buff_atk1_turns = 2
            itens_usados1 = True
            print("Item usado.")
        elif acao == "4":
            print("Status: [1] Buffer Overflow [2] Loop Infinito [3] Tela Azul [4] Cache Hit")
            escolha = input()
            if escolha == "1" and not status_usado1['Buffer Overflow']:
                dano_bo = int(jogador2_hp_max * 0.05)
                jogador2_hp -= dano_bo
                print(f"Buffer Overflow! Inimigo perde {dano_bo} HP.")
                status_usado1['Buffer Overflow'] = True
            elif escolha == "2" and not status_usado1['Loop Infinito']:
                skip_turn2 = True
                print("Loop Infinito! Inimigo perde a próxima vez.")
                status_usado1['Loop Infinito'] = True
            elif escolha == "3" and not status_usado1['Tela Azul']:
                jogador2_defesa = 0
                buff_def2_turns = 2
                print("Tela Azul! Defesa do inimigo zerada por 2 turnos.")
                status_usado1['Tela Azul'] = True
            elif escolha == "4" and not status_usado1['Cache Hit'] and jogador1_hp < jogador1_hp_max * 0.25:
                cura_ch = int(jogador1_hp_max * 0.30)
                jogador1_hp += cura_ch
                print(f"Cache Hit! Recupera {cura_ch} HP.")
                status_usado1['Cache Hit'] = True

    if jogador2_hp <= 0:
        print("Jogador 1 venceu!")
        break

    if modo == "2":
        acao2 = random.choice(["1", "2"])
    else:
        if skip_turn2:
            print("Jogador 2 perde a vez por Loop Infinito!")
            skip_turn2 = False
            acao2 = None
        else:
            print("Jogador 2: [1] Atacar [2] Curar [3] Itens [4] Status")
            acao2 = input()

    if acao2 == "1":
        critico = random.randint(1, 10) == 1
        dano = max(0, jogador2_ataque - jogador1_defesa)
        if critico:
            dano *= 2
            print(f"CRÍTICO! Inimigo causa {dano} de dano.")
        else:
            print(f"Inimigo ataca! Você perde {dano} HP.")
        jogador1_hp -= dano
    elif acao2 == "2":
        cura = random.randint(10, 50)
        jogador2_hp += cura
        print(f"Inimigo curou {cura} HP.")
    elif modo != "2" and acao2 == "3" and not itens_usados2:
        print("Itens: [1] Poção de Força [2] Poção de Cura [3] Poção de Defesa [4] Poção de Ataque")
        escolha = input()
        if escolha == "1":
            jogador2_ataque += 10
            buff_atk2_turns = 2
        elif escolha == "2":
            jogador2_hp += random.randint(20, 80)
        elif escolha == "3":
            jogador2_defesa += 10
            buff_def2_turns = 2
        elif escolha == "4":
            jogador2_ataque += 10
            buff_atk2_turns = 2
        itens_usados2 = True
        print("Item usado.")
    elif modo != "2" and acao2 == "4":
        print("Status: [1] Buffer Overflow [2] Loop Infinito [3] Tela Azul [4] Cache Hit")
        escolha = input()
        if escolha == "1" and not status_usado2['Buffer Overflow']:
            dano_bo = int(jogador1_hp_max * 0.05)
            jogador1_hp -= dano_bo
            status_usado2['Buffer Overflow'] = True
            print(f"Buffer Overflow! Você perde {dano_bo} HP.")
        elif escolha == "2" and not status_usado2['Loop Infinito']:
            skip_turn1 = True
            status_usado2['Loop Infinito'] = True
            print("Loop Infinito! Você perde a próxima vez.")
        elif escolha == "3" and not status_usado2['Tela Azul']:
            jogador1_defesa = 0
            buff_def1_turns = 2
            status_usado2['Tela Azul'] = True
            print("Tela Azul! Sua defesa zerada por 2 turnos.")
        elif escolha == "4" and not status_usado2['Cache Hit'] and jogador2_hp < jogador2_hp_max * 0.25:
            cura_ch = int(jogador2_hp_max * 0.30)
            jogador2_hp += cura_ch
            status_usado2['Cache Hit'] = True
            print(f"Cache Hit! Inimigo recupera {cura_ch} HP.")

    if jogador1_hp <= 0:
        print("Jogador 2 venceu!")
        break

    if buff_atk1_turns > 0:
        buff_atk1_turns -= 1
        if buff_atk1_turns == 0:
            jogador1_ataque -= 10
    if buff_def1_turns > 0:
        buff_def1_turns -= 1
        if buff_def1_turns == 0:
            jogador1_defesa = original_def1
    if buff_atk2_turns > 0:
        buff_atk2_turns -= 1
        if buff_atk2_turns == 0:
            jogador2_ataque -= 10
    if buff_def2_turns > 0:
        buff_def2_turns -= 1
        if buff_def2_turns == 0:
            jogador2_defesa = original_def2

    turno += 1
