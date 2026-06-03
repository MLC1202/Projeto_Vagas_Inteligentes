from machine import Pin, PWM, I2C, SPI
from ssd1306 import SSD1306_I2C
from mfrc522 import MFRC522
import utime

# ── Pinagem ──────────────────────────────────────────
OLED_SDA   = 4
OLED_SCL   = 5
RFID_SCK   = 18
RFID_MOSI  = 19
RFID_MISO  = 16
RFID_RST   = 20
RFID_CS    = 17
SERVO_PIN  = 15
TRIG_PIN   = 7
ECHO_PIN   = 6
VAGA1_PIN  = 10
VAGA2_PIN  = 11

# ── Constantes ajustáveis ─────────────────────────────
SERVO_FECHADO      = 90
SERVO_ABERTO       = 180
TEMPO_ABERTO_MS    = 5000
DISTANCIA_CARRO_CM = 15

# ── Cartões cadastrados ───────────────────────────────
CARTOES = {
    "33-255-158-26-90": "JOJO",
    "48-13-102-86-13":  "FEFE",
    "192-81-142-88-71": "MC IG",
}

# ── Estado do estacionamento ──────────────────────────
# None = livre, uid do cartão = ocupada
vagas = {
    1: None,
    2: None,
}

# ── Inicialização dos periféricos ─────────────────────
i2c  = I2C(0, scl=Pin(OLED_SCL), sda=Pin(OLED_SDA), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

spi  = SPI(0, baudrate=1000000, polarity=0, phase=0,
           sck=Pin(RFID_SCK), mosi=Pin(RFID_MOSI), miso=Pin(RFID_MISO))
rfid = MFRC522(spi=spi, gpioRst=RFID_RST, gpioCs=RFID_CS)

servo = PWM(Pin(SERVO_PIN))
servo.freq(50)

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

# ── Funções auxiliares ────────────────────────────────

def mostrar_linhas(*linhas):
    oled.fill(0)
    y = 0
    for linha in linhas:
        oled.text(str(linha), 0, y)
        y += 10
    oled.show()

def mover_servo(angulo):
    duty = int(1638 + (angulo / 180) * (8192 - 1638))
    servo.duty_u16(duty)
    utime.sleep_ms(500)

def abrir_cancela():
    mover_servo(SERVO_ABERTO)

def fechar_cancela():
    mover_servo(SERVO_FECHADO)

def medir_distancia_cm():
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(10)
    trig.low()

    timeout = utime.ticks_us()
    while echo.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), timeout) > 30000:
            return None

    inicio = utime.ticks_us()
    while echo.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), inicio) > 30000:
            return None

    fim = utime.ticks_us()
    return utime.ticks_diff(fim, inicio) * 0.0343 / 2

def tem_carro_na_cancela():
    d = medir_distancia_cm()
    return d is not None and d < DISTANCIA_CARRO_CM

def obter_vaga_livre():
    for num, uid in vagas.items():
        if uid is None:
            return num
    return None

def quantidade_vagas_livres():
    return sum(1 for uid in vagas.values() if uid is None)

def cartao_esta_dentro(uid):
    for num, ocupante in vagas.items():
        if ocupante == uid:
            return num
    return None

def ler_cartao():
    status, tagtype = rfid.request(rfid.REQIDL)
    if status == rfid.OK:
        status, uid = rfid.SelectTagSN()
        if status == rfid.OK:
            return "{}-{}-{}-{}-{}".format(uid[0], uid[1], uid[2], uid[3], uid[4])
    return None

def controlar_cancela():
    abrir_cancela()
    inicio = utime.ticks_ms()
    while True:
        passado = utime.ticks_diff(utime.ticks_ms(), inicio)
        carro   = tem_carro_na_cancela()
        if passado >= TEMPO_ABERTO_MS and not carro:
            break
        if carro:
            mostrar_linhas("Carro detectado", "Aguarde...", "Cancela aberta")
        utime.sleep_ms(300)
    mostrar_linhas("Fechando", "cancela...")
    fechar_cancela()

def tela_inicial():
    livres = quantidade_vagas_livres()
    v1 = "livre" if vagas[1] is None else "ocupada"
    v2 = "livre" if vagas[2] is None else "ocupada"
    mostrar_linhas(
        "Aproxime o cartao",
        "Vagas: {}".format(livres),
        "V1: {}".format(v1),
        "V2: {}".format(v2),
    )
    fechar_cancela()

# ── Loop principal ────────────────────────────────────

tela_inicial()

while True:
    uid = ler_cartao()

    if uid is not None:
        print("Cartão lido:", uid)

        if uid in CARTOES:
            nome = CARTOES[uid]
            vaga_ocupada_pelo_cartao = cartao_esta_dentro(uid)

            if vaga_ocupada_pelo_cartao is not None:
                # ── SAÍDA ──
                vagas[vaga_ocupada_pelo_cartao] = None
                mostrar_linhas("Ate logo,", nome,
                               "Vaga {} liberada".format(vaga_ocupada_pelo_cartao),
                               "Saindo...")
                controlar_cancela()
                utime.sleep(2)

            else:
                # ── ENTRADA ──
                vaga = obter_vaga_livre()
                if vaga is not None:
                    vagas[vaga] = uid
                    mostrar_linhas("Bem-vindo,", nome,
                                   "Vaga: {}".format(vaga),
                                   "Abrindo...")
                    controlar_cancela()
                    mostrar_linhas("Va para",
                                   "vaga {}".format(vaga))
                    utime.sleep(2)
                else:
                    mostrar_linhas("Estacionamento",
                                   "cheio!",
                                   "Acesso negado")
                    utime.sleep(2)
        else:
            mostrar_linhas("Cartao nao",
                           "cadastrado",
                           "Acesso negado")
            utime.sleep(2)

    tela_inicial()
    utime.sleep_ms(200)
