# Список правил обработки адресов

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

[AD/LDAP интеграция](/user_help/settings/ldap/index.php)

[Перевод](/user_help/settings/translate/index.php)

[XMPP сервер (КП)](/user_help/settings/xmpp/index.php)

[Настройки продукта (главный модуль)](/user_help/settings/settings/index.php)

[Настройки главного модуля](/user_help/settings/settings/settings.php)
[Модули](/user_help/settings/settings/module_admin.php)
[Автокеширование](/user_help/settings/settings/cache.php)
[Список мастеров](/user_help/settings/settings/wizard_list.php)
[Импорт мастера](/user_help/settings/settings/wizard_load.php)
[Пользовательские поля](/user_help/settings/settings/userfield_admin.php)
[Создание и редактирование пользовательского поля](/user_help/settings/settings/userfield_edit.php)
[CAPTCHA](/user_help/settings/settings/captcha.php)
[Агенты](/user_help/settings/settings/agent_list.php)
[Создание и редактирование агента](/user_help/settings/settings/agent_edit.php)
[Геолокация](/user_help/settings/settings/geoip_handlers_list.php)
[Соглашения и список согласий](/user_help/settings/settings/agreement_admin.php)
[Создание соглашения](/user_help/settings/settings/agreement_edit.php)

[Сайты](/user_help/settings/settings/sites/index.php)

[Языковые параметры](/user_help/settings/settings/lang_parametrs/index.php)

[Почтовые и СМС события](/user_help/settings/settings/mail_events/index.php)

[Обработка адресов](/user_help/settings/settings/urlrewrite/index.php)

[Список правил обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_list.php)
[Создание и редактирование правила обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_edit.php)
[Пересоздание правил обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_reindex.php)

[Интерфейс](/user_help/settings/settings/user_settings/index.php)

[Композитный сайт](/user_help/settings/settings/composite/index.php)

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Настройки продукта (главный модуль)](/user_help/settings/settings/index.php)

[Обработка адресов](/user_help/settings/settings/urlrewrite/index.php)

Список правил обработки адресов

# Список правил обработки адресов

Управление правилами преобразования адресов производится на странице **Обработка адресов** (*Настройки > Настройки продукта > Обработка адресов*).

Обработка адресов (**UrlRewrite**) применяется для того, чтобы скрипт мог отвечать не только по своему физическому, но и по любому другому указанному адресу. Например, можно задать такие настройки обработки адресов, что скрипт, лежащий в файле **/fld/c.php** и отвечающий по адресу **/fld/c.php?id=15** будет отвечать также по адресу **/catalog/15.php**.

Адрес, по которому будет отвечать скрипт, не должен физически существовать на сервере. Если такой адрес физически существует, то будет вызван скрипт по этому адресу. Система обработки адресов запущена в этом случае не будет.

  

### Фильтр

Форма фильтра используется для выбора из списка правил обработки в соответствии с указанными условиями. Нижеследующая таблица описывает параметры, по которым может выполняться поиск.

| Поле | Описание |
| --- | --- |
| Путь | Поиск правила по пути к файлу. |
| Сайт | Поиск правил для указанного сайта. |
| Условие | Поиск правил обработки адресов по условию применения. |
| Компонент | Поиск правил по полному имени компонента (*пространство\_имен:имя\_компонента*). |

Для того чтобы отобрать правила по заданным критериям поиска, нажмите кнопку **Найти**. Для отображения всех правил нажмите кнопку **Отменить**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Новая запись | Переход к [форме создания нового правила обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_edit.php). |
| Пересоздание | Переход к странице [Пересоздание правил обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_reindex.php). |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в формат MS Excel. |

### Список правил

| Поле | Описание |
| --- | --- |
| Колонка флажков | Поле предназначено для выбора правил, к которым предполагается применить какое-либо действие. |
| Действие | Действия над правилами:  * **Изменить** - переход к [форме редактирования правила обработки адресов](/user_help/settings/settings/urlrewrite/urlrewrite_edit.php); * **Удалить** - удаление правила обработки адресов. |
| Условие | Условие, по которому правило будет применено. |
| Компонент | Компонент, для которого работает правило обработки адресов. |
| Файл | Указывается путь к файлу, который будет отображен в результате обработки адреса. |
| Правило | Правило вызова страницы, путь к которой указан в поле **Файл**. |

### Смотрите также

* [Примеры правил (учебный курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=35&LESSON_ID=4901)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх