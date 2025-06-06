|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Дополнительные настройки** |

| |
| Тип полей |

| Указывается тип дополнительных полей. Возможен выбор из трех вариантов:  * **Лид/контакт**; * **Компания**; * **Сделка**. |
| **Шаблоны ссылок** |

| |
| URL списка типов |

| Указывается страница со списком типов полей. |
| URL списка полей |

| Указывается страница со списком полей. |
| URL редактирования поля |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.fields.list",

	"",

	Array(

		"FIELS_ENTITY_ID" => "CRM_LEAD",

		"ENTITY_LIST_URL" => "field.php",

		"FIELDS_LIST_URL" => "field.list.php?entity_id=#entity_id#",

		"FIELD_EDIT_URL" => "field.edit.php?entity_id=#entity_id#&field_id=#field_id#"

	)

);?>


```