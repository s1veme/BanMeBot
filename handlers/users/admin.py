from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot

from filters import IsAdmin

from utils.json_utils import text_json

@dp.message_handler(IsAdmin(), Command(commands='getwords', prefixes='/'))
async def get_words(message: types.Message):
    BLACKLIST_WORDS = message.bot.get('BLACKLIST_WORDS')
    
    if not BLACKLIST_WORDS:
        return await message.answer('Список слов пуст :(')
    
    text = ''
    for index, word in enumerate(BLACKLIST_WORDS):
        text += f'{index} - {word}\n'
        
    await message.answer(text)
    
    
@dp.message_handler(IsAdmin(), Command(commands='addword', prefixes='/'))
async def get_words(message: types.Message):
    text = message.text.strip('/addword')
    text = text.lstrip()
    
    BLACKLIST_WORDS = message.bot.get('BLACKLIST_WORDS')    
    if not text:
        return await message.answer('Нельзя добавить ничего')
    
    if text in BLACKLIST_WORDS:
        return await message.answer('Такой текст уже есть!')
    
    message.bot['BLACKLIST_WORDS'] = text_json.add_word(text)['words']  
    
    
@dp.message_handler(IsAdmin(), Command(commands='rmword', prefixes='/'))
async def remove_word(message: types.Message):
    try:
        word_id = int(message.text.strip('/rmword '))
    except ValueError:
        return await message.answer('Вы должны ввести индекс! Только числа!')

    BLACKLIST_WORDS = message.bot.get('BLACKLIST_WORDS')
    try:
        del BLACKLIST_WORDS[word_id]
    except IndexError:
        return await message.answer('Такого слова нет!')
    
    text_json.remove_word(BLACKLIST_WORDS)
    message.bot['BLACKLIST_WORDS'] = BLACKLIST_WORDS
        