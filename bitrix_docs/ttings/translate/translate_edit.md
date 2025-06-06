# Перевод сообщений

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

[Перевод. Настройки модуля](/user_help/settings/translate/settings.php)
[Просмотр файлов](/user_help/settings/translate/translate_list.php)
[Перевод сообщений](/user_help/settings/translate/translate_edit.php)
[Выгрузка и загрузка](/user_help/settings/translate/translate_collector.php)

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

[Перевод](/user_help/settings/translate/index.php)

Перевод сообщений

# Перевод сообщений

На странице **Перевод сообщений** (*Настройки > Локализация > Просмотр файлов* и открыт некоторый файл) показаны языковые сообщения для языков, загруженных в систему. Вы можете редактировать языковые сообщения для показанных языков, а также удалять сообщения, установив флаг **удалить**.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Путь к файлу | При нажатии на имя папки происходит переход к списку файлов языковых сообщений в этой папке. |
| Показать все сообщения | Отображать все сообщения. |
| Показать только непереведенные | Отображать только непереведенные сообщения. |
| Показать PHP код | Переход на страницу перевода с показом ее PHP-кода. |
| Редактировать PHP | Переход к редактированию PHP-кода страницы перевода. |
| Выгрузить сообщения в CSV | Выгрузка сообщений языкового файла в формате CSV. |

### Форма "Перевод сообщений"

| Поле | Описание |
| --- | --- |
| Имя файла | Имя файла языковых сообщений. |
| Полный путь | Полный путь к файлу. |
| Всего сообщений | Количество языковых сообщений в файле. |
| Количество фраз | Общее количество сообщений для каждого языка, а также количество непереведенных (при наличии). |
| Список сообщений | |
| ID | Идентификатор языкового сообщения. |
| Удалить | Чтобы удалить языковое сообщение, установите флаг в это поле и нажмите кнопку **Применить**. |
| [язык] | Текст языкового сообщения для каждого языка.    В исходных строках сообщений возможно наличие шаблонов вида "**#ID#**", "**#COUNT#**". Если в оригинале подобные шаблоны присутствуют, в переводе их также необходимо сохранить. В момент использования данного сообщения шаблон будет заменен на конкретное значение. |
| Удалить сообщения | Доступны на выбор два варианта:  * **Удалить все сообщения** - будут удалены все сообщения в файле; * **Удалить сообщения, перевод которых отсутствует для текущего языка** - будут удалены только те сообщения, перевод у которых отсутствует для текущего языка (установленного в интерфейсе).  Для применения выбранного действия нажмите кнопку **Применить**. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх