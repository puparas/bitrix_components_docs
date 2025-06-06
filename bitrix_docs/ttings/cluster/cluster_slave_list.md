# Репликация

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

Репликация

**Недоступно в редакциях:**Бизнес, Малый бизнес, Стандарт, Старт

# Репликация

### Описание

Страница **Репликация** (*Настройки > Веб-кластер > [Группа] > Репликация*) содержит информацию о существующих резервных базах данных, позволяет добавлять новые резервные базы и управлять текущими.

**Внимание!** Страница *Настройки > Веб-кластер > Репликация* позволяет просматривать все базы данных для всех групп, но через нее добавить slave базу данных нельзя.

Запуск репликации начинается с копирования содержимого базы данных. На время копирования публичная часть сайта будет закрыта, а административная нет. Любые неучтенные модификации данных в период копирования могут в дальнейшем повлиять на правильность работы сайта.

**Репликация базы данных** - это процесс создания и поддержания в актуальном состоянии её копии.

Репликация позволяет:

* перенести часть нагрузки с основной базы данных (master) на одну или несколько ее копий (slave);
* использовать копии в качестве горячего резерва.

Для создания резервной базы данных нажмите кнопку **Добавить slave базу данных** и следуйте указаниям мастера. После создания базы в меню действий выполните команду **Начать использовать**.

**Внимание!** Для репликации необходимо использовать разные сервера с быстрым каналом связи между собой.

  
Запуск репликации начинается с копирования содержимого базы данных. На время копирования публичная часть сайта будет закрыта, а административная нет. Любые неучтенные модификации данных в период копирования могут в дальнейшем повлиять на правильность работы сайта.

**Примечание:** Страница репликации недоступна для **mssql** и **oracle** версий.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Добавить slave базу данных | Добавление резервной базы данных. |
| Обновить | Обновление списка баз данных модулей. |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

### Таблица "Slave базы данных"

| Поле | Описание |
| --- | --- |
| ID | Идентификатор базы данных. |
| Состояние | Состояние и время работы базы данных. |
| Название | Название базы данных. |
| Отставание (сек) | Отставание slave базы данных при большом количестве обновлений основной (master) базы данных, недостаточно быстром соединении между master и slave базами данных или недостаточной производительности slave базы данных.    Максимально возможное время отставания slave базы данных от master, при котором slave база данных будет автоматически отключена для снижения риска рассинхрониизации данных, можно задать в [настройках модуля](/user_help/settings/cluster/settings.php). |
| Статус | Текущий статус базы данных. |
| Использовать (%) | Рекомендуемая доля (вес) нагрузки на базу данных для использования встроенным в продукт балансировщиком SQL. |
| Описание | Описание базы данных. |
| Сервер | Адрес сервера. |
| База данных | Название базы данных, содержащей таблицы модулей. |
| Пользователь | Учетная запись MySQL, под которой веб-кластер работает с базой данных модулей. |

### Смотрите также

* [Репликация (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2719)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх