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

"bitrix:crm.config.bp",

	"",

	Array(

		"SEF_MODE" => "Y",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"ENTITY_LIST_URL" => "",

			"BP_LIST_URL" => "#entity_id#/",

			"BP_EDIT_URL" => "#entity_id#/edit/#bp_id#/"

		),

		"VARIABLE_ALIASES" => Array(

			"BP_LIST_URL" => Array(),

			"BP_EDIT_URL" => Array(),

			"ENTITY_LIST_URL" => Array(),

		)

	)

);?>


```