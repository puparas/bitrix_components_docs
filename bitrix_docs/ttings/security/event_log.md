# Журнал вторжений

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

Журнал вторжений

**Недоступно в редакциях:**Старт

# Журнал вторжений

**Журнал вторжений** (*Настройки > Проактивная защита > Журнал вторжений*) предназначен для ведения логов событий, связанных с потенциальными угрозами для безопасности сайта. Период времени, в течение которого хранятся записи, определяется настройками Главного модуля.

Журнал вторжений - это, фактически, штатная настройка для [Журнала событий](/user_help/settings/utilities/event_log/event_log.php). Срок хранения данных в Журнале определяется настройками [Главного модуля](/user_help/settings/settings/settings.php#events).

  

### Фильтр

Форма фильтра используется для выбора из списка вторжений в соответствии с указанными условиями. Нижеследующая таблица описывает параметры, по которым могут выбираться события.

| Поле | Описание |
| --- | --- |
| Найти | Позволяет найти вторжения по их основным параметрам: названию или идентификатору. Это поле присутствует, даже если фильтр свернут. |
| ID | Идентификатор вторжения. Соответствует полю **ID** списка вторжений. |
| Время | Позволяет указать период (начало и окончание) времени для отбора событий. |
| Срочность | Определяется, события какой срочности будут участвовать в поиске: **SECURITY** или **WARNING**. |
| Событие\* | Позволяет выполнить отбор событий по названию. |
| Источник\* | Позволяет выполнить отбор событий по источнику. |
| Объект\* | Позволяет выполнить отбор событий по объекту. |
| Сайт | Указывается сайт, для которого будет отображен список событий. |
| Пользователь | Задается имя пользователя, если событие было выполнено зарегистрированным пользователем, или идентификатор гостя для поиска событий (при наличии модуля **Веб-аналитика**). |
| Гость | Задается идентификатор гостя для отбора событий (при наличии модуля **Веб-аналитика**). |
| IP\* | Служит для отбора событий по IP адресу. |
| User Agent\* | Служит для отбора событий по User Agent. |
| URL\* | Служит для отбора событий по адресу страницы. |

\* - для данных полей Вы можете воспользоваться
специальными логическими выражениями



Облегчайте поиск информации вместе с логическими операторами. Система допускает использование пяти видов логических операторов. Давайте их рассмотрим.  
  
[Подробнее ...](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=2057&LESSON_PATH=3906.4507.2057) в курсе **Администратор.Базовый**.
.

Для того чтобы отобрать события по заданным критериям поиска, нажмите кнопку **Найти**. Для отображения всех событий нажмите кнопку **Отменить**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Настроить | Позволяет перейти к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в MS Excel. |

### Журнал событий

| Поле | Описание |
| --- | --- |
| ID | Идентификатор вторжения. |
| Время | Дата и время события. |
| Событие | Название произошедшего события. |
| Объект | Объект события. |
| IP | IP-адрес, с которого производилась атака. По ссылке **стоп-лист** можно добавить адрес в стоп-лист модуля **Веб-аналитика**. |
| URL | Адрес страницы, на которой выполнялось вторжение. |
| Пользователь | Имя пользователя, если событие было выполнено зарегистрированным пользователем, или идентификатор гостя (при наличии модуля **Веб-аналитика**). |
| Описание | Описание события. |
| Срочность | Срочность события (**SECURITY** или **WARNING**). |
| Источник | Источник события. |
| User Agent | Используемый User Agent. |
| Сайт | Сайт, на котором произошло событие. |
| Гость | Идентификатор гостя (при наличии модуля **Веб-аналитика**). |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх