# История профилей

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

[Список пользователей](/user_help/settings/users/user_admin.php)
[Создание и редактирование пользователя](/user_help/settings/users/user_edit.php)
[Группы пользователей](/user_help/settings/users/group_admin.php)
[Создание и редактирование группы пользователей](/user_help/settings/users/group_edit.php)
[Уровни доступа](/user_help/settings/users/task_admin.php)
[Создание и редактирование уровня доступа](/user_help/settings/users/task_edit.php)
[История профилей](/user_help/settings/users/profile_history.php)
[Устройства пользователей](/user_help/settings/users/user_devices.php)
[История входов](/user_help/settings/users/user_devices_history.php)
[Импорт пользователей](/user_help/settings/users/user_import.php)

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

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Пользователи](/user_help/settings/users/index.php)

История профилей

# История профилей

Страница **История профилей** (*Настройки > Пользователи > История профилей*) содержит список изменений профилей пользователей. Логирование изменений ведётся в только в том случае, если в [настройках главного модуля](/user_help/settings/settings/settings.php) отмечена опция **Сохранять историю изменения полей профиля пользователя**.

  

### Фильтр

Форма фильтра используется для фильтрации логов с изменениями профилей в соответствии с указанными условиями.

| Параметр | Описание |
| --- | --- |
| ID пользователя | Идентификатор пользователя. |
| Тип события | Определяется, какие события будут участвовать в поиске: добавление, изменение, удаление или все. |
| Дата добавления | Дата и время внесения изменений в профиль. |
| IP-адрес | Служит для отбора изменений профиля по IP-адресу, с которого они были внесены. |
| Браузер | Фильтрация по браузеру, с которого были внесены изменения в профиль. |
| URL страницы | Поле позволяет осуществить отбор изменений по адресу страницы, на которой они выполнялись. |
| Поле профиля | Служит для отбора пользователей по адресу электронной почты. |

Чтобы отобрать изменения профиля по заданным критериям поиска, нажмите на кнопку **Найти**. Для отображения всех изменений нажмите на кнопку **Отменить**.

### История изменений профиля

| Поле | Описание |
| --- | --- |
| ID | Идентификатор записи о внесенных изменениях в профиль. |
| Дата | Дата и время внесения изменений в профиль. |
| Пользователь | Указывается идентификатор и ФИО пользователя, информацию о котором добавили или изменили. Если пользователь был удален, то отображается лишь его идентификатор. |
| Событие | Указывается тип события, который был осуществлен с информацией профиля пользователя. |
| Кто изменил | Идентификатор и ФИО пользователя, выполнившего изменения. |
| Что изменено | Отображается информация по полям, в которые вносились изменения. |
| IP-адрес | IP-адрес, с которого были внесены изменения в профиль. |
| Браузер | Браузер, с которого были внесены изменения в профиль. |
| URL страницы | Отображается адрес страницы, на которой выполнялись изменения профиля. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх