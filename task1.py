from queue import Queue
import uuid


# Створити чергу заявок
queue = Queue()


def generate_request() -> None:
    request_id = str(uuid.uuid7()) # Створити нову заявку
    queue.put(request_id) # Додати заявку до черги


def process_request() -> None:
    if not queue.empty(): #Якщо черга не пуста:
        
        current_request = queue.get() #Видалити заявку з черги
        print(f"Заявка номер: {current_request} - обслуговується") #Обробити заявку

    else: #Інакше:
        
        print("Черга порожня") #Вивести повідомлення, що черга пуста


if __name__ == "__main__":

    while True: #Головний цикл програми:

        user_input = input("Натисніть Enter для створення заявки, або 'q' для виходу: ").lower()

        if user_input == '':
          generate_request() #Виконати generate_request() для створення нових заявок
          process_request() #Виконати process_request() для обробки заявок

        elif(user_input == 'q'): # Якщо юзер ввів щось поміж Enter або 'q'
          print("Вихід з програми.")
          break

        else: # Поки користувач не вийде з програми:
          print(f"Ви ввели: {user_input}, будь ласка введіть 'q' для виходу або натисність Enter для створення заявки:")