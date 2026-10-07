import time
from datetime import datetime

class SafePole:
    def __init__(self, local):
        self.local = local
        self.luz = False
        self.monitoramento = True

    def acionar_luz(self):
        if not self.luz:
            self.luz = True
            print("💡 Iluminação de segurança ATIVADA.")

    def desligar_luz(self):
        if self.luz:
            self.luz = False
            print("💡 Iluminação de segurança DESATIVADA.")

    def analisar_situacao(self, camera, microfone, movimento):
        """
        Simulação da análise feita pela inteligência artificial.
        Em um projeto real, esses dados poderiam vir de câmeras
        e sensores conectados ao poste.
        """

        risco = False
        motivo = []

        # Análise da câmera
        if camera == "briga":
            risco = True
            motivo.append("possível briga detectada")

        elif camera == "queda":
            risco = True
            motivo.append("possível queda detectada")

        # Análise do microfone
        if microfone == "grito":
            risco = True
            motivo.append("som de grito detectado")

        elif microfone == "disparo":
            risco = True
            motivo.append("som semelhante a disparo detectado")

        # Análise do sensor de movimento
        if movimento == "movimento_incomum":
            risco = True
            motivo.append("movimentação incomum detectada")

        if risco:
            self.acionar_luz()
            self.enviar_alerta(motivo)
        else:
            print("✅ Situação normal. Nenhum risco identificado.")
            self.desligar_luz()

    def enviar_alerta(self, motivos):
        horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print("\n🚨 ALERTA PARA A CENTRAL DE MONITORAMENTO")
        print(f"📍 Local: {self.local}")
        print(f"🕐 Horário: {horario}")
        print("⚠️ Possíveis situações identificadas:")

        for motivo in motivos:
            print(f"   - {motivo}")

        print("📡 Alerta enviado com sucesso!\n")


# -----------------------------
# SIMULAÇÃO DO SAFEPOLE
# -----------------------------

safe_pole = SafePole("Londrina - PR")

print("====================================")
print("        SAFEPOLE - SMART CITY")
print("====================================")
print("Sistema de segurança iniciado.\n")

# Exemplo 1: situação normal
safe_pole.analisar_situacao(
    camera="normal",
    microfone="normal",
    movimento="normal"
)

time.sleep(2)

# Exemplo 2: possível situação de risco
safe_pole.analisar_situacao(
    camera="briga",
    microfone="grito",
    movimento="movimento_incomum"
)

time.sleep(2)

# Exemplo 3: possível queda
safe_pole.analisar_situacao(
    camera="queda",
    microfone="normal",
    movimento="normal"
)
