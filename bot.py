import os
import telebot
from flask import Flask, request
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# လူကြီးမင်း၏ Telegram Bot Token
TOKEN = "8996299743:AAGt3ctPHXjdhhlvpYbzE5Lu-6sAZL7Dwl4"

# Threaded ကို False ထားခြင်းဖြင့် Webhook တွင် ပိုမိုတည်ငြိမ်စေပါသည်
bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)


def get_main_keyboard():
  markup = InlineKeyboardMarkup(row_width=1)
  btn1 = InlineKeyboardButton(
      "၁။ Guitar Chord And Retham Basis", callback_data="course_1"
  )
  btn2 = InlineKeyboardButton("၂။ Guitar Lead Basis", callback_data="course_2")
  markup.add(btn1, btn2)
  return markup


@bot.message_handler(commands=["start"])
def send_welcome(message):
  welcome_text = (
      "မင်္ဂလာပါခင်ဗျာ... 🎸\n\n"
      "လေ့လာလိုသော သင်ခန်းစာ ခလုတ်ကို နှိပ်၍ အသေးစိတ် ကြည့်ရှုနိုင်ပါသည်။"
  )
  bot.send_message(
      message.chat.id, welcome_text, reply_markup=get_main_keyboard()
  )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  data = call.data
  if data == "course_1":
    text = (
        "🎸 <b>Guitar Chord And Retham Basis</b>\n"
        "(ဂီတာ ကောဒ့် နှင့် ရမ်သမ် အခြေခံ)\n\n"
        "၁။ chords ကောဒ့်များ\n"
        "၂။ key familial မိသားစုကီးများ\n"
        "၃။ Retham Style ရမ်သမ်စည်းချက်စတိုင်\n"
        "၄။ Song play သီချင်းတီးနည်း\n\n"
        "💰 <b>ဝယ်ယူရန် ငွေ 50000 ကျပ်</b>\n"
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
        parse_mode="HTML",
        reply_markup=markup,
    )

  elif data == "course_2":
    text = (
        "🎸 <b>Guitar Lead Basis</b>\n"
        "(ဂီတာ လိဒ် အခြေခံ)\n\n"
        "၁။ လက်အနေအထားလက်ကျင့်နည်း\n"
        "၂။ ကော့ဒ်ဖွဲ့စည်းပုံ\n"
        "၃။ Key C Position\n"
        "၄။ Major Shape\n\n"
        "💰 <b>ဝယ်ယူရန် ငွေ 60000 ကျပ်</b>\n"
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
        parse_mode="HTML",
        reply_markup=markup,
    )

  elif data in ["buy_1", "buy_2"]:
    c_code = "1" if data == "buy_1" else "2"
    text = (
        "💳 <b>ငွေပေးချေမည့် နည်းလမ်းကို ရွေးချယ်ပါ</b>\n\n"
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
        parse_mode="HTML",
        reply_markup=markup,
    )

  elif data.startswith("pay_kpay_"):
    c_code = data.split("_")[-1]
    text = (
        "💳 <b>Kpay ဖြင့် ငွေပေးချေရန်</b>\n\n"
        "နာမည် - <code>JOBAR</code>\n"
        "Kpay - <code>09795216907</code>\n\n"
        "ငွေလွှဲပြီးပါက အောက်ပါခလုတ်ကို နှိပ်၍ Screenshot ပို့ပေးပါခင်ဗျာ။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    # အက်မင်ဆီသို့ တိုက်ရိုက်ချတ်ဖွင့်ရန် Button (ID: 8414511023)
    btn_admin = InlineKeyboardButton(
        "💬 အက်မင်ဆီသို့ တိုက်ရိုက်ပို့ရန်", url="tg://user?id=8414511023"
    )
    btn_back_pay = InlineKeyboardButton(
        "🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}"
    )
    btn_back_home = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_admin, btn_back_pay, btn_back_home)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="HTML",
        reply_markup=markup,
    )

  elif data.startswith("pay_wave_"):
    c_code = data.split("_")[-1]
    text = (
        "💳 <b>Wave Pay ဖြင့် ငွေပေးချေရန်</b>\n\n"
        "နာမည် - <code>JOBAR</code>\n"
        "Wavepay - <code>09943667126</code>\n\n"
        "ငွေလွှဲပြီးပါက အောက်ပါခလုတ်ကို နှိပ်၍ Screenshot ပို့ပေးပါခင်ဗျာ။"
    )
    markup = InlineKeyboardMarkup(row_width=1)
    # အက်မင်ဆီသို့ တိုက်ရိုက်ချတ်ဖွင့်ရန် Button (ID: 8414511023)
    btn_admin = InlineKeyboardButton(
        "💬 အက်မင်ဆီသို့ တိုက်ရိုက်ပို့ရန်", url="tg://user?id=8414511023"
    )
    btn_back_pay = InlineKeyboardButton(
        "🔙 ငွေပေးချေမှု ရွေးချယ်ရန်", callback_data=f"buy_{c_code}"
    )
    btn_back_home = InlineKeyboardButton(
        "🔙 ပင်မစာမျက်နှာသို့ ပြန်သွားရန်", callback_data="back_home"
    )
    markup.add(btn_admin, btn_back_pay, btn_back_home)
    bot.edit_message_text(
        text,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode="HTML",
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


# --- Webhook Endpoint for Flask ---
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
  if request.headers.get("content-type") == "application/json":
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "", 200
  else:
    return "Forbidden", 403


@app.route("/")
def home():
  return "Bot is running with Webhook!"


if __name__ == "__main__":
  # Remove previous webhooks and set up the new Render Webhook URL
  bot.remove_webhook()
  RENDER_URL = "https://guitarmyanmar-bot.onrender.com"
  bot.set_webhook(url=f"{RENDER_URL}/{TOKEN}")

  app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
