# Шардинг

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

Шардинг

**Недоступно в редакциях:**Бизнес, Малый бизнес, Стандарт, Старт

# Шардинг

### Описание

Страница **Шардинг** (*Настройки > Веб-кластер > Шардинг*) содержит информацию о существующих базах данных, позволяет добавлять новые базы и управлять текущими.

**Вертикальный шардинг** - разделение одной базы данных веб-приложения на две и более базы данных за счет выделения отдельных модулей, без изменения логики работы веб-приложения.

**Горизонтальный шардинг** - распределение однотипных данных веб-приложения (например, учетных записей) между отдельными базами данных.

**Примечание:** В продукте пока поддерживается только **Вертикальный шардинг**.

Таблицы с данными некоторых модулей можно вынести в отдельную базу данных, перераспределив нагрузку, создаваемую запросами между различными серверами. Для этого нажмите кнопку **Добавить новую базу данных**.

После добавления подключения данные модуля можно перенести двумя способами:

* Первый способ доступен только для MySQL. Он заключается в том, чтобы в списке баз данных модулей в меню действий выбранной базы данных выполнить команду **Начать использовать**. Запустится мастер переноса данных.
* Второй способ заключается в удалении модуля и последующей его установки. На первом шаге установки появится возможность указать базу данных для использования модулем. В этом случае таблицы модуля не будут перенесены.

На данный момент поддерживаются следующие модули:

* **[Веб-аналитика](/user_help/statistic/index.php)**;
* **[Поиск](/user_help/settings/search/index.php)**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Добавить новую базу данных | Добавление новой базы данных. |
| Обновить | Обновление списка. |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

### Таблица "Базы данных модулей"

| Поле | Описание |
| --- | --- |
| ID | Идентификатор базы данных. |
| Состояние | Состояние и время работы базы данных. |
| Активность | Признак активности базы данных. |
| Статус | Текущий статус базы данных. |
| Название | Название базы данных. |
| Модули | Модули, осуществляющие работу с базой данных. |
| Описание | Описание базы данных. |
| Сервер | Адрес сервера базы данных. |
| База данных | Название базы данных, содержащей таблицы модулей. |
| Пользователь | Учетная запись MySQL, под которой веб-кластер работает с базой данных модулей. |

### Смотрите также

* [Шардинг (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2690)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх