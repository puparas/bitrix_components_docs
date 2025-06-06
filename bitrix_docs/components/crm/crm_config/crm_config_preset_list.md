|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL списка шаблонов |

| Указывается страница со списком шаблонов. |
| URL списка неиспользуемых пользовательских полей |

| Указывается страница со списком неиспользуемых пользовательских полей. |
| **Дополнительные настройки** |

| |
| Тип для шаблонов |

```
<?$APPLICATION->IncludeComponent(

	"bitrix:crm.config.preset.list",

	"",

	Array(

		"ENTITY_TYPE_ID" => "8",

		"PRESET_LIST_URL" => "list.php?entity_type=#entity_type#",

		"PRESET_UFIELDS_URL" => "ufields.php?entity_type=#entity_type#"

	)

);?>


```