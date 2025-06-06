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

| Указывается страница редактирования роли. |
| **Дополнительные настройки** |

| |
| Идентификатор роли |

```
<?$APPLICATION->IncludeComponent(

"bitrix:crm.config.perms.role.edit",

	"",

	Array(

		"ROLE_ID" => $_REQUEST["role_id"],

		"PATH_TO_ENTITY_LIST" => "perms.php",

		"PATH_TO_ROLE_EDIT" => "role.edit.php?role_id=#role_id#"

	)

);?>


```