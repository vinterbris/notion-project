<h1 align="center">Проект web и mobile автотестов</h1>
<p align="center">
    <a href="https://notion.so">
      <img src="resources/images/notion.png" width="" height="110">
    </a>
</p>



<h4 align="center">Python | Pytest | Selene | Appium | Jenkins | Allure | Selenoid | Browserstack | Telegram</h4>
<h4 align="center">
<img height="50" src="resources/images/Python.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Pytest.svg"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selene.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/appium.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/jenkins.png"/>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/allure.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selenoid.svg"/>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/browserstack.png"/>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/telegram.png"/>
</h4>



---

> <a target="_blank" href="http://176.123.163.26:8888/job/notion-project/">Ссылка на проект в мой Jenkins: доступны прогоны и allure отчёты</a>


### Реализованы тесты:

#### Web

- [x] Авторизация по временному коду или паролю
- [x] Добавление страницы
- [x] Добавление подстраницы
- [x] Публикация страницы
- [x] Создание пространства команды
- [x] Создание страницы из шаблона
- [x] Добавление страницы в избранное

#### Mobile

- [x] Авторизация по временному коду
- [x] Добавление страницы
- [x] Поиск страницы
- [x] Удаление страницы

## Запуск тестов

### Локально

1. Клонировать репозиторий

```bash
git clone https://github.com/vinterbris/qa_guru_python_9_24.git
```

2. В терминале pycharm создать и активировать виртуальное окружение

```bash
python -m venv .venv 
source .venv/bin/activate 
```

3. Установить зависимости

```
pip install -r requirements.txt 
```

4. Создать и заполнить `.env` файлы на основе папки `.env.examples`:
* .env
* .env.mail
* .env.mobile
* .env.web

#### Варианты запуска:

* На selenoid или локально
* Все тесты
* Web-тесты
* Mobile-тесты

```bash
pytest
pytest tests/web
pytest tests/mobile
```

#### Получение отчета allure

```bash
allure serve
```

### Установка и настройка appium для локального запуска

<a target="_blank" href="https://autotest.how/appium-setup-for-local-android-tutorial-md">Инструкция по настройке системы и устройств для локального запуска мобильных тестов на платформе Android</a>



#### Для локального запуска мобильных тестов требуется запуск appium командой:

```
appium --base-path /wd/hub
```

#### Логин по одноразовым кодам

Для совершения логина используется сервис временной почты mailslurp:
В `.env` указываются id почтового ящика и api ключ:`MAIL_SLURP_API_KEY`,`MAIL_SLURP_INBOX_ID`

На локальном мобильном устройстве можно использовать гугл учетную запись. Для этого нужно переключить в .env
`USE_GOOGLE = True`

### Удаленно

#### Для запуска автотестов на selenoid и browserstack

1. В `.env` указываем `CONTEXT=remote`
2. Запускаем как указано выше



## Оповещения в мессенджер

> _Настроена отправка оповещений в телеграм канал. Возможна настройка для Email,Slack, Discord, Skype, Mattermost,
Rocket.Chat_

<img src="resources/images/screenshot_telegram.png" width="" height="450">

## Примеры запуска тестов

### Веб

https://github.com/vinterbris/qa_guru_python_9_24/assets/21102027/3f1aed6b-81fc-4469-9c73-3bf83a0c5d88

### Мобильных

https://github.com/vinterbris/qa_guru_python_9_24/assets/21102027/be7f4e28-4f6b-4023-afef-b68c09904981



