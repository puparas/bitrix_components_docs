# Список резервных копий

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

[Инструменты](/user_help/settings/utilities/index.php)

[Проверка системы](/user_help/settings/utilities/site_checker.php)
[Монитор качества](/user_help/settings/utilities/checklist.php)
[SQL запрос](/user_help/settings/utilities/sql.php)
[Командная PHP строка](/user_help/settings/utilities/php_command_line.php)

[Резервное копирование](/user_help/settings/utilities/dump/index.php)

[Резервное копирование](/user_help/settings/utilities/dump/dump.php)
[Список резервных копий](/user_help/settings/utilities/dump/dump_list.php)
[Регулярное резервное копирование](/user_help/settings/utilities/dump/dump_auto.php)

[Диагностика](/user_help/settings/utilities/php_settings/index.php)

[Журнал событий](/user_help/settings/utilities/event_log/index.php)

[Монитор производительности](/user_help/settings/perfmon/index.php)

[ЧатБоты (КП)](/user_help/settings/imbot/index.php)

[Компрессия](/user_help/settings/compression/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Настройки](/user_help/settings/index.php)

[Инструменты](/user_help/settings/utilities/index.php)

[Резервное копирование](/user_help/settings/utilities/dump/index.php)

Список резервных копий

# Список резервных копий

#### Список резервных копий

Список резервных копий размещается на отдельной странице *Настройки > Инструменты > Резервное копирование > Список резервных копий*

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Создать резервную копию | Запуск процесса резервного копирования с переходом на страницу **Создание резервной копии**. |
| Автоматическое создание | Переход на страницу настроек автоматического резервного копирования. |

| Поле | Описание |
| --- | --- |
| Колонка флажков | Поле предназначено для выбора файлов архива, к которым предполагается применить какое-либо правило или действие. |
| Действие | Действия над файлами архива (зависит от места размещения):  * **Скачать** - скачивание файла на локальный компьютер (доступно при размещении локально или в стороннем облачном хранилище); * **Получить ссылку для переноса** - используется при восстановлении данных с помощью **restore.php** (доступно при размещении локально или в стороннем облачном хранилище); * **Восстановить** - восстановление архива (доступно при размещении локально или в облачном хранилище 1С-Битрикс); * **Отправить в облако "имя\_облака"** - перенос файла в выбранное облачное хранилище (только для локального хранения); * **Переименовать** - смена имена файла (доступно при размещении локально или в стороннем облачном хранилище); * **Удалить** - удаление файла (доступно при размещении локально или в стороннем облачном хранилище). |
| Имя | Имя файла архива. |
| Размер архива | Размер файла, указанный в мегабайтах. |
| Размещение | Указание где размещён архив. |
| Изменен | Дата и время изменения файла. |

С помощью ссылки **Скачать**, расположенной на данной странице после таблицы со списком резервных копий, вы можете скачать скрипт восстановления **restore.php**.

**Примечание**. Список резервных копий размещённых в облаке 1С-Битрикс отображается и в разделе Облако 1С-Битрикс.

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх