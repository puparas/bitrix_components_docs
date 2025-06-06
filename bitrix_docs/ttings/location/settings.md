# Адреса и местоположения. Настройки модуля

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

[Адреса и местоположения. Настройки модуля](/user_help/settings/location/settings.php)

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

[Инструменты](/user_help/settings/utilities/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Адреса и местоположения](/user_help/settings/location/index.php)

Адреса и местоположения. Настройки модуля

# Адреса и местоположения. Настройки модуля

Закладки

Настройки модуля **Адреса и местоположения** располагаются по пути: *Настройки > Настройки продукта > Настройки модулей > Адреса и местоположения*.

  

### Настройки

Закладка предназначена для настройки общих параметров модуля.

| Поле | Описание |
| --- | --- |
| Формат адреса | Выбирается национальный формат адреса из списка. Список постоянно пополняется и расширяется новыми форматами. |
| Уровень журналирования | Выбирается один из уровней журналирования:  * Ошибки * Информация * Отладка * нет |

### Источники

Закладка позволяет настроить источники местоположений.

| Поле | Описание |
| --- | --- |
| Google | |
| Ключ с правами на Google Maps JavaScript API, Places API, Geocoding API для использования в браузере пользователя | Введите ключ API с соответствующими правами, полученный на Google Maps Platform    **Google Maps Platform** – это набор API и библиотек для размещения карт Google на вашем сайте, в приложении для Android и iOs, а также во внутренних системах компании, например CRM и ERP.   [Подробнее...](https://cloud.google.com/maps-platform/) . Подробная инструкция по получению ключей приведена в Пользовательской документации    Чтобы в поле «Адрес» в реквизитах компаний автоматически выводились подсказки от Google или чтобы можно было указывать адрес непосредственно на карте понадобится 2 ключа.  [Подробнее...](https://dev.1c-bitrix.ru/user_help/components/content/google_maps/map_google_key.php) . **Примечание**: Смотрите дополнительную информацию о том, как получить ключ, [в документации Google](https://developers.google.com/maps/documentation/javascript/get-api-key). |
| Ключ с правами на Google Places API, Geocoding API для использования на сервере | Введите ключ API с соответствующими правами, полученный на Google Maps Platform    **Google Maps Platform** – это набор API и библиотек для размещения карт Google на вашем сайте, в приложении для Android и iOs, а также во внутренних системах компании, например CRM и ERP.   [Подробнее...](https://cloud.google.com/maps-platform/) . Подробная инструкция по получению ключей приведена в Пользовательской документации    Чтобы в поле «Адрес» в реквизитах компаний автоматически выводились подсказки от Google или чтобы можно было указывать адрес непосредственно на карте понадобится 2 ключа.  [Подробнее...](https://dev.1c-bitrix.ru/user_help/components/content/google_maps/map_google_key.php) . **Примечание**: Смотрите дополнительную информацию о том, как получить ключ, [в документации Google](https://developers.google.com/maps/documentation/javascript/get-api-key). |
| Показывать фотографии мест при показе карты | Если опция отмечена, то при показе карты будут отображаться фотографии мест. **Внимание!** За использование этой опции Google может взимать дополнительную плату. |
| Показывать карту для нераспознанных адресов | Если опция отмечена, то карта будет отображаться для нераспознанных адресов. **Внимание!** За использование этой опции Google может взимать дополнительную плату. |

### Доступ

Закладка позволяет настроить права на доступ к модулю для всех имеющихся в системе групп пользователей.

| Поле | Описание |
| --- | --- |
| По умолчанию | Уровень доступа групп пользователей, для которых установлено право "по умолчанию". |
| [группа\_пользователей] | Изменение настроек доступа для конкретной группы. Возможно назначение следующих прав доступа к модулю **Адреса и местоположения**:  * **[D] закрыт** - запрет на доступ; * **[R] просмотр всех данных модуля** - разрешается только просмотр всех данных модуля; * **[W] запись** - полный доступ к ресурсам модуля. |
| Добавить право доступа | Ссылка, позволяющая добавить дополнительное право доступа для группы пользователей. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх