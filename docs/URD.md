# URD — Sistema de Vagas Inteligente

**Projeto:** Vaga Inteligente — Raspberry Pi Pico  
**Versão:** 1.0.0  
**Data:** 03/06/2026  
**Curso/Disciplina:** Microcontroladores e Sistemas Embarcados

---

## 1. Conceito / Descrição do projeto

O projeto consiste em um sistema embarcado para controle inteligente de acesso a um estacionamento com **2 vagas**.  
A solução utiliza **Raspberry Pi Pico** programado em **MicroPython**, com leitura de **RFID** para identificação do usuário, sensores de obstáculo **IR** para verificar a ocupação das vagas, um sensor **ultrassônico HC-SR04** para segurança da cancela, um **servo motor** para acionamento mecânico e um **display OLED** para exibição de mensagens ao usuário.

O sistema deve permitir a entrada apenas de usuários cadastrados e somente quando houver vaga livre. Caso o estacionamento esteja cheio ou o cartão não esteja cadastrado, o acesso deve ser negado. A cancela deve permanecer aberta enquanto houver um veículo na região de passagem, evitando fechamento indevido.

---

## 2. Diagrama de blocos do sistema

O sistema é composto pelos seguintes módulos:

- **Microcontrolador:** Raspberry Pi Pico.
- **Leitor RFID:** MFRC522.
- **Sensores de vaga:** 2 sensores de obstáculo IR.
- **Sensor de segurança da cancela:** HC-SR04.
- **Atuador mecânico:** servo motor SG90/MG996.
- **Interface com o usuário:** display OLED I2C.

---

## 3. Requisitos do sistema

| ID | Requisito | Tipo |
|---|---|---|
| UR-01 | Ser composto por módulos prontos e de fácil acesso | Obrigatório |
| UR-02 | Identificar o usuário por meio de cartão/tag RFID | Obrigatório |
| UR-03 | Verificar a ocupação das vagas por sensores de obstáculo IR | Obrigatório |
| UR-04 | Controlar a abertura e o fechamento da cancela por servo motor | Obrigatório |
| UR-05 | Exibir mensagens de status em display OLED | Obrigatório |
| UR-06 | Permitir entrada apenas quando houver vaga livre | Obrigatório |
| UR-07 | Negar acesso quando o cartão não estiver cadastrado | Obrigatório |
| UR-08 | Negar acesso quando o estacionamento estiver cheio | Obrigatório |
| UR-09 | Detectar a presença de veículo na região da cancela com sensor ultrassônico | Obrigatório |
| UR-10 | Impedir o fechamento da cancela enquanto houver veículo na passagem | Obrigatório |
| UR-11 | Utilizar alimentação adequada em 3,3 V e 5 V conforme cada módulo | Obrigatório |
| UR-12 | Ser integrado com código funcional em MicroPython | Obrigatório |

---

## 4. Funcionamento esperado

1. O sistema inicia e mostra no display OLED a quantidade de vagas livres.
2. O usuário aproxima um cartão RFID.
3. O sistema verifica se o cartão está cadastrado.
4. Se o cartão for válido, o sistema verifica se existe vaga livre.
5. Se houver vaga livre, o display informa a vaga disponível e a cancela é aberta.
6. Se o estacionamento estiver cheio, o acesso é negado.
7. Se o cartão não estiver cadastrado, o acesso também é negado.
8. Após a entrada, a cancela só pode ser fechada quando o sensor ultrassônico indicar que não há veículo na região de passagem.

---

## 5. Tecnologias utilizadas

- **MicroPython**
- **Raspberry Pi Pico**
- **MFRC522**
- **Sensores IR de obstáculo**
- **HC-SR04**
- **Servo motor**
- **Display OLED I2C**


---

## 6. Justificativa das tecnologias

As tecnologias escolhidas atendem ao objetivo do projeto por serem compatíveis com uma solução de baixo custo e fácil montagem.  
O uso do Raspberry Pi Pico permite programação em MicroPython e boa integração com sensores e atuadores.  
O RFID garante identificação rápida, os sensores IR resolvem a detecção de vagas, o OLED facilita a interação com o usuário e o servo permite simular o acionamento da cancela de forma simples e funcional.

---

## 7. Resultado esperado

Espera-se um sistema funcional capaz de:

- controlar o acesso ao estacionamento;
- identificar usuários autorizados;
- indicar vagas livres;
- acionar a cancela automaticamente;
- aumentar a segurança do acesso;
- apresentar documentação clara e organizada no GitHub.
