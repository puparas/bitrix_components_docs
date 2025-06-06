# Конфигуратор валюты

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

Конфигуратор валюты

**Недоступно в редакциях:**Стандарт, Старт

# Конфигуратор валюты

Закладки

Форма служит для создания новой валюты. В отличие от [ручной формы](/user_help/settings/currency/currency_edit.php) создания валюты конфигуратор автоматически проставляет большую часть данных.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список | Переход на страницу со списком валют. |
|

### Поиск и основные настройки

  

| Поле | Описание |
| --- | --- |
| Поиск валюты | Поле для ввода названия валюты. При вводе в поле **Выбор валюты** ниже будут оставаться валюты, подходящие под условия поиска. |
| Выбор валюты | Список всех валют. Выбор валюты из списка автоматически заполняет неизменяемые поля в секции **Основные настройки валюты** и на закладке Языковые настрйоки. |
| Основные настройки валюты | |
| \*Курс обмена по умолчанию | Курс валюты, который будет использоваться при конвертации валюты, если в форме "Курсы валют" для данной валюты не задан другой курс. Для базовой валюты курс должен быть равен 1. Для остальных валют курс устанавливается относительно базовой валюты.   При создании валюты нужно узнать её текущий курс по отношению к базовой и проставить в данном окне.  Например, установите курс для RUB в 1, тогда курс для USD может быть равен 30.5, а для EUR - 34.2. Подробнее о курсах валют смотрите раздел помощи [Курсы валют](/user_help/settings/currency/currency_rates.php). |
 Индекс сортировки | Относительный "вес", влияющий на положение валюты в общем списке. |

\* - Поля, обязательные для заполнения.

### Языковые настройки

На закладке автоматически проставятся варианты настроек для каждого языка интерфейса, установленного в системе.

| Поле | Описание |
| --- | --- |
| В публичной части не показывать незначащие нули в дробной части цены | Простановка флажка в опция убирает в публичной части показ незначащих нулей у дробной части цены.    Если у вас цена 12500,00 рублей - будет отображено 12500, если у вас 12500,50 - будет отображено 12500,50 |

\* - Поля, обязательные для заполнения.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх