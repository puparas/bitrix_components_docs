# Создание/редактирование подключения к облачному хранилищу

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

[Облачные хранилища](/user_help/settings/clouds/clouds_storage_list.php)
[Создание/редактирование подключения к облачному хранилищу](/user_help/settings/clouds/clouds_storage_edit.php)

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

[Облачные хранилища](/user_help/settings/clouds/index.php)

Создание/редактирование подключения к облачному хранилищу

# Создание/редактирование подключения к облачному хранилищу

### Контекстная панель

Форма используется создания или изменения параметров подключения и использования облачного хранилища.

| Кнопка | Описание |
| --- | --- |
| Список | Переход на страницу [Облачные хранилища](/user_help/settings/clouds/clouds_storage_list.php). |

### Закладка Подключение

Настройка параметров подключения и использования облачного хранилища.

| Поле | Описание |
| --- | --- |
| ID | Идентификатор контейнера облачного хранилища файлов. |
| Активность | Признак активности контейнера облачного хранилища файлов. Если контейнер не активен, то старые данные будут читаться из него, а новые будут сохраняться на хостинге, на котором расположен проект. |
| Сортировка | Задается относительный "вес", влияющий на положение контейнера в списке. |
| Провайдер | Выбирается поставщик услуг облачного хранения файлов:  * Amazon Simple Storage Service; * Google Storage; * OpenStack Object Storage; * Rackspace Cloud Files; * Clodo.ru; * Selectel; * HotBox; * Yandex Object Storage; * S3 compatible storage – другие S3-совместимые хранилища. |
| Регион | Выбирается регион, в котором географически располагаются сервера (значения поля зависят от выбранного провайдера). |
| [дополнительные\_поля\_для\_доступа\_к\_сервису] | В зависимости от провайдера, в полях указываются параметры доступа к сервисам облачного хранения файлов. Например: **Ключ доступа**, **Секретный ключ**.    **Примечание:** Для некоторых провайдеров под полями расположена краткая инструкция по подключению. |
| Контейнер | Задается уникальное название контейнера. По умолчанию в поле уже указано название. |
| Только для чтения | При отмеченной опции контейнер будет использоваться в режиме чтения. Новые файлы будут сохраняться не в контейнере, а на хостинге с проектом. |
| Каноническое имя домена (CNAME) | Указывается каноническое имя домена. |

### Закладка Правила

Настройка правил для отбора файлов в облачное хранилище.

| Поле | Описание |
| --- | --- |
| | Список модулей | Список расширений | Список размеров |  | | --- | --- | --- | --- | | [1] | [2] | [3] | [4] |  | Поле | Описание | | --- | --- | | [1] Список модулей | Указывается идентификатор модуля. Например: **iblock**, **advertising**. Если параметр не задан, то под действие правила подпадают файлы любых модулей. | | [2] Список расширений | Указываются расширения файлов для хранения в облачном хранилище. Например: **gif**, **png**, **jpeg**, **jpg**. Если не задано, то под действие правила подпадают файлы с любым расширением. Список является нечувствительным к регистру. | | [3] Список размеров | Задается размеров файлов. Допустимо использовать суффиксы, такие как: **K**, **M** или **G**. Так же возможно задавать диапазоны размеров. Например: **1K-1M**, **2.3M-**. Если параметр не задан, то под действие правила подпадают файлы любого размера. | | [4] кнопка **Х** | Кнопка, позволяющая удалить правило. | | |
| Добавить новое правило | Ссылка, позволяющая добавить новое правило отбора файлов в облачное хранилище. |

### Смотрите также

* [Создание подключения (учебный курс Администратор.Базовый](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=3102)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх