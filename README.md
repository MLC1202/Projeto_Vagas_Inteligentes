# Vaga Inteligente (2 vagas) — Raspberry Pi Pico

Sistema embarcado para controle de acesso de um estacionamento com 2 vagas.
Identificação por RFID, detecção de ocupação por sensores IR de obstáculo e acionamento de cancela via servo,
com mensagens em display.

## Diagrama de blocos
<img width="798" height="583" alt="DiagramaDeBlocosEstacionamento drawio (1)" src="https://github.com/user-attachments/assets/a209d5c0-69cc-4502-a508-f493c519eeca" />



## Funcionalidades
- Leitura de cartão RFID para identificação do usuário
- Verificação de vagas livres/ocupadas usando sensores de obstáculo
- Detecção de aproximação na cancela usando sensor de distância
- Display OLED com mensagens de status:
  - "Desculpe, estacionamento cheio"
  - "Bem-vindo, NOME. Dirija-se à vaga X"
- Controle da cancela por servo motor
- Controle de entrada com:
  - Identificação por RFID
  - Verificação de vaga disponível
  - Abertura da cancela
- Controle de saída com:
  - Identificação por RFID
  - Detecção do veículo na região da cancela
  - Confirmação de liberação da vaga pelo sensor de obstáculo

## Hardware
- Raspberry Pi Pico
- Leitor RFID MFRC-522 + cartões/tags
- 2x Sensor de Obstáculo IR (1 por vaga)
- Sensor de distância – Ultrassom HC-SR04 (cancela)
- Servo MG996 (cancela) + fonte 5V (2A)
- Display OLED I2C 128×32
- Conversor 
- Protoboard + jumpers + cabo USB (programação/alimentação do Pico)

## Como rodar (exemplo)
> Preencher quando o projeto estiver configurado (MicroPython/Thonny ou Pico SDK/PlatformIO).

## Documentação
- `docs/documentacao.md`
- `docs/diagrama-blocos.png`
