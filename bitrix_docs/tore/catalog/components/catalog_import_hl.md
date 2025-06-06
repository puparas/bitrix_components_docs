# Импорт в Highload-блоки

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

[Мастер магазина](/user_help/store/storeassist.php)

[Интернет-магазин](/user_help/store/sale/index.php)

[Торговый каталог](/user_help/store/catalog/index.php)

[Торговый каталог. Настройки модуля](/user_help/store/catalog/settings_catalog.php)
[Ввод цен - общая информация](/user_help/store/catalog/prices.php)

[Каталоги](/user_help/store/catalog/products/index.php)

[Складской учет](/user_help/store/catalog/warehouse/index.php)

[Компоненты](/user_help/store/catalog/components/index.php)

[Импорт в Highload-блоки](/user_help/store/catalog/components/catalog_import_hl.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Магазин](/user_help/store/index.php)

[Торговый каталог](/user_help/store/catalog/index.php)

[Компоненты](/user_help/store/catalog/components/index.php)

Импорт в Highload-блоки

**Недоступно в редакциях:**Стандарт, Старт

# Импорт в Highload-блоки

### Описание catalog.import.hl

**catalog.import.hl** - компонент импорта в хайлоаблоки. Используется при обмене с 1С для выгрузки на сайт справочников.

Компонент отсутствует в визуальном редакторе.

Компонент относится к модулю [Торговый каталог](/user_help/store/catalog/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| Желаемая максимальная длительность одного шага | **INTERVAL** | Указывается интервал одного шага в секундах при импорте каталога в систему. 0 - выполнять загрузку за один шаг. |
| Группы пользователей, которым разрешена загрузка | **GROUP\_PERMISSIONS** | Указывается группа(-ы) пользователей, которым разрешено экспортировать инфоблок через этот компонент. |
| Использование сжатия | **USE\_ZIP** | [Y|N] При отмеченной опции данные сжимаются ZIP форматом (если доступно). Это позволяет заметно уменьшить размер файлов. |
| Желаемый максимальный размер одного архива | **FILE\_SIZE\_LIMIT** | Указывается размер единовременно загружаемой части файла в байтах. Передаётся в 1С |
| Использование специального каталога | **USE\_TEMP\_DIR** | [Y|N] При отмеченной опции используется специальный каталог для временных файлов обмена. |

### Пример вызова

```
<?APPLICATION->IncludeComponent("bitrix:catalog.import.hl", "", Array(
        "INTERVAL" => COption::GetOptionString("catalog", "1C_INTERVAL", "-"),
        "GROUP_PERMISSIONS" => explode(",", COption::GetOptionString("catalog", "1C_GROUP_PERMISSIONS", "")),
        "FILE_SIZE_LIMIT" => COption::GetOptionString("catalog", "1C_FILE_SIZE_LIMIT", 200*1024),
        "USE_CRC" => COption::GetOptionString("catalog", "1C_USE_CRC", "Y"),
        "USE_ZIP" => COption::GetOptionString("catalog", "1C_USE_ZIP", "Y"),
        )
    );?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх