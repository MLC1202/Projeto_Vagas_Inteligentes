# Vaga Inteligente (2 vagas) — Raspberry Pi Pico

Sistema embarcado para controle de acesso de um estacionamento com 2 vagas.
Identificação por RFID, detecção de ocupação por ultrassom e acionamento de cancela via servo,
com mensagens em display.

## Funcionalidades
- Leitura de cartão RFID (UID / identificação)
- Verificação de vagas livres/ocupadas (2x ultrassom)
- Display com status:
  - "Desculpe, estacionamento cheio"
  - "Bem-vindo, NOME. Dirija-se à vaga X"
- Controle de cancela via servo
- Saída com dupla verificação (cartão + confirmação do sensor da vaga vazia)

## Hardware
- Raspberry Pi Pico
- RFID MFRC-522
- 2x HC-SR04 (1 por vaga)
- Servo MG996
- Display OLED I2C

## Como rodar (exemplo)
> Preencher quando o projeto estiver configurado (PlatformIO ou Pico SDK).

## Documentação
- `docs/documentacao.md`
- `docs/diagrama-blocos.png`
