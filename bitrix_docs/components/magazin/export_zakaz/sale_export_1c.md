# Экспорт заказов в "1С:Предприятие"

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

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Аффилиаты](/user_help/components/magazin/affiliates/index.php)

[Корзина](/user_help/components/magazin/basket/index.php)

[Процедура заказа](/user_help/components/magazin/zakaz/index.php)

[Рекомендуемые товары](/user_help/components/magazin/recommended/index.php)

[Список профилей текущего пользователя](/user_help/components/magazin/profiles/index.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

[Экспорт заказов в "1С:Предприятие"](/user_help/components/magazin/export_zakaz/sale_export_1c.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

Экспорт заказов в "1С:Предприятие"

**Недоступно в редакциях:**Стандарт, Старт

# Экспорт заказов в "1С:Предприятие"

### Описание **sale.export.1c**

Компонент служит для экспорта заказов в "1С:Предприятие" в формате CommerceML v2. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Экспорт заказов > Экспорт заказов в "1С:Предприятие"*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Сайт, заказы которого выгружать в "1С:Предприятие" | **SITE\_LIST** | Указывается сайт(ы), заказы которого(ых) будут выгружены. Привязка может производиться либо к текущему сайту, либо к одному определённому сайту из имеющихся в системе. |
| Создавать новые заказы и контрагенты из 1С | **IMPORT\_NEW\_ORDERS** | Y|N] При отмеченной опции новые заказы и контрагенты из 1С будут добавляться на сайт при выполнении процедуры обмена заказами. |
| Сайт, на который добавлять новые заказы и контрагенты | **SITE\_NEW\_ORDERS** | Указываются сайты, на которые будут добавляться новые заказы и контрагенты. |
| Выгружать только оплаченные заказы | **EXPORT\_PAYED\_ORDERS** | [Y|N] При отмеченной опции будут выгружаться только оплаченные заказы. |
| Выгружать только заказы c разрешенной доставкой | **EXPORT\_ALLOW\_DELIVERY\_ORDERS** | [Y|N] При отмеченной опции будут выгружаться только заказы c разрешенной доставкой. |
| Менять статусы заказов по информации из 1С | **CHANGE\_STATUS\_FROM\_1C** | [Y|N] При отмеченной опции статусы заказов на сайте будут изменяться в соответствии с данными из 1С (т.е. изменяется статус заказа в 1С и после выполнения обмена данными статус заказа на сайте будет изменен на тот, который был задан в 1С). |
| Выгружать заказы начиная со статуса | **EXPORT\_FINAL\_ORDERS** | Указывается статус, начиная с которого будут выгружаться товары:  * **N** - **Принят**; * **F** - **Выполнен**. |
| Заменять валюту при выгрузке в "1С:Предприятие" на | **REPLACE\_CURRENCY** | При выгрузке валюта товаров будет заменена на указанную. Конвертация при этом не происходит. |
| Группы пользователей, которым разрешена выгрузка | **GROUP\_PERMISSIONS** | Указывается группа(-ы), пользователи которых имеют права на выгрузку заказов в 1С. |
| Использовать сжатие zip, если доступно | **USE\_ZIP** | [Y|N] При отмеченной опции данные сжимаются ZIP форматом (если доступно). Это позволяет заметно уменьшить размер файлов. |
| Интервал одного шага в секундах (0 - выполнять загрузку за один шаг) | **INTERVAL** | Указывается интервал одного шага в секундах при экспорте заказов в 1С. **0** - выполнять загрузку за один шаг. |
| Размер единовременно загружаемой части файла (в байтах) | **FILE\_SIZE\_LIMIT** | Указывается размер единовременно загружаемой части файла в байтах. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sale.export.1c","",Array(
		"SITE_LIST" => "s1",
		"IMPORT_NEW_ORDERS" => "N",
		"SITE_NEW_ORDERS" => "",
		"CHANGE_STATUS_FROM_1C" => "N",
		"EXPORT_PAYED_ORDERS" => "Y",
		"EXPORT_ALLOW_DELIVERY_ORDERS" => "Y",
		"EXPORT_FINAL_ORDERS" => "N",
		"REPLACE_CURRENCY" => "руб.",
		"GROUP_PERMISSIONS" => Array("1"),
		"USE_ZIP" => "Y",
		"INTERVAL" => "30",
		"FILE_SIZE_LIMIT" => "204800"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх