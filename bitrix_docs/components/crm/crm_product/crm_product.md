|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Торговый каталог |

| Указывается каталог, товары которого будут показаны. |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.product",

	"",

	Array(

		"CATALOG_ID" => "34",

		"SEF_MODE" => "Y",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"product_list" => "product_list/#section_id#/",

			"product_edit" => "product_edit/#product_id#/",

			"product_show" => "product_show/#product_id#/",

			"section_list" => "section_list/#section_id#/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"product_list" => Array(),

			"product_edit" => Array(),

			"product_show" => Array(),

			"section_list" => Array(),

		)

	)

);?>


```