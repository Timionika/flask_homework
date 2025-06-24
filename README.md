# flask twits api
Простой REST API, реализованный с помощью Flask, позволяющий управлять "твитами" — короткими сообщениями с указанием автора. Поддерживает операции создания, чтения, обновления и удаления твитов.

Основные возможности
POST /twit — создание нового твита
GET /twit — получение всех твитов
PUT /twit/<int:twit_id> — обновление существующего твита
DELETE /twit/<int:twit_id> — удаление твита

После клонирования репрозитория устоновите все нужные зависимости.

```pip install -r requirements.txt```

Если хотите предаврительно создать виртуальное окружение проекта, то выполните команды 

```python -m venv venv```

```venv\Scripts\activate```

После запуска main.py выполните следующие запросы по инструкции: 

1.POST http://127.0.0.1:8002/twit 
Данный запрос выполните 2 раза с разным телом. 
Тело запроса: 

{
  "body": "Twit 0",
  "author": "@username"
}

{
  "body": "Twit 1",
  "author": "@username"
}

Результатом будет на оба случая 
{
  "status": "success"
}



2. GET http://127.0.0.1:8002/twit
Результатом будет 
{
  "twits": [
    {
  "body": "Twit 0",
  "author": "@username"
},
{
  "body": "Twit 1",
  "author": "@username"
}
   ] 
}

3. PUT http://127.0.0.1:8002/twit/1
И отправтье изменненое тело запроса
{
  "body": "Twit 1 new",
  "author": "@username"
}
  

4. DELETE http://127.0.0.1:8002/twit/0
   Реультатом будет удаление
   {
  "body": "Twit 0",
  "author": "@username"
} 

5. GET http://127.0.0.1:8002/twit
   Результатом будет:
   {
  "twits": [
    {
  "body": "Twit 0",
  "author": "@username"
}
   ] 
}
