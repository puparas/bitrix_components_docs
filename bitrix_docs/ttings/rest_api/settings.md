# REST API. Настройки модуля

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

[REST API. Настройки модуля](/user_help/settings/rest_api/settings.php)

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

[REST API](/user_help/settings/rest_api/index.php)

REST API. Настройки модуля

# REST API. Настройки модуля

### Форма настроек

  
Форма настроек модуля **REST API** (*Настройки > Настройки продукта > Настройки модулей > REST API*) предназначена для задания параметров модуля.
  
  

### Вкладка Настройки

| Поле | Описание |
| --- | --- |
| Модуль mod\_zip включен и настроен (требуется для экспорта) | При отмеченной опции для экспорта архива приложения будет использоваться модуль mod\_zip    **mod\_zip** — HTTP-модуль для NGINX, динамически собирающий ZIP-архивы. В простых конфигурациях mod\_zip берет список файлов в локальной файловой системе и обслуживает их как один ZIP-архив. В более сложных настройках mod\_zip может передавать файлы компонентов с вышестоящих серверов с помощью собственного прокси-кода NGINX. В отличие от многих сценариев создания ZIP, этот процесс никогда не занимает больше нескольких КБ ОЗУ, даже при сборке архивов, размер которых (потенциально) составляет сотни мегабайт.    [Подробнее...](https://www.nginx.com/resources/wiki/modules/zip/) |
| Максимальный размер импортируемого файла (МБ) | Устанавливается ограничение на размер файла импорта |

### Вкладка Логирование

| Поле | Описание |
| --- | --- |
| Активность логирования | Статус логирования (работает или отключено) |
| Включить логирование | Устанавливается (выбирается из списка) время, на которое нужно включить лог использования RESTа. Доступно три периода времени: на 10 минут, 1 час или сутки. Логироваться будет весь REST, в том числе поэтапная работа исходящих событий. Через указанное время логирование отключится автоматически |
| До окончания активности осталось | Поле отображается, если логирование включено. Показывает сколько времени осталось до автоматического отключения логирования |
| Отключить логирование | Опция отображается, если логирование включено. Позволяет отключить его досрочно |
| Удалить собранные ранее данные | Выполняется удаление данных, собранных при предыдущем включении логирования |
| Собрано данных | При нажатии на ссылку-число собранных данных можно просмотреть более подробный лог использования RESTа |
| Настройки фильтрации | |
| Идентификатор клиента (client\_id) | Задаются параметры для выполнения импорта посредством REST.  При большом объеме выгружаемых данных это значительно ускорит импорт.  Подробное описание смотрите в документации по REST — [Как правильно выгружать большие объемы данных](https://dev.1c-bitrix.ru/rest_help/rest_sum/start.php) |
| Идентификатор пароля (password\_id) |
| Область видимости (scope) |
| Метод (method) |
| Идентификатор пользователя (user\_id) |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх