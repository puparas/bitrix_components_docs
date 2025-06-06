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

"bitrix:crm.config.external_sale",

	"",

	Array(

		"SEF_MODE" => "Y",

		"AJAX_MODE" => "Y",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"edit" => "edit-#id#.php",

			"sync" => "sync-#id#.php"

		),

		"AJAX_OPTION_JUMP" => "Y",

		"AJAX_OPTION_STYLE" => "Y",

		"AJAX_OPTION_HISTORY" => "Y",

		"AJAX_OPTION_ADDITIONAL" => "",

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"edit" => Array(),

			"sync" => Array(),

		)

	)

);?>


```