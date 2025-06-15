# 🔧 Исправление ошибки Docker Compose ContainerConfig

## 🚨 Проблема

Ошибка `KeyError: 'ContainerConfig'` в Docker Compose 1.29.2 возникает из-за поврежденных метаданных контейнера или конфликтов версий.

```
ERROR: for backlog_postgres  'ContainerConfig'
KeyError: 'ContainerConfig'
```

## 🛠️ Решения

### Решение 1: Автоматическое исправление (Рекомендуется)

```bash
# Запустите скрипт автоматического исправления
./scripts/fix-docker.sh
```

Этот скрипт:
- Остановит и удалит проблемные контейнеры
- Очистит Docker систему
- Использует исправленную конфигурацию
- Запустит сервисы пошагово

### Решение 2: Обновление Docker Compose

```bash
# Обновите Docker Compose до последней версии
./scripts/update-docker-compose.sh
```

### Решение 3: Ручное исправление

#### Шаг 1: Очистка
```bash
# Остановите все контейнеры
docker-compose down --remove-orphans

# Удалите проблемные контейнеры
docker stop backlog_postgres backlog_backend backlog_frontend backlog_nginx backlog_certbot
docker rm backlog_postgres backlog_backend backlog_frontend backlog_nginx backlog_certbot

# Очистите систему
docker system prune -f
docker volume prune -f
```

#### Шаг 2: Использование исправленной конфигурации
```bash
# Создайте резервную копию
cp docker-compose.yml docker-compose.yml.backup

# Используйте исправленную версию
cp docker-compose.fixed.yml docker-compose.yml
```

#### Шаг 3: Пошаговый запуск
```bash
# Запустите сервисы по одному
docker-compose up -d postgres
sleep 15

docker-compose up -d backend
sleep 10

docker-compose up -d frontend
sleep 10

docker-compose up -d nginx certbot
```

## 🔍 Диагностика

### Проверка версии Docker Compose
```bash
docker-compose --version
```

### Проверка статуса контейнеров
```bash
docker-compose ps
docker ps -a
```

### Проверка логов
```bash
docker-compose logs postgres
docker-compose logs backend
```

## 📋 Что изменено в исправленной версии

1. **Новые имена контейнеров** - избегаем конфликтов
2. **Именованные volumes** - предотвращаем проблемы с метаданными
3. **Явные драйверы** - четкое определение типов volumes
4. **Упрощенная структура** - убраны потенциально проблемные элементы

## ✅ Проверка исправления

После применения исправления проверьте:

```bash
# Статус сервисов
docker-compose ps

# Доступность приложения
curl -I http://unl-backlog.duckdns.org:8080
curl -I https://unl-backlog.duckdns.org:8443

# Логи для диагностики
docker-compose logs --tail=50
```

## 🆘 Если проблема остается

1. **Перезагрузите Docker daemon**:
   ```bash
   sudo systemctl restart docker
   ```

2. **Полная очистка Docker**:
   ```bash
   docker system prune -a --volumes
   ```

3. **Переустановите Docker Compose**:
   ```bash
   sudo apt remove docker-compose
   sudo apt install docker-compose-plugin
   ```

4. **Используйте Docker Compose V2**:
   ```bash
   # Вместо docker-compose используйте
   docker compose up -d
   ```

## 📞 Поддержка

Если ни одно из решений не помогло:

1. Проверьте версии Docker и Docker Compose
2. Убедитесь, что у вас достаточно места на диске
3. Проверьте права доступа к Docker socket
4. Создайте issue с полными логами ошибки 