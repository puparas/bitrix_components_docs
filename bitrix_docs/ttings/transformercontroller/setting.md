# Настройки модуля

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

[Настройки модуля](/user_help/settings/transformercontroller/setting.php)

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

[Сервер конвертации файлов (КП)](/user_help/settings/transformercontroller/index.php)

Настройки модуля

**Недоступно в редакциях:**Бизнес, Малый бизнес, Стандарт, Старт

# Настройки модуля

Страница настроек модуля (*Настройки > Настройки продукта > Настройки модулей > Сервер конвертации файлов*) предназначена для задания параметров подключения к севреру очередей и настройки работы самих очередей.

Закладки:

#### Общие настройки

| Поле | Описание | Комментарий |
| --- | --- | --- |
| Режим отладки | Чекбокс включения режима отладки | Если включен, то данные о запросах и отправляемых командах будут писаться в файлах: `/var/log/rabbitmq/` и `/var/log/transformer/` |
| Время установления соединения при проверке лицензии | Параметр установления соединения с сервером проверки лицензий. |  |
| Время ожидания ответа при проверке лицензии | Параметр установления времени ожидания ответа сервера проверки лицензий. |  |
| Адреса через запятую, с которых должны обрабатываться запросы на конвертацию |  | Оставьте пустым, если адрес не должен проверяться. |

#### Настройки RabbitMQ

| Поле | Описание | Комментарий |
| --- | --- | --- |
| Логин | Параметры авторизации и подключения к серверу |  |
| Пароль |  |
| Адрес |  |
| Порт |  |
| Виртуальный хост |  |

#### Настройка очередей

На этой закладке вы можете изменить значения по умолчанию количество обработчиков.

#### Статус

Информационная закладка показывает статус работы сервера. При использовании BitrixVM настройка сервера производится автоматически и статусы меняются после запуска виртуальной машины.

#### Дополнительно

* Настройка роли Transformer (учебный курс)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх