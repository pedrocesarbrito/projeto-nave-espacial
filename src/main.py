import random

# =========================
# 1.1 TELEMETRIA (dados)
# =========================

def gerar_dados():
    return {
        "temp_interna": round(random.uniform(0, 40), 1),
        "temp_externa": round(random.uniform(-10, 50), 1),
        "integridade": random.choice([0, 1]),  # 0 = falha, 1 = ok
        "energia": round(random.uniform(0, 100), 1),
        "pressao_principal": round(random.uniform(0, 120), 1),
        "pressao_auxiliar": round(random.uniform(0, 120), 1),
        "modulos_criticos": random.choice([0, 1])  # 0 = falha, 1 = ok
    }

# =========================
# 1.2 + 1.3 VERIFICAÇÃO
# =========================

def avaliar_lancamento(dados):
    motivos = []

    if not (15 <= dados["temp_interna"] <= 25):
        motivos.append("Temperatura interna fora da faixa")

    if not (4 <= dados["temp_externa"] <= 35):
        motivos.append("Temperatura externa fora da faixa")

    if dados["integridade"] == 0:
        motivos.append("Falha estrutural")

    if dados["energia"] < 60:
        motivos.append("Energia insuficiente")

    if not (30 <= dados["pressao_principal"] <= 100):
        motivos.append("Pressão do tanque principal fora da faixa")

    if not (30 <= dados["pressao_auxiliar"] <= 100):
        motivos.append("Pressão do tanque auxiliar fora da faixa")

    if dados["modulos_criticos"] == 0:
        motivos.append("Falha nos módulos críticos")

    if len(motivos) == 0:
        return "PRONTO PARA DECOLAR", ["Todos os parâmetros OK"]
    else:
        return "DECOLAGEM ABORTADA", motivos

# =========================
# 1.4 ANÁLISE ENERGÉTICA
# =========================

def calcular_autonomia(energia_percentual):
    capacidade_total = 1000  # kWh
    consumo_decolagem = 300
    perdas = 50

    energia_disponivel = capacidade_total * (energia_percentual / 100)
    autonomia = energia_disponivel - consumo_decolagem - perdas

    return autonomia

# =========================
# EXECUÇÃO
# =========================

dados = gerar_dados()

resultado, motivos = avaliar_lancamento(dados)
autonomia = calcular_autonomia(dados["energia"])

# =========================
# OUTPUT
# =========================

print("=== DADOS DA NAVE ===")
for chave, valor in dados.items():
    print(f"{chave}: {valor}")

print("\n=== RESULTADO ===")
print(resultado)

for motivo in motivos:
    print("-", motivo)

print("\n=== ANÁLISE ENERGÉTICA ===")
print(f"Autonomia restante: {autonomia:.2f} kWh")

if autonomia < 0:
    print("⚠ Energia insuficiente para decolagem!")
else:
    print("Energia suficiente para decolagem.")
