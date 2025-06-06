# DAV (КП). Настройки модуля

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

[DAV (КП)](/user_help/settings/dav/index.php)

[DAV (КП). Настройки модуля](/user_help/settings/dav/settings.php)

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

[DAV (КП)](/user_help/settings/dav/index.php)

DAV (КП). Настройки модуля

# DAV (КП). Настройки модуля

Вкладки

Форма настроек модуля **DAV** (*Настройки > Настройки продукта > Настройки модулей > DAV*) предназначена для задания общесистемных параметров для синхронизации календарей и контактов с внешними системами.

  

### Вкладка Exchange

| Поле | Описание | Примечание |
| --- | --- | --- |
| Включить синхронизацию календарей Exchange | При отмеченной опции будет включена синхронизация календарей с MS Exchange. |  |
| Включить синхронизацию контактов Exchange | При отмеченной опции будет включена синхронизация контактов с MS Exchange. |  |
| Включить синхронизацию задач Exchange | При отмеченной опции будет включена синхронизация задач с MS Exchange. |  |
| Включить запрос количества непрочитанных сообщений Exchange | При отмеченной опции будет отправляться запрос к MS Exchange на количество непрочитанных сообщений, которые будут выводиться в панели статусов публичной части портала. |  |
| Схема подключения к Exchange серверу | Выбирается протокол подключения к серверу MS Exchange: **HTTP** или **HTTPS**. |  |
| Адрес Exchange сервера | Указывается адрес для подключения с сервером MS Exchange. |  |
| Порт Exchange сервера | Указывается порт для подключения с сервером MS Exchange. |  |
| Имя пользователя для соединения с Exchange сервером | Указывается имя пользователя. | Модулю **DAV** нужен доступ к профилям всех пользователей Exchange, которые будут подключены к синхронизации. Роль пользователя Exchange, логин и пароль которого указываются в настройках модуля DAV, может включать в себя доступ только к тем объектам, которые предполагается синхронизировать. Например, держатель роли может обладать правами на календари, но не на контакты пользователей. Учетные записи пользователей не изменяются и не удаляются. |
| Пароль пользователя для соединения с Exchange сервером | Указывается пароль пользователя. |
| Шаблон почтового ящика Exchange сервера | Указывается шаблон почтового ящика в MS Exchange (Например: @test.com). |  |
| Использовать логин в качестве имени почтового ящика на Exchange сервере | При отмеченной опции будет использоваться логин пользователя портала в качестве имени почтового ящика на сервере MS Exchange (Например: логин пользователя на портале - user, шаблон почтового ящика в MS Exchange - @test.com, то итоговый почтовый ящик пользователя будет user@test.com). | Если опция отключена, то для правильной работы MS Exchange с пользователями необходимо:  1. в форме редактирования профиля каждого пользователя во вкладке **Дополнительно** включить [пользовательское поле](/learning/course/index.php?COURSE_ID=48&LESSON_ID=2808#warning) **Почтовый ящик Exchange** (код поля: UF\_BXDAVEX\_MAILBOX) с помощью кнопки **Настроить** (либо нажать кнопку **Отменить действия настроек полей формы на время сессии**); 2. указать почтовый ящик пользователя в MS Exchange.   **Внимание!** при включении этой опции становится невозможным подключение E-mail трекера в CRM. |
| Путь к Outlook Web App | Указывается путь к Outlook Web App (OWA) - специальному приложению, которое позволяет работать в браузере с MS Exchange. После чего в панели статусов появится ссылка для перехода к OWA. |  |

### Вкладка DAV

| Поле | Описание |
| --- | --- |
| Включить синхронизацию календарей CalDAV | При отмеченной опции будет включена синхронизация между порталом и мобильными устройствами, используя протокол CalDAV (Например, для владельцев мобильных устройств по управлением Apple iOS). |

### Вкладка Прокси

| Поле | Описание |
| --- | --- |
| Использовать прокси | При отмеченной опции для работы DAV будет использоваться прокси-сервер. Для этого необходимо указать настройки подключения к прокси-серверу:  * Схема подключения к прокси; * Адрес прокси; * Порт прокси; * Логин прокси; * Пароль прокси. |

### Смотрите также

* [Работа с модулем DAV](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=48&CHAPTER_ID=04769)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх