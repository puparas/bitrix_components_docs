# Memcached

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

[Веб-кластер. Настройки модуля](/user_help/settings/cluster/settings.php)
[Шардинг](/user_help/settings/cluster/cluster_dbnode_list.php)
[Создание и редактирование подключения к базе данных](/user_help/settings/cluster/cluster_dbnode_edit.php)
[Репликация](/user_help/settings/cluster/cluster_slave_list.php)
[Memcached](/user_help/settings/cluster/cluster_memcache_list.php)
[Группы серверов](/user_help/settings/cluster/cluster_index.php)
[Сессии](/user_help/settings/cluster/cluster_session.php)
[Веб-сервера](/user_help/settings/cluster/cluster_webnode_list.php)
[Создание и редактирование веб-сервера](/user_help/settings/cluster/cluster_webnode_edit.php)
[Лицензирование](/user_help/settings/cluster/cluster_server_list.php)

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

[Веб-кластер](/user_help/settings/cluster/index.php)

Memcached

**Недоступно в редакциях:**Бизнес, Малый бизнес, Стандарт, Старт

# Memcached

### Описание

Страница **Memcached** (*Настройки > Веб-кластер > Memcached*) содержит информацию о существующих серверах memcached, позволяет подключать новые memcached-серверы и управлять существующими.

Для снижения нагрузки по синхронизации файлов рекомендуем использовать memcached. Основная его функция - сохранение кеша не в файлах, а в оперативной памяти.

Использование нескольких memcached-серверов (распределенный кеш данных) позволяет повысить надежность системы за счет устойчивости подсистемы кешировния к выходу из строя отдельных компонентов, повышает эффективность за счет централизованного использования кеша веб-приложением и обладает неограниченной масштабируемостью за счет добавления новых memcached-серверов.

**Примечание:** Для работы потребуется php расширение **memcache**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Добавить | Добавление сервера memcached. |
| Обновить | Обновление списка серверов memcached. |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

### Таблица "Memcached-серверы"

| Поле | Описание |
| --- | --- |
| ID | Идентификатор сервера. |
| Состояние | Состояние и время работы сервера. |
| Статус | Текущий статус сервера. |
| Использовать (%) | Рекомендуемая доля (вес) хранимого в данном сервере кеша. |
| Сервер | Адрес сервера. |

### Смотрите также

* [Memcached (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2725)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх