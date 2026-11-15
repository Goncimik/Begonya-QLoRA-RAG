"""Begonya - Begonvil Otel araçları ve ajan döngüsü."""

import csv
import json
import re
from proje import (
    KIMLIK, KURUM, ISARET, TABLO,
    TABLO_ANAHTAR, TABLO_ARACI, TABLO_ACIKLAMA)

ARA = None

def kucuk(metin):
    return str(metin).replace("İ", "i").replace("I", "ı").lower().strip()

# Araç 1: Otel rehberinde arama
def rehberde_ara(soru):
    if ARA is None:
        return "Rehber araması henüz hazır değil."
    return "\n\n".join(ARA(soru, 3))

# Oda verilerini yükle
with open(TABLO, encoding="utf-8-sig", newline="") as f:
    SATIRLAR = list(csv.DictReader(f))

# Araç 2: Oda bilgileri
def tablo_ara(deger):
    aranan = kucuk(deger)
    bulunan = [
        s for s in SATIRLAR
        if aranan and aranan in kucuk(s[TABLO_ANAHTAR])]
    if not bulunan:
        return f"'{deger}' için oda kaydı bulunamadı."
    return "\n".join(
        "; ".join(f"{k}: {v}" for k, v in s.items())
        for s in bulunan[:5])

# Araç 3: Hesap makinesi
def hesapla(ifade):
    if not re.fullmatch(r"[\d\s+\-*/().]+", str(ifade)):
        return "Geçersiz hesaplama ifadesi."
    try:
        sonuc = eval(str(ifade), {"__builtins__": {}}, {})
        if not isinstance(sonuc, (int, float)):
            return "Hesaplanamadı."
        return (
            str(int(sonuc))
            if float(sonuc).is_integer()
            else str(round(sonuc, 2)))
    except Exception:
        return "Hesaplanamadı."

# Araç 4: Bize özel konaklama ücreti hesaplayıcısı
def konaklama_ucreti(oda_ve_gece):
    """Örnek parametre: Aile Odası | 2"""
    try:
        oda, gece_yazisi = [
            x.strip()
            for x in str(oda_ve_gece).split("|", 1)]
        gece = int(gece_yazisi)
        if not 1 <= gece <= 365:
            return "Gece sayısı 1 ile 365 arasında olmalıdır."
    except (ValueError, TypeError):
        return "Lütfen 'Aile Odası | 2' biçiminde yazın."

    kayit = next(
        (
            s for s in SATIRLAR
            if kucuk(s[TABLO_ANAHTAR]) == kucuk(oda)),
        None)
    if kayit is None:
        return f"'{oda}' için oda tipi bulunamadı."

    gecelik = int(kayit["gecelik_fiyat_tl"])
    toplam = gecelik * gece
    gecelik_yazi = f"{gecelik:,}".replace(",", ".")
    toplam_yazi = f"{toplam:,}".replace(",", ".")

    return (
        f"{kayit[TABLO_ANAHTAR]}: {gece} gece x "
        f"{gecelik_yazi} TL = {toplam_yazi} TL. "
        "Bu, indirimsiz temel oda ücretidir; "
        "ek hizmetler ve müsaitlik dahil değildir.")

# Modelin kullanacağı araçlar
ARACLAR = [
    {
        "ad": "rehberde_ara",
        "param": "soru",
        "fonk": rehberde_ara,
        "aciklama": f"{KURUM} rehberindeki kuralları ve hizmetleri arar.",
        "tema": "otel kuralları, iptal, spa, havuz, transfer, evcil hayvan"},
    {
        "ad": TABLO_ARACI,
        "param": TABLO_ANAHTAR,
        "fonk": tablo_ara,
        "aciklama": TABLO_ACIKLAMA,
        "tema": (
            "oda kapasitesi, manzara, gecelik fiyat; oda tipleri: "
            + ", ".join(s[TABLO_ANAHTAR] for s in SATIRLAR))},
    {
        "ad": "hesapla",
        "param": "ifade",
        "fonk": hesapla,
        "aciklama": "Dört işlem yapar. Örnek: 22 * 9.",
        "tema": "aritmetik işlemler, toplam, fark, çarpım"},
    {
        "ad": "konaklama_ucreti",
        "param": "oda_ve_gece",
        "fonk": konaklama_ucreti,
        "aciklama": (
            "Oda tipine ve gece sayısına göre toplam temel ücreti "
            "hesaplar. Parametre örneği: 'Aile Odası | 2'. "
            "İndirim ve ek hizmet dahil değildir."),
        "tema": (
            "belirli bir odada 2, 3, 4 veya 5 gece kalma ücreti; "
            "oda_ve_gece değeri 'Aile Odası | 2' biçimindedir. "
            "Oda tipleri: "
            + ", ".join(s[TABLO_ANAHTAR] for s in SATIRLAR))}]

FONK = {a["ad"]: a["fonk"] for a in ARACLAR}

ARAC_LISTESI = "\n".join(
    f"- {a['ad']}({a['param']}: str): {a['aciklama']}"
    for a in ARACLAR)

AJAN_SISTEM = f"""{KIMLIK}
Soruları araçlarla çözersin. Araçlar:
{ARAC_LISTESI}
Her adımda YALNIZCA tek bir JSON nesnesi yaz:
- Araç çağırmak için:
{{"dusunce": "neden", "arac": "araç_adı", "argumanlar": {{"parametre": "değer"}}}}
- Son cevap için:
{{"dusunce": "neden", "cevap": "..."}}
Kurallar: Rehberdeki ve tablodaki bilgileri araçla öğren; uydurma.
Her hesabı uygun hesaplama aracıyla yap.
Tek seferde tek araç çağır."""

# Ajan döngüsü
def ajan(soru, sor, maks_adim=4):
    mesajlar = [
        {"role": "system", "content": AJAN_SISTEM},
        {"role": "user", "content": soru}]
    izler = []

    for _ in range(maks_adim):
        ham = sor(mesajlar)
        try:
            karar = json.loads(
                ham[ham.index("{"):ham.rindex("}") + 1])
            assert isinstance(karar, dict)
        except Exception:
            mesajlar += [
                {"role": "assistant", "content": ham},
                {"role": "user", "content": "Araç sonucu: geçersiz JSON."}]
            continue

        mesajlar.append({
            "role": "assistant",
            "content": json.dumps(karar, ensure_ascii=False)})

        if karar.get("cevap") or karar.get("arac") not in FONK:
            return (karar.get("cevap") or ham), izler

        argumanlar = karar.get("argumanlar") or {}

        try:
            sonuc = FONK[karar["arac"]](*argumanlar.values())
        except Exception as hata:
            sonuc = f"Araç hatası: {hata}"

        izler.append(
            f"{karar['arac']}({', '.join(map(str, argumanlar.values()))})")
        mesajlar.append({
            "role": "user",
            "content": f"Araç sonucu: {sonuc}"})

    return f"Adım sınırına ulaşıldı. {ISARET}", izler
