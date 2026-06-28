# A Jornada do Herói: Destinos de Vale Sereno

Um **story game interativo em Python**, no estilo RPG, onde suas escolhas moldam o destino do herói e da aldeia de Vale Sereno. Cada decisão altera o alinhamento moral (herói, vilão ou neutro) e conduz a um dos 10 finais épicos, cada um com uma batalha final contra um chefe diferente.

## 📖 Enredo
Uma praga de trevas corrompe a pacata Vale Sereno. Como jovem herói, você deve descobrir a origem do mal e salvar sua vila. A jornada se ramifica entre explorar ruínas arcanas ou liderar o povo, e a partir daí as escolhas definem sua evolução:

- **Ascensão Arcana e Mágica**: Arquimago, Lich, Bruxo
- **Evolução Marcial e Heroica**: Paladino, Campeão
- **Transcendência Divina**: Semideus, Avatar
- **Corrupção Monstruosa**: Vampiro, Licantropo
- **Poder Terreno**: Imperador

## ⚔️ Mecânicas
- **Narrativa ramificada**: escolhas em texto com impacto no alinhamento e no final.
- **Alinhamento oculto**: cada decisão soma pontos em `heroi`, `vilao` ou `neutro`. O alinhamento dominante define o chefão final.
- **Combate por turnos**: sistema simples de ataque/defesa com dano aleatório (`random`).
- **Três chefes finais**:
  - Herói enfrenta o **Senhor das Sombras** (ameaça maligna).
  - Vilão enfrenta o **Paladino da Luz** (justiceiro sagrado).
  - Neutro enfrenta o **Guardião do Equilíbrio** (elemental ancestral).
- **Decisões reversíveis**: a escolha inicial (ruínas ou liderança) pode ser repensada antes de seguir; as demais são irreversíveis.
- **Rejogabilidade**: múltiplos finais e possibilidade de recomeçar após cada partida.

## ▶️ Como Executar
1. Certifique-se de ter **Python 3.6+** instalado.
2. Baixe o arquivo `jornada_do_heroi.py` (ou cole o código-fonte).
3. Execute no terminal:
   ```bash
   python jornada_do_heroi.py
