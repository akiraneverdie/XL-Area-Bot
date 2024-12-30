# XL Area Check Bot 📱

Bot Telegram untuk mengecek area XL di seluruh Indonesia. Bot ini membantu pengguna mengetahui area XL di kota/kabupaten mereka yang menentukan kuota, zona waktu, dan harga paket data XL.

## Features ✨

- Cek area XL berdasarkan kota/kabupaten
- Mendukung format KAB. dan KOTA
- Pencarian tidak case sensitive
- Menampilkan region dan area XL
- Interface yang user-friendly dengan emoji
- Error handling yang informatif

## Commands 📝

- `/start` - Mulai bot dan lihat informasi penggunaan
- `/help` - Tampilkan panduan penggunaan bot
- `/cek [kota]` - Cek area XL untuk kota/kabupaten tertentu

## Installation 🛠️

1. Clone repository ini
```bash
git clone https://github.com/akirameverdie/XL-Area-Bot.git
cd XL-Area-Bot
```

2. Install dependencies
```bash
pip3 install python-telegram-bot
```

3. Konfigurasi bot
- Buat bot baru melalui [@BotFather](https://t.me/BotFather)
- Copy token bot yang diberikan
- Edit `BOT_TOKEN` di file `bot.py`
- Edit `BOT_OWNER` dengan username Telegram Anda

4. Jalankan bot
```bash
python3 bot.py
```

## Usage 📱

1. Mulai chat dengan bot
2. Kirim command `/start` untuk melihat informasi penggunaan
3. Gunakan `/cek` untuk mengecek area:
```
/cek KOTA BANDUNG
/cek KAB. BOGOR
/cek KOTA SURABAYA
```

## Example Output 📋

```
🔍 Hasil Pencarian Area XL

📍 Daerah: KOTA BANDUNG
🌏 Region: JAWA BARAT
📱 Area XL: Area 1

💡 Area ini menentukan:
• Kuota Internet XL
• Zona Waktu Penggunaan
• Harga Paket Data
```

## Contributing 🤝

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## Requirements 📦

- Python 3.7+
- python-telegram-bot 20.0+

## Support 💬

- Report bug ke [@suamichasca](https://t.me/suamichasca)
- Request fitur baru melalui issues

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Contact 📧

Owner Bot - [@suamichasca](https://t.me/suamichasca)

Project Link: [https://github.com/akirameverdie/XL-Area-Bot](https://github.com/akirameverdie/XL-Area-Bot)