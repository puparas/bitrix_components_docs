# Монитор производительности. Настройки модуля

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

Монитор производительности. Настройки модуля

# Монитор производительности. Настройки модуля

Вкладки

Форма настроек модуля **Монитор производительности** (*Настройки > Настройки продукта > Настройки модулей > Монитор производительности*) предназначена для задания параметров модуля.

  

### Настройки

Вкладка предназначена для настройки параметров сбора информации и для управления монитором производительности.

| Поле | Описание |
| --- | --- |
| Максимальная длина URL при отображении | Указывается максимальное количество символов для отображения URL'ов. |
| Вести журнал предупреждений PHP | При отмеченной опции ошибки PHP будут регистрироваться в журнале. Просмотреть журнал ошибок можно на странице [Ошибки PHP](/user_help/settings/perfmon/perfmon_error_list.php). |
| Вести журнал кеширования | При отмеченной опции информация о файлах кеша будет сохраняться в журнале. Просмотреть журнал можно на странице [Кеширование](/user_help/settings/perfmon/perfmon_cache_list.php). |
| Записывать только операции с большими файлами кеша | При отмеченной опции в журнал будут записываться только операции с файлами кеша, размер которых больше, чем указано в поле **Размер файла кеша больше которого считать его большим.** |
| Размер файла кеша больше которого считать его большим | Задается размер файла кеша, по превышении которого он считается "большим". |
| Вести журнал SQL запросов | При отмеченной опции SQL запросы будут регистрироваться в журнале. Просмотреть журнал запросов можно на странице [SQL запросы](/user_help/settings/perfmon/perfmon_sql_list.php). |
| Сохранять стек вызова для SQL запросов | Включает отображение стека запроса на странице [SQL запросы](/user_help/settings/perfmon/perfmon_sql_list.php). |
| Записывать только медленные SQL запросы | Включает фильтры запросов по времени. При включенной опции максимальное время работы монитора может составлять 1 неделю (при выключенной опции максимальное время работы монитора составляет 1 час). |
| Время исполнения после которого считать запрос медленным | Задание продолжительности, по превышении которой запрос считается "медленным". |
| Активность монитора | В поле отображается текущий статус активности монитора производительности. |
| Включить монитор [Отключить монитор] | Для включения монитора в поле **Включить монитор** укажите время, на которое монитор будет включен (например, **на 1 минуту**), и нажмите кнопку **Применить** или **Сохранить**.     Для выключения монитора установите флаг в поле **Отключить монитор** и нажмите кнопку **Применить** или **Сохранить**. |
| Удалить собранные ранее данные | При отмеченной опции собранные ранее данные по производительности будут удалены. **Опция доступна только при отключенном мониторе**. |

### Генератор таблетов

Вкладка предназначена для [разработчиков](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2410&LESSON_PATH=3913.5062.5748.2410). На ней включается автоматическая генерация таблетов для ORM и настраиваются параметры генератора.

| Поле | Описание |
| --- | --- |
| Разрешить генерацию таблетов для ORM | Включает автоматическую генерацию таблетов для ORM. Если разрешено, то на странице Настройки > Производительность > Таблицы в меню действий для таблицы станет доступен пункт **ORM**. |
| Параметры генератора | |
| Использовать короткие алиасы классов | При включенной опции используются короткие алиасы классов. Пример: `new Reference()` вместо `new Fields\Relations\Reference()`. |
| Описание параметров полей таблета через методы | При включенной опции параметры поля задаются через вывозы соответствующих методов. |
| Имена полей в карте | При включенной опции метод getMap таблета будет возвращаться массив, где индексами являются имена полей. При выключенной - нумерованный массив. |
| Проверка значений в виде замыканий | Опция влияет на стиль генерируемого кода:  * **выключена** – в классе будет   отдельная функция валидатор    ; * **включена** – в классе будет   анонимная функция    (замыкание). |

### Доступ

Вкладка позволяет настроить права на доступ к модулю для всех имеющихся в системе групп пользователей.

| Поле | Описание |
| --- | --- |
| По умолчанию | Уровень доступа групп пользователей, для которых установлено право "по умолчанию". |
| [группа\_пользователей] | Изменение настроек доступа для конкретной группы. Возможно назначение следующих прав доступа к модулю **Монитор производительности**:  * **[D] доступ закрыт** - запрет на доступ; * **[R] просмотр всей статистики** - доступ открыт только на просмотр статистики по производительности сайта; * **[W] полный административный доступ** - полный доступ к ресурсам модуля. |
| Добавить право доступа | Ссылка, позволяющая добавить дополнительное право доступа для группы пользователей. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх