# Перевод. Настройки модуля

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

Перевод. Настройки модуля

# Перевод. Настройки модуля

Закладки

Форма настроек модуля **Перевод** (*Настройки > Настройки продукта > Настройки модулей > Перевод*) предназначена для задания общесистемных параметров модуля.

  

### Настройки

| Поле | Описание |
| --- | --- |
| Ограничить области перевода | Указываются пути к папкам    papka_vib0.png через запятую, с которыми разрешено работать через модуль. Это позволяет начинать просмотр файлов сразу из указанной папки    papka_vib.png , а не от корня сайта, то есть без лишних переходов по папкам открывать просмотр в нужной папке. |
| Добавить на панель инструментов кнопку "Выводить языковые файлы" | При отмеченной опции на панель инструментов будет выведена кнопка **Переводы**. При выборе пункта меню **Выводить языковые файлы** кнопки **Переводы** внизу страницы сайта будут выведены адреса всех языковых файлов, используемых на данной странице. |
| Делать резервную копию редактируемых файлов | При отмеченной опции при изменении файла перевода будет создаваться его резервная копия. |
| Папка для резервных копии редактируемых файлов | Указывается папка, в которой будут храниться резервные копии редактируемых файлов. |
| Сортировать фразы в языковом файле при сохранении по кодам фраз | Поле предназначено для разработчиков.  При отмеченной опции фразы в языковом файле сортируются при сохранении по кодам фраз    **Языковое сообщение** - группа фраз на разных языках, имеющая один смысл. Список сообщений в файле хранится в следующем виде:    Подробнее в курсе [Разработчик Bitrix Framework](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=43&LESSON_ID=3396&LESSON_PATH=3913.4564.4926.3396#example_file). . |
| Не выполнять сортировку фраз для языков | Выбираются языки, для которых не требуется выполнять сортировку фраз (для выбора нескольких языков необходимо зажать кнопку Ctrl). Функция работает совместно с **Сортировать фразы в языковом файле при сохранении по кодам фраз**. |
| Символ разделитель полей в экспортируемых CSV файлах | Выбор символа разделителя полей в файлах CSV при экспорте. |
| Папка для экспортируемых файлов | Указывается, куда будут складироваться собранные языковые пакеты (tar.gz). |

### Доступ

| Поле | Описание |
| --- | --- |
| По умолчанию | Уровень доступа групп пользователей, для которых установлено право **по умолчанию**. |
| [группа\_пользователей] | Изменение настроек доступа для конкретной группы. Возможно назначение следующих прав доступа к модулю **Перевод**:  * **[D] закрыт** - запрет на доступ; * **[R] просмотр всех данных модуля** - разрешается только просмотр всех данных модуля; * **[W] запись** - полный доступ к ресурсам модуля. |
| Добавить право доступа | Ссылка, позволяющая добавить дополнительное право доступа для группы пользователей. |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх