# Настройки пользовательских полей

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

[Настройка интеграции с "1С:Предприятие"](/user_help/components/crm/crm_config/crm_exchg1c.php)
[Настройка пользовательского поля](/user_help/components/crm/crm_config/crm_config_fields_edit.php)
[Настройка связей ролей](/user_help/components/crm/crm_config/config_perms.php)
[Настройки бизнес-процессов](/user_help/components/crm/crm_config/config_bp.php)
[Настройки пользовательских полей](/user_help/components/crm/crm_config/crm_config_fields.php)
[Настройки прав доступа (комплексный компонент)](/user_help/components/crm/crm_config/access_config.php)
[Настройки шаблонов реквизитов клиентов](/user_help/components/crm/crm_config/crm_config_preset.php)
[Редактирование роли](/user_help/components/crm/crm_config/role_edit.php)
[Редактирование шаблона бизнес-процесса](/user_help/components/crm/crm_config/bp_edit.php)
[Связь с магазином (комплексный компонент)](/user_help/components/crm/crm_config/external_sale.php)
[Список бизнес-процессов](/user_help/components/crm/crm_config/bp_list.php)
[Список неиспользуемых пользовательских полей](/user_help/components/crm/crm_config/crm_config_preset_ufields.php)
[Список пользовательских полей](/user_help/components/crm/crm_config/crm_config_fields_list.php)
[Список типов пользовательских полей](/user_help/components/crm/crm_config/crm_config_fields_types.php)
[Список типов шаблонов бизнес-процессов](/user_help/components/crm/crm_config/bp_types.php)
[Список шаблонов реквизитов клиентов](/user_help/components/crm/crm_config/crm_config_preset_list.php)

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

[Настройки](/user_help/components/crm/crm_config/index.php)

Настройки пользовательских полей

# Настройки пользовательских полей

### Описание **crm.config.fields**

Позволяет выполнить настройку пользовательских полей в модуле CRM. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *CRM > Настройки > Настройки пользовательских полей*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта): | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **ENTITY\_LIST\_URL** - страница списка типов; * **FIELDS\_LIST\_URL** - страница списка полей; * **FIELD\_EDIT\_URL** - страница редактирования поля. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
"bitrix:crm.config.fields",
	"",
	Array(
		"SEF_MODE" => "Y",
		"SEF_FOLDER" => "/crm/configs/sendsave/",
		"SEF_URL_TEMPLATES" => Array(
			"ENTITY_LIST_URL" => "",
			"FIELDS_LIST_URL" => "#entity_id#/",
			"FIELD_EDIT_URL" => "#entity_id#/edit/#field_id#/"
		),
		"VARIABLE_ALIASES" => Array(
			"index" => Array(),
			"list" => Array(),
			"edit" => Array(),
			"show" => Array(),
			"convert" => Array(),
			"import" => Array(),
			"service" => Array(),
			"FIELDS_LIST_URL" => Array(),
			"FIELD_EDIT_URL" => Array(),
			"ENTITY_LIST_URL" => Array(),
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх