import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

congrats_list = [
    "С 8 марта! Желаю, чтобы мужчины читали мысли, а не нотации. И чтобы шоколад был всегда под рукой!",
    "Поздравляю! Пусть в твоей жизни будет как можно меньше неожиданных счетов и как можно больше внезапных букетов.",
    "С праздником! Желаю тебе быть королевой, даже когда ты в пижаме и с маской на лице.",
    "Пусть твои нервы будут крепче, чем желание всё проконтролировать!",
    "С 8 марта! Желаю, чтобы в доме всегда было чисто… но только если для этого есть настроение. А если нет — пусть будет как есть.",
    "Пусть все, кто говорит «ты чего такая злая?», просто исчезнут из твоей жизни. А лучше — принесут кофе.",
    "Желаю, чтобы твой внутренний голос говорил только приятное. А если он начинает критиковать — отправляй его в отпуск до 9 марта.",
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌸 Привет! Я праздничный бот.\n"
        "Напиши /congrats, и я скажу что-то приятное и смешное!"
    )

async def congrats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = random.choice(congrats_list)
    await update.message.reply_text(msg)

def main():
    app = Application.builder().token("8622094597:AAH96HVAf6t6lMJwYceAVcuLENVTsCcJZq8").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("congrats", congrats))
    print("Бот запущен... Нажми Ctrl+C для остановки.")
    app.run_polling()

if __name__ == "__main__":
    main()
