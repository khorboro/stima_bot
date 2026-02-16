ttl = 300
while True:
    cifra = int(input('Введите текущую нагрузку врача:')) #1
    if cifra <= 60:  # 1arg
        ttl = ttl - 300 * 0.5
    elif 61 <= cifra <= 70:
        ttl = ttl - 300 * 0.3
    elif 71 <= cifra <= 80:
        ttl = ttl - 300 * 0.2
    elif 81 <= cifra <= 90:
        ttl = ttl - 300 * 0.1
    elif 91 <= cifra <= 100:
        ttl = ttl
    elif 101 <= cifra <= 130:
        ttl = ttl + 300 * 0.1
    elif 131 <= cifra <= 160:
        ttl = ttl + 300 * 0.2
    elif cifra > 160:
        ttl = ttl + 300 * 0.3
    break

while True: #2
    slovo = input(
        "Соблюдение стандартов медицинской помощи. Введите: да или нет, где выполнил это да, где нарушения это нет:")
    if slovo == "Да".lower():  # 2 arg
        ttl = ttl
    elif slovo == "Нет".lower():
        ttl = ttl - 300 * 0.1
    break

while True: # 3
    slovo = input(
        "Соблюдение  правил учета, порядка  хранения,  получения, использования лекарственных средств и медицинских изделий, сроков их годности. Введите: да или нет, где отсутствие это да, где выявлено это нет:")
    if slovo == "Да".lower():  # 3 arg
        ttl = ttl
    elif slovo == "Нет".lower():
        ttl = ttl - 300 * 0.1
    break

while True: #4
    cifra = int(input("Введите количество направленных на прививки от врача:"))
    if cifra < 70:  # 4 arg
        ttl = ttl - 300 * 0.1
    elif 71 <= cifra <= 100:
        ttl = ttl
    elif cifra > 100:
        ttl = ttl + 300 * 0.1
    break

while True: # 5
    slovo = input(
        "Случаи заболеваний, впервые выявленные в далеко зашедших стадиях, в т.ч. онкологические (случаи ЗНО, выявленные в 3-4 клинических стадиях по зависимым от врача причинам). Введите: нет или есть, где 1) это отсутствие, 2) есть нарушения. n - количество нарушений")
    if slovo == "Нет".lower():  # 5arg
        ttl = ttl
    elif slovo == "Есть".lower():
        n = int(input())
        ttl = ttl - 300 * (0.1 * n)
    break

while True:  # 6
    cifra = int(input("Введите количество дефектов контроля качества: "))
    if cifra == 0:
        ttl = ttl
    elif 1 <= cifra < 5:
        ttl = ttl - 300 * 0.1
    elif cifra >= 5:
        ttl = ttl - 300 * 0.2
    break

while True:  # 7
    slovo = input("Введите: да или нет, есть или нет благодарности в МЗ:")
    if slovo == "Да".lower():
        ttl = ttl + 300 * 0.1
    elif slovo == "Нет".lower():
        ttl = ttl
    break

while True: #8
    cifra = int(input("Введите случаи оформления диспансеризации:"))
    if cifra == 20:
        ttl = ttl + 300 * 0.05
    elif cifra < 20:
        ttl = ttl
    elif 21 <= cifra <= 30:
        ttl = ttl + 300 * 0.1
    elif 31 <= cifra <= 40:
        ttl = ttl + 300 * 0.15
    elif cifra >= 31:
        ttl += 300 * 0.2
    break

while True: #9
    cifra = int(input("Введите количество направлений на диспансеризацию:"))
    if cifra <= 50:
        ttl = ttl
    elif 51 <= cifra <= 59:
        ttl += 300 * 0.05
    elif 60 <= cifra <= 79:
        ttl += 300 * 0.1
    elif 80 <= cifra <= 99:
        ttl += 300 * 0.15
    elif cifra >= 100:
        ttl += 300 * 0.2
    break

while True:
    cifra = int(input("Введите текущую нагрузку врача по диспансерному наблюдению:"))
    if cifra <= 70:
        ttl -= 300 * 0.3
    elif 71 <= cifra <= 80:
        ttl -= 300 * 0.2
    elif 81 <= cifra <= 90:
        ttl -= 300 * 0.1
    elif 91 <= cifra <= 100:
        ttl = ttl
    elif 101 <= cifra <= 130:
        ttl += 300 * 0.1
    elif 131 <= cifra <= 160:
        ttl += 300 * 0.2
    elif cifra >= 161:
        ttl += 300 * 0.3
    break

while True:
    slovo = input("Привлечение к дополнительной работе. Введите: да или нет, 1) привлекался, 2) не привлекался: ")
    if slovo == 'Да'.lower():
        ttl += 300 * 0.1
    elif slovo == "Нет".lower():
        ttl = ttl
    break

while True:
    slovo = input(
        "Соблюдение правил внутреннего распорядка. Введите: нет или есть, где: 1) выполнение, 2) имеется нарушение. n - количество нарушений")
    if slovo == "Нет".lower():
        ttl = ttl
    elif slovo == "есть".lower():
        n = int(input())
        ttl -= 300 * (0.1 * n)
    break

while True:
    slovo = input(
        "Соблюдение сроков оформления документов на МСЭ. Введите: нет или есть, где: 1) до 30 дней, 2) имеется нарушение сроков. n - количество нарушений сроков")
    if slovo == "Нет".lower():
        ttl = ttl
    elif slovo=="есть".lower():
        n=int(input())
        ttl-=300*(0.1*n)
    break

while True:
    slovo=input("Выполнение СЭМД 500 и более. Введите: да или нет, 1)выполнение, 2) не выполнение: ")
    if slovo == "Да".lower():
        ttl=ttl
    elif slovo == "Нет".lower():
        ttl-=300*0.1
    break

print(f'Итоговое количество баллов: {ttl}')



