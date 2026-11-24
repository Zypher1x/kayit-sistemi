kayıt_durumu = False
giriş_durumu = False
x = False
deneme = 0

while x == False:
    print('Kayıt-Giriş-Çıkış')
    işlem = input().lower()


    if işlem == 'kayıt':
        if kayıt_durumu == True:
            print('Zaten Kayıtlısınız. Lütfen Giriş Yapınız.')

        while kayıt_durumu == False:
            kayıt_kullanıcı_adı = input('Kullanıcı Adınızı Giriniz:')
            kayıt_şifre = input('Şifrenizi Giriniz:')
            kayıt_şifre_tekrar = input('Şifrenizi Tekrar Girniz:')

            if kayıt_şifre == kayıt_şifre_tekrar:
                print('Başarılı Bir Şekilde Kayıt Oldunuz.')
                print('Artık Giriş Yapabilirsiniz')
                kayıt_durumu = True
            else:
                print('Şifreleriniz Eşleşmiyor. Birdaha Deneyiniz.')

    elif işlem == 'giriş' and kayıt_durumu == False:
            print('Lütfen İlk Başta Kayıt Olunuz.')


    elif işlem == 'giriş':
        while giriş_durumu == False:
            if kayıt_durumu == True:
                giriş_kullanıcı_adı = input('Kullanıcı Adınızı Giriniz:')
                giriş_şifre = input('Şifrenizi Giriniz:')
                if giriş_kullanıcı_adı == kayıt_kullanıcı_adı and giriş_şifre == kayıt_şifre:
                    print('Başarılı Bir Şekilde Giriş Yaptınız.')
                    giriş_durumu = True
                    x = True
                else:
                    deneme = deneme + 1
                    if deneme == 5:
                        print('Hesabınız Kitlendi')
                        x = True
                        break
                    else:
                        print('Kullanıcı Adınız yada Şifreniz Yanlış. Tekrar Deneyiniz')


    elif işlem == 'çıkış':
        print('Sistemden Çıkış Yapılıyor...')
        break

    elif x == True:
        break

    else:
        print('Geçerli Bir İşlem Giriniz.')
