from telegram import Update
from telegram.ext import *
import logging

BOT_TOKEN = "TOKEN_BOT_KAMU"
BOT_OWNER = "@suamichasca"
BOT_USERNAME = "@XLAreaBot"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

areas = {
    'BANTEN': {
        'Area 2': [
            'KOTA TANGERANG SELATAN', 'KOTA TANGERANG', 'KAB. TANGERANG', 
            'KAB. PANDEGLANG', 'KAB. LEBAK', 'KAB. SERANG', 'KOTA SERANG', 
            'KOTA CILEGON'
        ]
    },
    'DI YOGYAKARTA': {
        'Area 1': [
            'KAB. KULON PROGO', 'KOTA YOGYAKARTA', 'KAB. SLEMAN', 
            'KAB. BANTUL', 'KAB. GUNUNGKIDUL'
        ]
    },
    'DKI JAKARTA': {
        'Area 2': [
            'KOTA JAKARTA PUSAT', 'KOTA JAKARTA SELATAN', 'KOTA JAKARTA BARAT',
            'KOTA JAKARTA TIMUR', 'KOTA JAKARTA UTARA'
        ],
        'Area 3': [
            'KAB. KEPULAUAN SERIBU'
        ]
    },
    'JAWA BARAT': {
        'Area 1': [
            'KAB. BANDUNG', 'KAB. KUNINGAN', 'KAB. PURWAKARTA', 'KOTA BANDUNG'
        ],
        'Area 2': [
            'KAB. BANDUNG BARAT', 'KOTA CIMAHI', 'KAB. CIREBON', 'KOTA CIREBON',
            'KAB. INDRAMAYU', 'KAB. SUBANG'
        ],
        'Area 3': [
            'KAB. BOGOR', 'KOTA BOGOR', 'KOTA DEPOK', 'KOTA BEKASI', 
            'KOTA BANJAR', 'KAB. CIAMIS', 'KOTA TASIKMALAYA', 'KAB. MAJALENGKA',
            'KAB. SUMEDANG', 'KAB. BEKASI', 'KAB. TASIKMALAYA', 'KAB. GARUT'
        ],
        'Area 4': [
            'KAB. CIANJUR', 'KAB. PANGANDARAN', 'KAB. KARAWANG',
            'KOTA SUKABUMI', 'KAB. SUKABUMI'
        ]
    },
    'JAWA TENGAH': {
        'Area 2': [
            'KAB. TEGAL', 'KOTA SURAKARTA', 'KOTA TEGAL', 'KAB. BREBES',
            'KAB. KEBUMEN', 'KAB. PEMALANG', 'KOTA SEMARANG'
        ],
        'Area 3': [
            'KAB. BOYOLALI', 'KOTA SALATIGA', 'KAB. SEMARANG', 'KAB. CILACAP',
            'KAB. GROBOGAN', 'KAB. KENDAL', 'KAB. REMBANG'
        ],
        'Area 4': [
            'KOTA PEKALONGAN', 'KAB. PEKALONGAN', 'KAB. BATANG',
            'KAB. PURBALINGGA', 'KAB. KUDUS', 'KAB. SUKOHARJO', 'KAB. KLATEN',
            'KOTA MAGELANG', 'KAB. BANYUMAS', 'KAB. MAGELANG',
            'KAB. TEMANGGUNG', 'KAB. SRAGEN', 'KAB. BANJARNEGARA',
            'KAB. KARANGANYAR', 'KAB. WONOSOBO', 'KAB. JEPARA', 'KAB. DEMAK',
            'KAB. PURWOREJO', 'KAB. BLORA', 'KAB. WONOGIRI', 'KAB. PATI'
        ]
    },
    'JAWA TIMUR': {
        'Area 2': [
            'KOTA PROBOLINGGO', 'KAB. BANGKALAN', 'KAB. SIDOARJO',
            'KAB. BANYUWANGI', 'KOTA SURABAYA', 'KAB. SAMPANG',
            'KAB. PAMEKASAN', 'KAB. SUMENEP', 'KAB. PACITAN'
        ],
        'Area 3': [
            'KAB. LUMAJANG', 'KAB. PROBOLINGGO'
        ],
        'Area 4': [
            'KAB. JOMBANG', 'KOTA BLITAR', 'KAB. BLITAR', 'KOTA KEDIRI',
            'KAB. LAMONGAN', 'KAB. KEDIRI', 'KAB. NGAWI', 'KAB. MOJOKERTO',
            'KOTA MOJOKERTO', 'KAB. MAGETAN', 'KAB. GRESIK', 'KAB. TULUNGAGUNG',
            'KAB. NGANJUK', 'KAB. PASURUAN', 'KOTA PASURUAN', 'KAB. BOJONEGORO',
            'KAB. MADIUN', 'KAB. BONDOWOSO', 'KAB. TUBAN', 'KOTA MADIUN',
            'KAB. SITUBONDO', 'KAB. JEMBER', 'KOTA MALANG', 'KAB. MALANG',
            'KAB. PONOROGO', 'KOTA BATU', 'KAB. TRENGGALEK'
        ]
    },
    'BENGKULU': {
        'Area 3': [
            'KAB. SELUMA'
        ],
        'Area 4': [
            'KAB. BENGKULU SELATAN', 'KAB. KAUR', 'KAB. LEBONG',
            'KAB. REJANG LEBONG', 'KAB. BENGKULU TENGAH', 'KOTA BENGKULU',
            'KAB. BENGKULU UTARA', 'KAB. KEPAHIANG', 'KAB. MUKO MUKO'
        ]
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = f"""
🔵 *XL Area Check Bot* 🔵

Bot untuk cek Area XL di seluruh Indonesia.
Dibuat untuk memudahkan cek area XL di daerahmu!

*Command List:*
• /start - Mulai bot
• /cek [kota] - Cek area XL
• /help - Bantuan penggunaan

*Contoh Penggunaan:*
/cek KOTA BANDUNG
/cek KAB. BOGOR

*Info:*
• Owner Bot: {BOT_OWNER}
• Last Update: 30/12/2024
    """
    await update.message.reply_text(start_text, parse_mode='Markdown')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = f"""
📌 *Panduan Penggunaan Bot*

1️⃣ *Format Pengecekan Area:*
/cek [nama kota/kabupaten]

2️⃣ *Contoh Command:*
• /cek KOTA JAKARTA SELATAN
• /cek KAB. BANDUNG
• /cek KOTA SURABAYA

3️⃣ *Tips Penggunaan:*
• Gunakan format KAB. atau KOTA
• Penulisan bisa kapital/non-kapital
• Pastikan nama daerah sudah benar

*Info Bot:*
• Owner: {BOT_OWNER}
• Report bug? Contact owner
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def cek(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        text = """
⚠️ *Format Salah!*

*Cara Penggunaan:*
/cek [nama kota/kabupaten]

*Contoh:*
• /cek KOTA BANDUNG
• /cek KAB. BOGOR
• /cek KOTA SURABAYA

❓ Butuh bantuan? Ketik /help
        """
        await update.message.reply_text(text, parse_mode='Markdown')
        return

    query = ' '.join(context.args).upper()
    found = False

    for region, area_data in areas.items():
        for area_name, cities in area_data.items():
            if any(query in city for city in cities):
                result = f"""
🔍 *Hasil Pencarian Area XL*

📍 Daerah: `{query}`
🌏 Region: `{region}`
📱 Area XL: `{area_name}`

💡 _Area ini menentukan:_
• Kuota Internet XL
• Zona Waktu Penggunaan
• Harga Paket Data

*Info Bot:*
👨‍💻 Owner: {BOT_OWNER}
                """
                await update.message.reply_text(result, parse_mode='Markdown')
                found = True
                break
        if found:
            break

    if not found:
        not_found = f"""
❌ *Daerah Tidak Ditemukan!*

"{query}" tidak ada dalam database.

*Pastikan:*
• Gunakan format: KAB. atau KOTA
• Periksa kembali nama daerah
• Lihat /help untuk bantuan

*Contact:*
Owner: {BOT_OWNER}
        """
        await update.message.reply_text(not_found, parse_mode='Markdown')

def error(update, context):
    print(f'Update {update} caused error {context.error}')
    logger.warning(f'Update {update} caused error {context.error}')

def main():
    print('Starting bot...')
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('cek', cek))

    app.add_error_handler(error)

    print('Bot is running!')
    app.run_polling(poll_interval=1)

if __name__ == '__main__':
    main()