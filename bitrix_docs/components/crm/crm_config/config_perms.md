|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Шаблоны ссылок** |

| |
| URL привязки ролей |

| Указывается страница со списком ролей. |
| URL редактирования роли |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.perms.relation",

	"",

	Array(

		"PATH_TO_ENTITY_LIST" => "perms.php",

		"PATH_TO_ROLE_EDIT" => "role.edit.php?role_id=#role_id#"

	)

);?>


```