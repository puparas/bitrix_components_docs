# Редактирование шаблона бизнес-процесса

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

Редактирование шаблона бизнес-процесса

# Редактирование шаблона бизнес-процесса

### Описание **crm.config.bp.edit**

Одностраничный компонент, позволяет отредактировать шаблон бизнес-процесса модуля CRM. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *CRM > Настройки > Редактирование шаблона бизнес-процесса*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Шаблоны ссылок** | | |
| URL списка типов | **ENTITY\_LIST\_URL** | Указывается страница со списком типов шаблонов бизнес-процессов. |
| URL списка шаблонов | **BP\_LIST\_URL** | Указывается страница со списком шаблонов бизнес-процессов. |
| URL редактирования шаблона | **BP\_EDIT\_URL** | Указывается страница редактирования шаблона бизнес-процесса. |
| **Дополнительные настройки** | | |
| Тип шаблона | **BP\_ENTITY\_ID** | Указывается тип шаблона бизнес-процесса. |
 Идентификатор шаблона | **BP\_BP\_ID** | Указывается идентификатор шаблона. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
"bitrix:crm.config.bp.edit",
	"",
	Array(
		"BP_ENTITY_ID" => $_REQUEST["entity_id"],
		"BP_BP_ID" => $_REQUEST["bp_id"],
		"ENTITY_LIST_URL" => "bp.php",
		"BP_LIST_URL" => "bp.list.php?entity_id=#entity_id#",
		"BP_EDIT_URL" => "bp.edit.php?entity_id=#entity_id#&bp_id=#bp_id#"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх