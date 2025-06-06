# Коннекторы для внешних мессенджеров (КП). Настройки модуля

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

[Коннекторы для внешних мессенджеров (КП). Настройки модуля](/user_help/settings/imconnector/settings.php)

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

[Коннекторы для внешних мессенджеров (КП)](/user_help/settings/imconnector/index.php)

Коннекторы для внешних мессенджеров (КП). Настройки модуля

# Коннекторы для внешних мессенджеров (КП). Настройки модуля

<!--
<h4 id="topictoctitle">В этом разделе
- [Закладка "Настройки коннекторов мессенджеров"](#option)
- [Кнопки управления](#buttons)
--!>

Форма настроек модуля **Коннекторы для внешних мессенджеров** (*Настройки > Настройки продукта > Настройки модулей > Коннекторы для внешних мессенджеров*) предназначена для задания параметров модуля.

#### Закладка Настройки коннекторов мессенджеров

Форма позволяет изменить публичный адрес для доступа к порталу, включить режим отладки и выбрать коннекторы.

| Поле | Описание |
| --- | --- |
| Публичный адрес сайта | Адрес, по которому будет обращаться внешний сервис к вашему порталу для вывода сообщений в открытую линию. Как правило, совпадает с реальным адресом портала. После соответствующих настроек роутера локальной сети может не совпадать с публичным адресом, но эти меры - крайность, в случае строгих требований по безопасности. |
| Включить режим отладки | Включает логирование работы модуля в файле `/bitrix/modules/imconnector_error.log`. **Примечание.** В файл пишется только лог ошибок, включать данную опцию имеет смысл только для отладки, лог трассировки сообщений в этот файл не пишется. |
| Разрешить поиск Открытых линий в Битрикс24.Network | Опция разрешает поиск Открытых линий в **Битрикс24.Network**. |
| Список используемых коннекторов | Выбираются коннекторы, которые будут использоваться для каналов открытых линий. По умолчанию включены все коннекторы. |

<!--
<a class="link" name="buttons">

#### Кнопки управления

| Кнопка | Описание |
| --- | --- |
| Применить | Сохранение параметров модуля. |
| По умолчанию | Сброс сделанных настроек до настроек по умолчанию. |

--!>

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх