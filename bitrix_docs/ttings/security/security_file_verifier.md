# Контроль целостности

Документация для разработчиков

[Документация для разработчиков](https://dev.1c-bitrix.ru/api_help/)
[Документация по D7](https://dev.1c-bitrix.ru/api_d7/)
[Документация по REST](https://dev.1c-bitrix.ru/rest_help/)
[Пользовательская документация](https://dev.1c-bitrix.ru/user_help/)

Темная тема

[Основные сведения](/user_help/index.php)
[Реализация и системные требования](/user_help/reqintro.php)

[Справочная система и документация](/user_help/help/index.php)

[Контент](/user_help/content/index.php)

[Сайты 24](/user_help/sites24/index.php)

[Маркетинг](/user_help/marketing/index.php)

[Магазин](/user_help/store/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Адреса и местоположения](/user_help/settings/location/index.php)

[Избранное](/user_help/settings/favorites/index.php)

[Пользователи](/user_help/settings/users/index.php)

[Поиск](/user_help/settings/search/index.php)

[Проактивная защита](/user_help/settings/security/index.php)

[Проактивная защита. Настройки модуля](/user_help/settings/security/settings.php)
[Сканер безопасности](/user_help/settings/security/security_scanner.php)
[Панель безопасности](/user_help/settings/security/security_panel.php)
[Проактивный фильтр](/user_help/settings/security/security_filter.php)
[Веб-антивирус](/user_help/settings/security/security_antivirus.php)
[Журнал вторжений](/user_help/settings/security/event_log.php)
[Двухэтапная авторизация](/user_help/settings/security/security_otp.php)

[Поиск троянов](/user_help/settings/security/xscan/index.php)

[Контроль целостности](/user_help/settings/security/security_file_verifier.php)
[Защита административного раздела](/user_help/settings/security/security_iprule_admin.php)
[Защита сессий](/user_help/settings/security/security_session.php)
[Защита редиректов](/user_help/settings/security/security_redirect.php)
[Защита от фреймов](/user_help/settings/security/security_frame.php)
[Контроль активности](/user_help/settings/security/security_stat_activity.php)
[Стоп-лист](/user_help/settings/security/security_iprule_list.php)
[Создание и редактирование правила стоп-листа](/user_help/settings/security/security_iprule_edit.php)
[Хосты/домены](/user_help/settings/security/security_hosts.php)

[DAV (КП)](/user_help/settings/dav/index.php)

[Push and Pull](/user_help/settings/pull/index.php)

[REST API](/user_help/settings/rest_api/index.php)

[Валюты](/user_help/settings/currency/index.php)

[Веб-кластер](/user_help/settings/cluster/index.php)

[Веб-сервисы](/user_help/settings/webservice/index.php)

[Диск (КП)](/user_help/settings/disk/index.php)

[Конвертер файлов (КП)](/user_help/settings/transformer/index.php)

[Коннекторы для внешних мессенджеров (КП)](/user_help/settings/imconnector/index.php)

[Открытые линии (КП)](/user_help/settings/imopenlines/index.php)

[Распознавание лиц (КП)](/user_help/settings/faceid/index.php)

[Сервер конвертации файлов (КП)](/user_help/settings/transformercontroller/index.php)

[Служба сообщений](/user_help/settings/message_service/index.php)

[Телефония](/user_help/settings/voximplant/index.php)

[Облако 1С-Битрикс](/user_help/settings/bitrixcloud/index.php)

[Облачные хранилища](/user_help/settings/clouds/index.php)

[AD/LDAP интеграция](/user_help/settings/ldap/index.php)

[Перевод](/user_help/settings/translate/index.php)

[XMPP сервер (КП)](/user_help/settings/xmpp/index.php)

[Настройки продукта (главный модуль)](/user_help/settings/settings/index.php)

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Проактивная защита](/user_help/settings/security/index.php)

Контроль целостности

**Недоступно в редакциях:**Старт

# Контроль целостности

Контроль целостности файлов необходим для того, чтобы быстро выяснить, вносились ли изменения в файлы системы.
В любой момент вы можете проверить целостность ядра, системных областей, публичной части продукта.

  

### Предварительные операции

  

### Закладка Контроль целостности скрипта

Форма позволяет настроить параметры защиты скрипта паролем.

| Поле | Описание |
| --- | --- |
| Пароль\* | Указывается пароль, который необходимо запомнить. Рекомендуется использовать пароль длиной не менее 10 символов, состоящий из латинских букв и цифр. |
| Пароль ещё раз\* | Указывается пароль ещё раз. |
| Ключевое слово\* | Указывается ключевое слово, которое необходимо запомнить. Это слово должно отличаться от пароля. Если при последующем запуске кодовое слово будет отличаться от указанного, то скрипт контроля файлов был изменен. |

\* - поля, обязательные для заполнения.

**Примечание**: при первом запуске скрипта будут отображены все поля формы. При последующих запусках будет отображено только поле **Пароль**.

  

### Закладка Выбор действия

Форма позволяет выбрать действие: проверить файлы либо собрать информацию о файлах.

| Поле | Описание |
| --- | --- |
| Проверить файлы | При отмеченной опции будет осуществлен переход к проверке целостности файлов системы. |
| Собрать информацию по файлам | При отмеченной опции будет осуществлен сбор информации по файлам для того, чтобы в дальнейшем выполнить проверку целостности системы. |

### Сбор информации

  

### Закладка Сбор данных

Форма позволяет настроить параметры сбора данных.

| Поле | Описание |
| --- | --- |
| Область сбора данных\* | Указываются необходимые для обработки папки системы. |
| Расширения файлов\* | Указываются расширения файлов, по которым должна быть собрана информация. Расширения файлов указываются через запятую без пробелов. |
| Пароль для шифрования\* | Указывается пароль, который будет использоваться для шифрования и последующего дешифрования собранного верификационного файла. |
| Время выполнения шага (сек) | Задается время выполнения одного шага сбора данных в секундах. |

\* - поля, обязательные для заполнения.

  

### Закладка Отчет

Форма позволяет просмотреть результат процесса сбора данных, по окончании которого в целях безопасности рекомендуется скачать файл с верификационными данными на локальный компьютер.

### Проверка целостности системы

  

### Закладка Выбор файла

Форма позволяет выбрать файл с верификационными данными для проверки целостности системы либо хранящийся в системе либо с локальном компьютера.

| Поле | Описание |
| --- | --- |
| Выбор файла с верификационными данными | Указывается файл с верификационными данными, хранящийся в системе. |
| Загрузка файла с верификационными данными | Указывается путь к файлу с верификационными данными. |

  

### Закладка Проверка данных

Форма позволяет настроить параметры проверки целостности системы.

| Поле | Описание |
| --- | --- |
| Пароль для дешифрования\* | Указывается пароль, который был задан при создании файла с верификационными данными. |
| Время выполнения шага (сек) | Указывается время выполнения одного шага проверки (чем меньше время выполнения одного шага, тем больше нагрузка на сервер). |

\* - поля, обязательные для заполнения.

  

### Закладка Отчет

Форма позволяет просмотреть результат проверки целостности системы.

### Смотрите также

* [Повышенный уровень защиты (учебный курс Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2674)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх