# HAT Basmadan · ¥70'lik Modüllerle Kablolu Alternatif

**Basitleştirilmiş Çince (özgün dil)**

> Resmi HAT 4 katmanlı, çift taraflı yerleşimli, 110 bileşenli bir karttır — numune üretimi ve SMT bir seferde binlerce yuana mal olur, **birçok kişi buna değmeyeceğini düşünüyor**.
> Bu belge alternatif çözümdür: bir düşürücü modül + bir yarı çift yönlü dönüştürücü kart, gerisi kablolama. **İşlevsel olarak yalnızca kart üzerindeki ses ve kapanma algılama sinyali eksik kalır.** (¥ = Çin yuanı)

Önce HAT'ın aslında ne işe yaradığını öğrenmek için [Donanım başlangıç](03-donanim-baslangic.md) belgesine, sonra onsuz nasıl yapılacağını öğrenmek için bu belgeye bakın.

[![HAT'sız kablolama şeması](https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/hw/不打HAT-接线图.png)](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/不打HAT-接线图.html)

> **Şemanın kaynak dosyası [`不打HAT-接线图.html`](https://github.com/fanhao375/microduck-replica/blob/789ef5e45b6102d7e71fecefbf58606520147cfa/docs/不打HAT-接线图.html)'dir** — gömülü SVG, indirdikten sonra tarayıcıda açılır; yakınlaştırılabilir, metin seçilebilir, A3 yazdırılabilir.
> Modül veya pin değiştirmek için doğrudan onu düzenleyin. Yukarıdaki PNG yalnızca GitHub'daki önizlemedir.

**Hedef**: Ana kart pilden güç alsın, dönüştürücü kart üzerinden servo veri yoluyla haberleşsin, ToF I²C'ye bağlansın — **HAT kartı basılmadan**, binlerce yuanlık numune üretimi yerine ¥70'lik modüller.

> ⚠️ **Bu bölüm bir plandır, henüz yapılmamıştır.** Kablolama kısmı şartnamelerden ve resmi şematikten, yazılım kısmı resmi `setup-board.sh` kaynak kodundan gelir.
> Yaparken bir adım yanlışsa buradan düzeltin. Yaptıktan sonra «yapılmamış, doğrulanması gerekenler» bölümünü temizleyin.

## Ne alınmalı

Taobao linkleri geçersiz hale gelir, ancak **arama terimleri ve bakılacak sayılar gelmez**. Her satırı «arama terimi» ile arayın, «satın almadan önce bakın» ile seçin. Uygun olanı bulunca linki [Elektronik satın alma listesi](06-elektronik-satin-alma.md)'ne yapıştırın.

| Parça | Arama terimi | Satın almadan önce bakın | Yaklaşık fiyat |
|---|---|---|---|
| **Düşürücü modül** | «UBEC 5V 3A 2S» | **Giriş alt sınırı ≤ 6 V** (birçoğu 2–6S yazar ama gerçekte 7 V'tan başlar, 2S pil bitmek üzereyken önce regülasyondan çıkar) · çıkış ≥ 2 A sürekli · senkron düşürücü, **LM2596 almayın** | ¥10–15 |
| **Yarı çift yönlü dönüştürücü kart** | «串口总线舵机驱动板 ST SC» (seri veri yolu servo sürücü kartı ST SC) | TTL sürümü veya USB sürümü olabilir. **Mantık besleme aralığı 3,3 V'u içermeli** (bazıları yalnızca 5 V yer, o zaman ana karta bağlanamaz) · servo tarafı güç 8,4 V'u geçebilmeli. **Elinizde FE-URT-2 varsa o USB sürümüdür, şimdilik almayabilirsiniz** (bkz. Adım 4) | ¥22 |
| 2×20 pin başlık | «树莓派 彩色排针 2x20» (Raspberry Pi renkli pin başlığı 2x20) | 2,54 mm · dik · renkli olanı pin saymak için iyidir | ¥1 |
| Yüksek dayanıklı microSD ×2 | «SanDisk 高耐久 64G» veya «海康 PLUS 64G» (Hikvision PLUS 64G) | **JD kendi satışı** · High Endurance / güvenlik kamerası için etiketli · Ultra / EVO gibi normal kartlar **değil** | ¥90×2 |
| Kart okuyucu | «USB3.0 读卡器 TF» (USB3.0 kart okuyucu TF) | USB 3.0 | ¥15 |
| Silikon kablo | «18AWG 硅胶线 红黑» (18AWG silikon kablo kırmızı siyah) | 18 veya 20 AWG · silikon kılıf (yumuşak, ısıya dayanıklı) · kırmızı siyah birer metre | ¥10 |
| Sigorta yuvası + sigorta | «5x20 保险丝座 带线» (5x20 sigorta yuvası kablolu) + «5A 保险丝 5x20» | Kablolu yuva lehim işini kısaltır · hızlı atan 5 A | ¥5 |
| Güç anahtarı | «船型开关 KCD1» (kayık tipi anahtar KCD1) | Anma ≥ 6 A · tek kutuplu tek konumlu yeterli | ¥3 |
| PH2.0 3P terminal kablosu ×5 | «PH2.0 3P 端子线 单头» (PH2.0 3P terminal kablosu tek uçlu) | 2,0 mm aralık · 3 pin · tek uçlu kablolu (diğer uç çıplak) | ¥5 |
| Dupont kablo | «杜邦线 母对母 20cm» (Dupont kablo dişi-dişi 20cm) | Dişi-dişi · 20 cm · bir sırada 40 adet | ¥5 |
| 470 µF elektrolitik | «470uF 16V 电解电容» (470uF 16V elektrolitik kondansatör) | 16 V veya üzeri · 105 ℃ | ¥1 |
| *(isteğe bağlı) USB ses kartı* | «USB 声卡 免驱 3.5mm» (USB ses kartı sürücüsüz 3,5mm) | **Sürücüsüz** (Linux UAC standardını tanır) · mikrofon girişli | ¥15 |
| *(isteğe bağlı) Küçük hoparlör* | «3W 4欧 小喇叭» (3W 4 ohm küçük hoparlör) | 4 Ω 3 W · ses kartının 3,5 mm çıkışına amfi üzerinden bağlanır, ya da doğrudan amfili USB mini hoparlör alın | ¥5 |

HAT basılmazsa şunlar kaybedilir: **kapanma algılama sinyali** (LM5050-1 IO_06), kart üzerindeki BMI088 (resmi yazılım zaten kullanmıyor), **kart üzerindeki ses** — ses USB ses kartıyla geri kazanılabilir, bkz. Adım 8.
Kapanma sinyali yok + microSD = ani güç kesilmesi karta zarar verir, **önce yazılımla kapatın, sonra gücü kesin**.

## Adım 1 · Ana kartı açın, hiçbir şey bağlamayın

> ⚠️ **2024-11'den sonra alınan Zero 3W V1.12 sürümüdür (WiFi modülü AIC8800), Armbian resmi imajı doğrudan yazılırsa açılmaz**:
> LED çift yanıp söner, sisteme asla girilmez, yerel ağda bulunamaz. Nedeni, Armbian'ın bu kart için verdiği ana hat U-Boot'un (bellek başlatma yazılımı 2024-01'den v1.21)
> yeni kartı kaldıramamasıdır; Radxa'nın kendi önyükleyicisine geçince düzelir. Radxa resmi sistemi açılıyor, Armbian açılmıyorsa sebep budur.
> Bunu bulmak iki günümüzü aldı, dokuz kart yazdık, bkz. [Tuzaklar](14-tuzaklar.md). Aşağıdaki kart hazırlama betiği bu adımı ve diğer tuzakları birlikte halleder.

**İmaj**: Armbian **26.2.1 · Debian 13 (trixie) · minimal · vendor çekirdek 6.1.115**, Pollen resmi dokümanının belirttiği sürüm.
Çin içi yansı sitelerinde artık yalnızca 26.8.1 kalmış, 26.2.1 burada (376 MB):

```
https://fi.mirror.armbian.de/archive/radxa-zero3/archive/Armbian_26.2.1_Radxa-zero3_trixie_vendor_6.1.115_minimal.img.xz
```

`current_6.18` seçmeyin (ana hat çekirdek, resmi çalışma zamanı tanımaz), masaüstü sürümü seçmeyin.

**1a · Kartı hazırlama** (WiFi, parola, önyükleyici, seri portu imaja gömer; yazdıktan sonra takıp doğrudan ssh yapılır)

Depodaki [`tools/radxa/`](../tools/radxa/) içindeki üç dosyayı yerel bir klasöre kopyalayın; bilgisayarda WSL2 olmalıdır (yoksa yönetici PowerShell'de `wsl --install` çalıştırın, bir kez yeniden başlatın):

1. Not Defteri ile `card.conf` dosyasını açın, WiFi adını ve parolasını değiştirin. Kullanıcı adı ve parola varsayılan `duck` / `duck1234`'tür. Çin içinde resmi yazılımı kurmak gerekirse `HTTP_PROXY=` satırına bilgisayardaki vekilin adresini yazın (örneğin Clash'te «yerel ağa izin ver» açıp `http://bilgisayarIP:7890` yazın).
2. `1-做卡.ps1` (kart hazırlama) dosyasına sağ tıklayıp → «PowerShell ile çalıştır» deyin, indirilen `.img.xz` dosyasını seçin. WSL içinde açar, önyükleyiciyi değiştirir, yapılandırmayı yazar; bir dakikada `xxx-鸭子卡.img` (2,2 GB) çıkar.
3. Pin başlığını önceden lehimleyin: önce çapraz iki pini lehimleyin, çevirip dik durup durmadığına bakın, sonra kalan 38'i lehimleyin.

**1b · Kartı yazma** (Rufus taşınabilir sürüm, 2 MB, kurulum gerekmez)

1. [rufus.ie](https://rufus.ie/zh/) adresinden `rufus-x.xxp.exe` indirin. Kart okuyucuyu bilgisayara takın, **yalnızca bu bir USB depolama türü aygıt takılı olsun**, Rufus'a çift tıklayın. İnternetten güncelleme sorarsa **Hayır** deyin:

   <img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/flash/烧卡-1-Rufus问更新-点否.png" width="420">

2. «Aygıt» otomatik olarak kart okuyucuyu seçer. «**SEÇ**»e tıklayıp yukarıda oluşturulan `xxx-鸭子卡.img` dosyasını seçin:

   <img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/flash/烧卡-2-设备自动选中-点选择.png" width="380">

3. «**BAŞLAT**», «karttaki veriler silinecek» uyarısında Tamam'a tıklayın, yazma yaklaşık 2 dakika sürer:

   <img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/flash/烧卡-3-正在写入.png" width="380">

4. Durum çubuğu «HAZIR»a dönünce bitmiştir, Rufus'u kapatın, kartı çıkarın. **Bu sırada Windows birkaç kez «diski biçimlendirmek ister misiniz» diye soracaktır, hepsinde İptal'e tıklayın**; Linux bölümlerini tanımaz, normaldir.

   <img src="https://raw.githubusercontent.com/fanhao375/microduck-replica/789ef5e45b6102d7e71fecefbf58606520147cfa/assets/flash/烧卡-4-完成-准备就绪.png" width="380">

**1c · Açma, IP bulma, ssh**

Kartı Radxa'ya takın, 5V şarj adaptörünü (Apple 20W gibisi yeter, Huawei hızlı şarj adaptörü kullanmayın) **`5V IN / USB_OTG` portuna** takın (kartın arka yüzündeki serigrafi, TF kart yuvasına yakın uç).
2–3 dakika bekleyin, kendi kendine WiFi'ye bağlanır. LED'e bakın: **birkaç saniye çift yanıp sönme → iki dakika çift yanıp sönme → sabit yanma** açıldığı anlamına gelir; sürekli çift yanıp sönüp değişmiyorsa açılmamıştır.
Yönlendirici arayüzünde `radxa-zero3` adlı bir cihaz bulup IP'sini alın, Windows'un kendi ssh'ı ile:

```
ssh duck@那个IP        # 密码就是 card.conf 里那个
```

(Yorum: `那个IP` = o IP; parola `card.conf` içindeki parolanın aynısıdır.)

**Bir imkân daha: bu USB kablosu aynı zamanda seri porttur.** Kartın `5V IN` portunu bilgisayarın USB portuna takın (bilgisayar güç verir), aygıt yöneticisinde ek bir «USB seri aygıt (COMx)» belirir,
seri terminali 115200 ile açınca giriş istemi gelir, root parolası `card.conf` içindedir. WiFi bağlanmıyor, ssh girilemiyorsa hepsinde buradan girip bakılabilir.

Açıldı, ssh yapılabildi ise devam edin. **Açılmama sorunlarını kablolama sorunlarıyla karıştırmayın.**

## Adım 2 · `/dev/ttyS2`'nin görünmesini sağlayın

Kart hazırlama betiği bunu zaten açtı: extlinux içine `uart2-m0` overlay'i takıldı, çekirdek konsolu tty1'e konuldu, `serial-getty@ttyS2` ve `ttyFIQ0` mask'lendi. ssh ile girip doğrulayın:

```bash
ls -l /dev/ttyS2            # 有
sudo fuser -v /dev/ttyS2    # 没人占
cat /proc/cmdline           # 里面没有 console=ttyS2 / ttyFIQ0
```

(Yorumlar: «var»; «kimse kullanmıyor»; «içinde console=ttyS2 / ttyFIQ0 yok».)

Resmi `setup-board.sh`, `/boot/armbianEnv.txt` içindeki `overlay_prefix` / `overlays` / `console` değerlerini değiştirmeye çalışır; bu kartta etkisizdir (Radxa U-Boot extlinux kullanır, boot.scr'yi okumaz),
ancak kendi kontrol maddelerinin hepsi geçer, olduğu gibi çalıştırın. **`apt upgrade` ile çekirdek paketi güncellenirse extlinux.conf içindeki dosya adı da buna göre değiştirilmelidir**, yükseltmeden önce `/boot/extlinux/extlinux.conf`'a bakın.

Aynı şekilde, ileride overlay eklenecekse (örneğin kamera `rk3568-radxa-zero3-rpi-camera-v2.dtbo`, `setup-board.sh` bunu bu isme yansıtır), extlinux.conf'taki `fdtoverlays` satırının sonuna yolu ekleyip yeniden başlatın. Kamera bağlı değilken `mediad` sürekli yeniden başlar, `robotctl health` içindeki diğer kalemler etkilenmez, normaldir.

## Adım 3 · Güç, her bölümden sonra ölçün

```
NP-F550 ──► 开关 ──► 保险丝 5A ──┬──► 降压模块 ──► 5 V ──► Radxa pin 2（或 4）
                                 │        │
                                 │        └── 输入端并 470 µF
                                 │
                                 └──► 舵机总线 VDD（原压，18 AWG）
共地：电池负极 · 降压输出地 · Radxa pin 6 · 舵机总线 GND
```

(Şema etiketleri: 开关 = anahtar; 保险丝 = sigorta; 降压模块 = düşürücü modül; 输入端并 470 µF = giriş ucuna 470 µF paralel; 舵机总线 VDD（原压）= servo veri yolu VDD (pil ham gerilimi); 共地 = ortak toprak: pil eksi ucu · düşürücü çıkış toprağı · Radxa pin 6 · servo veri yolu GND.)

```
1  接开关、保险丝，量：开关闭合时保险丝两端应导通
2  接降压模块，先别接 Radxa，量输出：5.0 V ±0.2，极性对
3  ⚠️ 确认极性再插 Radxa —— pin 2/4 是无保护的，接反烧板
4  Radxa 拔掉 USB-C，靠 pin 2 的 5 V 点亮，ssh 能进
5  再接舵机总线的 VDD
```

Adımlar (Türkçe):

1. Anahtarı ve sigortayı bağlayın, ölçün: anahtar kapalıyken sigortanın iki ucu iletken olmalı
2. Düşürücü modülü bağlayın, henüz Radxa'yı bağlamayın, çıkışı ölçün: 5,0 V ±0,2, kutup doğru
3. ⚠️ Radxa'yı takmadan önce kutbu doğrulayın — pin 2/4 korumasızdır, ters bağlanırsa kart yanar
4. Radxa'nın USB-C'sini çıkarın, pin 2'deki 5 V ile açın, ssh girilebilmeli
5. Ardından servo veri yolunun VDD'sini bağlayın

## Adım 4 · Servo veri yolunu ana karta bağlayın

```
Radxa 40 针                     转接板 MCU 侧
pin 1   3.3 V    ──────────►   VCC       ⚠️ 只能 3.3 V，接 5 V 它的 TX 会打坏主控 RX
pin 8   UART2_TX ──────────►   RX        ← 交叉
pin 10  UART2_RX ◄──────────   TX        ← 交叉
pin 6   GND      ──────────►   GND

转接板舵机侧
DATA  ──► 舵机总线 S
V     ◄── 舵机总线 VDD（电池原压，第 3 步接的）
G     ──► 共地
```

(Şema etiketleri: Radxa 40 pin = Radxa 40 pin; 转接板 MCU 侧 = dönüştürücü kart MCU tarafı; ⚠️ yalnızca 3,3 V, 5 V bağlanırsa onun TX'i ana kartın RX'ini yakar; 交叉 = çapraz; 转接板舵机侧 = dönüştürücü kart servo tarafı; 舵机总线 S = servo veri yolu S; 舵机总线 VDD（电池原压，第 3 步接的）= servo veri yolu VDD (pil ham gerilimi, Adım 3'te bağlandı); 共地 = ortak toprak.)

**USB sürümü dönüştürücü kart**: pin 1/8/10'u bağlamaya gerek yok, Radxa'nın USB portuna takılır, seri port `/dev/ttyUSB0` veya `/dev/ttyACM0` olur,
sonrasında `robotd.toml` içindeki `port` o değere çevrilir. Pratiktir, ancak Adım 2'deki uart2-m0 overlay'i kullanılmaz hale gelir (agetty yine mask'lidir, zararsız).

> 💡 **Feetech FE-URT-2 hata ayıklama kartı, USB sürümü dönüştürücü karttır** — ID'ler ayarlandıktan sonra doğrudan robota taşınır: USB-C'yi Radxa host portuna, TTL portundaki S'yi veri yoluna, G'yi veri yolu toprağına bağlayın.
> **Pil ham gerilimini doğrudan servo veri yoluna verin, URT-2'nin V1 terminaline vermeyin** — V1 USB 5 V ile doğrudan bağlı olabilir, 7,4 V verilirse Radxa'ya geri besleme yapar.
> Karttaki DIP anahtar sinyal seviyesidir (3,3 / 5 V), 5 V'a çevirin. Dönüştürücü kart şimdilik alınmayabilir.
> Önce Radxa'nın CH343'ü tanıyıp tanımadığını doğrulayın: `dmesg | tail` ile `ttyACM0` var mı bakın; yoksa WCH resmi sitesinde Linux sürücü kaynak kodu bulunur.
> Tek hata ayıklama kartı odur, içeri yerleştirilince bilgisayarda servo ayarlanamaz — **15 servonun ID'lerinin hepsini ayarlayıp bitirdikten sonra taşıyın**.

**Veri yolu nasıl dallanır** — baş, sol bacak, sağ bacak gövdede üç yola ayrılır. Yarı çift yönlü tek hat veri yolu **paraleldir, zincir değildir**; yıldız ve ağaç da çalışır, papatya zinciri yalnızca kablolamayı kolaylaştırır:

```
转接板 TTL ──┬──► 头颈   30 → 31 → 32 → 33 → 34
             ├──► 左腿   20 → 21 → 22 → 23 → 24
             └──► 右腿   10 → 11 → 12 → 13 → 14
             （imu_to_dxl 200 挂躯干里任一路）
```

(Etiketler: 转接板 TTL = dönüştürücü kart TTL; 头颈 = baş-boyun; 左腿 = sol bacak; 右腿 = sağ bacak; «imu_to_dxl 200 gövdedeki herhangi bir yola bağlanır».)

Ayırma yöntemi: URT-2'nin kendi iki TTL portundan biri bir yola, üçüncü yol servodan ayrıca bölünür; ya da «servo veri yolu dağıtım kartı 3P» bir giriş dört çıkış (¥5) alınır; ya da üç kablo paralel lehimlenir.
**V ve G'yi 18 AWG ile üç dala ayrı ayrı çekin**, S'yi istediğiniz yoldan geçirebilirsiniz. ⚠️ **Üç yolun akımının hepsini `imu_to_dxl` kartından geçirmeyin** — dört soketi paralel olsa da 2 katmanlı kartta doğrudan bakır yollar birkaç amper için tasarlanmamıştır, yanar. Kart bir yolun ucuna veya ortasına bağlanır.

## Adım 5 · Tek servo ile iletişimi doğrulayın

Yalnızca **bir adet** ID'si ayarlanmış servo bağlayın (örneğin sol diz 23), ana kartta:

```bash
# 官方运行时带的总线基准工具（第 7 步装完才有），或先用 Python 快速 ping：
pip install feetech-servo-sdk    # 或 scservo_sdk
# 1 Mbps，ping ID 23 —— 回了就通了
```

(Yorumlar: «Resmi çalışma zamanıyla gelen veri yolu kıyaslama aracı (Adım 7 tamamlanınca bulunur) ya da önce Python ile hızlıca ping»; «veya scservo_sdk»; «1 Mbps, ID 23'e ping — cevap geldiyse çalışıyor».)

Çalışmazsa sırayla kontrol edin: `ls /dev/ttyS2` var mı → `fuser` ile kimse kullanıyor mu → TX/RX çapraz mı → dönüştürücü kart VCC'si 3,3 V mu → S hattı teması.

## Adım 6 · ToF

```
VL53L8CX          Radxa 40 针
SDA      ◄──►    pin 3
SCL      ◄──►    pin 5
3V3      ◄───    pin 17     （pin 1 给转接板了，分开用）
GND      ────►   pin 6
```

(Yorum: «pin 1 dönüştürücü karta verildi, ayrı kullanın».)

pin 3/5 kart üzerinde pull-up'lıdır, dışarıdan eklemeye gerek yok.

⚠️ **I²C için bir overlay daha gerekir.** Resmi çözüm `i2c3`'ü M0'a yeniden mux'lamaktır (yani pin 3/5), bedeli USB-C PD müzakeresini kaybetmektir.
Resmi overlay `deploy/audio/i2c3-pihat.dts` içindedir, HAT için yazılmıştır, **HAT basmadan doğrudan kullanılıp kullanılamayacağı doğrulanacak**.

## Adım 7 · Resmi çalışma zamanını çalıştırın

```bash
curl -fsSL https://raw.githubusercontent.com/pollen-robotics/microduck/main/scripts/provision.sh -o /tmp/provision.sh
sudo sh /tmp/provision.sh
# = setup-board.sh → migrate-network.sh → 重启 → install.sh，全自动
robotctl health
```

(Yorum: «= setup-board.sh → migrate-network.sh → yeniden başlat → install.sh, tamamen otomatik».)

`robotd.toml` `/etc/robot/` altındadır, seri port varsayılanı `/dev/ttyS2`'dir, USB sürümü dönüştürücü kartta `/dev/ttyUSB0` olarak değiştirilir.

## Adım 8 · Ses istiyorsanız (isteğe bağlı)

HAT basılmayınca codec de yoktur; resmi çığlıklar, kafa okşama algılama, ToF elektronik org, çoklu ördek korosu çalışmaz — **ancak robotun yürümesi etkilenmez**; resmi yorumun aslı: «codec'siz kartta yürüyüş tamamen aynıdır, yalnızca ses çıkmaz».

Sesi geri istiyorsanız bir **USB ses kartı** takın (sürücüsüz olanlar, Linux doğrudan tanır):

```bash
aplay -l                          # 看到 USB Audio 那张卡的名字，比如 card 1: Device
sudo nano /etc/robot/robotd.toml
```

(Yorum: «USB Audio kartının adını görün, örneğin card 1: Device».)

```toml
[audio]
enabled = true
device = "plughw:CARD=Device"     # 换成 aplay -l 看到的名字，官方默认是 plughw:aic3104
```

(Yorum: «aplay -l'de gördüğünüz adla değiştirin, resmi varsayılan plughw:aic3104'tür».)

```bash
sudo systemctl restart robotd
```

Hoparlörü ses kartının 3,5 mm çıkışına bağlayın (küçük hoparlör amfi ister, doğrudan amfili USB mini hoparlör almak en kolayıdır), mikrofonu ses kartının mic girişine bağlayın.

⚠️ **Doğrulanmadı**: resmi `sounds` ve `pet_detect`, aic3104'ün örnekleme hızı ve kanal sayısına göre yazılmıştır, USB ses kartı uymayabilir. Çalıştırınca bu maddeyi düzeltin.

## Yapılmamış, doğrulanması gerekenler

| Kalem | Şüphe | Nasıl doğrulanır |
|---|---|---|
| Üçüncü taraf dönüştürücü kart @ 1 Mbps | Resmi HAT'ın yön devresi `1G08+1G125+1G126`'dır, ¥22'lik kartın yön değiştirme hızı yeterli mi | Adım 5 çalışırsa, `bench_dynamixel_bus` hata sayacı 0 ise |
| `i2c3-pihat.dts` HAT'sız kullanılabilir mi | Bu overlay HAT için yazılmıştır | Adım 6'da `i2cdetect -y 3` ile 0x29 görülmesi |
| Düşürücü modül servo kalkış gerilim düşüşüne dayanır mı | 15 servo aynı anda hareket edince pil gerilimi düşer | Yürürken ana kart yeniden başlamıyorsa; başlıyorsa giriş kondansatörünü büyütün |
| Armbian'ın tam olarak hangi imajı | Resmi taraf 26.2.x diyor, minimal mi desktop mu demiyor | Adım 1'de ssh ile girilebilmesi yeterli |
| USB ses kartı aic3104'ün yerini tutar mı | Resmi ses kodu codec'in örnekleme hızına göre yazılmıştır | Adım 8'de `robotctl health` ses satırı hata vermez, açılışta ses çıkar |

Kablolama şeması için belgenin başına bakın; kaynak dosyası aynı dizindeki `不打HAT-接线图.html`'dir.

---
*Zekaland Robot Ördek belgeleri · Lisans ve katkıda bulunanlar: [ATIF.md](../ATIF.md)*
