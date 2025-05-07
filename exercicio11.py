import random

hp_base = random.randint(200, 1000)
hp_jogador1 = hp_base
hp_jogador2 = hp_base
hp_max_jogador1 = hp_base
hp_max_jogador2 = hp_base

ataque_jogador1 = random.randint(1, 50)
defesa_jogador1 = random.randint(1, 50)
ataque_jogador2 = random.randint(1, 50)
defesa_jogador2 = random.randint(1, 50)

itens_usados_jogador1 = False
itens_usados_jogador2 = False
status_jogador1 = {"Buffer Overflow": False, "Loop Infinito": False, "Tela Azul": False, "Cache Hit": False}
status_jogador2 = {"Buffer Overflow": False, "Loop Infinito": False, "Tela Azul": False, "Cache Hit": False}
perdeu_vez_jogador1 = False
perdeu_vez_jogador2 = False

buff_ataque_jogador1 = 0
buff_defesa_jogador1 = 0
buff_ataque_jogador2 = 0
buff_defesa_jogador2 = 0

defesa_original_jogador1 = defesa_jogador1
defesa_original_jogador2 = defesa_jogador2

modo_jogo = input("[1] Multiplayer ou [2] vs CPU? ")

turno_atual = 1
while hp_jogador1 > 0 and hp_jogador2 > 0:
    if buff_ataque_jogador1 == 0 and buff_defesa_jogador1 == 0:
        ataque_jogador1 = max(1, ataque_jogador1)
        defesa_jogador1 = defesa_original_jogador1
    if buff_ataque_jogador2 == 0 and buff_defesa_jogador2 == 0:
        ataque_jogador2 = max(1, ataque_jogador2)
        defesa_jogador2 = defesa_original_jogador2

    print(f"--- Turno {turno_atual} ---")
    print(f"Jogador 1: HP {hp_jogador1}/{hp_max_jogador1} ATQ {ataque_jogador1} DEF {defesa_jogador1}")
    print(f"{'CPU' if modo_jogo == '2' else 'Jogador 2'}: HP {hp_jogador2}/{hp_max_jogador2} ATQ {ataque_jogador2} DEF {defesa_jogador2}")

    if perdeu_vez_jogador1:
        print("Jogador 1 perde a vez por Loop Infinito!")
        perdeu_vez_jogador1 = False
    else:
        print("Jogador 1: [1] Atacar [2] Curar [3] Itens [4] Status")
        acao_jogador1 = input()
        if acao_jogador1 == "1":
            critico = random.randint(1, 10) == 1
            dano = max(0, ataque_jogador1 - defesa_jogador2)
            if critico:
                dano *= 2
                print(f"CRÍTICO! Causa {dano} de dano.")
            else:
                print(f"Ataca! Inimigo perde {dano} HP.")
            hp_jogador2 -= dano
        elif acao_jogador1 == "2":
            cura = random.randint(10, 50)
            hp_jogador1 += cura
            print(f"Curou {cura} HP.")
        elif acao_jogador1 == "3" and not itens_usados_jogador1:
            print("Itens: [1] Poção de Força (+10 ATQ por 2 turnos) [2] Poção de Cura (+20-80 HP) [3] Poção de Defesa (+10 DEF por 2 turnos) [4] Poção de Ataque (+10 ATQ por 2 turnos)")
            escolha_item = input()
            if escolha_item == "1":
                ataque_jogador1 += 10
                buff_ataque_jogador1 = 2
            elif escolha_item == "2":
                hp_jogador1 += random.randint(20, 80)
            elif escolha_item == "3":
                defesa_jogador1 += 10
                buff_defesa_jogador1 = 2
            elif escolha_item == "4":
                ataque_jogador1 += 10
                buff_ataque_jogador1 = 2
            itens_usados_jogador1 = True
            print("Item usado.")
        elif acao_jogador1 == "4":
            print("Status: [1] Buffer Overflow [2] Loop Infinito [3] Tela Azul [4] Cache Hit")
            escolha_status = input()
            if escolha_status == "1" and not status_jogador1['Buffer Overflow']:
                dano_bo = int(hp_max_jogador2 * 0.05)
                hp_jogador2 -= dano_bo
                print(f"Buffer Overflow! Inimigo perde {dano_bo} HP.")
                status_jogador1['Buffer Overflow'] = True
            elif escolha_status == "2" and not status_jogador1['Loop Infinito']:
                perdeu_vez_jogador2 = True
                print("Loop Infinito! Inimigo perde a próxima vez.")
                status_jogador1['Loop Infinito'] = True
            elif escolha_status == "3" and not status_jogador1['Tela Azul']:
                defesa_jogador2 = 0
                buff_defesa_jogador2 = 2
                print("Tela Azul! Defesa do inimigo zerada por 2 turnos.")
                status_jogador1['Tela Azul'] = True
            elif escolha_status == "4" and not status_jogador1['Cache Hit'] and hp_jogador1 < hp_max_jogador1 * 0.25:
                cura_ch = int(hp_max_jogador1 * 0.30)
                hp_jogador1 += cura_ch
                print(f"Cache Hit! Recupera {cura_ch} HP.")
                status_jogador1['Cache Hit'] = True

    if hp_jogador2 <= 0:
        print("Jogador 1 venceu!")
        break

    if modo_jogo == "2":
        acao_jogador2 = random.choice(["1", "2"])
    else:
        if perdeu_vez_jogador2:
            print("Jogador 2 perde a vez por Loop Infinito!")
            perdeu_vez_jogador2 = False
            acao_jogador2 = None
        else:
            print("Jogador 2: [1] Atacar [2] Curar [3] Itens [4] Status")
            acao_jogador2 = input()

    if acao_jogador2 == "1":
        critico = random.randint(1, 10) == 1
        dano = max(0, ataque_jogador2 - defesa_jogador1)
        if critico:
            dano *= 2
            print(f"CRÍTICO! Inimigo causa {dano} de dano.")
        else:
            print(f"Inimigo ataca! Você perde {dano} HP.")
        hp_jogador1 -= dano
    elif acao_jogador2 == "2":
        cura = random.randint(10, 50)
        hp_jogador2 += cura
        print(f"Inimigo curou {cura} HP.")
    elif modo_jogo != "2" and acao_jogador2 == "3" and not itens_usados_jogador2:
        print("Itens: [1] Poção de Força [2] Poção de Cura [3] Poção de Defesa [4] Poção de Ataque")
        escolha_item = input()
        if escolha_item == "1":
            ataque_jogador2 += 10
            buff_ataque_jogador2 = 2
        elif escolha_item == "2":
            hp_jogador2 += random.randint(20, 80)
        elif escolha_item == "3":
            defesa_jogador2 += 10
            buff_defesa_jogador2 = 2
        elif escolha_item == "4":
            ataque_jogador2 += 10
            buff_ataque_jogador2 = 2
        itens_usados_jogador2 = True
        print("Item usado.")
    elif modo_jogo != "2" and acao_jogador2 == "4":
        print("Status: [1] Buffer Overflow [2] Loop Infinito [3] Tela Azul [4] Cache Hit")
        escolha_status = input()
        if escolha_status == "1" and not status_jogador2['Buffer Overflow']:
            dano_bo = int(hp_max_jogador1 * 0.05)
            hp_jogador1 -= dano_bo
            status_jogador2['Buffer Overflow'] = True
            print(f"Buffer Overflow! Você perde {dano_bo} HP.")
        elif escolha_status == "2" and not status_jogador2['Loop Infinito']:
            perdeu_vez_jogador1 = True
            status_jogador2['Loop Infinito'] = True
            print("Loop Infinito! Você perde a próxima vez.")
        elif escolha_status == "3" and not status_jogador2['Tela Azul']:
            defesa_jogador1 = 0
            buff_defesa_jogador1 = 2
            status_jogador2['Tela Azul'] = True
            print("Tela Azul! Sua defesa zerada por 2 turnos.")
        elif escolha_status == "4" and not status_jogador2['Cache Hit'] and hp_jogador2 < hp_max_jogador2 * 0.25:
            cura_ch = int(hp_max_jogador2 * 0.30)
            hp_jogador2 += cura_ch
            status_jogador2['Cache Hit'] = True
            print(f"Cache Hit! Inimigo recupera {cura_ch} HP.")

    if hp_jogador1 <= 0:
        print("Jogador 2 venceu!")
        break

    if buff_ataque_jogador1 > 0:
        buff_ataque_jogador1 -= 1
        if buff_ataque_jogador1 == 0:
            ataque_jogador1 -= 10
    if buff_defesa_jogador1 > 0:
        buff_defesa_jogador1 -= 1
        if buff_defesa_jogador1 == 0:
            defesa_jogador1 = defesa_original_jogador1
    if buff_ataque_jogador2 > 0:
        buff_ataque_jogador2 -= 1
        if buff_ataque_jogador2 == 0:
            ataque_jogador2 -= 10
    if buff_defesa_jogador2 > 0:
        buff_defesa_jogador2 -= 1
        if buff_defesa_jogador2 == 0:
            defesa_jogador2 = defesa_original_jogador2

    turno_atual += 1
