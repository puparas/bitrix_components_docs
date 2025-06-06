|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL списка типов |

| Указывается страница со списком типов шаблонов бизнес-процессов. |
| URL списка шаблонов |

| Указывается страница со списком шаблонов бизнес-процессов. |
| URL редактирования шаблона |

| Указывается страница редактирования шаблона бизнес-процесса. |
| **Дополнительные настройки** |

| |
| Тип шаблона |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.bp.edit",

	"",

	Array(

		"BP_ENTITY_ID" => $_REQUEST["entity_id"],

		"BP_BP_ID" => $_REQUEST["bp_id"],

		"ENTITY_LIST_URL" => "bp.php",

		"BP_LIST_URL" => "bp.list.php?entity_id=#entity_id#",

		"BP_EDIT_URL" => "bp.edit.php?entity_id=#entity_id#&bp_id=#bp_id#"

	)

);?>


```