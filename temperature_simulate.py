from Adafruit_IO import Client, Feed
import random
import time

# تنظیمات حساب Adafruit IO
ADAFRUIT_IO_USERNAME = "YOUR_USERNAME"
ADAFRUIT_IO_KEY = "YOUR_KEY"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# پیدا کردن Feed مربوطه
temperature_feed = aio.feeds('room-temperature')

# شبیه‌سازی ارسال داده سنسور
while True:
    # تولید یک عدد تصادفی به عنوان دمای اتاق (بین 20 تا 30 درجه)
    simulated_temperature = round(random.uniform(20.0, 30.0), 2)
    print(f"ارسال دما: {simulated_temperature} °C")

    # ارسال داده به پلتفرم ابری (Adafruit IO)
    aio.send_data(temperature_feed.key, simulated_temperature)

    # منتظر ماندن برای 10 ثانیه
    time.sleep(10)