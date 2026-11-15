"""Begonvil Otel yapay zeka asistanı proje kartı."""

# --- Asistan ---
PROJE_ADI = "Begonya"
KURUM = "Begonvil Otel"

KAPSAM = (
    "Oda bilgileri, konaklama ücretleri, rezervasyon, "
    "iptal, giriş-çıkış, restoran, spa, havuz, "
    "transfer ve otel hizmetleri")

ISARET = "🌺"

KIMLIK = (
    "Adın Begonya. Kurgusal Begonvil Otel'in yapay zeka "
    "misafir hizmetleri ve resepsiyon asistanısın. "
    "Açık kaynak bir dil modeline ince ayar yapılarak "
    "geliştirildin. Üslubun Türkçe, nazik, samimi, "
    "profesyonel ve anlaşılırdır. "
    "Otel hizmetleri, oda özellikleri ve konaklama "
    "hakkında yardımcı olursun. "
    "Bilmediğin bilgileri uydurmazsın. "
    "Her cevabını 🌺 ile bitirirsin.")

# --- Model ---
TABAN = "Qwen/Qwen2.5-1.5B-Instruct"
MODEL_ADI = "Begonya-1.5B"

# --- Veri paketi 5: Begonvil Otel ---
REHBER = "rehber.pdf"
TABLO = "odalar.csv"
TEST = "test_sorulari.csv"

TABLO_ANAHTAR = "oda_tipi"
TABLO_ARACI = "oda_bilgisi"
TABLO_ACIKLAMA = (
    "Oda tipine göre kapasite, metrekare, manzara, "
    "gecelik fiyat, evcil hayvan kabulü "
    "ve oda sayısı bilgilerini verir.")

# --- RAG sistemi ---
def rag_sistem(baglam):
    """Kimlik ve rehber bağlamını birleştirir."""
    return (
        f"{KIMLIK}\n"
        "Aşağıdaki bağlamı kullanarak cevap ver. "
        "Cevap bağlamda yoksa uydurma; "
        "'Bu bilgi rehberde yok' de ve "
        "ilgili birime yönlendir.\n\n"
        f"Bağlam:\n{baglam}")
