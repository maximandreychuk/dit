## тестовое

Создать минимальный сервис, который
1. отвечает на порту 8000
2. имеет http-методы:
    - GET /check_health/
    - POST /matrix_operations
    - POST /heximal_operations

Имя репозитория и тэг на Dockerhub
```
docker push 7ras0tresh/dit-test:v1
docker run -p 8000:8000 7ras0tresh/dit-test:v1
```
Документация будет доступна по ссылке
```
http://0.0.0.0:8000/docs
```

Примеры /matrix_operations

(1) status 200

```
Request:
{
  "matrix_1": [
    [1,2], [3,4]
  ],
  "matrix_2": [
    [10,20], [30,40]
  ],
  "operation_type": "add"
}
```
```
Response 200:
{
  "matrix": [
    [
      11,
      22
    ],
    [
      33,
      44
    ]
  ],
  "operation_type": "add"
}
```
(2) status 400 
```
Request 
{
  "matrix_1": [
    [1,2], [3,4]
  ],
  "matrix_2": [
    [10,20], [30,40]
  ],
  "operation_type": "empty"
}
```
```
Response 400:
{
  "detail": "Invalid operation type"
}
```