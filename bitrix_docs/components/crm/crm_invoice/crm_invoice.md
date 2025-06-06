|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID счёта |

| Поле содержит код, в котором передается идентификатор счета. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

```


<?$APPLICATION->IncludeComponent(

	"bitrix:crm.invoice",

	"",

	Array(

		"SEF_MODE" => "Y",

		"ELEMENT_ID" => $_REQUEST["invoice_id"],

		"NAME_TEMPLATE" => "",

		"SEF_FOLDER" => "/crm/invoice/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"list" => "list/",

			"edit" => "edit/#invoice_id#/",

			"show" => "show/#invoice_id#/",

			"payment" => "payment/#invoice_id#/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"list" => Array(),

			"edit" => Array(),

			"show" => Array(),

			"payment" => Array(),

		)

	)

);?>


```