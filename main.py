import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from dotenv import load_dotenv
import os

load_dotenv()


API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

class Form(StatesGroup):
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

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer("Бот запущен. Введите текущую нагрузку врача в процентах: ")
    await state.set_state(Form.q1)


@dp.message(Form.q1)
async def process_q1(message: types.Message, state: FSMContext):
    await state.update_data(q1=message.text)
    await message.answer("Соблюдение стандартов медицинской помощи. Введите: да или нет, где выполнил это да, где нарушения это нет: ")
    await state.set_state(Form.q2)

@dp.message(Form.q2)
async def process_q2(message: types.Message, state: FSMContext):
    await state.update_data(q2=message.text)
    await message.answer("Соблюдение  правил учета, порядка  хранения,  получения, использования лекарственных средств и медицинских изделий, сроков их годности. Введите: да или нет, где отсутствие это да, где выявлено это нет: ")
    await state.set_state(Form.q3)

@dp.message(Form.q3)
async def process_q3(message: types.Message, state: FSMContext):
    await state.update_data(q3=message.text)
    await message.answer("Введите количество направленных на прививки от врача: ")
    await state.set_state(Form.q4)

@dp.message(Form.q4)
async def process_q4(message: types.Message, state: FSMContext):
    await state.update_data(q4=message.text)
    await message.answer("Случаи заболеваний, впервые выявленные в далеко зашедших стадиях, в т.ч. онкологические (случаи ЗНО, выявленные в 3-4 клинических стадиях по зависимым от врача причинам). Введите: нет или есть ")
    await state.set_state(Form.q5)

@dp.message(Form.q5)
async def process_q5(message: types.Message, state: FSMContext):
    await state.update_data(q5=message.text)
    await message.answer("Введите количество дефектов контроля качества: ")
    await state.set_state(Form.q6)

@dp.message(Form.q6)
async def process_q6(message: types.Message, state: FSMContext):
    await state.update_data(q6=message.text)
    await message.answer("Введите: да или нет, есть или нет благодарности в МЗ: ")
    await state.set_state(Form.q7)

@dp.message(Form.q7)
async def process_q7(message: types.Message, state: FSMContext):
    await state.update_data(q7=message.text)
    await message.answer("Введите случаи оформления диспансеризации: ")
    await state.set_state(Form.q8)

@dp.message(Form.q8)
async def process_q8(message: types.Message, state: FSMContext):
    await state.update_data(q8=message.text)
    await message.answer("Введите количество направлений на диспансеризацию: ")
    await state.set_state(Form.q9)

@dp.message(Form.q9)
async def process_q9(message: types.Message, state: FSMContext):
    await state.update_data(q9=message.text)
    await message.answer("Введите текущую нагрузку врача по диспансерному наблюдению: ")
    await state.set_state(Form.q10)

@dp.message(Form.q10)
async def process_q10(message: types.Message, state: FSMContext):
    await state.update_data(q10=message.text)
    await message.answer("Привлечение к дополнительной работе. Введите: да или нет, 1) привлекался, 2) не привлекался: ")
    await state.set_state(Form.q11)

@dp.message(Form.q11)
async def process_q11(message: types.Message, state: FSMContext):
    await state.update_data(q11=message.text)
    await message.answer("облюдение правил внутреннего распорядка. Введите: нет или есть, где: 1) выполнение, 2) имеется нарушение: ")
    await state.set_state(Form.q12)

@dp.message(Form.q12)
async def process_q12(message: types.Message, state: FSMContext):
    await state.update_data(q12=message.text)
    await message.answer("Соблюдение сроков оформления документов на МСЭ. Введите: нет или есть, где: 1) до 30 дней, 2) имеется нарушение сроков. ")
    await state.set_state(Form.q13)

@dp.message(Form.q13)
async def process_q13(message: types.Message, state: FSMContext):
    await state.update_data(q13=message.text)
    await message.answer("Выполнение СЭМД 500 и более. Введите: да или нет, 1)выполнение, 2) не выполнение: ")
    await state.set_state(Form.q14)


@dp.message(Form.q14)
async def process_final(message: types.Message, state: FSMContext):
    await state.update_data(q14=message.text)
    data = await state.get_data()
    base_result = 300
    try:
        # Преобразуем строку из state в число
        cifra = int(float(data.get('q1', 0))) #1

        # Логика расчета коэффициентов
        if cifra <= 60:
            base_result *= 0.5
        elif cifra <= 70:
            base_result *= 0.7
        elif cifra <= 80:
            base_result *= 0.8
        elif cifra <= 90:
            base_result *= 0.9
        elif cifra <= 100:
            pass
        elif cifra <= 130:
            base_result *= 1.1
        elif cifra <= 160:
            base_result *= 1.2
        else:
            base_result *= 1.3
    except ValueError:
        await message.answer("Ошибка в данных вопроса №1. Похоже, там введено не число.")

    try: #2
        slovo = data.get('q2', '').strip().lower()
        if slovo == "Нет".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №2. Похоже, там введено не слово.")

    try: #3
        slovo = data.get('q3', '').strip().lower()
        if slovo == "Нет".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №3. Похоже, там введено не слово.")

    try: #4
        cifra = int(float(data.get('q4', 0)))

        if cifra < 70:  # 4 arg
            base_result -= 300 * 0.1
        elif cifra > 100:
            base_result += 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №4. Похоже, там введено не число.")

    try: #5
        slovo = data.get('q5', '').strip().lower()
        if slovo == "Нет".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №5. Похоже, там введено не слово.")

    try: #6
        cifra = int(float(data.get('q6', 0)))

        if 1 <= cifra < 5:
            base_result -= 300 * 0.1
        elif cifra >= 5:
            base_result -= 300 * 0.2
    except ValueError:
        await message.answer("Ошибка в данных вопроса №6. Похоже, там введено не число.")

    try: #7
        slovo = data.get('q7', '').strip().lower()
        if slovo == "Нет".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №7. Похоже, там введено не слово.")

    try: #8
        cifra = int(float(data.get('q8', 0)))

        if cifra == 20:
            base_result += 300 * 0.05
        elif 21 <= cifra <= 30:
            base_result += 300 * 0.1
        elif 31 <= cifra <= 40:
            base_result += 300 * 0.15
        elif cifra >= 31:
            base_result += 300 * 0.2
    except ValueError:
        await message.answer("Ошибка в данных вопроса №8. Похоже, там введенf не число.")

    try: #8
        cifra = int(float(data.get('q9', 0)))

        if 51 <= cifra <= 59:
            base_result += 300 * 0.05
        elif 60 <= cifra <= 79:
            base_result += 300 * 0.1
        elif 80 <= cifra <= 99:
            base_result += 300 * 0.15
        elif cifra >= 100:
            base_result += 300 * 0.2
    except ValueError:
        await message.answer("Ошибка в данных вопроса №9. Похоже, там введенf не число.")

    try: #9
        cifra = int(float(data.get('q10', 0)))

        if cifra <= 70:
            base_result -= 300 * 0.3
        elif 71 <= cifra <= 80:
            base_result -= 300 * 0.2
        elif 81 <= cifra <= 90:
            base_result -= 300 * 0.1
        elif 101 <= cifra <= 130:
            base_result += 300 * 0.1
        elif 131 <= cifra <= 160:
            base_result += 300 * 0.2
        elif cifra >= 161:
            base_result += 300 * 0.3
    except ValueError:
        await message.answer("Ошибка в данных вопроса №10. Похоже, там введенf не число.")

    try: #10
        slovo = data.get('q11', '').strip().lower()
        if slovo == "Да".lower():
            base_result += 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №11. Похоже, там введено не слово.")

    try:
        slovo = data.get('q12', '').strip().lower()
        if slovo == "Есть".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №12. Похоже, там введено не слово.")

    try:
        slovo = data.get('q13', '').strip().lower()
        if slovo == "Есть".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №13. Похоже, там введено не слово.")

    try:
        slovo = data.get('q14', '').strip().lower()
        if slovo == "Нет".lower():
            base_result -= 300 * 0.1
    except ValueError:
        await message.answer("Ошибка в данных вопроса №14. Похоже, там введено не слово.")

    await message.answer(f"Расчет окончен! Итоговое значение: {base_result}")
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())