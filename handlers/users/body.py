import logging



import asyncio

from aiogram.types import InputFile
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.types import ContentType, Message

from photos import *
from photos.credit_image import *
from keyboards.inline.callback_buttom import *

from loader import dp, bot




@dp.message_handler(text='🛸Поделиться с другом')
async def send_friends(message: Message):
    await message.answer('Жми на "Поделиться ботом" 👇', reply_markup=send_bot)


@dp.message_handler(text="🏪Подобрать банк")
async def found_bank(message: Message):
    photo = InputFile(path_or_bytesio="photos/loading1.jpg")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=(f"<i>Приступаю к поиску </i>"))

    await asyncio.sleep(3)

    photo1 = InputFile(path_or_bytesio="photos/loading2.jpg")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo1, caption=(f"<i><b>Поиск успешно выполнен!</b></i>\n"
                                                                            f"<i>Мне было очень сложно найти банки с хорошими условиями</i>\n"
                                                                            f"<i>которые могут продолжать свою работу во время кризиса! </i>\n"
                                                                            f"<i>Поэтому если тебе нужны деньги срочно</i>\n"
                                                                            f"<i>советую тебе заполнить анкеты во всех банках</i>"), reply_markup=show_search)

@dp.message_handler(text='👑Популяриные предложения')
async def popular_value(message: Message):
    await message.answer("Выбери подходящее предложение👇🏻", reply_markup=popular_menu)


# ВНИЗУ БУДЕ КРЕДИТНЕ МЕНЮ
@dp.callback_query_handler(text="show_credit")
async def firs_catalog(call: CallbackQuery):
    photo2 = InputFile(path_or_bytesio="photos/credit_image/Miloan.jpg")
    await call.message.reply_photo(photo=photo2, caption=("<b>Miloan</b> - <i>При помощи нашего сервиса, каждый желающий</i>\n"
                                                            "<i>может получить кредит прямо на свою банковскую карту и </i>\n"
                                                            "<i>всего за 15 минут. Первый кредит бесплатно (под 0,01%). Сумма</i>\n"
                                                            "<i>первого займа – до 15000 гривен.</i>\n"
                                                            "<a href='https://rozetka.com.ua'>Подробнее</a>👈\n\n"
                                                            "<b>Условия:</b>\n"
                                                            "• Сумма займа: Первый займ – до 15000 гривен\n"
                                                            "• Срок займа: до 30 дней\n"
                                                            "• Скидки на повторные кредиты\n\n"
                                                            "<b>Требование к заёмщику:</b>\n"
                                                            "• Возраст: от 18 до 65 лет\n"
                                                            "• Гражданство Украины\n"
                                                            "• Наличие действующей банковской карты любого украинского банка\n"
                                                            "• Отсутствие просрочек по кредитам"
                                                        ), reply_markup=first_klick)
                                                                                                                    
                                                                                                                    
@dp.callback_query_handler(text="give_next")           
async def second_catalog(call: CallbackQuery):
    photo3 = InputFile(path_or_bytesio="photos/credit_image/bistro_dengi.jpg")
    await call.message.reply_photo(photo=photo3, caption=("<b>ШвидкоГроші</b> - <i>лидер украинского рынка моментального</i>\n"
                                                            "<i>кредитования. Компания предоставляет моментальные  </i>\n"
                                                            "<i>кредиты ОНЛАЙН и наличными до 5000 грн. без залога, справок и</i>\n"
                                                            "<i>поручителей.</i>\n"
                                                            "<a href='https://rozetka.com.ua'>Подробнее</a>👈\n\n"
                                                            "<b>Условия:</b>\n"
                                                            "• Сумма займа: от 600 до 10 000 грн.\n"
                                                            "• Для повторных клиентов - до 20 000 грн. под 1%\n"
                                                            "• Сроки пользования кредитом можно продлевать, при оплате процентов за пользование\n\n"
                                                            "<b>Требование к заёмщику:</b>\n"
                                                            "• Возраст: от 18 до 60 лет\n"
                                                            "• Гражданство Украины\n"
                                                            "• Наличие у клиента постоянного трудового дохода (может работать неофициально)"
                                                                    ), reply_markup=second_menu)   


@dp.callback_query_handler(text="next_variant")           
async def gotovka_catalog(call: CallbackQuery):
    photo3 = InputFile(path_or_bytesio="photos/credit_image/credit1.jpg")
    await call.message.reply_photo(photo=photo3, caption=("<b>Ваша Готивочка</b> - <i>Главной составляющей системы </i>\n"
                                                            "<i>кредитования 'Ваша Готівочка' является удобство! </i>\n"
                                                            "<i>Мы предлагаем простые и понятные условия займа.</i>\n"
                                                            
                                                            "<a href='https://rozetka.com.ua'>Подробнее</a>👈\n\n"
                                                            "<b>Условия:</b>\n"
                                                            "• Сумма займа: от 200 до 9000 грн.\n"
                                                            "• Время рассмотрения заявки – 15 мин.\n"
                                                            "• Без справки о доходах\n\n"

                                                            "<b>Преимущества.</b>\n"
                                                            "не просим клиента ксерокопию документов или фото документов\n"
                                                            "не просим клиента фото с паспортом или банковской картой\n"
                                                            "не просим клиента указывать аккаунт в социальной сети\n"
                                                            "не просим у клиента справку о доходах\n"
                                                            "не просим клиента телефон родственника\n\n"

                                                            "<b>Требование к заёмщику:</b>\n"
                                                            "• Возраст: от 18 до 60 лет\n"
                                                            "• Гражданство Украины\n"
                                                            "• наличие банковской карты (для перечисления кредитных средств) и мобильного телефона"
                                                                    ), reply_markup=there_menu)                                                                                                                                               
                                                                   
                                                                       
                                                                       
@dp.callback_query_handler(text="gotivochka3")           
async def credit_plus(call: CallbackQuery):
    photo3 = InputFile(path_or_bytesio="photos/credit_image/credit2.jpg")
    await call.message.reply_photo(photo=photo3, caption=("<b>CreditPlus</b> - <i>Мы являемся обществом со 100% иностранным </i>\n"
                                                            "<i>капиталом. Благодаря этому ведем ответственный бизнес в</i>\n"
                                                            "<i>Украине, который включает набор обязательных целей и </i>\n"
                                                            "<i>гарантий для всех заинтересованных сторон.</i>\n"
                                                            "<a href='https://rozetka.com.ua'>Подробнее</a>👈\n\n"
                                                            "<b>Условия:</b>\n"
                                                            "• Сумма займа:  до 15 000 грн.\n"
                                                            "• Время рассмотрения заявки – до 7 минут\n"
                                                            "• Без справки о доходах\n\n"
                                                            "<b>Требование к заёмщику:</b>\n"
                                                            "• Возраст: от 18 до 55 лет\n"
                                                            "• Гражданство Украины\n"
                                                            "• наличие банковской карты (для перечисления кредитных средств) и мобильного телефона"
                                                                    ), reply_markup=foo_menu)                                                                          
                                                                       
                                                                       
                                                                    
@dp.callback_query_handler(text="crediplus")
async def evro_groshi(call: CallbackData):
    photo4 = InputFile(path_or_bytesio="photos/credit_image/evrogroshi.jpg")
    await call.message.reply_photo(photo=photo4, caption=(
                                                        '<b>Eurogroshi</b> - <i>При помощи нашего сервиса, каждый желающий </i>\n'
                                                        '<i>может получить кредит прямо на свою банковскую карту и </i>\n'
                                                        '<i>всего за 15 минут</i>\n'
                                                        '<a href="https://rozetka.com.ua">Подробнее</a>👈\n\n'
                                                        '<b>Условия:</b>\n'
                                                        '• Сумма первого займа: до 4500 грн.\n'
                                                        '• Срок займа: до 30 дней\n'
                                                        '• Скидки на повторные кредиты\n\n'
                                                        "<b>Требование к заёмщику:</b>\n"
                                                        '• Возраст: от 18 лет\n'
                                                        '• Гражданство Украины\n'
                                                        '• Наличие действующей банковской карты любого украинского банка\n'
                                                        '• Отсутствие просрочек по кредитам\n'
                                                        ), reply_markup=five_menu)     

@dp.callback_query_handler(text="evrogroshi")
async def zecredit(call: CallbackData):
    photo5 = InputFile(path_or_bytesio="photos/credit_image/zecreditor.jpg")
    await call.message.reply_photo(photo=photo5, caption=(
                                                        '<b>Zecredit</b> - <i>это онлайн сервис благодаря которому наш клиент </i>\n'
                                                        '<i>может получить кредит всего за считанные минуты на </i>\n'
                                                        '<i>банковскую карту. Благодаря условиям конкуренции рынка т</i>\n'                                                        '<a href="https://rozetka.com.ua">Подробнее</a>👈\n\n'
                                                        '<i>нашей компанией была выбрана стратегия программы </i>\n'
                                                        '<i>лояльности для клиентов. Компания работает прозрачно, что </i>\n'
                                                        '<i>формирует доверие у основного сегмента рынка.</i>\n'
                                                        '<a href="https://rozetka.com.ua">Подробнее</a>👈\n\n'
                                                        '<b>Условия:</b>\n'
                                                        '• Сумма первого займа: до 3000 грн.\n'
                                                        '• Срок займа: до 30 дней\n'
                                                        '• Cервис работает круглосуточно, акция 1% на первый кредит\n\n'
                                                        "<b>Требование к заёмщику:</b>\n"
                                                        '• Возраст: от 18 лет\n'
                                                        '• Гражданство Украины\n'
                                                        '• Наличие действующей банковской карты любого украинского банка\n'
                                                        '• Отсутствие просрочек по кредитам\n'
                                                        ), reply_markup=six_menu)                                                                                   
