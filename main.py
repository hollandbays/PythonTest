from aiogram import Bot,Dispatcher,executor, types
import python_weather
import asyncio

bot = Bot(token= "6138706563:AAG3HnfODXnH4sLeyMfHfTILTod2plBdX0Q")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather)

#echo
@dp.message_handler()
async  def echo(message: types.Message):
 weather = await client.find(message.text)
 celcius = (weather.current.temperature-32)/1.8

 resp_msg  = weather.location_name
 resp_msg += f"ТемпературА: {celcius}"
 await message.answer(resp_msg)
#run running poly
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
