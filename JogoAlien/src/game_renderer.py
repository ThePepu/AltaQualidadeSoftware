import sys
import pygame


class GameRenderer:
    """Responsável por desenhar todos os elementos na tela."""
    def __init__(self, screen, settings, ship, bullets, aliens) -> None:
        self.screen = screen
        self.settings = settings
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens

    def _render_screen(self) -> None:
        """Redesenha a tela a cada passagem pelo laço."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self._draw_bullets()
        pygame.display.flip()

    def _draw_bullets(self) -> None:
        """Desenha todos os projéteis na tela."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()