|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| ID инфоблока |

| Указывается идентификатор одного из созданных в системе Highload-блоков. |
| ID записи |

| Указывается идентификатор записи Highload-блока. |
| Путь к странице списка записей |

| Путь к странице со списком всех записей Highload-блока. |
| Проверять права доступа |

```
<?$APPLICATION->IncludeComponent("bitrix:highloadblock.view","",Array(

		"BLOCK_ID" => $_REQUEST['BLOCK_ID'],

		"CHECK_PERMISSIONS" => "Y",

		"ROW_ID" => $_REQUEST['ID'],

		"LIST_URL" => "list.php?IBLOCK_ID=#IBLOCK_ID#"

	)

);?>


```