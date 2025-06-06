|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID контакта |

| Поле содержит код, в котором передается идентификатор контакта. |
| Вид отображения меню |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.contact.menu",

	"",

	Array(

		"ELEMENT_ID" => $_REQUEST["contact_id"],

		"TYPE" => "page"

	)

);?>


```