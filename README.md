# IoT Room Temperature Simulator
# شبیه‌ساز دمای اتاق اینترنت اشیا

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Adafruit IO](https://img.shields.io/badge/Platform-Adafruit_IO-green?logo=adafruit)
![IoT](https://img.shields.io/badge/Project-IoT_Learning-lightgrey)

A simple and beginner-friendly IoT project that simulates a temperature sensor and sends data to the Adafruit IO cloud platform. This is a perfect first step to understand the data flow in an IoT system without any hardware.
پروژه ای ساده و مناسب شروع یادگیری اینترنت اشیا که یک سنسور دما را شبیه‌سازی کرده و داده ها را به پلتفرم ابری Adafruit IO ارسال می‌کند. این پروژه اولین قدم عالی برای درک جریان داده در یک سیستم IoT بدون نیاز به سخت‌افزار است.

---

## 📖 Overview | بررسی کلی

This project demonstrates the core concept of IoT:
1.  **Data Generation:** Simulating a physical sensor (temperature reading).
2.  **Connectivity:** Sending data to the cloud using the MQTT protocol (handled by the Adafruit IO library).
3.  **Cloud Platform:** Storing and visualizing the data on Adafruit IO.
4.  **User Interface:** Viewing the data in a real-time dashboard.

این پروژه مفهوم اصلی IoT را نشان می‌دهد:
1.  **تولید داده:** شبیه‌سازی یک سنسور فیزیکی (خواندن دما).
2.  **اتصال:** ارسال داده به ابر با استفاده از پروتکل MQTS (که توسط کتابخانه Adafruit IO مدیریت می‌شود).
3.  **پلتفرم ابری:** ذخیره و نمایش داده ها در Adafruit IO.
4.  **رابط کاربری:** مشاهده داده ها در یک داشبورد .

---

## 🚀 Getting Started | شروع به کار

### Prerequisites | پیش نیازها

*   Python 3.6 or higher | پایتون نسخه ۳.۶ یا بالاتر
*   pip (Python package manager) | pip (مدیریت بسته های پایتون)
*   An [Adafruit IO account](https://io.adafruit.com/) (It's free!) | یک حساب [Adafruit IO](https://io.adafruit.com/) (رایگان است!)

### Installation & Setup | نصب و راه اندازی

1.  **Clone this repository** | **کلون کردن این ریپازیتوری**
    ```bash
    git clone https://github.com/YOUR_USERNAME/IoT-Room-Temperature-Simulator.git
    cd IoT-Room-Temperature-Simulator
    ```

2.  **Install the required library** | **نصب کتابخانه مورد نیاز**
    We use the Adafruit IO Python library. | از کتابخانه پایتون Adafruit IO استفاده می کنیم.
    ```bash
    pip install adafruit-io
    ```

3.  **Get your Adafruit IO Key** | **دریافت کلید Adafruit IO**
    *   Log in to your Adafruit IO account. | وارد حساب Adafruit IO خود شوید.
    *   Click on **"My Key"** from the top menu. | از منوی بالا روی **"My Key"** کلیک کنید.
    *   Copy your **Username** and **Active Key**. | **Username** و **Active Key** خود را کپی کنید.

4.  **Configure the script** | **پیکربندی اسکریپت**
    Open the `temperature_simulator.py` file in a text editor. Replace the placeholders with your credentials:
    فایل `temperature_simulator.py` را در یک ویرایشگر متن باز کنید. مقادیر زیر را با اطلاعات خود جایگزین کنید:
    ```python
    ADAFRUIT_IO_USERNAME = "YOUR_ADAFRUIT_IO_USERNAME"  # جایگزینی با یوزرنیم شما
    ADAFRUIT_IO_KEY = "YOUR_ADAFRUIT_IO_ACTIVE_KEY"     # جایگزینی با کلید شما
    ```

---

## 🎯 How to Run | نحوه اجرا

After configuring the script, simply run it from your terminal or command prompt:
بعد از پیکربندی اسکریپت، به سادگی آن را از ترمینال یا خط فرمان اجرا کنید:

```bash
python temperature_simulator.py
```
You should see an output in the terminal showing the simulated temperature values being sent every 10 seconds:
خروجی در ترمینال را خواهید دید که مقادیر شبیه‌سازی شده دما را هر ۱۰ ثانیه نمایش می‌دهد:

ارسال دما: 23.45 °C
ارسال دما: 26.78 °C
-----------------------------------------------------------------------------------------------
📊 Creating the Dashboard | ساخت داشبورد
Go to your Adafruit IO Dashboards page.
به صفحه Adafruit IO Dashboards خود بروید.

Click Create New Dashboard and name it (e.g., "Room Monitor").
روی Create New Dashboard کلیک کنید و یک نام برای آن انتخاب کنید (مثلا "Room Monitor").

Inside the new dashboard, click Create New Block.
داخل داشبورد جدید، روی Create New Block کلیک کنید.

Choose a Line Chart or Gauge block.
یک بلوک Line Chart (نمودار خطی) یا Gauge (گیج) انتخاب کنید.

Select the room-temperature feed you created during the setup.
Feed ای با نام room-temperature که حین راه اندازی ساخته شد را انتخاب کنید.

Now you will see your simulated data live on the dashboard!
حالا داده های شبیه‌سازی شده خود را به صورت زنده در داشبورد خواهید دید!

--------------------------------------------------------------------------------------------
📷 Screenshot | تصویر نمونه
--------------------------------------------------------------------------------------------
📝 Next Steps | مراحل بعدی
This project simulates the data. To take the next step, you can:

Use a real sensor like a DHT11 or DHT22 with an ESP8266 or Raspberry Pi.

Learn about other IoT platforms like AWS IoT Core or Azure IoT Hub.

Explore other communication protocols like MQTT in more depth.

این پروژه داده را شبیه‌سازی می‌کند. برای قدم بعدی می‌توانید:

از یک سنسور واقعی مانند DHT11 یا DHT22 به همراه ESP8266 یا Raspberry Pi استفاده کنید.

پلتفرم های IoT دیگر مانند AWS IoT Core یا Azure IoT Hub را یاد بگیرید.

پروتکل های ارتباطی دیگر مانند MQTT را به صورت عمیق‌تر بررسی کنید.
