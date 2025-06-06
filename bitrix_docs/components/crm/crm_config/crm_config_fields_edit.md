|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Дополнительные настройки** |

| |
| Тип поля |

| Указывается тип дополнительного поля. Возможен выбор из трех вариантов:  * **Лид/контакт**; * **Компания**; * **Сделка**. |
| Дополнительное поле |

| Имя переменной, где будет храниться мнемоническое имя поля. |
| **Шаблоны ссылок** |

| |
| URL списка типов |

| Указывается страница со списком типов полей. |
| URL списка полей |

| Указывается страница со списком полей. |
| URL редактирования поля |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.fields.edit",

	"",

	Array(

		"FIELS_ENTITY_ID" => "CRM_LEAD",

		"FIELS_FIELD_ID" => $_REQUEST["field_id"],

		"ENTITY_LIST_URL" => "field.php",

		"FIELDS_LIST_URL" => "field.list.php?entity_id=#entity_id#",

		"FIELD_EDIT_URL" => "field.edit.php?entity_id=#entity_id#&field_id=#field_id#"

	)

);?>


```