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

"bitrix:crm.config.exch1c",

	".default",

	Array(

		"SEF_MODE" => "Y",

		"NAME_TEMPLATE" => "#LAST_NAME# #NAME# #SECOND_NAME#",

		"SEF_FOLDER" => "/docs/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"catalog" => "catalog/",

			"invoice" => "invoice/"

		),

		"VARIABLE_ALIASES" => Array(

			"PATH_TO_ROLE_EDIT" => Array(),

			"index" => Array(),

			"catalog" => Array(),

			"invoice" => Array(),

		)

	)

);?>


```