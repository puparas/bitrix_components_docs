# Облачные хранилища

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

[Облачные хранилища](/user_help/settings/clouds/clouds_storage_list.php)
[Создание/редактирование подключения к облачному хранилищу](/user_help/settings/clouds/clouds_storage_edit.php)

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

Облачные хранилища

# Облачные хранилища

### Контекстная панель

Страница **Облачные хранилища** (*Настройки > Облачные хранилища*) содержит информацию о существующих облачных хранилищах, позволяет подключать новые контейнеры для хранения файлов и управлять текущими.

| Кнопка | Описание |
| --- | --- |
| Добавить | Переход к форме [создания нового подключения к облачному хранилищу](/user_help/settings/clouds/clouds_storage_edit.php). |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

### Список облачных хранилищ

| Поле | Описание |
| --- | --- |
| Меню действий | Доступные действия:  * **Изменить** - переход к форме [редактирования подключения к облачному хранилищу](/user_help/settings/clouds/clouds_storage_edit.php); * **Переместить файлы в облачное хранилище** - перенос файлов с локального хранилища (хостинг, на котором расположен проект) в облачное согласно установленным правилам (задается в форме [редактирования подключения к облачному хранилищу](/user_help/settings/clouds/clouds_storage_edit.php)); * **Вернуть файлы из облачного хранилища** - перенос файлов из облачного хранилища в локальное (хостинг, на котором расположен проект); * **Оценить объём и количество дубликатов** - выполнить поиск дубликатов файлов в облачном хранилище. По окончании поиск будет выведено сообщение с количеством дубликатов и занимаемом ими объёме с возможностью перехода к детальному [списку дубликатов](https://dev.1c-bitrix.ru/user_help/settings/clouds/clouds_storage_list.php#dublicates). Доступно с версии **22.0.0** модуля Облачные хранилища; * **Деактивировать** - перевод контейнера облачного хранилища в неактивное состояние. В этом случае данные будут доступны для чтения, но запись будет невозможна; * **Удалить** - удаление подключения к облачному хранилищу. |
| Сортировка Индекс сортировки. | |
| ID | Идентификатор контейнера. |
| Активность | Признак активности контейнера облачного хранилища. |
| Файлов | Количество файлов в контейнере. |
| Объем | Объем данных в контейнере облачного хранилища. |
| Режим | Режим работы контейнера (чтение/запись). |
| Сервис | Поставщик услуг облачного хранения. |
| Контейнер | Название контейнера, в котором хранятся файлы. |

### Список дубликатов файлов

Страница открывается при нажатии на ссылку список в результатах действия **Оценить объём и количество дубликатов**.

  

**Контекстная панель**.

| Кнопка | Описание |
| --- | --- |
| Обработать всё | Кнопка на контекстной панели, по нажатии на которую будут удалены все дубликаты, найденные в контейнере Облачного хранилища. |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |

  

**Список дубликатов**.

| Поле | Описание |
| --- | --- |
| Меню действий | Доступные действия:  * **Обработать** - будут удалены дубликаты только для выбранной строки. |
| Контрольная сумма | Контрольная сумма файла. |
| Размер файла | Размер одного файла. |
| Файлов | Количество файлов с одинаковой контрольной суммой. |
| Файлы | Список файлов в виде ссылок. По нажатии на ссылку открывается файл. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **haner** 18.03.2012 23:09:41 |
| --- |
| В дополнение к документации: <http://dev.1c-bitrix.ru/community/webdev/user/68564/blog/delaem-krasivye-ssylki-na-fayly-v-clodo/> |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх