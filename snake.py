import pygame
import time
import random

pygame.init()

# Ekran boyutları
ekran_genislik = 800
ekran_yukseklik = 600

# Renkler
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)

# Ekran oluşturma
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption('Yılan Oyunu')

# Zaman kontrolü
saat = pygame.time.Clock()

# Yılan ve yiyecek başlangıç koordinatları
yilan_x = ekran_genislik / 2
yilan_y = ekran_yukseklik / 2
yilan_hizi = 10
yilan_genislik = 15
yilan_yukseklik = 15

yiyecek_x = round(random.randrange(0, ekran_genislik - yilan_genislik) / 10.0) * 10.0
yiyecek_y = round(random.randrange(0, ekran_yukseklik - yilan_yukseklik) / 10.0) * 10.0

# Yılanın boyunu ve hızını kontrol eden değişkenler
yilan_parcalari = []
yilan_boyu = 1

# Ana döngü
oyun_bitti = False
oyun_devam = True
while oyun_devam:

    while oyun_bitti:
        ekran.fill(beyaz)
        font = pygame.font.SysFont(None, 50)
        mesaj = font.render("Oyun Bitti! Yeniden başlamak için R tuşuna basın. Çıkış yapmak için Q tuşuna basın.", True, siyah)
        ekran.blit(mesaj, (ekran_genislik / 6, ekran_yukseklik / 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    oyun_devam = False
                    oyun_bitti = False
                if event.key == pygame.K_r:
                    yilan_x = ekran_genislik / 2
                    yilan_y = ekran_yukseklik / 2
                    yilan_hizi = 10
                    yilan_parcalari = []
                    yilan_boyu = 1
                    yiyecek_x = round(random.randrange(0, ekran_genislik - yilan_genislik) / 10.0) * 10.0
                    yiyecek_y = round(random.randrange(0, ekran_yukseklik - yilan_yukseklik) / 10.0) * 10.0
                    oyun_bitti = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            oyun_devam = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yilan_hizi = -10
                yilan_y = 0
            elif event.key == pygame.K_RIGHT:
                yilan_hizi = 10
                yilan_y = 0
            elif event.key == pygame.K_UP:
                yilan_hizi = 0
                yilan_y -= 10  # Yılanı yukarı yönde hareket ettir
            elif event.key == pygame.K_DOWN:
                yilan_hizi = 0
                yilan_y += 10  # Yılanı aşağı yönde hareket ettir
    if yilan_x == yiyecek_x and yilan_y == yiyecek_y:
        yiyecek_x = round(random.randrange(0, ekran_genislik - yilan_genislik) / 10.0) * 10.0
        yiyecek_y = round(random.randrange(0, ekran_yukseklik - yilan_yukseklik) / 10.0) * 10.0
        yilan_boyu += 1


    if yilan_x >= ekran_genislik or yilan_x < 0 or yilan_y >= ekran_yukseklik or yilan_y < 0:
        oyun_bitti = True

    yilan_x += yilan_hizi
    ekran.fill(beyaz)

    pygame.draw.rect(ekran, yesil, [yiyecek_x, yiyecek_y, yilan_genislik, yilan_yukseklik])
    yilan_bas = []
    yilan_bas.append(yilan_x)
    yilan_bas.append(yilan_y)
    yilan_parcalari.append(yilan_bas)
    if len(yilan_parcalari) > yilan_boyu:
        del yilan_parcalari[0]

    for parca in yilan_parcalari[:-1]:
        if parca == yilan_bas:
            oyun_bitti = True

    pygame.draw.rect(ekran, siyah, [yilan_x, yilan_y, yilan_genislik, yilan_yukseklik])

    saat.tick(30)
    pygame.display.update()

    if yilan_x == yiyecek_x and yilan_y == yiyecek_y:
        yiyecek_x = round(random.randrange(0, ekran_genislik - yilan_genislik) / 10.0) * 10.0
        yiyecek_y = round(random.randrange(0, ekran_yukseklik - yilan_yukseklik) / 10.0) * 10.0
        yilan_boyu += 1

pygame.quit()
quit()
