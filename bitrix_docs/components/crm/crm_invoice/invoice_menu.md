|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID счёта |

| Поле содержит код, в котором передается идентификатор счёта. |
| Вид отображения меню |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.invoice.menu",

	"",

	Array(

		"ELEMENT_ID" => $_REQUEST["invoice_id"],

		"TYPE" => "list"

	)

);?>


```