import pygame
import sys
import math

# Inicialização do pygame
pygame.init()

# Configurações da janela
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Estrada com Curvas")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# Configurações da estrada
horizon_y = 50  # Linha do horizonte
road_top_y = horizon_y + 100  # Ponto superior do triângulo principal
road_base_y = HEIGHT  # Base da estrada
road_width_top = 100  # Largura do topo do triângulo principal
road_width_base = 400  # Largura da base do triângulo principal

# Configurações do triângulo invertido (curvas)
curve_offset = 0  # Deslocamento inicial da base
curve_speed = 2  # Velocidade do deslocamento
curve_amplitude = 400  # Amplitude máxima das curvas
curve_frequency = 0.02  # Frequência das curvas

# Função principal
def main():
    global curve_offset
    global road_top_y
    global horizon_y
    clock = pygame.time.Clock()
    running = True
    frame = 0  # Contador de quadros para gerar movimento dinâmico

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualizar o deslocamento da base do triângulo invertido
        road_top_y=road_top_y+20
        if road_top_y>road_base_y - 100:
            road_top_y=100
            curve_offset = math.sin(frame * curve_frequency) * curve_amplitude
            frame += curve_speed

        # Desenhar a cena
        WINDOW.fill(BLACK)

        # Linha do horizonte
        pygame.draw.line(WINDOW, WHITE, (0, horizon_y), (WIDTH, horizon_y), 2)
        
        # Triângulo principal (estrada)
        main_road_points = [
            (WIDTH // 2 - road_width_top // 2, road_top_y),  # Topo esquerdo
            (WIDTH // 2 + road_width_top // 2, road_top_y),  # Topo direito
            (WIDTH // 2 + road_width_base // 2, road_base_y),  # Base direita
            (WIDTH // 2 - road_width_base // 2, road_base_y),  # Base esquerda
        ]
        pygame.draw.polygon(WINDOW, WHITE, main_road_points)

        # Triângulo invertido (curvas)
        curve_points = [
            (WIDTH // 2 - road_width_top // 2, road_top_y),  # Topo esquerdo
            (WIDTH // 2 + road_width_top // 2, road_top_y),  # Topo direito
            (WIDTH // 2 + curve_offset,horizon_y),  # Ponta invertida
        ]
        pygame.draw.polygon(WINDOW, WHITE, curve_points)

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

