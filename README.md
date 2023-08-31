# snake
# English explanation

This code is a simple Python game using the Pygame library. The goal of the game is to control a snake, eat food on the screen to grow longer, and avoid hitting the walls or itself. Let's break down the sections of the code:

Library Imports and Initial Setup:

pygame.init(): Initializes the Pygame library.
Defines initial settings such as screen dimensions and colors.
Creating the Screen and Settings:

pygame.display.set_mode(): Creates a game screen with the specified dimensions.
pygame.display.set_caption(): Sets the window title.
Time Control:

clock = pygame.time.Clock(): Creates a clock object to control the game's speed.
Initial Positions and Variables:

Defines the initial coordinates, speed, and dimensions of the snake and food.
Randomly generates the coordinates of the food.
Defines variables to control the snake's size and growth.
Main Game Loop:

The main game loop begins with while game_continue:.
When the game ends (game_over == True), it displays the "Game Over!" message and waits for the player to press the quit or restart keys.
Keyboard Controls:

pygame.event.get(): Handles keyboard and mouse events.
Controls the snake's movement by checking keyboard events to move it up, down, left, or right.
Snake Movement and Collision Detection:

Calculates the snake's coordinates and size updates.
Handles the snake eating food and growing.
Checks if the snake hits the screen boundaries or itself to determine if the game ends.
Updating the Game Screen:

pygame.display.update(): Updates the game screen.
Game Over and Cleanup:

****************************
# Turkce aciklama 
Bu kod, basit bir yılan oyunu için Python ve Pygame kütüphanesini kullanıyor. Oyundaki amacınız, yılanı kontrol ederek ekrandaki yemleri yemek ve yılanın büyümesini sağlamak. Aynı zamanda yılanın duvarlara veya kendi kendine çarpıp oyunu sonlandırmadan kaçınmaya çalışıyorsunuz. Şimdi kodun bölümlerini açıklayayım:

Kütüphane İmportları ve Başlangıç Ayarları:
____________________________________
pygame.init(): Pygame kütüphanesini başlatır.
Ekran boyutları ve renkler gibi başlangıç ayarlarını tanımlar.
Ekran Oluşturma ve Ayarlar:

pygame.display.set_mode(): Belirtilen boyutta bir oyun ekranı oluşturur.
pygame.display.set_caption(): Pencere başlığını ayarlar.
Zaman Kontrolü:

saat = pygame.time.Clock(): Oyun hızını kontrol etmek için bir saat objesi oluşturur.
Başlangıç Konumları ve Değişkenler:

Yılanın ve yiyeceğin başlangıç koordinatlarını, hızını ve boyutlarını tanımlar.
Yiyecek koordinatları rastgele belirlenir.
Yılanın boyutunu ve büyüme durumunu kontrol eden değişkenler tanımlanır.
Ana Oyun Döngüsü:

Oyunun ana döngüsü while oyun_devam: ile başlar.
Oyun bittiğinde (oyun_bitti == True), "Oyun Bitti!" mesajını görüntüler ve oyuncudan çıkış veya yeniden başlama tuşlarına basmasını bekler.
Tus Kontrolleri:

pygame.event.get(): Klavye ve fare olaylarını işler.
Klavye olaylarını kontrol ederek yılanın yukarı, aşağı, sola veya sağa hareket etmesini sağlar.
Yılanın Hareketi ve Çarpışma Kontrolü:

Yılanın koordinatlarını ve boyunu güncellemek için gerekli hesaplamaları yapar.
Yılanın yiyeceği yemesi durumunda büyümesini sağlar.
Yılanın ekran sınırlarına veya kendi kendine çarpışmasına göre oyunun bitip bitmediğini kontrol eder.
Oyun Ekranının Güncellenmesi:

pygame.display.update(): Oyun ekranını günceller.
Oyun Sonu ve Temizlik:

Pygame'i kapatır ve programı sonlandırır.
Bu kod, basit bir yılan oyununun temel mantığını gösterir. Ancak, oyunun daha karmaşık hale getirilmesi ve grafiksel iyileştirmelerin yapılması için pek çok fırsat bulunmaktadır.
