# Дела

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

[Дела](/user_help/components/crm/crm_activity/crm_activity.php)
[Список задач](/user_help/components/crm/crm_activity/task_list.php)
[Список звонков/встреч](/user_help/components/crm/crm_activity/activity_calendar_list.php)

[Компании](/user_help/components/crm/crm_company/index.php)

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

Дела

# Дела

### Описание **crm.activity**

Комплексный компонент, позволяет управлять списком дел.

В визуальном редакторе компонент расположен по пути *CRM > Дела > Дела*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - основная страница; |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| **Дополнительные настройки** | | |
| Формат имени | **NAME\_TEMPLATE** | Выбирается формат отображения имени. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent(
	"bitrix:crm.activity",
	"",
	Array(
		"NAME_TEMPLATE" => "",
		"SEF_MODE" => "N"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх