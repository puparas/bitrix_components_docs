# Проактивная защита. Настройки модуля

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

Проактивная защита. Настройки модуля

**Недоступно в редакциях:**Старт

# Проактивная защита. Настройки модуля

Закладки

Форма настроек модуля **Проактивная защита** (*Настройки > Настройки продукта > Настройки модулей > Проактивная защита*) предназначена для задания общесистемных параметров модуля.

  

### Настройки

| Поле | Описание |
| --- | --- |
| Разрешать блокировать себя по IP (с показом предупреждения) | При отмеченной опции будет разрешено блокировать самого себя по IP адресу, при этом будет показано предупреждение. |
| Путь к файлу-флажку запрета блокировки по IP | Указывается путь к файлу-флажку, с помощью которого можно снять ограничение по IP-адресам. По умолчанию файл имеет имя следующего формата: **ipcheck\_disable\_*<случайный\_набор\_из\_32\_символов>***. |
| Настройки журналирования | |
| Секция позволяет указать, как и куда будет сохраняться информация о событиях, запись которых можно включить на административных страницах модуля (Настройки > Проактивная защита). | |
| Формат сообщения | Указывается формат записи данных о событии.    Доступные поля сообщения:  * **#AUDIT\_TYPE#** - Имя аудитора безопасности; * **#SITE\_ID#** - ID текущего сайта; * **#USER\_INFO#** - Информация о пользователе; * **#URL#** - Запрашиваемый url; * **#VARIABLE\_NAME#** - Имя переменной, содержащей опасные данные; * **#VARIABLE\_VALUE#** - Опасные данные; * **#VARIABLE\_VALUE\_BASE64#** - Опасные данные (base64-кодированные). |
| Формат информации о пользователе | Указывается формат записи данных о пользователе, связанным с событием.    Доступные поля сообщения:  * **#REMOTE\_ADDR#** - IP-адрес; * **#USER\_AGENT#** - User-Agent; * **#USER\_ID#** - ID пользователя. |
| Заносить записи в журнал событий | При отмеченной опции информация о событиях будет заноситься в [журнал событий](/user_help/settings/utilities/event_log/event_log.php). |
| Заносить записи в Syslog | При отмеченной опции информация о событиях будет заноситься в системный журнал: Syslog или же штатный журнал событий ОС Windows. |
| Тип журналирования (facility) | Задается [тип журналирования (facility)](http://php.net/manual/ru/function.openlog.php) для записей о событиях. |
| Уровень оповещения | Задается [уровень оповещения (priority)](http://php.net/manual/ru/function.syslog.php) для записей о событиях. |
| Заносить записи в файл | При отмеченной опции информация о событиях будут заноситься в файл. |
| Абсолютный путь к файлу | Задается абсолютный путь к файлу, в который будет производиться запись информации о событиях. |

### Доступ

| Поле | Описание |
| --- | --- |
| По умолчанию | Уровень доступа групп пользователей, для которых установлено право "по умолчанию". |
| [группа\_пользователей] | Изменение настроек доступа для конкретной группы. Возможно назначение следующих прав доступа к модулю **Проактивная защита**:  * **[D] Доступ закрыт** - запрет на доступ; * **[F] Обход проактивного фильтра** - для указанной группы пользователей будет осуществляться обход проактивного фильтра; * **[S] Управление одноразовыми паролями** - разрешается управлять одноразовыми паролями; * **[T] Просмотр всех данных** - разрешается только просмотр всех данных модуля; * **[W] Полный административный доступ** - полный доступ к ресурсам модуля. |
| Добавить право доступа | Ссылка, позволяющая добавить дополнительное право доступа для группы пользователей. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх