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

"bitrix:crm.config.perms",

	"",

	Array(

		"SEF_MODE" => "Y",

		"SEF_FOLDER" => "/crm/configs/sendsave/",

		"SEF_URL_TEMPLATES" => Array(

			"PATH_TO_ENTITY_LIST" => "",

			"PATH_TO_ROLE_EDIT" => "#role_id#/edit/"

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

			"PATH_TO_ROLE_EDIT" => Array(),

			"PATH_TO_ENTITY_LIST" => Array(),

		)

	)

);?>


```