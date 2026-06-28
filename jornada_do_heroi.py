import sys
import time
import random

# ===== ESTADO GLOBAL =====
alinhamento = {"heroi": 0, "vilao": 0, "neutro": 0}
heroi_nome = ""

# ===== FUNÇÕES UTILITÁRIAS =====
def print_slow(texto, intervalo=0.03):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(intervalo)
    print()

def obter_escolha(opcoes_validas, mensagem="Sua escolha: ", permitir_voltar=False):
    """Garante que o usuário escolha um número válido. Se permitir_voltar=True, 0 é opção 'Voltar'."""
    while True:
        try:
            escolha = int(input(mensagem))
            if escolha in opcoes_validas or (permitir_voltar and escolha == 0):
                return escolha
            else:
                if permitir_voltar:
                    print(f"Opção inválida. Escolha um número entre {list(opcoes_validas)} ou 0 para voltar.")
                else:
                    print(f"Opção inválida. Escolha entre {list(opcoes_validas)}.")
        except ValueError:
            print("Por favor, digite um número.")

def atualizar_alinhamento(tipo):
    """Adiciona 1 ponto ao alinhamento indicado."""
    if tipo in alinhamento:
        alinhamento[tipo] += 1

def determinar_alinhamento():
    """Retorna o tipo de alinhamento dominante (heroi, vilao ou neutro)."""
    h = alinhamento["heroi"]
    v = alinhamento["vilao"]
    n = alinhamento["neutro"]
    if h > v and h > n:
        return "heroi"
    elif v > h and v > n:
        return "vilao"
    else:
        return "neutro"

# ===== SISTEMA DE COMBATE =====
def batalha(nome_inimigo, vida_inimigo, dano_inimigo, vida_heroi=100):
    """Combate por turnos. Retorna True se o herói vencer, False se perder."""
    print_slow(f"\n⚔️ {nome_inimigo} surge diante de você! ⚔️", 0.02)
    print_slow(f"Prepare-se para a batalha, {heroi_nome}!\n")
    
    # Habilidades especiais baseadas no alinhamento (apenas cosméticas aqui, poderiam dar bônus)
    if determinar_alinhamento() == "heroi":
        print_slow("Sua aura heroica brilha, concedendo coragem.")
        dano_base = 18
    elif determinar_alinhamento() == "vilao":
        print_slow("Seu poder sombrio pulsa, aumentando seu dano.")
        dano_base = 20
    else:
        print_slow("Você se mantém equilibrado, adaptando-se ao combate.")
        dano_base = 17
    
    defesa_ativa = False
    
    while vida_heroi > 0 and vida_inimigo > 0:
        print(f"\n{heroi_nome}: {vida_heroi} HP  |  {nome_inimigo}: {vida_inimigo} HP")
        print("1. Atacar")
        print("2. Defender (reduz próximo dano pela metade)")
        acao = obter_escolha([1, 2])
        
        # Ação do herói
        if acao == 1:
            dano = random.randint(dano_base - 3, dano_base + 5)
            print_slow(f"Você ataca com {dano} de dano!")
            vida_inimigo -= dano
            defesa_ativa = False
        elif acao == 2:
            print_slow("Você se prepara para defender.")
            defesa_ativa = True
        
        if vida_inimigo <= 0:
            break
        
        # Ação do inimigo
        dano_inim = random.randint(dano_inimigo[0], dano_inimigo[1])
        if defesa_ativa:
            dano_inim = max(1, dano_inim // 2)
            print_slow(f"{nome_inimigo} ataca, mas você defende! Dano reduzido: {dano_inim}")
            defesa_ativa = False
        else:
            print_slow(f"{nome_inimigo} ataca causando {dano_inim} de dano.")
        vida_heroi -= dano_inim
    
    if vida_heroi > 0:
        print_slow(f"\n✨ Você derrotou {nome_inimigo}! ✨\n")
        return True
    else:
        print_slow(f"\n💀 Você foi derrotado por {nome_inimigo}... 💀\n")
        return False

def chefao():
    """Determina o chefe de acordo com o alinhamento e inicia a batalha."""
    tipo = determinar_alinhamento()
    if tipo == "heroi":
        # Inimigo vilão: Senhor das Sombras
        return batalha("Senhor das Sombras (Necromante Supremo)", 120, (12, 22))
    elif tipo == "vilao":
        # Inimigo herói: Paladino da Luz
        return batalha("Paladino da Luz (Campeão da Justiça)", 130, (10, 20))
    else:
        # Inimigo neutro: Guardião do Equilíbrio
        return batalha("Guardião do Equilíbrio (Elemental Ancestral)", 125, (11, 21))

# ===== CENAS DO JOGO =====
def intro():
    global heroi_nome
    print_slow("\n" + "="*60)
    print_slow("           A JORNADA DO HERÓI: DESTINOS DE VALE SERENO")
    print_slow("="*60 + "\n", 0.02)
    heroi_nome = input("Antes de começarmos, diga-me, herói: qual é o seu nome? ")
    print_slow(f"\nAh, {heroi_nome}... que os ventos da sorte soprem a seu favor.")
    print_slow("Você é um jovem da pacata aldeia de Vale Sereno.")
    print_slow("Uma praga de trevas se espalha pela terra, corrompendo tudo.")
    print_slow("O conselho de anciãos o convocou para uma missão: descobrir a origem do mal e salvar a vila.\n")

def escolha_inicial():
    """Permite voltar atrás se o jogador se arrepender."""
    while True:
        print_slow("\nO ancião diz: 'A antiga cidadela na Floresta Sussurrante pode conter respostas.'")
        print_slow("Como deseja proceder?\n")
        print("1. Explorar as ruínas proibidas imediatamente.")
        print("2. Convocar os aldeões e preparar um exército.")
        print("0. Voltar e conversar mais com o ancião (reinicia a escolha)")
        escolha = obter_escolha([1, 2], permitir_voltar=True)
        if escolha == 0:
            print_slow("Você pede um momento para refletir...")
            continue
        else:
            # Confirmação
            if escolha == 1:
                print_slow("\nVocê decide se embrenhar na floresta sozinho. Tem certeza?")
            else:
                print_slow("\nVocê decide liderar o povo. Tem certeza?")
            print("1. Sim, seguir em frente.")
            print("2. Não, quero repensar.")
            conf = obter_escolha([1, 2])
            if conf == 1:
                if escolha == 1:
                    atualizar_alinhamento("neutro")  # Exploração solitária tende ao neutro
                    return "ruinas"
                else:
                    atualizar_alinhamento("heroi")   # Liderança altruísta
                    return "lideranca"
            else:
                print_slow("Você volta a considerar suas opções...")
                continue

def ruinas_entrada():
    print_slow("\nVocê segue pela Floresta Sussurrante. A entrada da cidadela em ruínas se revela.")
    print_slow("Três corredores se abrem, cada um pulsando com energia distinta:\n")
    print("1. Portal Arcano (runas azuis, cheiro de ozônio).")
    print("2. Santuário Sagrado (luz dourada, calor reconfortante).")
    print("3. Câmara Sombria (sombras dançantes, frio mortal).")
    escolha = obter_escolha([1, 2, 3])
    if escolha == 1:
        atualizar_alinhamento("neutro")  # Busca por conhecimento arcano
        return "magia"
    elif escolha == 2:
        atualizar_alinhamento("heroi")   # Fé nos deuses
        return "fe"
    else:
        atualizar_alinhamento("vilao")   # Caminho sombrio
        return "tentacao"

def caminho_magia():
    print_slow("\nVocê entra em uma biblioteca arcana. No centro, três tomos ancestrais:\n")
    print("1. Tomo da Magia Pura (domínio das leis da realidade).")
    print("2. Tomo da Necromancia (segredos da imortalidade obscura).")
    print("3. Círculo de Invocação (pacto com entidade do Abismo).")
    escolha = obter_escolha([1, 2, 3])
    if escolha == 1:
        atualizar_alinhamento("neutro")  # Conhecimento sem amarras morais
        return "final_arquimago"
    elif escolha == 2:
        atualizar_alinhamento("vilao")   # Necromancia é vil
        return "final_lich"
    else:
        atualizar_alinhamento("vilao")   # Pacto obscuro
        return "final_bruxo"

def caminho_fe():
    print_slow("\nSantuário banhado em luz. Uma voz ecoa: 'O que você oferece, mortal?'\n")
    print("1. Fazer juramento sagrado (tornar-se Paladino).")
    print("2. Oferecer seu corpo como avatar divino.")
    print("3. Desafiar o deus e reivindicar a centelha divina.")
    escolha = obter_escolha([1, 2, 3])
    if escolha == 1:
        atualizar_alinhamento("heroi")
        return "final_paladino"
    elif escolha == 2:
        atualizar_alinhamento("heroi")   # Sacrifício altruísta
        return "final_avatar"
    else:
        atualizar_alinhamento("neutro")  # Desafio auto interessado
        return "final_semideus"

def caminho_tentacao():
    print_slow("\nCâmara sombria com altar e oferendas: um cálice de sangue e uma pele bestial.\n")
    print("1. Beber do cálice (tornar-se Vampiro).")
    print("2. Vestir a pele (tornar-se Licantropo).")
    escolha = obter_escolha([1, 2])
    if escolha == 1:
        atualizar_alinhamento("vilao")
        return "final_vampiro"
    else:
        atualizar_alinhamento("neutro")  # Bestial, não necessariamente mal
        return "final_licantropo"

def caminho_lideranca():
    print_slow("\nVocê lidera os aldeões. Que tipo de comandante será?\n")
    print("1. Treinar até se tornar o guerreiro supremo (Campeão).")
    print("2. Forjar alianças e artefatos para erguer um império (Imperador).")
    escolha = obter_escolha([1, 2])
    if escolha == 1:
        atualizar_alinhamento("heroi")
        return "final_campeao"
    else:
        atualizar_alinhamento("neutro")  # Poder terreno, ambição
        return "final_imperador"

# ===== FINAIS (com batalha incluída) =====
def executar_final(tipo_final):
    """Chama a batalha final e depois o epílogo específico."""
    if not chefao():
        print_slow("Sua jornada termina aqui. Fim de jogo.")
        return False  # Derrota, encerra o jogo
    # Se vitória, continua para o final
    if tipo_final == "arquimago":
        final_arquimago()
    elif tipo_final == "lich":
        final_lich()
    elif tipo_final == "bruxo":
        final_bruxo()
    elif tipo_final == "paladino":
        final_paladino()
    elif tipo_final == "avatar":
        final_avatar()
    elif tipo_final == "semideus":
        final_semideus()
    elif tipo_final == "vampiro":
        final_vampiro()
    elif tipo_final == "licantropo":
        final_licantropo()
    elif tipo_final == "campeao":
        final_campeao()
    elif tipo_final == "imperador":
        final_imperador()
    return True

def final_arquimago():
    print_slow(f"\n{heroi_nome} estuda o Tomo da Magia Pura e transcende.")
    print_slow("Com um gesto, dissipa a praga. Torna-se o Soberano Arcano, guardião de Vale Sereno.\n")
    print("FIM: Arquimago / Soberano Arcano.")

def final_lich():
    print_slow(f"\n{heroi_nome} entoa as palavras proibidas e se torna um Lich imortal.")
    print_slow("Comanda legiões de mortos para eliminar a praga. Governa como Necromante Supremo.\n")
    print("FIM: Lich / Necromante Supremo.")

def final_bruxo():
    print_slow(f"\n{heroi_nome} sela o pacto e vira receptáculo de um ser cósmico.")
    print_slow("Sua magia eldritch aniquila a praga, mas sua alma está acorrentada ao Abismo.\n")
    print("FIM: Bruxo / Pactuário.")

def final_paladino():
    print_slow(f"\n{heroi_nome} recebe a lâmina sagrada. Como Cavaleiro Sagrado, purifica a terra.")
    print_slow("Vale Sereno ergue um templo em sua honra. Eterno protetor da luz.\n")
    print("FIM: Paladino / Cavaleiro Sagrado.")

def final_avatar():
    print_slow(f"\n{heroi_nome} torna-se o Avatar divino. A praga é erradicada pelo seu brilho.")
    print_slow("Sua vontade agora ecoa a do deus. Um Vessel Divino guia a vila para uma era de milagres.\n")
    print("FIM: Avatar / Vessel Divino.")

def final_semideus():
    print_slow(f"\n{heroi_nome} desafia e vence o deus, arrancando uma centelha divina.")
    print_slow("Ascende como Semideus da Proteção. Observa das estrelas e molda o destino.\n")
    print("FIM: Semideus / Ascendido.")

def final_vampiro():
    print_slow(f"\n{heroi_nome} bebe o cálice e se torna um vampiro imortal.")
    print_slow("Subjuga a praga e governa seu domínio com mão de ferro imortal.\n")
    print("FIM: Vampiro / Senhor dos Não-Mortos.")

def final_licantropo():
    print_slow(f"\n{heroi_nome} se funde à besta. Na forma híbrida, destroça a fonte do mal.")
    print_slow("Agora luta contra seus instintos, guardião bestial da floresta.\n")
    print("FIM: Licantropo / Quimera.")

def final_campeao():
    print_slow(f"\n{heroi_nome} treina até o limite humano. Seus feitos em batalha alteram a geografia.")
    print_slow("Torna-se uma Lenda Viva, o Campeão cujo nome ecoa por milênios.\n")
    print("FIM: Campeão / Lenda Viva.")

def final_imperador():
    print_slow(f"\n{heroi_nome} une as aldeias sob uma coroa arcana. Sua palavra se torna lei.")
    print_slow("A praga é extinguida por seus exércitos. Governa como Rei-Feiticeiro.\n")
    print("FIM: Imperador / Rei-Feiticeiro.")

# ===== FLUXO PRINCIPAL =====
def main():
    intro()
    while True:
        # Reseta alinhamento para nova jornada
        global alinhamento
        alinhamento = {"heroi": 0, "vilao": 0, "neutro": 0}
        
        caminho = escolha_inicial()
        
        if caminho == "ruinas":
            destino = ruinas_entrada()
            if destino == "magia":
                final_tipo = caminho_magia()
            elif destino == "fe":
                final_tipo = caminho_fe()
            else:
                final_tipo = caminho_tentacao()
        else:
            final_tipo = caminho_lideranca()
        
        # Traduz o tipo de final para a string usada em executar_final
        mapa_finais = {
            "final_arquimago": "arquimago",
            "final_lich": "lich",
            "final_bruxo": "bruxo",
            "final_paladino": "paladino",
            "final_avatar": "avatar",
            "final_semideus": "semideus",
            "final_vampiro": "vampiro",
            "final_licantropo": "licantropo",
            "final_campeao": "campeao",
            "final_imperador": "imperador"
        }
        tipo = mapa_finais.get(final_tipo)
        vitoria = executar_final(tipo)
        
        if not vitoria:
            # Derrota: pergunta se quer tentar de novo
            print("\nDeseja tentar novamente?")
            print("1. Recomeçar do início.")
            print("2. Sair do jogo.")
            if obter_escolha([1, 2]) == 2:
                break
            else:
                continue
        
        # Se vitória, pergunta se quer jogar novamente
        print("\nDeseja explorar outro destino?")
        print("1. Sim, nova jornada.")
        print("2. Encerrar.")
        if obter_escolha([1, 2]) == 2:
            print_slow("\nQue as estrelas guiem seus passos, herói. Até a próxima lenda.")
            break

if __name__ == "__main__":
    main()
