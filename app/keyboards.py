from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝Каталог'),
            KeyboardButton(text='📞Связь'),
        ],
        [
            KeyboardButton(text='⚙️Админ-панель'),
            KeyboardButton(text='🛒Корзина'),
        ]
    ], resize_keyboard=True)


async def category():
    category_keyboard = InlineKeyboardBuilder()
    category_keyboard.add(InlineKeyboardButton(text="✅ категория 1", callback_data="category1"))
    category_keyboard.add(InlineKeyboardButton(text="✅ категория 2", callback_data="category2"))
    category_keyboard.add(InlineKeyboardButton(text="✅ категория 3", callback_data="category3"))
    return category_keyboard.adjust(1).as_markup()


async def back():
    subcategory_keyboard = InlineKeyboardBuilder()
    subcategory_keyboard.add(InlineKeyboardButton(text="🔙 Назад", callback_data="back_"))
    return subcategory_keyboard.adjust(1).as_markup()


async def subcategory():
    subcategory_keyboard = InlineKeyboardBuilder()
    subcategory_keyboard.add(InlineKeyboardButton(text="✅ подкатегория 1", callback_data="subcategory1"))
    subcategory_keyboard.add(InlineKeyboardButton(text="✅ подкатегория 2", callback_data="subcategory2"))
    subcategory_keyboard.add(InlineKeyboardButton(text="✅ подкатегория 3", callback_data="subcategory3"))
    return subcategory_keyboard.adjust(1).as_markup()


async def item():
    item_keyboard = InlineKeyboardBuilder()
    item_keyboard.add(InlineKeyboardButton(text="✅ товар/услуга 1", callback_data="item1"))
    item_keyboard.add(InlineKeyboardButton(text="✅ товар/услуга 2", callback_data="item2"))
    item_keyboard.add(InlineKeyboardButton(text="✅ товар/услуга 3", callback_data="item3"))
    return item_keyboard.adjust(1).as_markup()


async def basket_item():
    basket_keyboard = InlineKeyboardBuilder()
    basket_keyboard.add(InlineKeyboardButton(text="🗑 Добавить в корзину", callback_data="basket"))
    basket_keyboard.add(InlineKeyboardButton(text="💬 Связаться с менеджером", url='https://t.me/asdqzef'))
    basket_keyboard.add(InlineKeyboardButton(text="🔙 Назад", callback_data="back_"))
    return basket_keyboard.adjust(1).as_markup()


async def contact():
    contact_back = InlineKeyboardBuilder()
    contact_back.add(InlineKeyboardButton(text="🔙 Вернуться", callback_data="backContact"))
    return contact_back.adjust(1).as_markup()


async def apanel():
    akeyboard = InlineKeyboardBuilder()
    akeyboard.add(InlineKeyboardButton(text="Обновление карточек товаров", callback_data="update"))
    akeyboard.add(InlineKeyboardButton(text="Добавление новых карточек", callback_data="add"))
    akeyboard.add(InlineKeyboardButton(text="Удаление неактуальных карточек товаров", callback_data="delete"))
    akeyboard.add(InlineKeyboardButton(text="🔙 Вернуться", callback_data="backContact"))
    return akeyboard.adjust(1).as_markup()

async def basket():
    bkeyboard = InlineKeyboardBuilder()
    bkeyboard.add(InlineKeyboardButton(text="Оплатить", callback_data="pay"))
    bkeyboard.add(InlineKeyboardButton(text="🔙 Вернуться", callback_data="backContact"))
    return bkeyboard.adjust(1).as_markup()
