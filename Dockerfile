# Базовый образ с Python 3.9 и необходимыми инструментами
FROM python:3.12

# Установка рабочей директории
WORKDIR /app

# Копирование requirements.txt
COPY requirements.txt requirements.txt

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода приложения
COPY . .

# Экспонирование порта
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]