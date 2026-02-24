import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from dotenv import load_dotenv
import os
import random
from database import get_doctor_history, get_all_doctors, save_doctor, init_db

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")

if not API_TOKEN:
    print("ОШИБКА: Токен не найден в переменных окружения!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class Form(StatesGroup):
    doctor_name = State()
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    q9 = State()
    q10 = State()
    q11 = State()
    q12 = State()
    q13 = State()
    q14 = State()
    q15 = State()


@dp.message(Command("roll"))
async def cmd_roll(message: types.Message):
    random_number = random.randint(0, 99)
    await message.answer(f"🎲 Ваше число: {random_number}")

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Бот запущен. Введите фамилию врача: ")
    await state.set_state(Form.doctor_name)

@dp.message(Command("history"))
async def cmd_history(message: types.Message):
    rows = get_all_doctors()
    if not rows:
        await message.answer("База данных пуста.")
        return
    text = "📋 *Последние записи:*\n\n"
    for name, score, created_at in rows:
        date = created_at[:10] if created_at else "—"
        text += f"👨‍⚕️ *{name}* — {score} баллов ({date})\n"
    await message.answer(text, parse_mode="Markdown")


@dp.message(Command("doctor"))
async def cmd_doctor(message: types.Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.answer("Использование: /doctor Фамилия")
        return
    name = args[1].strip()
    rows = get_doctor_history(name)
    if not rows:
        await message.answer(f"Врач *{name}* не найден в базе.", parse_mode="Markdown")
        return
    text = f"👨‍⚕️ *История врача {name}:*\n\n"
    for score, created_at in rows:
        date = created_at[:10] if created_at else "—"
        text += f"• {score} баллов — {date}\n"
    await message.answer(text, parse_mode="Markdown")

@dp.message(Form.doctor_name)
async def process_doctor_name(message: types.Message, state: FSMContext):
    await state.update_data(q15=message.text)
    await message.answer(f"Врач: {message.text}\n\nВведите текущую нагрузку врача в процентах (от 0 до 160+):")
    await state.set_state(Form.q1)

@dp.message(Form.q1)
async def process_q1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text)
    await message.answer("Соблюдение стандартов медицинской помощи. Да - это выполнил, нарушений нет, а нет - имеются нарушения: ")
    await state.set_state(Form.q2)

@dp.message(Form.q2)
async def process_q2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text)
    await message.answer("Соблюдение  правил учета, порядка  хранения,  получения, использования лекарственных средств и медицинских изделий, сроков их годности. Введите: да - это выполнил, нарушений нет,а нет - имеются нарушения: ")
    await state.set_state(Form.q3)

@dp.message(Form.q3)
async def process_q3(message: types.Message, state: FSMContext):
    await state.update_data(q3=message.text)
    await message.answer("Введите количество направленных на прививки от врача (от 0 до 100+): ")
    await state.set_state(Form.q4)

@dp.message(Form.q4)
async def process_q4(message: types.Message, state: FSMContext):
    await state.update_data(q4=message.text)
    await message.answer("Случаи заболеваний, впервые выявленные в далеко зашедших стадиях, в т.ч. онкологические (случаи ЗНО, выявленные в 3-4 клинических стадиях по зависимым от врача причинам). Введите: нет или есть ")
    await state.set_state(Form.q5)

@dp.message(Form.q5)
async def process_q5(message: types.Message, state: FSMContext):
    await state.update_data(q5=message.text)
    await message.answer("Введите количество дефектов контроля качества (0, от 1 до 5, 5 и более): ")
    await state.set_state(Form.q6)

@dp.message(Form.q6)
async def process_q6(message: types.Message, state: FSMContext):
    await state.update_data(q6=message.text)
    await message.answer("Есть ли зарегистрированные благодарности в МЗ (введите: да или нет): ")
    await state.set_state(Form.q7)

@dp.message(Form.q7)
async def process_q7(message: types.Message, state: FSMContext):
    await state.update_data(q7=message.text)
    await message.answer("Введите случаи оформления диспансеризации (от 0 до 40+ случаев): ")
    await state.set_state(Form.q8)

@dp.message(Form.q8)
async def process_q8(message: types.Message, state: FSMContext):
    await state.update_data(q8=message.text)
    await message.answer("Введите количество направлений на диспансеризацию (от 0 до 100+ случаев): ")
    await state.set_state(Form.q9)

@dp.message(Form.q9)
async def process_q9(message: types.Message, state: FSMContext):
    await state.update_data(q9=message.text)
    await message.answer("Введите текущую нагрузку врача по диспансерному наблюдению (от 0 до 160+%) ")
    await state.set_state(Form.q10)

@dp.message(Form.q10)
async def process_q10(message: types.Message, state: FSMContext):
    await state.update_data(q10=message.text)
    await message.answer("Привлечение к дополнительной работе. Да - привлекался, нет - не привлекался: ")
    await state.set_state(Form.q11)

@dp.message(Form.q11)
async def process_q11(message: types.Message, state: FSMContext):
    await state.update_data(q11=message.text)
    await message.answer("Соблюдение правил внутреннего распорядка. Есть - выполнение, нет - имеется нарушение: ")
    await state.set_state(Form.q12)

@dp.message(Form.q12)
async def process_q12(message: types.Message, state: FSMContext):
    await state.update_data(q12=message.text)
    await message.answer("Соблюдение сроков оформления документов на МСЭ. Нет - до 30 дней без нарушений, есть - имеется нарушение сроков. ")
    await state.set_state(Form.q13)

@dp.message(Form.q13)
async def process_q13(message: types.Message, state: FSMContext):
    await state.update_data(q13=message.text)
    await message.answer("Выполнение СЭМД 500 и более (да или нет): ")
    await state.set_state(Form.q14)

@dp.message(Form.q14)
async def process_q14(message: types.Message, state: FSMContext):
    await state.update_data(q14=message.text)
    await process_final(message, state)

@dp.message(Form.q15)
async def process_final(message: types.Message, state: FSMContext):
    data = await state.get_data()
    base_result = 300

    def safe_float_get(key, default=0):
        try:
            val = data.get(key, default)
            if val == '':
                return 0
            return float(val)
        except (ValueError, TypeError):
            return 0

    def safe_str_get(key, default=''):
        val = data.get(key, default)
        if val is None:
            return ''
        return str(val).strip().lower()

    # 1 - Нагрузка врача
    number_of_cases = safe_float_get('q1')
    if number_of_cases <= 60:
        base_result *= 0.5
    elif number_of_cases <= 70:
        base_result *= 0.7
    elif number_of_cases <= 80:
        base_result *= 0.8
    elif number_of_cases <= 90:
        base_result *= 0.9
    elif number_of_cases <= 100:
        pass
    elif number_of_cases <= 130:
        base_result *= 1.1
    elif number_of_cases <= 160:
        base_result *= 1.2
    else:
        base_result *= 1.3


    # 2 - Стандарты медпомощи
    slovo = safe_str_get('q2')
    if slovo in ["нет", "no", "н"]:
        base_result -= 300 * 0.1


    # 3 - Учёт лекарств
    slovo = safe_str_get('q3')
    if slovo in ["нет", "no", "н"]:
        base_result -= 300 * 0.1

    # 4 - Направлено на прививки
    number_of_cases = safe_float_get('q4')
    if number_of_cases < 70:  # 4 arg
        base_result -= 300 * 0.1
    elif number_of_cases > 100:
        base_result += 300 * 0.1

    # 5 - Далеко зашедшие стадии (q5)
    slovo = safe_str_get('q5')
    if slovo in ["есть", "yes", "да", "д", "е"]:
        base_result -= 300 * 0.1

    # 6 - Дефекты контроля качества
    number_of_cases = safe_float_get('q6')
    if 1 <= number_of_cases < 5:
        base_result -= 300 * 0.1
    elif number_of_cases >= 5:
        base_result -= 300 * 0.2

    # 7 - Благодарности (q7)
    slovo = safe_str_get('q7')
    if slovo in ["да", "yes", "д"]:
        base_result += 300 * 0.1

    # 8 - Диспансеризация (оформление)
    number_of_cases = safe_float_get('q8')
    if number_of_cases == 20:
        base_result += 300 * 0.05
    elif 21 <= number_of_cases <= 30:
        base_result += 300 * 0.1
    elif 31 <= number_of_cases <= 40:
        base_result += 300 * 0.15
    elif number_of_cases >= 41:
        base_result += 300 * 0.2

    # 9 - Направления на диспансеризацию
    number_of_cases = safe_float_get('q9')
    if 51 <= number_of_cases <= 59:
        base_result += 300 * 0.05
    elif 60 <= number_of_cases <= 79:
        base_result += 300 * 0.1
    elif 80 <= number_of_cases <= 99:
        base_result += 300 * 0.15
    elif number_of_cases >= 100:
        base_result += 300 * 0.2

    # 10 - Диспансерное наблюдение
    number_of_cases = safe_float_get('q10')
    if number_of_cases <= 70:
        base_result -= 300 * 0.3
    elif 71 <= number_of_cases <= 80:
        base_result -= 300 * 0.2
    elif 81 <= number_of_cases <= 90:
        base_result -= 300 * 0.1
    elif 101 <= number_of_cases <= 130:
        base_result += 300 * 0.1
    elif 131 <= number_of_cases <= 160:
        base_result += 300 * 0.2
    elif number_of_cases >= 161:
        base_result += 300 * 0.3

    # 11 - Дополнительная работа
    slovo = safe_str_get('q11')
    if slovo in ["да", "yes", "д"]:
        base_result += 300 * 0.1

    # 12 - Внутренний распорядок
    slovo = safe_str_get('q12')
    if slovo in ["есть", "yes", "да", "д", "е"]:
        base_result -= 300 * 0.1

    # 13 - Сроки МСЭ
    slovo = safe_str_get('q13')
    if slovo in ["есть", "yes", "да", "д", "е"]:
        base_result -= 300 * 0.1

    # 14 - СЭМД
    slovo = safe_str_get('q14')
    if slovo in ["нет", "no", "н"]:
        base_result -= 300 * 0.1

    doctor_name = data.get('q15', '')
    final_score = int(base_result)

    save_doctor(doctor_name, final_score)

    history = get_doctor_history(doctor_name)

    result_text = (
        f"✅ Расчёт окончен!\n\n"
        f"👨‍⚕️ Врач: *{doctor_name}*\n"
        f"🏆 Стимулирующих баллов: *{final_score}*\n\n"
        f"📊 История последних расчётов:\n"
    )
    for score, created_at in history:
        date = created_at[:10] if created_at else "—"
        result_text += f"• {score} баллов — {date}\n"

    await message.answer(result_text, parse_mode="Markdown")
    await state.clear()


async def main():
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())