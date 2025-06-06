|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID контакта |

| Поле содержит код, в котором передается идентификатор контакта. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

```


<?$APPLICATION->IncludeComponent(

	"bitrix:crm.contact",

	"",

	Array(

		"SEF_MODE" => "Y",

		"ELEMENT_ID" => $_REQUEST["contact_id"],

		"NAME_TEMPLATE" => "",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"list" => "list/",

			"edit" => "edit/#contact_id#/",

			"show" => "show/#contact_id#/",

			"service" => "service/",

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

			"service" => Array(),

		)

	)

);?>


```