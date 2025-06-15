# 🎓 Студенческий планировщик учебных задач

Полнофункциональное веб-приложение (PWA) для планирования, отслеживания и закрытия учебных задач и задолженностей студентов.

## 🚀 Возможности

### ✅ Реализованные функции:
- **Регистрация и авторизация** - JWT токены, хеширование паролей
- **Dashboard** - приветствие, статистика задач, ближайшие дедлайны
- **Управление задачами** - создание, редактирование, удаление, статусы
- **Календарь** - просмотр задач по датам
- **Приоритеты** - годовые долги, семестровые долги, текущие задачи
- **Этапы задач** - разбиение больших задач на подзадачи
- **Статистика** - аналитика выполнения, просроченные задачи
- **PWA поддержка** - установка как приложение, offline режим
- **Адаптивный дизайн** - работает на мобильных и десктопах
- **REST API** - полная документация в Swagger

## 🛠️ Технологии

### Frontend:
- **Next.js 14** - React фреймворк с App Router
- **TypeScript** - типизация
- **Tailwind CSS** - стилизация
- **PWA** - прогрессивное веб-приложение
- **React Hook Form** - формы
- **Axios** - HTTP клиент

### Backend:
- **FastAPI** - современный Python API фреймворк
- **SQLAlchemy** - ORM для работы с БД
- **Alembic** - миграции БД
- **PostgreSQL** - основная база данных
- **JWT** - аутентификация
- **Pydantic** - валидация данных

### DevOps:
- **Docker & Docker Compose** - контейнеризация
- **Nginx** - веб-сервер (в продакшене)

## 📋 Требования

- Docker и Docker Compose
- Git

## 🚀 Быстрый запуск

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/yourname/student-planner.git
cd student-planner
```

2. **Создайте файл переменных окружения для backend:**
```bash
# Создайте файл backend/.env
cat > backend/.env << EOF
DATABASE_URL=postgresql://postgres:password@postgres:5432/student_planner
SECRET_KEY=your-super-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=true
EOF
```

3. **Запустите все сервисы:**
```bash
docker-compose up --build
```

4. **Дождитесь запуска всех сервисов:**
- Backend API: http://localhost:8000
- Frontend: http://localhost:3000
- PostgreSQL: localhost:5432

5. **Откройте приложение в браузере:**
- Главная страница: http://localhost:3000
- API документация: http://localhost:8000/docs

## 🎯 Использование

### Первые шаги:
1. Перейдите на http://localhost:3000
2. Нажмите "Создать аккаунт" для регистрации
3. Заполните email, пароль и имя
4. Войдите в систему
5. Начните добавлять задачи!

### Основные функции:
- **Dashboard** - обзор задач, статистика, ближайшие дедлайны
- **Задачи** - полный список с фильтрацией по типу, приоритету, статусу
- **Календарь** - визуальное планирование по датам
- **Профиль** - настройки уведомлений, смена пароля

## 📁 Структура проекта

```
student-planner/
├── backend/                    # FastAPI приложение
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   │   ├── auth.py       # Аутентификация
│   │   │   ├── crud.py       # Операции с БД
│   │   │   ├── db.py         # Модели и подключение к БД
│   │   │   ├── schemas.py    # Pydantic схемы
│   │   │   └── main.py       # Главный файл приложения
│   │   ├── alembic/           # Миграции БД
│   │   ├── requirements.txt   # Python зависимости
│   │   └── Dockerfile
│   │
│   ├── frontend/               # Next.js приложение
│   │   ├── app/               # Страницы (App Router)
│   │   ├── components/        # React компоненты
│   │   ├── lib/               # Утилиты и API клиент
│   │   ├── public/            # Статические файлы
│   │   ├── styles/            # CSS стили
│   │   ├── package.json       # Node.js зависимости
│   │   └── Dockerfile
│   │
│   ├── docker-compose.yml     # Конфигурация Docker
│   └── README.md
```

## 🔧 Разработка

### Запуск в режиме разработки:

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

### Работа с БД:

**Создание миграции:**
```bash
cd backend
alembic revision --autogenerate -m "Описание изменений"
```

**Применение миграций:**
```bash
alembic upgrade head
```

## 📝 API Документация

После запуска backend, API документация доступна по адресам:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Основные endpoints:
- `POST /api/v1/auth/register` - Регистрация
- `POST /api/v1/auth/login` - Авторизация
- `GET /api/v1/auth/me` - Текущий пользователь
- `GET /api/v1/tasks/` - Список задач
- `POST /api/v1/tasks/` - Создать задачу
- `GET /api/v1/tasks/stats/summary` - Статистика задач

## 🎨 Дизайн

Приложение использует минималистичный дизайн с акцентом на удобство использования:
- **Цветовая схема:** Синие оттенки (primary), серые тона для фона
- **Типографика:** Inter шрифт для читаемости
- **Приоритеты задач:**
  - 🔴 Красный - Годовые долги
  - 🟠 Оранжевый - Семестровые долги  
  - 🔵 Синий - Текущие задачи

## 🔒 Безопасность

- JWT токены для аутентификации
- Хеширование паролей с bcrypt
- CORS настройки
- Валидация данных на frontend и backend
- SQL инъекции защита через SQLAlchemy ORM

## 📱 PWA возможности

- Установка как нативное приложение
- Offline кэширование
- Адаптивный интерфейс
- Быстрая загрузка
