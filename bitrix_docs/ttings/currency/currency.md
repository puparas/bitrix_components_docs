# Список валют

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

[Валюты. Настройки модуля](/user_help/settings/currency/settings.php)
[Список валют](/user_help/settings/currency/currency.php)
[Создание и редактирование валюты](/user_help/settings/currency/currency_edit.php)
[Конфигуратор валюты](/user_help/settings/currency/currency_add_from_classifier.php)
[Курсы валют](/user_help/settings/currency/currency_rates.php)
[Создание и редактирование курса валюты](/user_help/settings/currency/currency_rates_edit.php)

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

[Валюты](/user_help/settings/currency/index.php)

Список валют

**Недоступно в редакциях:**Стандарт, Старт

# Список валют

Форма **Валюты** (*Настройки > Валюты > Список валют*) служит для управления валютами системы. *Валюты* в системе используются для работы интернет-магазина.

**Важно!** Помните, что магазин не может функционировать, если в системе не задана хотя бы одна валюта.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Добавить валюту | Переход к форме [создания](/user_help/settings/currency/currency_edit.php) новой валюты. |
| Курсы валют | Переход к форме [настройки](/user_help/settings/currency/currency_rates.php) курсов валют. |
| Настроить | Позволяет перейти к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в **MS Excel**. |

### Список валют

| Поле | Описание |
| --- | --- |
| Колонка флажков | Поле предназначено для выбора валют, к которым предполагается применить какое-либо правило или действие. |
| Действия | Доступные действия над валютой:  * **Изменить** - переход к [редактированию](/user_help/settings/currency/currency_edit.php) валюты. * **Сделать базовой** - использование валюты в качестве базовой. Пункт доступен только для небазовых валют. * **Удалить**- удаление валюты. Пункт доступен только для небазовых валют. |
| Валюта | Трехбуквенное обозначение валюты (например, **RUB**, **EUR**, **USD**). |
| Название | Полное название валюты. |
| Сорт. | Относительный "вес", влияющий на положение валюты в общем списке. |
| Номинал | Номинал, или количество валюты, для которого устанавливается обменный курс. Обычно равен номиналу, устанавливаемому ЦБ РФ. Для большинства валют номинал будет равен 1 (например, 30.5 RUB за **1** USD). У некоторых валют он будет отличен от 1 (например, 14.25 RUB за **1000** BYR). |
| Курс по умолчанию | Курс валюты, который будет использоваться при конвертации валют, если в форме "Курсы валют" другие курсы не заданы. |
| Базовая | Отметка о том, является ли валюта базовой. |
| Цифровой код | Трехзначный цифровой код валюты (см. международные обозначения валют). |
| Дата изменения | Дата и время изменения валюты. |
| Кем изменена | Имя пользователя, изменившего валюту. |
| Дата создания | Дата и время создания валюты. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх