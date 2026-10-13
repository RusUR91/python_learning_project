import json

def main():
    try:
        # Читаем файл
        with open('input.txt', 'r', encoding='utf-8') as f:
            content = f.read()

        # Проверка на пустой файл
        if not content.strip():
            print("Empty file")
            return

        # Парсинг JSON
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            print("Invalid input format")
            return

        # Извлекаем списки с помощью get (если ключей нет — пустой список)
        list1 = data.get('list1', [])
        list2 = data.get('list2', [])

        # Проверка, что полученные значения — списки
        if not isinstance(list1, list) or not isinstance(list2, list):
            print("Invalid input format")
            return

        # Алгоритм слияния (проход за один раз)
        merged = []
        i = j = 0

        while i < len(list1) and j < len(list2):
            if list1[i]['year'] <= list2[j]['year']:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1

        # Добавляем остатки
        while i < len(list1):
            merged.append(list1[i])
            i += 1

        while j < len(list2):
            merged.append(list2[j])
            j += 1

        # Формируем результат и выводим
        result = {"list0": merged}
        print(json.dumps(result, ensure_ascii=False, indent=2))

    except FileNotFoundError:
        print("File not found")
    except KeyError:
        print("Invalid input format")
    except Exception:
        print("Invalid input format")


if __name__ == "__main__":
    main()
