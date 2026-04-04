import csv
from connect import connect

def create_table():
    connection = connect()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL
                );
            """)
            connection.commit()
            print("Таблица готова к работе.")
        except Exception as ex:
            print(f"Ошибка БД: {ex}")
        finally:
            cursor.close()
            connection.close()

#ВЫЗОВЫ ПРОЦЕДУР (CALL)

def upsert_contact(name, phone):
    """Задача 2: Вызов процедуры Insert or Update"""
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()
            print(f"Контакт {name} успешно обработан (добавлен/обновлен).")
        except Exception as ex:
            print(f"Ошибка процедуры upsert: {ex}")
        finally:
            cur.close()
            conn.close()

def delete_contact_proc(name=None, phone=None):
    """Задача 5: Вызов процедуры удаления"""
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            # Передаем None для тех параметров, которые не используем
            cur.execute("CALL delete_contact_proc(NULL, %s, %s)", (name or None, phone or None))
            conn.commit()
            print("Запрос на удаление выполнен.")
        except Exception as ex:
            print(f"Ошибка удаления: {ex}")
        finally:
            cur.close()
            conn.close()

def bulk_insert(file_path):
    """Задача 3: Массовая вставка из CSV через процедуру с валидацией"""
    conn = connect()
    if conn:
        try:
            names, phones = [], []
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader) # Пропуск заголовка
                for row in reader:
                    names.append(row[0])
                    phones.append(row[1])
            
            cur = conn.cursor()
            cur.execute("CALL bulk_insert_contacts(%s, %s)", (names, phones))
            conn.commit()
            print(f"Массовый импорт из {file_path} завершен.")
        except Exception as ex:
            print(f"Ошибка массовой вставки: {ex}")
        finally:
            cur.close()
            conn.close()

# ВЫЗОВЫ ФУНКЦИЙ(SELECT)

def search_by_pattern(pattern):
    """Задача 1: Поиск по паттерну через функцию"""
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
            results = cur.fetchall()
            display_results(results)
        finally:
            cur.close()
            conn.close()

def get_paginated(limit, offset):
    """Задача 4: Пагинация через функцию"""
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            results = cur.fetchall()
            display_results(results)
        finally:
            cur.close()
            conn.close()

def display_results(results):
    if not results:
        print("Записей не найдено.")
    else:
        print(f"{'ID':<5} | {'Имя':<20} | {'Телефон':<15}")
        print("-" * 45)
        for row in results:
            print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15}")

def main():
    create_table()
    while True:
        print("\n--- PhoneBook Practice 8 (Procedures & Functions) ---")
        print("1. Добавить/Обновить контакт (Upsert)")
        print("2. Массовый импорт из CSV (с валидацией)")
        print("3. Поиск по имени или номеру (Pattern Search)")
        print("4. Просмотр с пагинацией")
        print("5. Удалить контакт")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            n = input("Имя: ")
            p = input("Телефон: ")
            upsert_contact(n, p)
        elif choice == '2':
            path = input("Введите имя CSV файла: ")
            bulk_insert(path)
        elif choice == '3':
            patt = input("Введите часть имени или телефона: ")
            search_by_pattern(patt)
        elif choice == '4':
            limit = int(input("Сколько записей вывести? "))
            offset = int(input("Сколько записей пропустить? "))
            get_paginated(limit, offset)
        elif choice == '5':
            name = input("Имя для удаления (пусто, если по телефону): ")
            phone = input("Телефон для удаления (пусто, если по имени): ")
            delete_contact_proc(name=name, phone=phone)
        elif choice == '0':
            break

if __name__ == "__main__":
    main()