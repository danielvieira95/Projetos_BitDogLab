from machine import Pin
import time

# Configuração dos pinos
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)
led_vermelho = Pin(12, Pin.OUT)
led_verde = Pin(11, Pin.OUT)
led_azul = Pin(13, Pin.OUT)

# Inicialização do LED
led_vermelho.value(0)
led_verde.value(0)
led_azul.value(0)

while True:
    # Verifica se o Botão A foi pressionado
    if botao_a.value() == 0:
        for i in range(5):

            led_azul.value(1)  # Liga o LED azul
            time.sleep(0.1)
            led_azul.value(0) 
            time.sleep(0.1)
            i+=1
    else:
        led_azul.value(0)  # Desliga o LED azul
    
    # Pequeno atraso para evitar leitura errada devido ao bounce do botão
    time.sleep(0.1)
