|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Внешний вид** |

| |
| Выводимые колонки |

| Выбираются поля, которые будут выведены в списке товаров, находящихся в корзине. |
| **Дополнительные настройки** |

| |
| Код пользователя |

| Параметр содержит код, в котором передается идентификатор пользователя. |
| Страница корзины |

| Указывается путь к странице с корзиной. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Страница оформления заказа |

| Указывается путь к странице c процедурой оформления заказа. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Процедура оформления заказа](/user_help/store/sale/components_2/order/sale_order_full.php). |
| Показывать отложенные товары |

| [Y|N] При отмеченной опции в корзине будут отображаться отложенные товары. |
| Показывать товары, недоступные для покупки |

| [Y|N] При отмеченной опции будут отображаться товары, недоступные для покупки. |
| Показывать товары, на которые подписан покупатель |

```
<?$APPLICATION->IncludeComponent(

	"bitrix:sale.basket.basket.small.mail",

	"",

	Array(

		"COMPONENT_TEMPLATE" => ".default",

		"COLUMNS_LIST" => array("NAME","DISCOUNT_FORMATED","WEIGHT_FORMATED","PRICE_FORMATED","QUANTITY_FORMATED"),

		"USER_ID" => "{#USER_ID#}",

		"PATH_TO_BASKET" => "/personal/basket.php",

		"PATH_TO_ORDER" => "/personal/order.php",

		"SHOW_DELAY" => "Y",

		"SHOW_NOTAVAIL" => "Y",

		"SHOW_SUBSCRIBE" => "Y"

	)

);?>


```