import psycopg2
import csv


host = "localhost"
port = 5432
database = "phonebook"
user = "postgres"
password = "1234"


def connect():
    connection = None 

    try:   
        connection = psycopg2.connect(host = host, user = user, password = password, database = database, port = port) 

    except Exception as ex:
        print("Соединение не установлено...") 
        print(ex)
    
    return connection


def create_table():
    connection = connect() 
    cursor = None
    if connection is not None: 
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
            print("Таблица успешно создана/Проверена, она существует!")

        except Exception as ex:
            print(f'Что то пошло не так {ex}')

        finally:
            cursor.close() 
            connection.close() 


def insert_contact(name, phone): 
    connection = connect()
    cursor = None

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO phonebook(name, phone) VALUES(%s, %s);", (name, phone))
            connection.commit()

            print(f'{name} успешно вставлен в базу с номером {phone}')
        except Exception as ex:
            print(f'Ошибка добавления в базу данных пользователя {name} с телефоном {phone}, ошибка = {ex}')
        finally:
            cursor.close()
            connection.close()

def insert_from_csv(file_path): 
    connection = connect()
    cursor = None

    if connection:
        try:
            cursor = connection.cursor()

            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader) 

                for row in reader:
                    cursor.execute("INSERT INTO phonebook(name, phone) VALUES(%s, %s);", (row[0], row[1]))
            
            connection.commit()
            print(f'{file_path} был успешно вставлен в базу')
        except Exception as ex:
            print(f'{file_path} - ошибка добавления {ex}')
        finally:
            cursor.close()
            connection.close()

def update_contact(id, new_name=None, new_phone=None):
    conn = connect()
    cursor = None

    if conn:
        try:
            cur = conn.cursor()

            if new_name: 
                cur.execute("UPDATE phonebook SET name=%s WHERE id=%s", (new_name, id)) 
            
            if new_phone: 
                cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (new_phone, id)) 
            
            conn.commit()
            print(f'{id} успешно изменено')
        except Exception as ex:
            print(f'{id} ошибка = {ex}')
        finally:
            cur.close()
            conn.close()
        
def get_contact(con_id=None, name_filter=None, phone_filter=None):
    conn = connect()
    cursor = None

    if conn:
        try:
            cur = conn.cursor()

            if con_id: 
                cur.execute("SELECT id, name, phone FROM phonebook WHERE id=%s", (con_id,))
                contact = cur.fetchone() 
                result = [contact] if contact else []
                
            else:
                sql = "SELECT id, name, phone FROM phonebook WHERE TRUE"
                params = [] 
                if name_filter:
                    sql += " AND name ILIKE %s"
                    params.append(f"%{name_filter}%")
                if phone_filter:
                    sql += " AND phone LIKE %s"
                    params.append(f"%{phone_filter}%")
                
                cur.execute(sql, tuple(params)) 
                result = cur.fetchall() 
            
            if not result:
                print("Ничего не найдено")
            else:
                for row in result:
                    print(f"ID: {row[0]} | Имя: {row[1]:<15} | Тел: {row[2]}")
        except Exception as ex:
            print(f'Ошибка = {ex}')
        finally:
            cur.close()
            conn.close()


def delete_contact(name=None, phone=None):    
    if not name and not phone:
        print("Ошибка: укажите имя или телефон для удаления!")
        return

    conn = connect()
    cursor = None

    if conn:
        try:
            cur = conn.cursor()

            if phone:
                cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
                print(f"Контакты с телефоном {phone} удалены.")            
            elif name:
                cur.execute("DELETE FROM phonebook WHERE name=%s", (name,)) 
                print(f"Контакты с именем {name} удалены.")      
            conn.commit()
        except Exception as ex:
            print(f'Ошибка при удалении = {ex}')
        finally:
            cur.close()
            conn.close()
    
    

def clear_all():
    conn = connect()
    cursor = None

    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM phonebook")
            conn.commit()
            print("База данных полностью очищена")
        except Exception as ex:
            print(f'Ошибка при удалении базы данных = {ex}')
        finally:
            cur.close()
            conn.close()
            


def main():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Добавить контакт (консоль)")
        print("2. Импорт из CSV")
        print("3. Все контакты")
        print("4. Найти контакт по id")
        print("5. Обновить данные")
        print("6. Удалить контакт")
        print("0. Выход")
        print("clear - удаление базы данных")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            n = input("Имя: ")
            p = input("Телефон: ")
            insert_contact(n, p)
        elif choice == '2':
            path = input("Введите название файла")
            insert_from_csv(path)
        elif choice == '3':
            name_f = input("Фильтр по имени (оставьте пустым для всех): ")
            phone_f = input("Фильтр по телефону (оставьте пустым для всех): ")
            get_contact(name_filter=name_f, phone_filter=phone_f)
        elif choice == '4':
            _id = input("Введите id")
            get_contact(_id)
        elif choice == '5':
            _id = input("Введите id контакта, который нужно поменять")
            new_name = input("Новое имя(пусто, если не нужно менять)")
            new_phone = input("Новый телефон(пусто, если не нужно менять)")
            update_contact(_id, new_name=new_name, new_phone=new_phone)
        elif choice == '6':
            name = input("Удалить контакты с именем(пусто, если не надо)")
            phone = input("Удалить контакты с этим номером(пусто, если не нужно)")
            delete_contact(name=name, phone=phone)
        elif choice == "clear":
            clear_all()
        elif choice == '0':
            break
        

if __name__ == "__main__":
    main()