|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID отчета |

| Указывается код, в котором передается идентификатор отчета. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.report",

	"",

	Array(

		"SEF_MODE" => "Y",

		"REPORT_ID" => $_REQUEST["report_id"],

		"SEF_FOLDER" => "/crm/reports/report/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"report" => "report/",

			"construct" => "construct/#report_id#/#action#/",

			"show" => "view/#report_id#/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"report" => Array(),

			"construct" => Array(),

			"show" => Array(),

		)

	)

);?>


```