|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID компании |

| Поле содержит код, в котором передается идентификатор компании. |
| Вид отображения меню |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.company.menu",

	"",

	Array(

		"ELEMENT_ID" => $_REQUEST["company_id"],

		"TYPE" => "show"

	)

);?>


```