# Ошибки PHP

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

[Монитор производительности. Настройки модуля](/user_help/settings/perfmon/settings.php)
[Панель производительности](/user_help/settings/perfmon/perfmon_panel.php)
[Скорость сайта (БУС)](/user_help/settings/perfmon/site_speed.php)
[Страницы](/user_help/settings/perfmon/perfmon_hit_grouped.php)
[Хиты](/user_help/settings/perfmon/perfmon_hit_list.php)
[Компоненты](/user_help/settings/perfmon/perfmon_comp_list.php)
[SQL запросы](/user_help/settings/perfmon/perfmon_sql_list.php)
[Кеширование](/user_help/settings/perfmon/perfmon_cache_list.php)
[Таблицы](/user_help/settings/perfmon/perfmon_table.php)
[Проверка БД](/user_help/settings/perfmon/repair_db.php)
[Анализ индексов](/user_help/settings/perfmon/perfom_index_list.php)
[Детальный анализ индекса](/user_help/settings/perfmon/perfom_index_detail.php)
[Список индексов](/user_help/settings/perfmon/perfom_index_complete.php)
[Настройки PHP](/user_help/settings/perfmon/perfmon_php.php)
[Сервер БД](/user_help/settings/perfmon/perfmon_db_server.php)
[История замеров производительности](/user_help/settings/perfmon/perfmon_history.php)
[Ошибки PHP](/user_help/settings/perfmon/perfmon_error_list.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

Ошибки PHP

# Ошибки PHP

На странице **Журнал ошибок PHP** (*Настройки > Производительность > Ошибки PHP (N)*) можно просмотреть журнал регистрации ошибок PHP, где **N** - общее количество ошибок.

  

**Примечание:** Данная страница отображается, только если в настройках модуля **Монитор производительности** указана опция **Вести журнал предупреждений PHP**.

  

### Фильтр

Форма фильтра используется для фильтрации записей журнала в соответствии с указанными условиями. Нижеследующая таблица описывает параметры, по которым могут выбираться записи.

| Поле | Описание |
| --- | --- |
| Найти | Позволяет найти записи об ошибках по их основным параметрам. Это поле присутствует, даже если фильтр свернут. |
| Хит | Позволяет найти записи по идентификатору хита. |
| Класс ошибки | Позволяет осуществлять поиск в журнале по классу (типу) ошибок. |
| Файл | Позволяет осуществлять поиск в журнале по файлу, в котором произошла ошибка. |
| Текст | Позволяет осуществлять поиск в журнале по тексту ошибки. |

Чтобы отфильтровать ошибки по заданным критериям поиска, нажмите кнопку **Найти**. Для отображения всех ошибок нажмите кнопку **Отменить**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Группировка | Позволяет задать способ группировки записей об ошибках в журнале:  * **Группировка включена** - журнал будет содержать поля: **Класс ошибки**, **Файл**, **Строка**, **Текст**, **Количество**; * **Группировка выключена** - журнал будет содержать поля: **ID**, **Хит**, **Класс ошибки**, **Файл**, **Строка**, **Текст**. |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в MS Excel. |

### Ошибки PHP

| Поле | Описание |
| --- | --- |
| ID | Идентификатор записи об ошибке в журнале. |
| Хит | Идентификатор хита. |
| Класс ошибки | Класс (тип) ошибки. |
| Файл | Путь к файлу в системе, в котором произошла ошибка. |
| Строка | Номер строки в файле. |
| Текст | Текст ошибки. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх