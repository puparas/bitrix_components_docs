|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL списка шаблонов |

| Указывается страница со списком шаблонов бизнес-процессов. |
| URL редактирования шаблона |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.bp.types",

	"",

	Array(

		"BP_LIST_URL" => "bp.list.php?entity_id=#entity_id#",

		"BP_EDIT_URL" => "bp.edit.php?entity_id=#entity_id#&bp_id=#bp_id#"

	)

);?>


```