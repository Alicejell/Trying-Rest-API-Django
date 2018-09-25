# Trying-Rest-API-Django


примеры curl:

Получить список книг:
curl -i -X GET http://127.0.0.1:8000/book/

Добавить книгу:
curl -i -X POST -d "name=Namebook&author_name=namename&year=1111" http://127.0.0.1:8000/book/

Удалить книгу:
curl -i -X DELETE http://127.0.0.1:8000/book/3/

Заменить книгу:
curl -i -X PUT -d "name=Namebook&author_name=namename&year=1111" http://127.0.0.1:8000/book/1/
