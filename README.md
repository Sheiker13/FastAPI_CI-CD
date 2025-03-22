
# 🚀 FastAPI CI/CD Monitoring Project

Полностью настроенный проект FastAPI с:

- ✅ CI/CD через GitHub Actions
- 🐳 Docker + Docker Compose
- 🔥 Prometheus + Grafana для мониторинга
- 📊 Метрики `/metrics` с Prometheus Client
- 📬 Telegram-оповещения из Grafana
- 🧪 Pytest + Coverage + Flake8
- 📦 Автоматический деплой (по SSH)

---

## 📁 Структура проекта

```
.
├── app/
│   ├── main.py           # FastAPI-приложение
│   ├── logger.py         # Логирование с ротацией
│   ├── metrics.py        # Прометей-метрики
├── tests/
│   └── test_main.py      # Pytest тесты
├── docker-compose.yml
├── Dockerfile
├── prometheus.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Запуск проекта

```bash
git clone https://github.com/your-username/fastapi-ci-cd.git
cd fastapi-ci-cd
docker-compose up --build
```

---

## 🌍 Endpoints

| Метод | URL            | Описание                      |
|-------|----------------|-------------------------------|
| GET   | `/`            | Главная страница              |
| GET   | `/health`      | Health check (для мониторинга) |
| GET   | `/metrics`     | Метрики для Prometheus        |

---

## 🔧 CI/CD Pipeline

Настроен в `.github/workflows/ci-cd.yml`:

- При пуше в `main`:
  - ✅ Установка зависимостей
  - ✅ Проверка стиля кода (`flake8`)
  - ✅ Прогон тестов (`pytest`)
  - ✅ Coverage-отчет
  - ✅ Автоматический деплой на сервер через SSH

---

## 📈 Мониторинг

- Prometheus собирает метрики с `/metrics`
- Grafana отображает графики:
  - 📊 Количество запросов (`request_count_total`)
  - ⏱ Задержка ответов (`request_latency_seconds`)
- Метрики настраиваются через `app/metrics.py`

### 🔔 Telegram Alert (Grafana)

- При задержке > 2 сек в течение 30 секунд срабатывает тревога
- Grafana отправляет сообщение в Telegram через собственного бота
- Настройка:
  - BotFather → токен
  - /getUpdates → chat_id
  - В Grafana → Alerting → Contact points

---

## 🧪 Тестирование

```bash
pytest --cov=app tests/
flake8 app
```

---

## 🛠 Решённые проблемы

### 🧩 Проблема: Telegram не отправлял уведомления
- Ошибка: `400 Bad Request` при отправке тревоги из Grafana
- Решение:
  - Не был получен `chat_id`, потому что не было первого сообщения боту
  - После отправки любого сообщения в Telegram боту `@your_bot` — Grafana успешно начала слать уведомления

---

### 🧩 Проблема: Grafana не показывала метрики
- Ошибка: `404 /metrics`
- Причина: отсутствовал эндпоинт `/metrics` в FastAPI
- Решение:
  - Добавлен `prometheus_client` и `app.add_route("/metrics", metrics_app)`

---

### 🧩 Проблема: CI/CD не запускался
- Причина: не было `.github/workflows/ci-cd.yml`
- Решение:
  - Добавлен рабочий CI/CD скрипт с этапами: `flake8`, `pytest`, `coverage`, `deploy via SSH`

---

### 📘 Этапы разработки

1. Инициализация проекта (FastAPI + Docker)
2. Настройка логирования и метрик
3. Создание тестов и проверка покрытия
4. Подключение Prometheus + Grafana
5. Создание Telegram-бота и тревог
6. Настройка CI/CD через GitHub Actions
7. Финальная упаковка и тестирование проекта

---


