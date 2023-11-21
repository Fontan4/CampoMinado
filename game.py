import pygame
import os

class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = screenSize[0] // self.board.getSize()[1], screenSize[1] // self.board.getSize()[0]
        self.loadImages()

        
    
    def run(self):
        pygame.init()
        pygame.display.set_caption("Campo Minado")
        pygame.display.set_icon(self.images["icon"])
        self.screen = pygame.display.set_mode(self.screenSize)
        running = True
        while running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()
            pygame.display.flip()
        pygame.quit()
    
    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self):
        self.images = {}
        for file in os.listdir("img"):
            if not file.endswith(".png"):
                continue
            image = pygame.image.load(r"img/" + file)
            print (self.pieceSize)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[file.split(".")[0]] = image
    
    def getImage(self, piece):
        string = "unclicked-bomb" if piece.getHasBomb() else str(piece.getNumAround())
        return self.images[string]