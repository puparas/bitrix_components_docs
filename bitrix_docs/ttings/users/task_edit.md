# Создание и редактирование уровня доступа

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

Создание и редактирование уровня доступа

# Создание и редактирование уровня доступа

Закладки

Форма создания/редактирования уровня доступа предназначена для настройки параметров существующего или вновь создаваемого уровня доступа. Также данная форма используется для просмотра параметров системных уровней доступа.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список уровней доступа | Переход на страницу со [списком уровней доступа](/user_help/settings/users/task_admin.php). |
| Добавить | Переход на страницу с формой создания нового уровня доступа. **Кнопка отображается при редактировании существующего уровня доступа.** |
| Копировать | Копирование редактируемого уровня доступа. **Кнопка отображается при редактировании существующего уровня доступа.** |
| Удалить | Удаление редактируемого уровня доступа. **Кнопка отображается при редактировании существующего уровня доступа.** |

### Параметры

На закладке выполняется настройка основных параметров уровня доступа.

| Поле | Описание |
| --- | --- |
| \*Название | Осмысленное название уровня доступа. |
| \*Модуль | Указывается модуль, к которому относится уровень доступа. |
| Системный | Отметка о том, что уровень является системным или нет. Проставляется автоматически. |
| Привязка | Выбирается привязка уровня доступа к функционалу модуля. Список привязок различается и зависит от выбранного модуля. |
| Буква | Буква уровня доступа. |
| Описание | Произвольное описание уровня. |

\* - поля, обязательные для заполнения.

### Включаемые операции

Закладка служит для настройки операций, которые возможно проводить, имея данный уровень доступа. Список операций меняется в зависимости от выбранного модуля и привязки на вкладке **Параметры**.

| Поле | Описание |
| --- | --- |
| [название операции] | Для возможности выполнения операций при этом уровне доступа необходимо, чтобы они были отмечены флагами. |

Функционал операций ясен из их названия. Но есть несколько операций главного модуля которые требуют пояснения:

* **Ограниченная модификация шаблонов (lpa\_template\_edit)** - редактирование шаблона, кроме php-кода в них.
* **Просмотр остальных настроек главного модуля (view\_other\_settings)** - просмотр настроек, кроме тех, которые связаны с php-кодом.
* **Редактирование остальных настроек главного модуля (edit\_other\_settings)** - редактирование настроек, кроме тех, которые связаны с php-кодом.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх