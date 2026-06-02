import pandas as pd

# 1. Загрузка файла
data_path = '../data/basket_charged.csv'
basket_data = pd.read_csv(data_path, decimal=',', dtype={'CHARGED_AMOUNT': 'float64'})

# 2. Проверка первых строк данных
print("Первые 5 строк данных:")
print(basket_data.head())

# 3. Проверка общей информации о данных
print("\nИнформация о данных:")
print(basket_data.info())

# 4. Проверка пропусков
print("\nПропуски в данных:")
print(basket_data.isnull().sum())

# 5. Преобразование столбца DATETIME в формат даты
basket_data['DATETIME'] = pd.to_datetime(basket_data['DATETIME'])

# 6. Проверка типов данных после преобразования
print("\nТипы данных после преобразования:")
print(basket_data.dtypes)

# 7. Базовая статистика по количеству загруженных материалов
print("\nБазовая статистика по CHARGED_AMOUNT:")
print(basket_data['CHARGED_AMOUNT'].describe())

# 8. Уникальные материалы и их коды
print("\nУникальные материалы:")
print(basket_data[['MAT_CODE', 'MAT_DEC']].drop_duplicates())