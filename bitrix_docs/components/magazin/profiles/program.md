|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Дополнительные настройки** |

| |
| Показывать информацию о следующем уровне накоплений |

| [Y|N] При отмеченной опции будет показана информация о том, как увеличить скидку, если такая возможность имеется. |
| Сайт |

| Выбирается сайт, на котором действуют накопительные скидки клиента, информацию по которым следует вывести к показу. |
| ID пользователя |

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.discsave.info",

	"",

	Array(

		"SITE_ID" => "s1",

		"USER_ID" => "",

		"SHOW_NEXT_LEVEL" => "Y"

	)

);?>


```