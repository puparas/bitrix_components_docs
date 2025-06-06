|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта): | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - основная страница; * **list** - страница списка сделок; * **funnel** - страница воронки продаж; * **edit** - страница редактирования сделки; * **show** - страница детального просмотра сделки; * **import** - страница импорта. |

**SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**.
  
Если режим поддержки ЧПУ **выключен**, то необходимо настроить параметр
**VARIABLE\_ALIASES**




|  |  |  |
| --- |

| --- |
| Имена переменных |

| Имена переменных для управления страницами. |

.| **Основные параметры** | | |
| ID сделки |

| Поле содержит код, в котором передается идентификатор сделки. |
| **Дополнительные настройки** |

| |
| Формат имени |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.deal",

	"",

	Array(

		"SEF_MODE" => "Y",

		"ELEMENT_ID" => $_REQUEST["deal_id"],

		"NAME_TEMPLATE" => "",

		"SEF_FOLDER" => "/docs/a-new-section-1/",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"list" => "list/",

			"funnel" => "funnel/",

			"edit" => "edit/#deal_id#/",

			"show" => "show/#deal_id#/",

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

			"convert" => Array(),

			"BP_LIST_URL" => Array(),

			"BP_EDIT_URL" => Array(),

			"ENTITY_LIST_URL" => Array(),

			"FIELDS_LIST_URL" => Array(),

			"FIELD_EDIT_URL" => Array(),

			"PATH_TO_ROLE_EDIT" => Array(),

			"PATH_TO_ENTITY_LIST" => Array(),

			"sync" => Array(),

			"funnel" => Array(),

		)

	)

);?>  

```