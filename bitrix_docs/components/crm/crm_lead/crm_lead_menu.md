|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID лида |

| Поле содержит код, в котором передается идентификатор лида. |
| Вид отображения меню |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.contact.menu",

	"",

	Array(

		"ELEMENT_ID" => $_REQUEST["lead_id"],

		"TYPE" => "page"

	)

);?>


```