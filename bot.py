import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# လူကြီးမင်း၏ Telegram Bot Token
TOKEN = '8996299743:AAGt3ctPHXjdhhlvpYbzE5Lu-6sAZL7Dwl4'
# NanoBanana Admin ID (ဝယ်ယူမှုများအတွက် သို့မဟုတ် Admin ဆက်သွယ်ရန်)
NANO_BANANA_ADMIN_ID = 8414511023

bot = telebot.TeleBot(TOKEN)

def get_main_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(
        "၁။ Guitar Chord Vs Retham Basis", 
        callback_data="course_1"
    )
    btn2 = InlineKeyboardButton(
        "၂။ Guitar Lead Basis", 
        callback_data="course_2"
    )
    markup.add(btn1, btn2)
    return markup

# /start နှိပ်လိုက်သည့်အခါ မင်္ဂလာစာလွှာနှင့် ခလုတ်များ ပြသမည်
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "မင်္ဂလာပါခင်ဗျာ... 🎸\n\n"
        "လေ့လာလိုသော သင်ခန်းစာ ခလုတ်ကို နှိပ်၍ အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())

# ခလုတ်များ နှိပ်လိုက်သည့်အခါ စာပြန်မည့် Callback Handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data = call.data
    
    if data == "course_1":
        text = (
            "🎸 *Guitar Chord Vs Retham Basis*\n"
            "(ဂီတာ ကောဒ့် နှင့် ရမ်သမ် အခြေခံ)\n\n"
            "၁။ chords ကောဒ့်များ\n"
            "၂။ key familial မိသားစုကီးများ\n"
            "၃။ Retham Style ရမ်သမ်စည်းချက်စတိုင်\n"
            "၄။ Song play သီချင်းတီးနည်း\n\n"
            "💰 *ဝယ်ယူရန် ငွေ ၄၀၀၀၀ ကျပ်*\n"
            "✨ တခါသွင်းပြီးရင် ရာသက်ပိုင်ကြည့်လို့ရပါပြီဗျ\n\n"
            "မှတ်ချက် ။ ။ မေတ္တာရပ်ခံစရာ ချက်ချင်းစာမပြန်နိင်တာရှိရင် သည်းခံပြီးခနစောင့်ပေးပါဗျ ကျေးဇူးတင်ပါသည်။"
        )
        
        markup = InlineKeyboardMarkup(row_width=1)
        btn_buy = InlineKeyboardButton("🛒 ဝယ်မည်", callback_data="buy_1")
        btn_back = InlineKeyboardButton("🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home")
        markup.add(btn_buy, btn_back)
        
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif data == "course_2":
        text = (
            "🎸 *Guitar Lead Basis*\n"
            "(ဂီတာ လိဒ် အခြေခံ)\n\n"
            "၁။ လက်အနေအထားလက်ကျင့်နည်း\n"
            "၂။ ကော့ဒ်ဖွဲ့စည်းပုံ\n"
            "၃။ Key C Position\n"
            "၄။ Major Shape\n\n"
            "💰 *ဝယ်ယူရန် ငွေ ၄၀၀၀၀ ကျပ်*\n"
            "✨ တခါသွင်းပြီးရင် ရာသက်ပိုင်ကြည့်လို့ရပါပြီဗျ\n\n"
            "မှတ်ချက် ။ ။ မေတ္တာရပ်ခံစရာ ချက်ချင်းစာမပြန်နိင်တာရှိရင် သည်းခံပြီးခနစောင့်ပေးပါဗျ ကျေးဇူးတင်ပါသည်။"
        )
        
        markup = InlineKeyboardMarkup(row_width=1)
        btn_buy = InlineKeyboardButton("🛒 ဝယ်မည်", callback_data="buy_2")
        btn_back = InlineKeyboardButton("🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home")
        markup.add(btn_buy, btn_back)
        
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    # ဝယ်မည်ခလုတ်နှိပ်သောအခါ ငွေပေးချေမှု နည်းလမ်းရွေးရန် (Kpay / Wave)
    elif data in ["buy_1", "buy_2"]:
        course_num = "၁" if data == "buy_1" else "၂"
        c_code = "1" if data == "buy_1" else "2"
        
        text = (
            f"💳 *ငွေပေးချေမည့် နည်းလမ်းကို ရွေးချယ်ပါ* (သင်ခန်းစာ - {course_num})\n\n"
            "အောက်ပါ ငွေလွှဲမည့် အကောင့်တစ်ခုကို ရွေးချယ်ပြီး ငွေလွှဲနိုင်ပါသည်။"
        )
        
        markup = InlineKeyboardMarkup(row_width=1)
        btn_kpay = InlineKeyboardButton("💵 Kpay ဖြင့် ဝယ်မည်", callback_data=f"pay_kpay_{c_code}")
        btn_wave = InlineKeyboardButton("💴 Wave Pay ဖြင့် ဝယ်မည်", callback_data=f"pay_wave_{c_code}")
        btn_back_course = InlineKeyboardButton("🔙 သင်ခန်းစာသို့ ပြန်သွားရန်", callback_data=f"course_{c_code}")
        btn_back_home = InlineKeyboardButton("🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home")
        
        markup.add(btn_kpay, btn_wave, btn_back_course, btn_back_home)
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    # Kpay ရွေးချယ်သည့်အခါ
    elif data.startswith("pay_kpay_"):
        c_code = data.split("_")[-1]
        text = (
            "💳 *Kpay ဖြင့် ငွေပေးချေရန်*\n\n"
            "နာမည် - (Owner)\n"
            "နံပါတ် - `09795216907`\n"
            "ငွေပမာဏ - *50000 ကျပ်*\n\n"
            "ငွေလွှဲပြီးပါက Screenshot ကို Admin (NanoBanana ID: `8414511023`) ထံ ပေးပို့ပေးပါခင်ဗျာ။"
        )
        
        markup = InlineKeyboardMarkup(row_width=1)
        btn_back_pay = InlineKeyboardButton("🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}")
        btn_back_home = InlineKeyboardButton("🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home")
        markup.add(btn_back_pay, btn_back_home)
        
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    # Wave Pay ရွေးချယ်သည့်အခါ
    elif data.startswith("pay_wave_"):
        c_code = data.split("_")[-1]
        text = (
            "💳 *Wave Pay ဖြင့် ငွေပေးချေရန်*\n\n"
            "နာမည် - (Owner)\n"
            "နံပါတ် - `09943667126`\n"
            "ငွေပမာဏ - *50000 ကျပ်*\n\n"
            "ငွေလွှဲပြီးပါက Screenshot ကို Admin (NanoBanana ID: `8414511023`) ထံ ပေးပို့ပေးပါခင်ဗျာ။"
        )
        
        markup = InlineKeyboardMarkup(row_width=1)
        btn_back_pay = InlineKeyboardButton("🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}")
        btn_back_home = InlineKeyboardButton("🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home")
        markup.add(btn_back_pay, btn_back_home)
        
        bot.edit_message_text(text, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif data == "back_home":
        welcome_text = (
            "မင်္ဂလာပါခင်ဗျာ... 🎸\n\n"
            "လေ့လာလိုသော သင်ခန်းစာ ခလုတ်ကို နှိပ်၍ အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။"
        )
        bot.edit_message_text(welcome_text, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=get_main_keyboard())

# Bot စတင်ပွင့်စေရန် Run ခြင်း
bot.infinity_polling()
import os
from threading import Thread
import telebot
from flask import Flask
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# လူကြီးမင်း၏ Telegram Bot Token
TOKEN = "8996299743:AAGt3ctPHXjdhhlvpYbzE5Lu-6sAZL7Dwl4"

# NanoBanana Admin ID (ဝယ်ယူမှုများအတွက် သို့မဟုတ် Admin ဆက်သွယ်ရန်)
NANO_BANANA_ADMIN_ID = 8414511023

bot = telebot.TeleBot(TOKEN)


def get_main_keyboard():
  markup = InlineKeyboardMarkup(row_width=1)
  btn1 = InlineKeyboardButton(
      "၁။ Guitar Chord Vs Retham Basis", callback_data="course_1"
  )
  btn2 = InlineKeyboardButton("၂။ Guitar Lead Basis", callback_data="course_2")
  markup.add(btn1, btn2)
  return markup


# /start နှိပ်လိုက်သည့်အခါ မင်္ဂလာစာလွှာနှင့် ခလုတ်များ ပြသမည်
@bot.message_handler(commands=["start"])
def send_welcome(message):
  welcome_text = (
      "မင်္ဂလာပါခင်ဗျာ... 🎸\n\n"
      "လေ့လာလိုသော သင်ခန်းစာ ခလုတ်ကို နှိပ်၍ အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။"
  )
  bot.send_message(
      message.chat.id, welcome_text, reply_markup=get_main_keyboard()
  )


# ခလုတ်များ နှိပ်လိုက်သည့်အခါ စာပြန်မည့် Callback Handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  data = call.data
  if data == "course_1":
    text = (
        "🎸 *Guitar Chord Vs Retham Basis*\n"
        "(ဂီတာ ကောဒ့် နှင့် ရမ်သမ် အခြေခံ)\n\n"
        "၁။ chords ကောဒ့်များ\n"
        "၂။ key familial မိသားစုကီးများ\n"
        "၃။ Retham Style ရမ်သမ်စည်းချက်စတိုင်\n"
        "၄။ Song play သီချင်းတီးနည်း\n\n"
        "💰 *ဝယ်ယူရန် ငွေ ၄၀၀၀၀ ကျပ်*\n"
        "✨ တခါသွင်းပြီးရင် ရာသက်ပိုင်ကြည့်လို့ရပါပြီဗျ\n\n"
        "မှတ်ချက် ။ ။ မေတ္တာရပ်ခံစရာ ချက်ချင်းစာမပြန်နိင်တာရှိရင် သည်းခံပြီးခနစောင့်ပေးပါဗျ ကျေးဇူးတင်ပါသည်။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    btn_buy = InlineKeyboardButton("🛒 ဝယ်မည်", callback_data="buy_1")
    btn_back = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_buy, btn_back)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup,
    )

  elif data == "course_2":
    text = (
        "🎸 *Guitar Lead Basis*\n"
        "(ဂီတာ လိဒ် အခြေခံ)\n\n"
        "၁။ လက်အနေအထားလက်ကျင့်နည်း\n"
        "၂။ ကော့ဒ်ဖွဲ့စည်းပုံ\n"
        "၃။ Key C Position\n"
        "၄။ Major Shape\n\n"
        "💰 *ဝယ်ယူရန် ငွေ ၄၀၀၀၀ ကျပ်*\n"
        "✨ တခါသွင်းပြီးရင် ရာသက်ပိုင်ကြည့်လို့ရပါပြီဗျ\n\n"
        "မှတ်ချက် ။ ။ မေတ္တာရပ်ခံစရာ ချက်ချင်းစာမပြန်နိင်တာရှိရင် သည်းခံပြီးခနစောင့်ပေးပါဗျ ကျေးဇူးတင်ပါသည်။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    btn_buy = InlineKeyboardButton("🛒 ဝယ်မည်", callback_data="buy_2")
    btn_back = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_buy, btn_back)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup,
    )

  # ဝယ်မည်ခလုတ်နှိပ်သောအခါ ငွေပေးချေမှု နည်းလမ်းရွေးရန် (Kpay / Wave)
  elif data in ["buy_1", "buy_2"]:
    course_num = "၁" if data == "buy_1" else "၂"
    c_code = "1" if data == "buy_1" else "2"
    text = (
        f"💳 *ငွေပေးချေမည့် နည်းလမ်းကို ရွေးချယ်ပါ* (သင်ခန်းစာ - {course_num})\n\n"
        "အောက်ပါ ငွေလွှဲမည့် အကောင့်တစ်ခုကို ရွေးချယ်ပြီး ငွေလွှဲနိုင်ပါသည်။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    btn_kpay = InlineKeyboardButton(
        "💵 Kpay ဖြင့် ဝယ်မည်", callback_data=f"pay_kpay_{c_code}"
    )
    btn_wave = InlineKeyboardButton(
        "💴 Wave Pay ဖြင့် ဝယ်မည်", callback_data=f"pay_wave_{c_code}"
    )
    btn_back_course = InlineKeyboardButton(
        "🔙 သင်ခန်းစာသို့ ပြန်သွားရန်", callback_data=f"course_{c_code}"
    )
    btn_back_home = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_kpay, btn_wave, btn_back_course, btn_back_home)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup,
    )

  # Kpay ရွေးချယ်သည့်အခါ
  elif data.startswith("pay_kpay_"):
    c_code = data.split("_")[-1]
    text = (
        "💳 *Kpay ဖြင့် ငွေပေးချေရန်*\n\n"
        "နာမည် - JOBAR\n"
        "နံပါတ် - `09795216907`\n"
        "ငွေပမာဏ - *50000 ကျပ်*\n\n"
        "ငွေလွှဲပြီးပါက Screenshot ကို Admin (NanoBanana ID: `8414511023`)"
        " ထံ ပေးပို့ပေးပါခင်ဗျာ။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    btn_back_pay = InlineKeyboardButton(
        "🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}"
    )
    btn_back_home = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_back_pay, btn_back_home)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup,
    )

  # Wave Pay ရွေးချယ်သည့်အခါ
  elif data.startswith("pay_wave_"):
    c_code = data.split("_")[-1]
    text = (
        "💳 *Wave Pay ဖြင့် ငွေပေးချေရန်*\n\n"
        "နာမည် - JOBAR\n"
        "နံပါတ် - `09943667126`\n"
        "ငွေပမာဏ - *50000 ကျပ်*\n\n"
        "ငွေလွှဲပြီးပါက Screenshot ကို Admin (NanoBanana ID: `8414511023`)"
        " ထံ ပေးပို့ပေးပါခင်ဗျာ။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    btn_back_pay = InlineKeyboardButton(
        "🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}"
    )
    btn_back_home = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_back_pay, btn_back_home)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup,
    )

  elif data == "back_home":
    welcome_text = (
        "မင်္ဂလာပါခင်ဗျာ... 🎸\n\n"
        "လေ့လာလိုသော သင်ခန်းစာ ခလုတ်ကို နှိပ်၍ အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။"
    )
    bot.edit_message_text(
        welcome_text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=get_main_keyboard(),
    )


# --- Flask ဝဘ်ဆာဗာ (Render တွင် Port Error မတက်စေရန်) ---
app = Flask("")


@app.route("/")
def home():
  return "Bot is running!"


def run():
  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


# Bot နှင့် Flask ကို အပြိုင် (Thread) ဖြင့် ဖွင့်ခြင်း
if __name__ == "__main__":
  t = Thread(target=run)
  t.start()
  bot.infinity_polling()
