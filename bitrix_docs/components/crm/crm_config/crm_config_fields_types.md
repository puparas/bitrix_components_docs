|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL списка полей |

| Указывается страница со списком полей. |
| URL редактирования поля |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.fields.types",

	"",

	Array(

		"FIELDS_LIST_URL" => "field.list.php?entity_id=#entity_id#",

		"FIELD_EDIT_URL" => "field.edit.php?entity_id=#entity_id#&field_id=#field_id#"

	)

);?>


```