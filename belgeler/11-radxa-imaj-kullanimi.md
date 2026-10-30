# Radxa Zero 3W · Açılabilen Armbian kartı (imaj kullanım notları)

> **2026-10-21: Eylül'deki iki taban imaj (20260920, 20260929) Releases'ten kaldırıldı;** çok eskiydiler. Hazır kart için [replika imajını](https://github.com/fanhao375/microduck-replica/releases/latest) kullanın: yazın ve kullanın; ana program, yürüme modeli ve Studio ile gelir. Bu dizindeki kart yapım betikleri durmaktadır, kendi kartınızı yapmak için eskisi gibi kullanılabilir; aşağıda o iki Release'e değinilen yerler yalnızca tarihçedir.

Bu imaj, bu makinede daha önce yaşanan bir sorunu çözer: **denenen resmi Armbian imajı Radxa Zero 3W V1.12 üzerinde açılmıyordu** (giriş yapılamıyor, yerel ağda bulunamıyor);
Radxa'nın kendi önyükleyicisi (bootloader) konunca açıldı. Armbian'ın resmi çekirdeği ve sistem paketleri korunur; önyükleme ile gerekli açılış, giriş ve ağ yapılandırması ayarlanır.

Herkese açık imaj **WiFi adı ve parolası içermez;** ilk açılışta yaklaşık 2~3 dakika bekleyin, ardından USB seri bağlantısıyla giriş yapıp ağı yapılandırın. Bekleme süresi ve yeşil LED durumu, gerçekten giriş yapılabildiğinin doğrulaması yerine geçmez.

- Uygun donanım: **Radxa Zero 3W V1.12** (2024-11 sonrası üretim, AIC8800D80 WiFi'li seri); diğer seriler için aşağıda 6. bölüme bakın
- Taban: Armbian 26.2.1 Trixie vendor çekirdeği 6.1.115 minimal (resmi, değiştirilmemiş)
- Neden böyle olduğu ve nasıl tespit edildiği: [Tuzaklar](14-tuzaklar.md) (Yazılım bölümü)

> 2026-09-28 kamera gelişmesi: Flat kablonun yönü/teması düzeltildikten sonra Radxa resmi B1 imajı IMX219'u tanıdı ve 40 karelik 1920×1080 kısa testi tamamladı; bu projenin imajıyla yeniden test yapılması planlanıyor; resmi sistemdeki sonuç bu imajın kamera kabulü sayılamaz. Bkz. [Bağlantı şeması ve tam kayıt](../tools/radxa/摄像头调试记录-20260928.md). Yeşil LED'in çift yanıp sönmesi normal `heartbeat` olabilir; tek başına açılış hatası kanıtı sayılmaz.

> **2026-09-28 ağ bağlantısı düzeltmesi:** 20 Eylül tarihli kart yapım betiği `wlan0` için DHCP yapılandırmasını atlamıştı. WiFi adı ve parolasını kaydetmek yalnızca kimlik doğrulama yapılandırmasını tamamlar; varsayılan netplan sadece kablolu ağ kartlarını kapsar. Betik artık düzeltildi; eski kartlar için 4. bölümdeki yapılandırmayı eklemek yeterlidir, yalnızca bunun için kartı yeniden yazmak gerekmez. Release eki `armbian-26.2.1-zero3w-v1.12-bootfix-20260920.img.xz` hâlâ özgün dosyadır, SHA256 değişmedi, **bu DHCP düzeltmesini içermez;** kart içindeki `/root/先连WiFi.txt` de eski bir açıklamadır, bu belgeyi esas alın. Bu makinede düzeltilmiş kişisel imaj DHCP adresi aldı ve SSH ile girildi, `networkctl` yeni eklenen yapılandırmanın kullanıldığını doğruladı; bu, herkese açık imajın değiştirildiği anlamına gelmez, tüm bağlantı kopması sorunlarının çözüldüğü anlamına da gelmez. Bkz. [Ağ ve HAT test kaydı](../tools/radxa/联网与HAT调试记录-20260928.md).

> **2026-09-29 güncellemesi:** İlk giriş `root / 1234` olmalıdır, bkz. 3. bölüm. Ayrıca, eski sürüm saklanarak bağımsız bir DHCP düzeltmeli aday imaj sunuldu; aday sürüm DHCP, ilk giriş mekanizması, dosya farkları ve gizlilik öğeleri açısından çevrimdışı incelendi, **ancak bu yeni ürün için kart yazılıp gerçek test yapılmadı.** Hâlâ bir temel sistemdir; robot çalışma zamanı, web hata ayıklama konsolu veya politika (yürüme modeli) içermez.

## 1. Resmi Armbian imajından farkları

Başlıca değişiklikler (DHCP, 2026-09-28 tarihli betik düzeltmesidir; eski Release imajlarına elle eklenmelidir):

| Ne değişti | Neden |
|---|---|
| Önyükleyici Radxa `u-boot-rk2410` ile değiştirildi (`idbloader.img` @sektör 64, `u-boot.itb` @sektör 16384) | Bu makinede daha önce görülen önyükleme uyumluluk sorunu değiştirme sonrasında çözüldü; paket sürümü ve sağlama değerleri kart yapım betiğine sabitlenmiştir |
| `/boot/extlinux/extlinux.conf` yazıldı | Radxa U-Boot extlinux üzerinden çalışır, Armbian'ın `boot.scr` dosyasını okumaz |
| `uart2-m0` ve `dwc3-peripheral` overlay'leri bağlandı, çekirdek konsolu `tty1`'e alındı | Birincisi `/dev/ttyS2`'yi (40 pinli başlıktaki seri port, servolar için) çıkarır; ikincisi OTG portunu bilgisayara takınca seri porta çevirir; çekirdek günlükleri artık servo veri yoluna yazılmaz |
| `g_serial` + `ttyGS0` giriş konsolu açıldı, `ttyS2` / `ttyFIQ0` üzerindeki giriş konsolları kapatıldı | Bilgisayara takınca giriş yapılabilir, ağ olmasa da kurtarma mümkün olur; `agetty` `ttyS2`'yi tuttuğu sürece servolar hiçbir şekilde iletişim kurmaz |
| Kablosuz kimlik doğrulama ve `wlan0` DHCP yapılandırıldı | WiFi'li sürümde kimlik bilgileri önceden yazılıdır; iki kart yapım modunda da `25-wlan0.network` yazılır; varsayılan netplan'ın kablosuz kartı kapsamaması eksikliği giderilir. Eski imajlarda elle yapılandırma gerekir |

## 2. Kartı yazma

| Sürüm | Fark |
|---|---|
| 20260920 ilk herkese açık sürüm | Özgün dosya ve SHA256 korunur; DHCP elle eklenmelidir, kart içindeki eski açıklama yanlıştır, SSH sunucu anahtarlarının yeniden oluşturulması gerekir |
| 20260929 aday sürüm | DHCP önceden yapılandırılmış, kart içindeki ilk giriş açıklaması düzeltilmiş, önceden üretilmiş SSH sunucu anahtarları kaldırılmış; yalnızca çevrimdışı doğrulandı, kart yazılıp gerçek test yapılmadı |

Rufus, balenaEtcher veya Armbian Imager'dan herhangi biriyle, 8 GB üstü bir karta yazın. Önce indirmenin doğru olduğunu doğrulayın:

```powershell
# Windows PowerShell
Get-FileHash .\armbian-26.2.1-zero3w-v1.12-dhcpfix-20260929.img.xz -Algorithm SHA256
```

```bash
# Linux / macOS
sha256sum armbian-26.2.1-zero3w-*.img.xz
```

Release sayfasındaki `SHA256` ile eşleşiyorsa yazın. Rufus `.img.xz` dosyasını doğrudan yazabilir, kendiniz açmanız gerekmez.

Eski sürümü kullanıyorsanız komuttaki dosya adını `armbian-26.2.1-zero3w-v1.12-bootfix-20260920.img.xz` yapın ve **eski** Release'in sağlama değerini doğrulayın; iki sürümün sağlama dosyalarını karıştırmayın.

## 3. İlk açılış

1. Kartı karta takın; **`5V IN / USB_OTG` (USB 2.0) portunu** veri kablosuyla bilgisayara bağlayın, güç bilgisayarın USB'sinden gelsin. Diğer **USB 3.0 Host** portu URT-2, USB bellek gibi çevre birimleri içindir; bilgisayarın bu kartın USB seri portunu tanıması için kullanılamaz.
2. Yaklaşık 2~3 dakika bekleyin; normal açılış ve USB gadget yüklemesinden sonra bilgisayarın aygıt yöneticisinde bir **COM portu** (USB seri aygıtı) görünmelidir. PuTTY / MobaXterm / seri port yardımcısıyla açın, **115200 8N1**, Enter'a basın. COM portu yoksa önce port, kablo ve güç beslemesini kontrol edin; yalnızca yeşil LED'e bakarak sistemin veya imajın bozuk olduğuna karar vermeyin.
3. **İlk giriş `root` / `1234` ile yapılır.** Ardından Armbian sihirbazını izleyerek ilk kurulumu tamamlayın; shell seçeneği çıkarsa `bash` seçebilirsiniz. Sihirbaz imajdaki ön ayarları okuyunca root parolası `duck1234` olarak değişir ve `duck` / `duck1234` kullanıcısı oluşturulur. "`duck` oluşturuldu" mesajını gördükten sonra normal kullanıcıya geçin; ilk kimlik doğrulamada `duck` kullanmayın.
4. **Sihirbaz bittikten hemen sonra parolayı değiştirin.** Hâlâ root terminalindeyken:

```bash
passwd            # root'unkini değiştir
passwd duck       # duck'ınkini değiştir
```

Bundan sonra `duck` ile giriş yapın. Zaten `duck` terminalindeyseniz kendi parolanızı `passwd` ile, root parolasını `sudo passwd root` ile değiştirin. Kartı kendisi yapıp `card.conf` dosyasını değiştirenler için kendi ön ayarları geçerlidir.

**Eski açıklama neden giriş yapamıyordu?** 2026-09-29'da 20 Eylül herkese açık imajı salt okunur incelendi: özgün `/etc/passwd` içinde `duck` yok, root parolası `1234` ile eşleşiyor;
`PRESET_ROOT_PASSWORD` ve `PRESET_USER_NAME`, girişten sonra `/etc/profile.d/armbian-check-first-login.sh` aracılığıyla çağrılan ilk giriş sihirbazı tarafından uygulanır, ilk kimlik doğrulama bilgisi değildir. Daha önceki "ilk giriş `duck / duck1234`, root parolası aynı" ifadesi hatalıydı.
Sihirbaz yarıda çıkarsa root parolası değişmiş, `duck` ise hâlâ oluşturulmamış olabilir; ayarlanmış root parolasıyla yeniden girip sihirbazı tamamlayın ya da mevcut root terminalinde önce `id duck` ile kontrol edin; bunun için gelişigüzel yeniden yazmayın.

Seri portta açılış günlüğünün görünmemesi normaldir: çekirdek günlükleri `tty1`'e verilmiştir, seri port yalnızca giriş içindir.

### Eski sürüm kartlar: SSH sunucu anahtarlarını yeniden üretme

20 Eylül herkese açık imajı önceden üretilmiş SSH sunucu anahtarları taşıyordu; bu imajdan klonlanan kartlar aynı anahtarları paylaşır. 29 Eylül aday imajında bu dosyalar kaldırıldı, `machine-id` boş bırakıldı ve özgün sistemdeki `sshd-keygen.service` hizmetinin etkin olduğu doğrulandı; ilk açılışta `ssh-keygen -A` çalışır. Bu bir statik mekanizma incelemesidir; yeni aday ürün kart yazılarak doğrulanmadı.

Eski sürümü yazmış kartlarda, ilk girişi **USB seri veya yerel terminalden** yaptıktan sonra aşağıdaki komutlarla bu makineye özgü anahtarlar yeniden üretilebilir; yeniden yazmak gerekmez:

```bash
sudo rm -f /etc/ssh/ssh_host_{rsa,ecdsa,ed25519}_key{,.pub}
sudo ssh-keygen -A
sudo systemctl restart ssh
sudo ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

Sunucu parmak izi değişir. Bilgisayardan bir sonraki SSH girişinde eski parmak izinin uyuşmadığı uyarısı çıkarsa, önce yukarıda ana kartta yerel olarak gösterilen parmak izi ile karşılaştırın, sonra bilgisayarda `ssh-keygen -R ana-kart-IP` ile bu adresin eski kaydını silip yeniden bağlanın.

**HAT / 40 pinli başlıktan güç veriliyorsa:** Bu bölümdeki sıradan USB veri kablosu bağlantısını doğrudan üst üste uygulamayın.
Radxa Zero 3W V1.12 resmi şemasının 20. ve 22. sayfalarında 40 pinli başlığın 2/4 numaralı pinleri ile OTG portunun
VBUS hattı aynı `+5V_INPUT` ağına bağlıdır; sıradan USB veri kablosu bilgisayarın 5V'unu HAT'ın 5V çıkışıyla birleştirir. HAT güç beslemesini ayıklarken öncelikle WiFi + SSH girişini kullanın; USB seri port gerekiyorsa
önce normal şekilde kapatıp HAT girişini ayırın, sonra yalnızca USB ile besleyin.

Düzeltme (2026-09-28): Bu bölümde önceden bilgisayarın bağlandığı port "USB 3.0 portu" olarak yazılmıştı; [Radxa resmi arayüz açıklaması](https://docs.radxa.com/en/zero/zero3) ve V1.12 şemasına göre düzeltildi.

## 4. WiFi'ye bağlanma

Aşağıdakiler bu projenin Armbian taban imajı için geçerlidir; `wpa_supplicant` + `systemd-networkd` kullanır. Sonradan NetworkManager'a geçildiyse bağlantıyı onun üzerinden değiştirin, başka bir kablosuz yönetim hizmetini aynı anda etkinleştirmeyin. Taban imajda NetworkManager / `nmtui` kurulu değildir.

Bu imajın kablosuz kimlik bilgileri netplan içinde değildir; bu yüzden üst akım `migrate-network.sh` betiğinin ağ geçiş adımları doğrudan uygulanamaz; geçişten önce kimlik bilgilerinin içe aktarılması, eski hizmetten çıkış ve bağlantı kopması durumunda kurtarma ele alınmalıdır, bkz. [dizin açıklaması](../tools/radxa/README.md).

### WiFi bilgileri zaten girildi, yalnızca DHCP eksik

WiFi adı ve parolasının doğru olduğunu doğrulayın, USB seri veya yerel terminalden girip şunu çalıştırın:

```bash
sudo mkdir -p /etc/systemd/network
sudo tee /etc/systemd/network/25-wlan0.network >/dev/null <<'NETWORK'
[Match]
Name=wlan0

[Network]
DHCP=ipv4
NETWORK
sudo chmod 644 /etc/systemd/network/25-wlan0.network
sudo systemctl enable --now systemd-networkd wpa_supplicant@wlan0
sudo networkctl reload
sudo networkctl reconfigure wlan0
```

Bu adım, mevcut WiFi kimlik doğrulama yapılandırmasını korur. Sonra aşağıdaki "Bağlantıyı kontrol etme" bölümüne göre sonucu doğrulayın; yalnızca DHCP eklemek parola hatasını, kablosuz sürücü sorununu veya güç sorununu çözmez.

### İlk kez ağa bağlanma veya WiFi değiştirme

USB seri veya yerel terminal üzerinden yapın. Aşağıdaki komutlar mevcut WiFi yapılandırmasının yerine geçer; kablosuz hizmeti yeniden başlatmak mevcut kablosuz SSH bağlantısını keser. Örnekteki WiFi adı ve parolayı kendinizinkilerle değiştirin, `country` alanına bulunduğunuz yerin iki harfli ülke kodunu yazın (Çin için `CN`; Türkiye için `TR`):

```bash
sudo mkdir -p /etc/wpa_supplicant /etc/systemd/network
sudo tee /etc/wpa_supplicant/wpa_supplicant-wlan0.conf >/dev/null <<'CONF'
ctrl_interface=DIR=/run/wpa_supplicant GROUP=netdev
update_config=1
country=CN

network={
    ssid="你的WiFi名"
    psk="你的WiFi密码"
    key_mgmt=WPA-PSK
    pairwise=CCMP
    ieee80211w=0
    scan_ssid=1
    priority=10
}
CONF
sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
sudo tee /etc/systemd/network/25-wlan0.network >/dev/null <<'NETWORK'
[Match]
Name=wlan0

[Network]
DHCP=ipv4
NETWORK
sudo chmod 644 /etc/systemd/network/25-wlan0.network
sudo systemctl enable --now systemd-networkd
sudo systemctl enable wpa_supplicant@wlan0
sudo systemctl restart wpa_supplicant@wlan0
sudo networkctl reload
sudo networkctl reconfigure wlan0
```

(Yukarıdaki örnekte `你的WiFi名` "WiFi adınız", `你的WiFi密码` "WiFi parolanız" anlamına gelir.)

Burada kablosuz hizmet açıkça yeniden başlatılır ki değiştirilen WiFi adı ve parolası geçerli olsun; yalnızca `enable --now` çalıştırmak, zaten çalışan hizmetin yapılandırmayı yeniden okumasını sağlamaz.

### Bağlantıyı kontrol etme

Yaklaşık 30 saniye bekleyin, sonra çalıştırın:

```bash
sudo wpa_cli -i wlan0 status   # 认证成功应有 wpa_state=COMPLETED
ip -4 a show wlan0            # 看有没有拿到 IPv4 地址
ip -4 route                   # 看有没有默认路由
networkctl status wlan0       # 看匹配的网络配置及 DHCP 状态
```

(Yorumlar: kimlik doğrulama başarılıysa `wpa_state=COMPLETED` olmalı; IPv4 adresi alınıp alınmadığına bakın; varsayılan rota olup olmadığına bakın; eşleşen ağ yapılandırmasına ve DHCP durumuna bakın.)

`wpa_supplicant` kablosuz ağa bağlanmayı, `systemd-networkd` ise `25-wlan0.network` dosyasına göre IPv4 adresi istemeyi üstlenir.
Bu imajla gelen `/etc/netplan/10-dhcp-all-interfaces.yaml` yalnızca `e*`, `lan[0-9]*` ve `wan[0-9]*` ile eşleşir, **`wlan0` için adres almaz.**

Yukarıdaki `WPA-PSK` / `CCMP` / `ieee80211w=0`, önceki AIC8800 hata ayıklamasında kullanılan WPA2 uyumlu yapılandırmadır; yönlendiricinin WPA2-PSK / AES'e izin vermesini gerektirir, yalnızca WPA3'e izin veren veya PMF zorunlu olan ağlarda kullanılamaz. Karma modda el sıkışma başarısız olursa önce bir WPA2 ağıyla karşılaştırmalı test yapın; her kimlik doğrulama hatasını aynı şifreleme algoritmasına bağlamayın.

Sorun giderme sırası: `wlan0` bulunamıyorsa önce aygıt/sürücüyü; kimlik doğrulama `COMPLETED` değilse WiFi adını, parolayı, sinyali ve yönlendirici modunu; kimlik doğrulama tamam ama IPv4 yoksa DHCP yapılandırmasını, ağ yönetim hizmetini ve yönlendiricinin adres atamasını kontrol edin. Daha fazla inceleme gerekiyorsa:

```bash
sudo journalctl -b -u wpa_supplicant@wlan0 -u systemd-networkd --no-pager -n 80
```

Günlük paylaşmadan önce WiFi adınız gibi kişisel bilgileri karartın; parola içeren kimlik doğrulama yapılandırma dosyalarını yüklemeyin.

Bağlandıktan sonra yönlendiricide `radxa-zero3` kaydını bulun; bundan sonra `ssh duck@kart-IP` yeterlidir, seri kabloya gerek kalmaz.

**Bilgisayar değiştirmek için sistemi yeniden yazmak gerekmez:** bilgisayar ve ana kartın birbirine erişebilen aynı yerel ağda olması yeterlidir; misafir ağı / AP izolasyonu karşılıklı erişimi engelleyebilir. **WiFi değiştirmek bağlantı yapılandırmasının değiştirilmesini gerektirir:** ana kart yeni parolayı kendiliğinden bilmez; bu bölümdeki gibi yeniden yapılandırın, yeniden yazmak gerekmez. DHCP'nin atadığı IP değişebilir; adresi yeniden sorgulayın, eski IP'yi sürekli kullanmayın.

Her seferinde elle bağlanmak istemiyorsanız: depodaki kart yapım betiğini kullanın; WiFi'yi kartı yazmadan önce içine yazar —
[`build-armbian-card.sh`](../tools/radxa/build-armbian-card.sh); `card.conf` içine WiFi adı ve parolasını yazıp ağlı bir kartı kendiniz üretebilirsiniz (bu herkese açık imaj aynı betikle, WiFi boş bırakılarak yapılmıştır).

## 5. Servo seri portu

`/dev/ttyS2` hazırdır (40 pinli başlığın 8. pini TX, 10. pini RX); giriş konsolu ve çekirdek günlükleri buradan kaldırılmıştır.

Dikkat: **RK3566'nın UART'ı tam çift yönlü 3,3 V iki telli yapıdadır; Feetech / Dynamixel veri yolu ise tek telli yarı çift yönlüdür** (half-duplex); arada üç durumlu tampon (tri-state buffer) veya dönüştürücü kart gerekir, doğrudan jumper telle bağlanırsa yanıt alınamaz. Bkz. [Tuzaklar](14-tuzaklar.md) ("HAT basmadan, jumper telle" bölümü).

## 6. Kartınız bu seriden değilse

Zero 3W birkaç seri çıkardı; kart üzerindeki WiFi modülü ve aygıt ağacı (device tree) değişti. Tespit yöntemi: bu kart yazılınca sisteme girilemiyor ama **Radxa resmi imajı açılıyor.**

### V1.12J (2026-09 serisi, AIC8800DS2) — birileri çalıştırmayı başardı

Grup üyeleri, kendi kartlarında **B1'in önyükleyicisi + B1'in DTB'si + Armbian 6.1.115 çekirdeği + Trixie sistemi** ile çalıştırdıklarını bildirdi; yalnızca önyükleyiciyi değiştirmek yetmiyor. Bu, belirli bir kart ve imaj birleşimine ait deneyimdir; iki tarafta da 6.1 vendor çekirdeği olduğu için DTB'nin ortak kullanılabileceği sonucuna varılamaz; bu proje bu birleşimi bağımsız olarak doğrulamadı. Aşağıdaki önyükleyici/aygıt ağacı karşılaştırmasını düşünmeden önce ağ yapılandırmasını ve kablolamayı eleyin.

Üç adım (`/dev/sdX` = Radxa B1 resmi imajı yazılmış kart, `/dev/sdY` = bu Armbian imajı yazılmış kart, **diskleri karıştırmayın**):

```bash
# 1) 扒 B1 的引导，写进 Armbian 卡
sudo dd if=/dev/sdX of=idbloader.img bs=512 skip=64    count=16320
sudo dd if=/dev/sdX of=u-boot.itb    bs=512 skip=16384 count=16384
sudo dd if=idbloader.img of=/dev/sdY bs=512 seek=64    conv=notrunc
sudo dd if=u-boot.itb    of=/dev/sdY bs=512 seek=16384 conv=notrunc

# 2) 把 B1 的 DTB 拷到 Armbian 卡（文件名以 B1 镜像里的为准，找 Zero 3W 那份）
sudo mount /dev/sdX1 /mnt/b1 ; sudo mount /dev/sdY1 /mnt/armbian
ls /mnt/b1/boot/dtbs/*/rockchip/ | grep -i zero3
sudo cp /mnt/b1/boot/dtbs/*/rockchip/rk3566-radxa-zero3.dtb /mnt/armbian/boot/dtb/rockchip/rk3566-radxa-zero3-b1.dtb

# 3) extlinux 的 fdt 指向它
sudo sed -i 's|^  fdt .*|  fdt /boot/dtb/rockchip/rk3566-radxa-zero3-b1.dtb|' /mnt/armbian/boot/extlinux/extlinux.conf
sync; sudo umount /mnt/b1 /mnt/armbian
```

(Yorumların anlamı: 1) B1'in önyükleyicisini çıkarıp Armbian kartına yaz; 2) B1'in DTB'sini Armbian kartına kopyala (dosya adı B1 imajındakine göre, Zero 3W'ninkini bulun); 3) extlinux'taki fdt satırını ona yönlendir.)

Radxa'nın DTB'sine geçtikten sonra **iki şeyi doğrulayın**, çünkü overlay'ler Armbian tarafındandır ve düğümlerin eşleşip eşleşmediğine bakmak gerekir:

- `ls /dev/ttyS2` var mı (40 pinli başlıktaki servo seri portu; `uart2-m0` overlay'i işe yaradı mı)
- Kartı bilgisayara takınca hâlâ COM portu çıkıyor mu (`dwc3-peripheral` overlay'i)

Eşleşmiyorsa `fdtoverlays` satırını kaldırıp Radxa'nın kendi overlay'lerini kullanın (B1 imajının `/boot/dtbo/` dizininde), ya da doğrudan Radxa'nın DTB'si üzerinde değişiklik yapın.

### Diğer seriler

Kendi başlatabildiğiniz resmi bir imajı karşılaştırma için kullanabilirsiniz; ancak önyükleyici, DTB ve overlay taşımadan önce kart ve çekirdek uyumluluğunu doğrulayın, seriler arası çalışması garanti edilemez.
Yine olmuyorsa 40 pinli başlıktaki hata ayıklama seri portunu (3,3 V USB-TTL, 1500000) bağlayıp U-Boot çıktısına bakın, ya da
[issue](https://github.com/fanhao375/microduck-replica/issues) açıp kart sürümünü, WiFi modülünü ve hangi adımda takıldığınızı açıkça yazın.

### Bilinen sorunlar

- **V1.12J'de HDMI takılıyken soğuk başlatma açılmıyor** (grup üyelerinin bildirimi, yukarıdaki üç adım uygulanmadan önceki durum). Karşılaşırsanız: önce HDMI'yi takmadan soğuk başlatın,
  açıldıktan sonra takın; ya da extlinux'taki `append` satırının sonuna `video=HDMI-A-1:d` ekleyerek HDMI çıkışını kapatın.
  Bu imajın çekirdek konsolu `console=tty1`'dir (ekrana gider), bununla ilgilidir.

## 7. Kaynak ve lisans

- Taban: [Armbian resmi Radxa Zero 3 imajı](https://www.armbian.com/radxa-zero-3/), 26.2.1 Trixie vendor 6.1.115 minimal, olduğu gibi kullanılmıştır, GPL ve kendi lisansları
- Önyükleyici: Radxa [`u-boot-rk2410`](https://radxa-repo.github.io/bookworm/pool/main/u/u-boot-rk2410/) `2017.09-64-39cd993`; `idbloader.img` ve `u-boot.itb` alınmıştır, GPL-2.0
- Kart yapım değişiklikleri [`build-armbian-card.sh`](../tools/radxa/build-armbian-card.sh) içindedir, kart yapım süreci kendiniz tarafından yeniden üretilebilir; mevcut betik DHCP, ilk giriş ipucu ve SSH sunucu anahtarı işleme düzeltmelerini içerir, çıktı eski Release eklerinden bayt bayt aynı olmaz. 20260929 aday sürümü özgün herkese açık imajı çevrimdışı yamalama yöntemiyle hazırlandı, ayrıntı için [doğrulama kaydı](../tools/radxa/镜像离线核验-20260929.md)

Bu imaj topluluk yapımıdır, **Armbian ve Radxa resmi ile ilgisi yoktur;** sorun çıkarsa onlara değil, bu depoda issue açarak başvurun.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
