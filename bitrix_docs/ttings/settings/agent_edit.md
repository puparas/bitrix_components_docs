# Создание и редактирование агента

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

Создание и редактирование агента

# Создание и редактирование агента

На странице вы можете создать нового или изменить параметры существующего агента.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список агентов | Переход на страницу со [списком агентов](/user_help/settings/settings/agent_list.php). |
| Добавить | Переход на страницу с формой создания нового агента. **Кнопка отображается при редактировании существующего агента.** |
| Удалить агента | Удаление редактируемого агента. **Кнопка отображается при редактировании существующего агента.** |

### Закладка Агент

| Поле | Описание |
| --- | --- |
| Дата последнего запуска | Дата и время последнего запуска агента. **Поле отображается при редактировании существующего агента.** |
| \*Дата и время следующего запуска (DD.MM.YYYY HH:MI:SS) | Указывается дата и время следующего запуска агента. |
| Активен | При отмеченной опции агент будет активным. Если агент неактивен, то он не может быть запущен. |
| Модуль | Указывается название модуля, к которому относится агент. При отсутствии идентификатора модуля считается, что функция агента не принадлежит ни к одному из модулей. |
| \*Функция агента | Задается полное название функции агента. Если функция-агент не принадлежит ни одному из модулей, то ее необходимо разместить в файле **/bitrix/php\_interface/init.php**. Данный файл автоматически подключается в прологе. |
| ID пользователя | Задается идентификатор пользователя. Если пользователь не выбран, то владельцем агента является система. |
| Сортировка | Относительный "вес" агента. Чем меньше указанное число, тем выше в списке агентов будет показан данный агент. |
| Периодичность выполнения | Доступны два значения:  * **через заданный интервал** - при отмеченной опции агент будет вызываться первый раз в соответствии со значением поля **Дата и время следующего запуска**, время следующего запуска будет выставлено ровно через интервал, заданный в одноимённом поле ниже. * **точно в указанное время** - при отмеченной опции агент будет вызываться точно во время заданное в поле **Дата и время следующего запуска**. |
| Интервал (сек.) | Указывается интервал вызова агента в секундах. |

\* - поля, обязательные для заполнения.

### Смотрите также

* [Пример создания агента (учебный курс "Разработчик Bitrix Framework")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=2290)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх