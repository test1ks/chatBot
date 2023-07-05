import openai
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="BOT KEY HERE")
dp = Dispatcher(bot)
api_key = "API KEY HERE"
openai.api_key = api_key
users = {556284707}
accepted_users = lambda message: message.from_user.id not in users


@dp.message_handler(accepted_users, content_types=["any"])
async def handle_unwanted_users(message: types.Message):
    await message.answer(
        "Sorry, bot only works for approved users. \nИзвините, бот работает только для одобренных пользователей."
    )
    return


@dp.message_handler(commands=["start", "help"])
async def welcome(message: types.Message):
    await message.reply("Привет, задавай свой вопрос")


@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=1.1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"],
    )
    await message.reply(response.choices[0].text)


if __name__ == "__main__":
    executor.start_polling(dp)
