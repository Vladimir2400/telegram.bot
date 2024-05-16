from aiogram import Router, F
from aiogram.client import bot
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile

import app.keyboards as kb

router = Router()

welcome_text = '''🌐 Добро пожаловать на интерактивную витрину нашего бота RobKO2400! 🤖✨
\nНачнем знакомство c функционалом:
\n- Данное сообщение, которое вы получили является ознакомительным текстом бота, его можно редактировать под ваши нужды.
\n- Снизу вышло меню кнопок для взаимодействий с ботом. Их можно сделать неограниченое количество и каждая кнопка может иметь свой функционал.
\n- Так же можете посмотреть функционал telegram web app, нажав на кнопку 'Магазин'.'''


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEMC0NmNJa2FMuZNviHdFYh-6wY3--ZGAACAQADFm5MEh97vwZE6duLNAQ')
    await message.answer(f'Здравствуй, {message.from_user.full_name}!\n\n{welcome_text}', reply_markup=kb.main)


@router.message(F.text == '📝Каталог')
async def cmd_catalog(message: Message):
    await message.delete()
    category_text = '''(⬆️Здесь может быть ваша фотография)
\nДобро пожаловать в каталог! Здесь вы можете настроить содержание по своему усмотрению. 
Ниже представлены кнопки, каждая из которых ведет в соответствующий раздел. 
В каждом разделе могут быть как уникальные, так и общие для всего каталога данные и опции. 
Нажмите на кнопку, чтобы перейти в интересующий вас раздел.'''
    await message.answer_photo(photo=FSInputFile('app/database/photos/категория.png'), caption=category_text,
                               reply_markup=await kb.category())


@router.callback_query(F.data.startswith('category'))
async def cmd_category(callback: CallbackQuery):
    await callback.answer('')
    category = callback.data[len('category'):]

    if category == '3':
        await callback.message.delete()
        await callback.message.answer(
            text='(⬆️здесь так же можно добавлять фото)\nА для категории 3 мы создали подкатегории и кнопки для перехода⤵️',
            reply_markup=await kb.subcategory())
    elif category == '1':
        await callback.message.delete()
        await callback.message.answer_photo(photo=FSInputFile('app/database/photos/лого.png'),
                                            caption='Обратите внимание, что каждый раздел предлагает либо повторяющиеся, либо уникальные информации и действия. В категории 1 уже обновлены изображение и описание для вашего удобства.',
                                            reply_markup=await kb.back())
    elif category == '2':
        await callback.message.edit_caption(
            caption='Для категории 2 здесь мы оставили картинку но сменили описание. Все гибко не правда ли?',
            reply_markup=await kb.back())


@router.callback_query(F.data.startswith('subcategory'))
async def cmd_subcategory(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        text='(⬆️здесь так же можно добавлять фото)\nВы также можете создавать дополнительные подуровни внутри подкатегорий, вместе с кнопками, обеспечивающими легкость навигации и перехода между разделами.',
        reply_markup=await kb.item())


@router.callback_query(F.data.startswith('item'))
async def cmd_subcategory(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.delete()
    await callback.message.answer_photo(photo=FSInputFile('app/database/photos/product.png'),
                                        caption='Здесь можно создать карточку определенного продукта и добавить кнопки для разных взаимодействий с ней\n\nЦена:',
                                        reply_markup=await kb.basket_item())
    # await callback.message.edit_text(text='здесь товары/услуги подкатегории 1', reply_markup=await kb.back())


@router.callback_query(F.data.startswith('back_'))
async def back_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    category_text = '''(⬆️Здесь может быть ваша фотография)
\nДобро пожаловать в каталог! Здесь вы можете настроить содержание по своему усмотрению. 
Ниже представлены кнопки, каждая из которых ведет в соответствующий раздел. 
В каждом разделе могут быть как уникальные, так и общие для всего каталога данные и опции. 
Нажмите на кнопку, чтобы перейти в интересующий вас раздел.'''
    await callback.message.answer_photo(photo=FSInputFile('app/database/photos/категория.png'), caption=category_text,
                                        reply_markup=await kb.category())


@router.message(F.text == '📞Связь')
async def contact(message: Message):
    await message.delete()
    await message.answer_photo(photo=FSInputFile('app/database/photos/whatsapp.jpg'), caption='''🤖 Хотите собственного бота? 🎩 Да легко!

🔍 Отсканируйте этот QR-код, как истинный сыщик, или отправьте мне сообщение в телеграфном стиле по адреcу @asdqzef в Телеграм!

📧 Или можете просто послать голубя с письмом на petrov_vova00@mail.ru - решать вам! (Только убедитесь, что ваш голубь знает, куда лететь!)

P.S. А вместо моего текста мог быть и ваш, но не обязательно.''', reply_markup=await kb.contact())


@router.callback_query(F.data.startswith('backContact'))
async def back_button(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()


@router.message(F.text == '⚙️Админ-панель')
async def admin_panel(message: Message):
    await message.delete()
    await message.answer('''Доступ в админ-панель разрешен!
\nАдмин панель можно настроить так, чтобы только определенные люди могли пользоваться ею. 
\nАдмин панель нужна для того чтобы исполнять какие-либо действия, к примеру сообщение-рассылка отправляет какое то сообщение от имени бота всем клиентам(очень удобный и полезный функционал).
Так же можно добавлять взаимодействия с ботом, что дает возможность не лезть в код бота, а менять все через админ панель. Вот несколько примеров: ''',
                         reply_markup=await kb.apanel())

@router.message(F.text == '🛒Корзина')
async def basket(message: Message):
    await message.delete()
    await message.answer_photo(photo=FSInputFile('app/database/photos/kassa.jpg'), caption='''Тут будет корзина и при нажатии на нее будут отображаться товары, которые добавил клиент.
В телеграме есть возможность добавить платежную систему(они указаны на картинке).
Если есть доп вопросы, то пишите сюда @asdqzef''', reply_markup=await kb.basket())

@router.callback_query(F.data.startswith('pay'))
async def pay(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()
    await callback.message.answer('<Тут будет платежная система> и после оплаты менеджер получит уведомление о заказе', reply_markup=await kb.contact())