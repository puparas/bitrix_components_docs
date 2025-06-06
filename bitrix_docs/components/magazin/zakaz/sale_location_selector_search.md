# Привязка к местоположению: строка поиска

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

[Смена способа оплаты](/user_help/components/magazin/zakaz/sale_order_payment_change.php)
[Калькулятор доставки (AJAX)](/user_help/components/magazin/zakaz/sale_ajax_delivery_calculator.php)
[Оформление заказа](/user_help/components/magazin/zakaz/sale_order_ajax.php)
[Подключение обработчика результата платежной системы](/user_help/components/magazin/zakaz/sale_order_payment_receive.php)
[Подключение платежной системы](/user_help/components/magazin/zakaz/sale_order_payment.php)
[Привязка к местоположению: выпадающие списки](/user_help/components/magazin/zakaz/sale_location_selector_steps.php)
[Привязка к местоположению: строка поиска](/user_help/components/magazin/zakaz/sale_location_selector_search.php)

[Рекомендуемые товары](/user_help/components/magazin/recommended/index.php)

[Список профилей текущего пользователя](/user_help/components/magazin/profiles/index.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Процедура заказа](/user_help/components/magazin/zakaz/index.php)

Привязка к местоположению: строка поиска

**Недоступно в редакциях:**Стандарт, Старт

# Привязка к местоположению: строка поиска

### Описание **sale.location.selector.search**

Компонент выводит форму, в которой выбор местоположения осуществляется с помощью ввода запроса в строку поиска. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Процедура оформления заказа > Привязка к местоположению: строка поиска*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

**Важно!** Компонент используется только при работе с местоположениями версии **2.0**.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID местоположения | **ID** | Идентификатор местоположения, которое должно быть отображено в форме. Можно не задавать, если задан **Символьный код местоположения**. |
| Символьный код местоположения | **CODE** | Символьный код местоположения, которое должно быть отображено в форме. Можно не задавать, если задан **ID местоположения**. |
| Имя поля ввода | **INPUT\_NAME** | Задается название переменной для имени поля ввода. |
| Сохранять связь через | **PROVIDE\_LINK\_BY** | Указывается, что необходимо записать в форму ввода при выборе местоположения: идентификатор (id) или символьный код (code). |
| **Источник данных** | | |
| Фильтровать по сайту | **FILTER\_BY\_SITE** | [Y|N] При отмеченной опции поиск местоположений осуществляется только среди тех, которые привязаны к сайту. |
| Отображать местоположения по-умолчанию | **SHOW\_DEFAULT\_LOCATIONS** | [Y|N] При отмеченной опции вверху формы поиска будут отображены избранные местоположения. |
| Cайт | **FILTER\_SITE\_ID** | Указывается сайт, по местоположениям которого будет делаться выборка. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Идентификатор javascript-контрола | **JSCONTROL\_GLOBAL\_ID** | Системный параметр. Не описывается. |
| Javascript-функция обратного вызова | **JS\_CALLBACK** | Системный параметр. Не описывается. |
| Не показывать ошибки, если они возникли при загрузке компонента | **SUPPRESS\_ERRORS** | [Y|N] При отмеченной опции ошибки, возникающие при загрузке компонента, отображаться не будут. |
| Инициализировать компонент только при наступлении указанного javascript-события на объекте window.document | **INITIALIZE\_BY\_GLOBAL\_EVENT** | Название javascript-события, при наступлении которого будет инициализироваться компонент. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.location.selector.search",
	"",
	Array(
		"COMPONENT_TEMPLATE" => ".default",
		"ID" => "980",
		"CODE" => "",
		"INPUT_NAME" => "LOCATION",
		"PROVIDE_LINK_BY" => "id",
		"JSCONTROL_GLOBAL_ID" => "",
		"JS_CALLBACK" => "",
		"FILTER_BY_SITE" => "Y",
		"SHOW_DEFAULT_LOCATIONS" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000000",
		"FILTER_SITE_ID" => "s1",
		"INITIALIZE_BY_GLOBAL_EVENT" => "",
		"SUPPRESS_ERRORS" => "N"	
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх