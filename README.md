<h1 align="center">Проект web и mobile автотестов<p align="center">
<a href="link.ru"> <img src="resources/images/notion.png" width="" height="110"> </a> </h1>


<h3 align="center">Python | Pytest | Selene | Jenkins | Allure | Selenoid | Browserstack | Telegram</h3>
<h3 align="center">
<img height="50" src="resources/images/Python.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Pytest.svg"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selene.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/jenkins.png"/>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/allure.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Selenoid.svg"/>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/telegram.png"/>
</h3>



---

Запуск в jenkins https://jenkins.autotests.cloud/job/C09-vbr_s-diploma/

* Запуск веб тестов на селеноид: tests/web --context=selenoid
* Запуск мобильных тестов в browserstack: tests/mobile --context=bstack

Локальный запуск:

```bash
python -m venv .venv 
source .venv/bin/activate 
pip install -r requirements.txt 
```

Варианты запуска:

* Веб на селеноид
* Веб локально
* Мобильные на браузерстак
* Мобильные на локальном эмуляторе или реальном телефоне

```bash
pytest tests/web --context=selenoid
pytest tests/web --context=local
tests/mobile --context=bstack
tests/mobile --context=local_mobile
```

Для локального запуска мобильных тестов требуется запуск appium командой:

```
appium --base-path /wd/hub
```

Для совершения логина используется сервис временной почты mailslurp:
В .env указываются id почтового ящика и api ключ

MAIL_SLURP_API_KEY
MAIL_SLURP_INBOX_ID

На локальном мобильном устройстве можно использовать гугл учетную запись. Для этого нужно переключить в .env
USE_GOOGLE = True
