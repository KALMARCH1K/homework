import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='')
dp = Dispatcher()
router = Router()

kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'),
                                    KeyboardButton(text='Информация')]], resize_keyboard=True)
inl_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Рассчитать норму калорий',
                                                                     callback_data='calories'),
                                                InlineKeyboardButton(text='Формулы расчета',
                                                                     callback_data='formulas')]])


class UsesState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@router.message(CommandStart())
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@router.message(F.text == 'Информация')
async def info(message):
    await message.answer('Информация:\nЭто учебный бот университета Urban. Он помогает твоему'
                         'здоровью!')


@router.message(F.text == 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=inl_kb)


@router.callback_query(F.data == 'formulas')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@router.callback_query(F.data == 'calories')
async def set_age(call, state: FSMContext):
    await state.set_state(UsesState.age)
    await call.message.answer('Введите свой возраст:')
    await call.answer()


@router.message(UsesState.age)
async def set_growth(message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UsesState.growth)
    await message.answer('Введите свой рост:')


@router.message(UsesState.growth)
async def set_weight(message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UsesState.weight)
    await message.answer('Введите свой вес:')


@router.message(UsesState.weight)
async def send_calories(message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    a = int(data['age'])
    g = int(data['growth'])
    w = int(data['weight'])
    res = 10 * w + 6.25 * g - 5 * a + 5
    await message.answer(f'Ваша норма: {res} ккал/сутки')
    await state.clear()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')