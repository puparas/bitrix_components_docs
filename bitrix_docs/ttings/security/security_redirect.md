# Защита редиректов

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

Защита редиректов

**Недоступно в редакциях:**Старт

# Защита редиректов

### Описание

**Фишинг** (англ. phishing, от password — пароль и fishing — рыбная ловля, выуживание) — вид интернет-мошенничества, целью которого является получение доступа к конфиденциальным данным пользователей (например, логинам и паролям).
Это достигается путем проведения массовых рассылок электронных писем от имени популярных брендов, например, от имени социальных сетей, банков, порталов. В письме часто содержится прямая ссылка на сайт, внешне не отличимая от настоящей.

Защита редиректов от фишинга осуществляется двумя методами:

* во-первых, можно определить злонамеренный редирект по отсутствию заголовка http протокола - ссылающаяся страница.
* во-вторых, можно подписать ссылки, генерируемые на сайте, цифровой подписью и проверять эту подпись при попытке редиректа.

Защита может заключаться в следующих вариантах действий:

* показать пользователю предупреждение, что он будет перенаправлен на другой сайт и показать на какой именно.
* принудительно перенаправить его на заведомо безопасный адрес. Например, главную страницу атакуемого сайта.

### Закладка Защита редиректов

Включение или отключение защиты редиректов от фишинга выполняется на странице **Защита редиректов от фишинга** (*Настройки > Проактивная защита > Защита редиректов*) с помощью кнопки **Включить защиту редиректов от фишинга** (**Выключить защиту редиректов от фишинга**).

### Закладка Параметры

Форма позволяет настроить параметры защиты редиректов.

| Поле | Описание |
| --- | --- |
| Методы защиты от фишинга | Указываются следующие методы защиты от фишинга:  * **Проверять наличие HTTP заголовка описывающего ссылающуюся страницу** - при отмеченной опции будет проверяться наличие HTTP заголовка, описывающего страницу; * **HTTP заголовок, описывающий ссылающуюся страницу, должен содержать текущий сайт** - при отмеченной опции будет проверяться наличие в HTTP заголовке записи о текущем сайте, который описывает ссылающуюся страницу; * **Добавлять цифровую подпись к перечисленным ниже URL** - при отмеченной опции к адресам, перечисленным в поле **Подписываемые URLs**, будет добавляться цифровая подпись.   **Примечание:** Начиная с версии модуля 14.0.3, для страниц в публичной части сайта с сообщениями функционала "*Защита редиректов от фишинга*" и "*Проактивный фильтр*" добавлены теги `noindex` и `nofollow`.  **Примечание:** Начиная с версии модуля 20.0.0 cтраница защиты от редиректов отдает HTTP-статус `404 Not Found`. |
| Подписываемые URLs | Указываются **Системные** и **Пользовательские** подписываемые URLs. Добавление полей ввода осуществляется с помощью кнопки **Добавить**. |
| Действия защиты от фишинга | Задается одно из следующих действий защиты от фишинга:  * **Перенаправить на другой сайт с показом сообщения и задержкой** - при отмеченной опции будет перенаправлен на другой сайт с показом соответствующего сообщения и выполнением задержки на несколько секунд. Текст сообщения задается в поле **Сообщение**, а период задержки пользователя – в поле **Задержка**. * **Перенаправить на заданный URL** - при отмеченной опци будет перенаправлен на заданный в поле **URL** адрес. |
| Занести попытку фишинга в журнал | При отмеченной опции попытка фишинга через редирект будет занесена в журнал событий. |

### Смотрите также

* [Высокий уровень защиты (учебный курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2673)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх