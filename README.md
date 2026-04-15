# Vaga Inteligente (2 vagas) — Raspberry Pi Pico

Sistema embarcado para controle de acesso de um estacionamento com 2 vagas.
Identificação por RFID, detecção de ocupação por sensores IR de obstáculo e acionamento de cancela via servo,
com mensagens em display.

## Funcionalidades
- Leitura de cartão RFID (UID / identificação)
- Verificação de vagas livres/ocupadas (2x sensor de obstáculo IR)
- Display com status:
  - "Desculpe, estacionamento cheio"
  - "Bem-vindo, NOME. Dirija-se à vaga X"
- Controle de cancela via servo
- Saída com dupla verificação (cartão + confirmação do sensor da vaga vazia)

## Hardware
- Raspberry Pi Pico
- Leitor RFID MFRC-522 + cartões/tags
- 2x Sensor de Obstáculo IR (1 por vaga)
- Servo MG996 (cancela) + fonte 5V (2A)
- Display OLED I2C 128×32
- Protoboard + jumpers + cabo USB (programação/alimentação do Pico)

## Como rodar (exemplo)
> Preencher quando o projeto estiver configurado (MicroPython/Thonny ou Pico SDK/PlatformIO).

## Documentação
- `docs/documentacao.md`
- `docs/diagrama-blocos.png`
