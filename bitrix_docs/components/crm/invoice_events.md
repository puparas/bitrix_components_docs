|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип сущности |

| Указывается тип сущностей, список действий над которыми будет выводить компонент. Доступно значение **Счет**. |
| ID элемента сущности |

| Указывается идентификатор счета. |
| Количество событий на странице |

| Выставляется число выводимых на одной странице событий. |
| **Дополнительные настройки** |

| |
| Формат имени |

```
<?$APPLICATION->IncludeComponent(

	"bitrix:crm.invoice.events",

	"",

	Array(

		"ENTITY_TYPE" => "INVOICE",

		"ENTITY_ID" => "",

		"EVENT_COUNT" => "20",

		"NAME_TEMPLATE" => "#LAST_NAME#, #NAME# #SECOND_NAME#"

	)

);?>


```