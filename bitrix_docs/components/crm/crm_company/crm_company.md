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

"bitrix:crm.company",

	"",

	Array(

		"SEF_MODE" => "Y",

		"ELEMENT_ID" => $_REQUEST["company_id"],

		"NAME_TEMPLATE" => "",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"list" => "list/",

			"edit" => "edit/#company_id#/",

			"show" => "show/#company_id#/",

			"import" => "import/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"report" => Array(),

			"construct" => Array(),

			"show" => Array(),

			"list" => Array(),

			"edit" => Array(),

			"import" => Array(),

		)

	)

);?>


```