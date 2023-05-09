
from button import Button
from algorithm import *


class Menu:
    def __init__(self):
        self.btnAi = Button(150, 200, 'AI')
        self.btnNguoi = Button(575, 200, 'NGƯỜI')
        self.btnTiep = Button(360, 740, 'TIẾP')
        self.btnNguoi.set_selected(True)

    def drawMenu(self):
        DISPLAYSURF.blit(MENU_BG, (0, 0))
        self.btnAi.update()
        self.btnNguoi.update()
        self.btnTiep.update()
        font = pygame.font.SysFont('cambria', 40, bold=True)
        DISPLAYSURF.blit(font.render('CHỌN BÊN ĐI TRƯỚC', True, BLACK, WHITE), (155, 100))

    def action(self, event):
        if self.btnAi.checkForInput(pygame.mouse.get_pos(), event):
            self.btnAi.set_selected(True)
            self.btnNguoi.set_selected(False)
            self.btnAi.update()
            self.btnNguoi.update()

        if self.btnNguoi.checkForInput(pygame.mouse.get_pos(), event):
            self.btnAi.set_selected(False)
            self.btnNguoi.set_selected(True)
            self.btnAi.update()
            self.btnNguoi.update()

        if self.btnTiep.checkForInput(pygame.mouse.get_pos(), event):
            MenuAlgo().drawMenuAlgo()
            return Screen.SELECT_ALGO
        else:
            return Screen.MENU

    def get_btnAi(self):
        return self.btnAi

    def get_btnNguoi(self):
        return self.btnNguoi

    def get_btnTiep(self):
        return self.btnTiep


class MenuAlgo:
    def __init__(self):
        self.btnMinMax = Button(150, 200, 'Min_Max')
        self.btnAlphaBeta = Button(575, 200, 'Alpha_Beta')
        self.btnBatDau = Button(360, 740, 'BẮT ĐẦU')
        self.btnQuayLai = Button(80, 40, 'QUAY LẠI', 150, 50)
        self.btnAlphaBeta.set_selected(True)

    def drawMenuAlgo(self):
        DISPLAYSURF.blit(MENU_BG, (0, 0))
        self.btnMinMax.update()
        self.btnAlphaBeta.update()
        self.btnBatDau.update()
        self.btnQuayLai.update()
        font = pygame.font.SysFont('cambria', 40, bold=True)
        DISPLAYSURF.blit(font.render('CHỌN THUẬT TOÁN', True, BLACK, WHITE), (170, 100))

    def get_btnAnphaBeta(self):
        return self.btnAlphaBeta

    def action(self, event, play_game, al_goes_first):
        if self.btnMinMax.checkForInput(pygame.mouse.get_pos(), event):
            self.btnMinMax.set_selected(True)
            self.btnAlphaBeta.set_selected(False)
            self.btnMinMax.update()
            self.btnAlphaBeta.update()

        if self.btnAlphaBeta.checkForInput(pygame.mouse.get_pos(), event):
            self.btnMinMax.set_selected(False)
            self.btnAlphaBeta.set_selected(True)
            self.btnMinMax.update()
            self.btnAlphaBeta.update()

        if self.btnBatDau.checkForInput(pygame.mouse.get_pos(), event):
            if self.btnAlphaBeta.selected:
                txt = "Thuật toán cắt tỉa Alpha Beta"
            else:
                txt = "Thuật toán Min_Max"
            Gaming().draw(txt)
            if al_goes_first:
                if self.btnAlphaBeta.selected:
                    play_game.Al_alpha_beta_play_first()
                else:
                    play_game.Al_min_max_first()

            return Screen.GAMING

            # return Screen.ALGORITHM
        elif self.btnQuayLai.checkForInput(pygame.mouse.get_pos(), event):
            Menu().drawMenu()
            return Screen.MENU
        return Screen.SELECT_ALGO

class Gaming:
    def __init__(self):
        self.imgX = pygame.image.load('img/X.png')
        self.imgY = pygame.image.load('img/O.png')
        self.gameBg = pygame.image.load('img/tic-tac-toe.jpg')
        self.alphaBeta = AlphaBeta()
        self.minMax = MinMax()

    def draw(self,txt):
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(self.gameBg, (0, 50))
        font = pygame.font.SysFont('cambria', 20, bold=True)
        # DISPLAYSURF.blit(font.render(txt, True, BLACK, WHITE), (440, 150))
        DISPLAYSURF.blit(font.render(txt, True, BLACK, WHITE), (100, 100))
        DISPLAYSURF.blit(FONT.render("MÁY: ", True, BLACK, WHITE), (460, 150))
        DISPLAYSURF.blit(FONT.render("NGƯỜI: ", True, BLACK, WHITE), (460, 220))
        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load('img/O.png'),(70, 70)), (570, 130))
        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load('img/X.png'), (70, 70)), (570, 200))
        DISPLAYSURF.blit(pygame.transform.scale(pygame.image.load('img/back.png'), (90, 90)), (10, 10))

    def Al_alpha_beta_play_first(self):
        self.alphaBeta.play_alpha_beta(ai_First= True)

    def Al_min_max_first(self):
        self.minMax.play_min_max(ai_First= True)


    def action(self,event, menuAlgo, ):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for i in range(0,3):
                for j in range(0,3):
                    if 70 + j*110 < x < 180 + j*110 and 220 + i*110 < y < 330 + i*110:
                        if menuAlgo.get_btnAnphaBeta().selected:
                            self.alphaBeta.play_alpha_beta(i, j)
                            print("Alpha")
                        else:
                            self.minMax.play_min_max(i, j)
                            print("Minmax")
                        return Screen.GAMING

            if 10 < x < 100 and 10 < y < 100:
                menuAlgo.drawMenuAlgo()
                self.alphaBeta.initialize_game()
                self.minMax.initialize_game()
                return Screen.SELECT_ALGO


        return Screen.GAMING













