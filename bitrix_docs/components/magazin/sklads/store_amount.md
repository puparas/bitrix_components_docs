# Остатки по складам

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

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Склады (комплексный компонент)](/user_help/components/magazin/sklads/warehouse.php)
[Список складов](/user_help/components/magazin/sklads/store_list.php)
[Информация о складе](/user_help/components/magazin/sklads/store_detail.php)
[Остатки по складам](/user_help/components/magazin/sklads/store_amount.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

Остатки по складам

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Остатки по складам

### Описание **catalog.store.amount**

Компонент выводит остатки выбранного товара по складам, на которых он имеется.

В визуальном редакторе компонент расположен по пути *Магазин > Склады > Остатки по складам*.

Компонент относится к модулю [Торговый каталог](/user_help/store/catalog/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Склады | **STORES** | Выбираются склады, информация по которым должна быть показана. Для выбора нескольких значений следует воспользоваться клавишей Ctrl. |
| Товар | **ELEMENT\_ID** | Идентификатор товара, остатки по складам которого должны быть отображены. Можно не указывать, если задан **Код товара**. |
| Код товара | **ELEMENT\_CODE** | Символьный код товара, остатки по складам которого должны быть отображены. Можно не указывать, если задан идентификатор в поле **Товар**. |
| Торговое предложение | **OFFER\_ID** | Идентификатор торгового предложения, остатки по складам которого должны быть отображены. |
| **Шаблоны ссылок** | | |
| URL на страницу, где будет показана детальная информация о складе | **STORE\_PATH** | Адрес страницы с детальной информацией по складу. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Заголовок | **MAIN\_TITLE** | Указывается заголовок блока о количестве товара на складе. |
| **Склады** | | |
| Свойства | **USER\_FIELDS** | Выбираются пользовательские поля складов для отображения. С помощью клавиши Ctrl можно выбрать несколько значений. |
| Поля | **FIELDS** | Выбираются поля складов для отображения. С помощью клавиши Ctrl можно выбрать несколько значений. |
| Отображать склад при отсутствие на нем товара | **SHOW\_EMPTY\_STORE** | [Y|N] При отмеченной опции склад будет отображен, даже если на нем нет товара. |
| Показывать вместо точного количества информацию о достаточности | **USE\_MIN\_AMOUNT** | [Y|N] При отмеченной опции количество имеющегося на складе товара будет заменено на выражение "достаточно" или "мало". Кроме того, становится доступным для настройки параметр Минимальное достаточное количество товара на складе     |  |  |  | | --- | --- | --- | | Минимальное достаточное количество товара на складе | **MIN\_AMOUNT** | Указывается значение, меньше которого о количестве товара на складе будет отображаться выражение "мало". Если количество товара на складе больше, чем это значение, то на странице будет отображаться выражение "достаточно". |  . |
| Показывать общую информацию по складам | **SHOW\_GENERAL\_STORE\_INFORMATION** | [Y|N] При Y будет показана только общая информация по складам. При значении N дается информация по складам в отдельности (не общей суммой). |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:catalog.store.amount",
	"",
	Array(
		"STORES" => array(),
		"ELEMENT_ID" => "29",
		"ELEMENT_CODE" => "",
		"OFFER_ID" => "",
		"STORE_PATH" => "/store/store_detail.php",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000",
		"MAIN_TITLE" => "Наличие товара на складах",
		"USER_FIELDS" => array("",""),
		"FIELDS" => array("TITLE","ADDRESS","PHONE","SCHEDULE",""),
		"SHOW_EMPTY_STORE" => "Y",
		"USE_MIN_AMOUNT" => "Y",
		"SHOW_GENERAL_STORE_INFORMATION" => "N",
		"MIN_AMOUNT" => "0"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх