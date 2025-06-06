# Инспектор сайтов

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

[Облако 1С-Битрикс. Настройки модуля](/user_help/settings/bitrixcloud/settings.php)
[Ускорение сайта CDN](/user_help/settings/bitrixcloud/bitrixcloud_cdn.php)
[Резервные копии](/user_help/settings/bitrixcloud/bitrixcloud_backup.php)
[Инспектор сайтов](/user_help/settings/bitrixcloud/bitrixcloud_monitoring_admin.php)
[Параметры инспектирования](/user_help/settings/bitrixcloud/bitrixcloud_monitoring_edit.php)

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

[Облако 1С-Битрикс](/user_help/settings/bitrixcloud/index.php)

Инспектор сайтов

# Инспектор сайтов

### Описание

На странице **Инспектор сайтов** (*Настройки > Облако 1С-Битрикс > Инспектор сайтов*) расположен инструмент, который проверяет доступность и работоспособность сайта и сообщает обо всех неполадках E-mail или push-уведомления для мобильных устройств.

**Примечание:** Проверка осуществляется со стороны серверов компании "1С-Битрикс", поэтому сайт должен быть доступен "снаружи".

Инспектор сайта отслеживает 4 параметра, очень важных для работы любого веб-проекта, и особенно интернет-магазина:

* раз в 5 минут проверяет доступность сайта из двух географических точек;
* раз в день проверяет срок действия домена.
    
  Инспектор сайта напомнит за 30 дней о необходимости продлить домен. Повторяться напоминания будут раз в неделю, пока домен не будет продлен;
* раз в день проверяет срок SSL-сертификата;
* раз в день проверяет срок действия лицензионного ключа.
    
  Инспектор сайта напомнит за 30 дней об окончании срока активности обновлений и технической поддержки для вашей лицензии.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Добавить сайт для инспектирования | Добавление сайта и [настройка параметров](/user_help/settings/bitrixcloud/bitrixcloud_monitoring_edit.php) его инспектирования.   **Примечание:** Для корректной работы сервиса для инспектируемого сайта должен быть указан домен на странице **Редактирования сайта** (*Настройки продукта > Сайты > Список сайтов > требуемый\_сайт*) или в поле **URL сайта** настроек **Главного модуля** (*Настройки > Настройки продукта > Настройки модулей > Главный модуль*). |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

### Результаты инспектирования

| Колонка | Описание |
| --- | --- |
| Домен | Инспектируемый сайт. |
| Результаты инспектирования | Информация о результатах инспекции. |

### Смотрите также

* [Инспектор сайтов (курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=5517)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх