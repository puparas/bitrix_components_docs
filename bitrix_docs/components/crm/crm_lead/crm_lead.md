|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID лида |

| Поле содержит код, в котором передается идентификатор лида. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

```


<?$APPLICATION->IncludeComponent(

"bitrix:crm.lead",

	"",

	Array(

		"SEF_MODE" => "Y",

		"ELEMENT_ID" => $_REQUEST["lead_id"],

		"NAME_TEMPLATE" => "",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"list" => "list/",

			"edit" => "edit/#lead_id#/",

			"show" => "show/#lead_id#/",

			"convert" => "convert/#lead_id#/",

			"import" => "import/",

			"service" => "service/"

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

			"convert" => Array(),

		)

	)			

);?>


```