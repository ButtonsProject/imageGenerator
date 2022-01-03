# SKB image generator
## Полностью готовая сборка для развертывания локально, или на сервисе heroku.
### Перед запуском необходимо:
1. Установить зависимости из requirements.txt
2. Выполнить manage.py makemigrations
3. Выполнить manage.py migrate
4. При локальном запуске изменить домен на localhost в generator-ui.
### Адреса API

GET /api/v1/generator/get/?id=1

POST /api/v1/generator/new

### Включение debug режима для более удобной отладки:
Задайте значение True параметру DEBUG, в файле skbImageGeneratorApi\settings.py
