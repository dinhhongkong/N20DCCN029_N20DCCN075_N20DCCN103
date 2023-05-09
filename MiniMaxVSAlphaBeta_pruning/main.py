from menu import *

pygame.init()

if __name__ == '__main__':
    # Tiêu đề và icon game:
    pygame.display.set_caption('Tic-Tac-Toe')
    icon = pygame.image.load('img/icon.png')
    pygame.display.set_icon(icon)
    menu = Menu()
    menuAlgo = MenuAlgo()
    playGame = Gaming()
    menu.drawMenu()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if SCREEN == Screen.MENU:
                SCREEN = menu.action(event)
            elif SCREEN == Screen.SELECT_ALGO:
                SCREEN = menuAlgo.action(event, playGame, menu.get_btnAi().selected)
            elif SCREEN == Screen.GAMING:
                SCREEN = playGame.action(event, menuAlgo)

        pygame.display.update()
