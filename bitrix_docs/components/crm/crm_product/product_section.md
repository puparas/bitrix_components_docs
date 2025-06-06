# Список разделов

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

[Дела](/user_help/components/crm/crm_activity/index.php)

[Компании](/user_help/components/crm/crm_company/index.php)

[Контакты](/user_help/components/crm/crm.contact/index.php)

[Лиды](/user_help/components/crm/crm_lead/index.php)

[Настройки](/user_help/components/crm/crm_config/index.php)

[Предложения](/user_help/components/crm/crm_quote/index.php)

[Реквизиты](/user_help/components/crm/crm_requisite/index.php)

[Сделки](/user_help/components/crm/crm_deal/index.php)

[Счета](/user_help/components/crm/crm_invoice/index.php)

[Товары](/user_help/components/crm/crm_product/index.php)

[Товары](/user_help/components/crm/crm_product/crm_product.php)
[Список товаров](/user_help/components/crm/crm_product/product_list.php)
[Редактирование товара](/user_help/components/crm/crm_product/product_edit.php)
[Просмотр товара](/user_help/components/crm/crm_product/product_show.php)
[Список разделов](/user_help/components/crm/crm_product/product_section.php)
[Туллбар](/user_help/components/crm/crm_product/product_menu.php)

[Просмотр событий](/user_help/components/crm/event_view.php)
[Отчеты (комплексный компонент)](/user_help/components/crm/crm_report.php)
[Просмотр событий счета](/user_help/components/crm/invoice_events.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Товары](/user_help/components/crm/crm_product/index.php)

Список разделов

# Список разделов

### Описание **crm.product.section.list**

Одностраничный компонент, необходим для управления списком разделов выбранного каталога. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *CRM > Товары > Список разделов*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Количество разделов на странице по умолчанию | **SECTION\_COUNT** | Максимальное число выводимых на одну страницу разделов. |
| Торговый каталог | **CATALOG\_ID** | Указывается каталог, разделы которого будут показаны на странице. |
| Раздел | **SECTION\_ID** | Указывается раздел, входящие разделы которого следует вывести. В случае, если оставить данный параметр неуказанным, то будут показаны разделы первого уровня. |
| Имя переменной идентификатора раздела | **SECTION\_ID\_PARAM** | Указывается имя переменной, в которой будет содержаться идентификатор раздела. |
| Шаблон пути к странице списка разделов | **PATH\_TO\_SECTION\_LIST** | Указывается путь к странице с перечнем разделов выбранного каталога. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
"bitrix:crm.product.section.list",
	"",
	Array(
		"SECTION_COUNT" => "20",
		"CATALOG_ID" => "33",
		"SECTION_ID" => "",
		"SECTION_ID_PARAM" => "section_id",
		"PATH_TO_SECTION_LIST" => "?section_id=#section_id#&sections"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх