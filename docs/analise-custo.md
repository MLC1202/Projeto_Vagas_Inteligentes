# Análise básica de custos — Sistema de Vagas Inteligente

Valores estimados em R$ com base em buscas no Mercado Livre em junho/2026.  
Os preços servem apenas como referência para análise de viabilidade.

## 1. Componentes principais

| Componente                              | Quantidade | Preço unitário aprox. (R$) | Custo total aprox. (R$) | Observação |
|----------------------------------------|------------|----------------------------|--------------------------|-----------|
| Raspberry Pi Pico WH                   | 1          | 50,00                      | 50,00                    | Versão com headers soldados |
| Leitor RFID MFRC-522 (kit com tags)    | 1          | 25,00                      | 25,00                    | Inclui cartão e chaveiro RFID |
| Servo motor MG996R metálico            | 1          | 40,00                      | 40,00                    | Alto torque para a cancela |
| Display OLED 0,96\" I2C SSD1306        | 1          | 25,00                      | 25,00                    | 128×64 ou 128×32 px |
| Sensor ultrassônico HC-SR04           | 1          | 10,00                      | 10,00                    | Detecção de carro na cancela |
| Sensor de obstáculo IR                 | 2          | 5,00                       | 10,00                    | Um por vaga |
| Conversor de nível lógico I2C 4 canais | 1          | 10,00                      | 10,00                    | Protege o GPIO do Pico (ECHO 5V) |
| Protoboard + jumpers                   | 1 kit      | 20,00                      | 20,00                    | Montagem do circuito |
| Fonte 5 V (USB ou dedicada)            | 1          | 30,00                      | 30,00                    | Alimentação do sistema/servo |

**Subtotal estimado:** ~R$ 220,00

## 2. Custos adicionais opcionais

| Item                           | Quantidade | Custo aprox. (R$) | Observação |
|--------------------------------|------------|--------------------|-----------|
| Caixa/acrílico/estrutura mecânica | 1      | 30,00              | Simular cancela e vagas |
| Materiais diversos (parafusos, fios extras, etc.) | 1 | 20,00 | Itens de consumo gerais |

**Total com opcionais:** ~R$ 270,00

## 3. Comentários sobre custo-benefício

- Todos os módulos utilizados são **populares, baratos e fáceis de encontrar**, o que atende ao requisito de usar componentes de fácil acesso.  
- O microcontrolador é o item mais caro, mas permite reaproveitamento em outros projetos e facilita a programação em MicroPython.  
- O custo total é compatível com um **protótipo acadêmico de baixo custo**, considerando que muitos itens podem ser reaproveitados de laboratório ou de outros projetos.
