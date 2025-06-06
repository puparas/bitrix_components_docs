# Панель инструментов

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

[Компании (комплексный компонент)](/user_help/components/crm/crm_company/crm_company.php)
[Панель инструментов](/user_help/components/crm/crm_company/crm_company_menu.php)
[Просмотр компании](/user_help/components/crm/crm_company/crm_company_view.php)
[Редактирование компании](/user_help/components/crm/crm_company/crm_company_edit.php)
[Список компаний](/user_help/components/crm/crm_company/crm_company_list.php)

[Контакты](/user_help/components/crm/crm.contact/index.php)

[Лиды](/user_help/components/crm/crm_lead/index.php)

[Настройки](/user_help/components/crm/crm_config/index.php)

[Предложения](/user_help/components/crm/crm_quote/index.php)

[Реквизиты](/user_help/components/crm/crm_requisite/index.php)

[Сделки](/user_help/components/crm/crm_deal/index.php)

[Счета](/user_help/components/crm/crm_invoice/index.php)

[Товары](/user_help/components/crm/crm_product/index.php)

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

[Компании](/user_help/components/crm/crm_company/index.php)

Панель инструментов

# Панель инструментов

### Описание **crm.company.menu**

Одностраничный компонент, позволяет настроить контентное меню сущности.

В визуальном редакторе компонент расположен по пути *CRM > Компании > Панель инструментов*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID компании | **ELEMENT\_ID** | Поле содержит код, в котором передается идентификатор компании. |
| Вид отображения меню | **TYPE** | Выбирается функционал для представления в контентном меню. Возможны четыре варианта:  * **LIST** - выводятся кнопки **Список компаний**, **Добавить компанию**; * **SHOW** - выводятся кнопки **Список компаний**, **Добавить компанию**; * **EDIT** - выводятся кнопки **Список компаний**, **Добавить компанию**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
"bitrix:crm.company.menu",
	"",
	Array(
		"ELEMENT_ID" => $_REQUEST["company_id"],
		"TYPE" => "show"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх