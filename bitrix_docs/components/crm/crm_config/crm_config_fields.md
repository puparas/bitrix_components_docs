|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

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