import pygmame

pygame.mixer.init()
pygame.init()
pygmame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.event.wait()