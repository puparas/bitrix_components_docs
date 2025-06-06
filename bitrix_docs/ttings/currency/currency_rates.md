# Курсы валют

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

Курсы валют

**Недоступно в редакциях:**Стандарт, Старт

# Курсы валют

Форма **Курсы валют** (*Настройки > Валюты > Курсы валют*) служит для управления курсами валют. С помощью этой формы вы легко можете поддерживать список курсов валют на все интересующие вас даты. То есть, вы можете вести своего рода дневник курсов валют. Эта информация может пригодиться вам в дальнейшем, например, при обзоре заказов, сделанных в магазине за определённый период.

При конвертации валют на текущую дату система берет самый новый из курсов. Если курс не найден, то берется курс по умолчанию (из формы [Валюты](/user_help/settings/currency/currency.php)).

  

### Фильтр

Поля формы служат для задания параметров поиска интересующих вас курсов валют.

| Поле | Описание |
| --- | --- |
| Дата | Диапазон дат, курсы на которые следует показать. Вы можете выбрать либо количество дней от текущей даты, либо установить диапазон дат с помощью календарей.   Данное поле отображается, даже если фильтр свернут. |
| Валюта | Определяет, выводить ли все курсы валют в списке или только курсы выбранной валюты. |

Для того чтобы отобрать курсы валют по заданным критериям поиска, нажмите кнопку "Найти". Для отображения всех курсов нажмите кнопку "Отменить".

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Создать курс валют | Переход к форме [создания](/user_help/settings/currency/currency_rates_edit.php) нового курса валюты. |
| Настроить | Позволяет перейти к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в **MS Excel**. |

### Список курсов валют

| Поле | Описание |
| --- | --- |
| Колонка флажков | Поле предназначено для выбора курсов валют, к которым предполагается применить какое-либо правило или действие. |
| Действия | Действия над курсом валюты:  * **Изменить**- [редактирование](/user_help/settings/currency/currency_rates_edit.php) курса валюты; * **Удалить**- удаление курса валюты. |
| Валюта | Валюта, для которой установлен курс. |
| Дата | Дата, на которую установлен данный курс. |
| Номинал | Единица измерения валюты (см. [Валюты](/user_help/settings/currency/currency.php)) |
| Курс | Обменный курс данной валюты по отношению к базовой валюте. |

### Смотрите также

* [Курсы валют (учебный курс "Администратор. Бизнес")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=3164)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх