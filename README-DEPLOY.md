# 🚀 Quick Deploy Guide

## Быстрый деплой на `unl-backlog.duckdns.org`

### 📋 Предварительные требования
- Docker и Docker Compose установлены
- Домен `unl-backlog.duckdns.org` указывает на ваш сервер
- Порты `8080` и `8443` открыты

### ⚡ Быстрый старт

```bash
# 1. Клонируйте репозиторий
git clone <repository-url>
cd backlog

# 2. Настройте окружение
cp .env.example .env
nano .env  # Отредактируйте пароли и email

# 3. Запустите деплой
./scripts/deploy.sh
```

### 🛠️ Управление сервисами

```bash
# Показать статус
./scripts/manage.sh status

# Просмотр логов
./scripts/manage.sh logs

# Перезапуск
./scripts/manage.sh restart

# Обновление SSL
./scripts/manage.sh ssl-renew

# Проверка здоровья
./scripts/manage.sh health
```

### 🌐 Доступ к приложению

После деплоя приложение доступно по адресам:
- **HTTP**: http://unl-backlog.duckdns.org:8080 (перенаправляется на HTTPS)
- **HTTPS**: https://unl-backlog.duckdns.org:8443

### 📊 Используемые порты

- `8080` - HTTP (nginx)
- `8443` - HTTPS (nginx)  
- `5433` - PostgreSQL

> **Примечание**: Порты изменены для избежания конфликтов с другими приложениями

### 🆘 Помощь

Подробные инструкции: [DEPLOYMENT.md](DEPLOYMENT.md)

Управление сервисами:
```bash
./scripts/manage.sh help
``` 