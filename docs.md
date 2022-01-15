# Генератор картинок для СКБ ЛАБ

Простой инструмент для быстрого создания картинок соответствующих фирменному стилю, по заранее заданным шаблонам.

## Используемый стек

- Язык программирование Python
- Фреймворк Django  для веб разработки.
- Django  REST  API  фреймворк для построения API
- Библиотека PIL  для работы с растровыми изображениями.
- React  js  для разработки веб интерфейса.

## Методы REST  API
GET  api/v1/generator/get/?id=num - Получение изображения (результата) по id  модели.

Возвращает PNG  изображение с названием в формате <тип генерации> _<дата и время (UTC)>.png. Пример: high_article_07-21_14-01.png


POST  api/v1/generator/new – Создание новой модели для генерации изображения.

Пример запроса:
```
{

"image":  <Входное изоображение>,

"gen_type":  "triangle_mask",

"params":  "color=yellow",

"text_fields":  "Сегодня;Завтра"

}
```

Пример ответа:
```
{

"id":  711,

"image":  "https://skbgen.herokuapp.com/images/test_image.jpg)",

"gen_type":  "checks",

"params":  "color=yellow",

"text_fields":  "Сегодня"

}
```

## Основные модели в проекте


### Изображение (Image)

Поля модели:

- Image – Входное изображение, может быть пустым. Загружается images.

- result  – Результат работы генератора, может быть пустым, загружается в result.

- gen_type – Тип генерации, на данный момент возможные значения – checks, high_article, typography, triangle_mask.

- text_fields – Текстовые поля разделенные, через “;”.  Максимальная длина 120 символов.

- Params – Параметры генерации модели. Сейчас доступен параметр color=<Выбранный цвет>. Максимальная длина 20 символов.

- created – Дата создания экземпляра модели

## Краткое описание процесса работы

1. Отправка POST  запроса на backend  с необходимыми полями.

2. Получение id  из ответа на POST  запрос.

3. Получение картинки по id  GET  запросом.

## Библиотека backendImageGenerator

Позволяет удобным образом генерировать картинки. 
Главным образом основана на библиотеке PIL.
Пример кода для генерации картинки типа triangle_mask_closed:
```
from Postcard.Postcard import *

result = Postcard("triangle_mask_closed", {"backGround" : Image.open("test.png"), "color": "orange", "text": "Example"})

result.create_result_post()

result.save('testResult.png')
```
### Список доступных типов:
- empty_triangles - заголовок сверху
- checks - галочки
- triangle_mask_closed - треугольная маска
- typographia - типографика
- title_ellipses - эллипсы (Нормально не работает, требуется внедрения ML функциональности)

## Схема продукта

[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1JlYWN0IGZyb250ZW5kXSAtLT58UkVTVCBBUEl8IEIoRGphbmdvIGJhY2tlbmQpXG4gICAgQiAtLT4gQ1tiYWNrZW5kIGdlbmVyYXRvciBiYXNlZCBvbiBQSUxdXG4gICAgQiAtLT4gRFtEYXRhIGJhc2VdIiwibWVybWFpZCI6eyJ0aGVtZSI6ImRlZmF1bHQifSwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)](https://mermaid.live/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICBBW1JlYWN0IGZyb250ZW5kXSAtLT58UkVTVCBBUEl8IEIoRGphbmdvIGJhY2tlbmQpXG4gICAgQiAtLT4gQ1tiYWNrZW5kIGdlbmVyYXRvciBiYXNlZCBvbiBQSUxdXG4gICAgQiAtLT4gRFtEYXRhIGJhc2VdIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)
