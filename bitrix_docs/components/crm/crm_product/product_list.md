# Список товаров

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

Список товаров

# Список товаров

### Описание **crm.product.list**

Одностраничный компонент, необходим для вывода списка товаров системы CRM. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *CRM > Товары > Список товаров*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Количество товаров на странице по умолчанию | **PRODUCT\_COUNT** | Указывается максимальное число выводимых на одной странице товаров. |
| Торговый каталог | **CATALOG\_ID** | Указывается каталог, товары которого будут показаны. |
| Раздел | **SECTION\_ID** | При наличии таковой выбирается секция указанного торгового каталога. |
| Шаблон пути к странице списка товаров | **PATH\_TO\_PRODUCT\_LIST** | Указывается путь к странице с перечнем товаров. |
  
| Шаблон пути к странице просмотра товара | **PATH\_TO\_PRODUCT\_SHOW** | Указывается путь к странице детального просмотра товара. |
| Шаблон пути к странице редактирования товара | **PATH\_TO\_PRODUCT\_EDIT** | Указывается путь к странице редактирования товара. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
"bitrix:crm.product.list",
	"",
	Array(
		"PRODUCT_COUNT" => "20",
		"CATALOG_ID" => "33",
		"SECTION_ID" => "0",
		"PATH_TO_PRODUCT_LIST" => "?section_id=#section_id#",
		"PATH_TO_PRODUCT_SHOW" => "?product_id=#product_id#&show",
		"PATH_TO_PRODUCT_EDIT" => "?product_id=#product_id#&edit"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх