# Тестовые данные (переменные)
expected_title = "Swag Labs"
actual_title = "Swag Labs"

# Простая проверка через условие
if actual_title == expected_title:
    print("Тест пройден: заголовок страницы совпадает!")
else:
    print("Тест упал: заголовки разные.")

# Настоящая проверка из автотестов (assert)
# Если значения не совпадут, Python сам остановит тест и выдаст ошибку
assert actual_title == expected_title, f"Ожидали {expected_title}, но получили {actual_title}"
print("Проверка assert тоже прошла успешно!")
