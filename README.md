# InnoGlobalHack
--------------------
[winner's solution on InnoGlobalHack](https://media.innopolis.university/news/innoglobalhack-final)

## Задача
В настоящее время многие мобильные
приложения сталкиваются с необходимостью
идентифицировать пользователей по их лицам. Задача
идентификации по лицу в целом является решенной. Однако
одной из актуальных проблем остается обеспечение
достоверности такой идентификации: необходимо отличить
реальное лицо от статичных изображений, скриншотов и
других типов мошенничества. В рамках этого задания вам
предстоит разработать систему проверки подлинности
изображения лица. Разрабатываемый сервис должен уметь
работать в картиночном режиме – пользователь загружает
фотографию, получает вердикт. 

## Демо
[Ссылка на перезентацию с демонстрацией решения](https://docs.google.com/presentation/d/135gFnvXTuMY0s2Gx6RO2vu4_WM_sKIHk/edit?usp=sharing&ouid=113877914532993525052&rtpof=true&sd=true)

## Решение
processing - обучение сети, получение датасета
backend/app/main_model - первая модель
backend/app/screen_detecting - [вторая модель](https://github.com/minivision-ai/Silent-Face-Anti-Spoofing/)

![image](https://github.com/BurykinaA/InnoGlobalHack/assets/92402616/851359f2-9678-48df-adbf-f6d39422c9bd)


## Запуск приложения
Эта инструкция позволит запустить приложение, используя Docker, на операционных системах Linux и Windows.

> Убедитесь, что Docker уже установлен на вашей машине. Если Docker не установлен, вы можете скачать его с [официального сайта Docker](https://www.docker.com/get-started/).

### Шаг 1: Клонировать репозиторий
Если у вас еще нет локальной копии репозитория, клонируйте его из Git-репозитория:

```bash
git clone https://github.com/JokerEur/WebAccessibility.git
cd WebAccessibility
```
### Шаг 2: Запустить Docker Compose
Теперь используем Docker Compose для создания и запуска контейнеров нашего приложения.

#### На Linux:
```bash
docker-compose up --build
или  
docker-compose up --build -d
```

#### На Windows:
```bash
docker-compose up --build 
или  
docker-compose up --build -d
```
### Шаг 3: Проверить работоспособность
Теперь приложение должно быть доступным и готово к использованию по адресу:

**Linux**: 
http://localhost:5173

**Windows**: 
http://localhost:5173

### Шаг 4: Остановить контейнеры (использовав docker-compose up --build -d)
Чтобы остановить контейнеры, выполните следующую команду:

```bash
docker-compose down
```
Это завершит работу всех контейнеров, связанных с приложением.


## Мы в медиа

https://habr.com/ru/companies/misis/articles/767384/

https://m.gazeta.ru/amp/tech/news/2023/10/16/21512545.shtml
