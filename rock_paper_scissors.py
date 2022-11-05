#Taş, kağıt, makas oyunu
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Taş, kağıt, makas oyununa başlamak istiyorsan;")
gameImages =  [rock, paper, scissors]
selected = int(input("Seçimlerde kullanabileceğiniz sayılar 0, 1 ve 2'dir.\nTaş için 0; \nKağıt için 1; \nMakas için 2;\n"))
print("Senin Seçimin:\n")
print(gameImages[selected])
pcList = [0,1,2]
pcSelected = random.choice(pcList)
print(pcSelected)
print("Bilgisayarın Seçimi:\n")
print(gameImages[pcSelected])

if pcSelected == 0:
    if selected == 2:
        print("Kaybettin")
    elif selected == 1:
        print("Kazandın")
    elif selected == pcSelected:
        print("Berabere")
    else: print("Geçersiz tuşlama yapıldı. Oynamak için tekrar başlayınız.")

if pcSelected == 1:
    if selected == 0:
        print("Kaybettin")
    elif selected == 2:
        print("Kazandın")
    elif selected == pcSelected:
        print("Berabere")
    else:
        print("Geçersiz tuşlama yapıldı. Oynamak için tekrar başlayınız.")

if pcSelected == 2:
    if selected == 1:
        print("Kaybettin")
    elif selected == 0:
        print("Kazandın")
    elif selected == pcSelected:
        print("Berabere")
    else:
        print("Geçersiz tuşlama yapıldı. Oynamak için tekrar başlayınız.")

