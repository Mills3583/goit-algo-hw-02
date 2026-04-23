from collections import deque


def check_palindrome(dq, original_string):
    # Базовий випадок: якщо залишилось 0 або 1 символ — це паліндром
    if len(dq) <= 1:
        print(f"Результат: '{original_string}' — це паліндром!")
        return True

    # Витягуємо символи з обох кінців
    first = dq.popleft()
    last = dq.pop()

    if first == last:
        # Якщо символи однакові, продовжуємо перевірку залишку
        return check_palindrome(dq, original_string)
    else:
        # Якщо хоча б одна пара не збіглася — це не паліндром
        print(f"Результат: '{original_string}' — НЕ паліндром!")
        return False


if __name__ == "__main__":
    raw_input = input("Введіть рядок: ")
    
    # Попередня обробка: нижній регістр та видалення пробілів
    user_string = raw_input.lower().replace(" ", "")

    if user_string:
        dq_chars = deque(user_string)
        check_palindrome(dq_chars, user_string)
    else:
        print("Ви ввели порожній рядок, завершення роботи...")