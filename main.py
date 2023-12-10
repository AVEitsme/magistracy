from typing import List


def get_number_count(array: List[int], number: int) -> int:
    return sum([1 if elem == number else 0 for elem in array])


def get_last_index_number(array: list, number: int) -> int:
    for index, elem in enumerate(reversed(array)):
        if elem != number:
            continue
        return len(array) - index - 1
    return -1


def count_substring(message: str, substring: str) -> int:
    return message.count(substring)


def first_task(arrays: List[List[int]], number: int) -> str:
    out_message = ""
    for array_number, array in enumerate(arrays):
        number_count = get_number_count(array, number)
        out_message += f"{array_number + 1}. Массив {array}. Количество элементов равных {number} = {number_count}\n"
    return out_message


def second_task(arrays: List[List[int]], number: int) -> str:
    out_message = ""
    index_sum = 0
    for array_number, array in enumerate(arrays):
        index_num = get_last_index_number(array, 0)
        if index_num != -1:
            index_sum += index_num
            out_message += f"{array_number + 1}. Массив {array}. Индекс последнего элемента со значением {number} = {index_num}\n"
            continue
        f"{array_number + 1}. Массив {array}. Индекс последнего элемента со значением {number} не найден\n"
    out_message += f"Сумма найденных индексов: {index_sum}\n"
    return out_message


def third_task(texts: List[str], substring: str) -> str:
    out_message = ""
    cache = {}
    for text_number, text in enumerate(texts):
        count = count_substring(text, substring)
        if count not in cache:
            cache[count] = []
        cache[count].append(text_number + 1)
        out_message += (
            f"Количество слов {substring} в тексте {text_number + 1} равно {count}\n"
        )
    out_message += f"Наибольшее количество вхождений слова {substring} в тексте(ах): {cache[max(cache)]}\n"
    return out_message


def run(
    first_task_parameters: List[List[int]],
    second_task_parameters: List[List[int]],
    third_task_parameters: List[str],
) -> None:
    while True:
        task_number = input("Введите номер задачи [1-3], 0 - для выхода: ")
        if task_number == "0":
            print("Завершаю работу программы...")
            break
        elif task_number == "1":
            print(first_task(first_task_parameters, 5))
        elif task_number == "2":
            print(second_task(second_task_parameters, 0))
        elif task_number == "3":
            print(third_task(third_task_parameters, "Иванушка"))
        else:
            print("Неизвестная задача, попробуйте снова")


def main() -> None:
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]
    Q = [5, 5, 2, 3, 66, 11, 55, 33, 4, 1]
    R = [5, 6, 5, 11, 23, 5, 5, 6, 5, 5]
    A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    B = [0, 11, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 11, 14]
    C = [11, 22, 33, 0, 13, 0, 23, 12, 1, 1, 1, 1, 1, 1, 11, 11, 11, 11, 11, 11]
    S1 = """
        Жил-был Иванушка-дурачок, собою красавец, а что ни сделает, всё у него смешно выходит, не так, как у людей.
        Нанял его в работники один мужик, а сам с женой собрался в город; жена и говорит Иванушке:
        – Останешься ты с детьми, гляди за ними, накорми их!
        – А чем? – спрашивает Иванушка.
        – Возьми воды, муки, картошки, покроши да свари – будет похлёбка!
        Мужик приказывает:
        – Дверь стереги, чтобы дети в лес не убежали!
    """
    S2 = """
        Уехал мужик с женой; Иванушка влез на полати, разбудил детей, стащил их на пол, сам сел сзади их и говорит:
        – Ну, вот, я гляжу за вами!
        Посидели дети некоторое время на полу, запросили есть.
        Иванушка втащил в избу кадку воды, насыпал в неё полмешка муки, меру[1] картошки, разболтал всё коромыслом и думает вслух:
        – А кого крошить надо?
    """
    S3 = """
        Услыхали дети – испугались:
        – Он, пожалуй, нас искрошит!
        И тихонько убежали вон из избы.
        Иванушка посмотрел вслед им, почесал затылок, соображает: «Как же я теперь глядеть за ними буду?
    """
    _ = run(
        first_task_parameters=[P, Q, R],
        second_task_parameters=[A, B, C],
        third_task_parameters=[S1, S2, S3],
    )


if __name__ == "__main__":
    main()
