# Малая корзина для почты

Документация для разработчиков

[Документация для разработчиков](https://dev.1c-bitrix.ru/api_help/)
[Документация по D7](https://dev.1c-bitrix.ru/api_d7/)
[Документация по REST](https://dev.1c-bitrix.ru/rest_help/)
[Пользовательская документация](https://dev.1c-bitrix.ru/user_help/)

Темная тема

[Основные сведения](/user_help/index.php)
[Реализация и системные требования](/user_help/reqintro.php)

[Справочная система и документация](/user_help/help/index.php)

[Контент](/user_help/content/index.php)

[Сайты 24](/user_help/sites24/index.php)

[Маркетинг](/user_help/marketing/index.php)

[Магазин](/user_help/store/index.php)

[Клиенты](/user_help/clients/index.php)

[Сервисы](/user_help/service/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[CRM (КП)](/user_help/components/crm/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Аффилиаты](/user_help/components/magazin/affiliates/index.php)

[Корзина](/user_help/components/magazin/basket/index.php)

[Корзина](/user_help/components/magazin/basket/sale_basket_basket.php)
[Малая корзина для почты](/user_help/components/magazin/basket/sale_basket_basket_small_mail.php)
[Ссылка на корзину](/user_help/components/magazin/basket/sale_basket_basket_line.php)

[Процедура заказа](/user_help/components/magazin/zakaz/index.php)

[Рекомендуемые товары](/user_help/components/magazin/recommended/index.php)

[Список профилей текущего пользователя](/user_help/components/magazin/profiles/index.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Корзина](/user_help/components/magazin/basket/index.php)

Малая корзина для почты

**Недоступно в редакциях:**Стандарт, Старт

# Малая корзина для почты

### Описание **sale.basket.basket.small.mail**

Одностраничный компонент отображает для почты список товаров, находящихся в корзине пользователя. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Корзина > Малая корзина для почты*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Внешний вид** | | |
| Выводимые колонки | **COLUMNS\_LIST** | Выбираются поля, которые будут выведены в списке товаров, находящихся в корзине. |
| **Дополнительные настройки** | | |
| Код пользователя | **USER\_ID** | Параметр содержит код, в котором передается идентификатор пользователя. |
| Страница корзины | **PATH\_TO\_BASKET** | Указывается путь к странице с корзиной. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Страница оформления заказа | **PATH\_TO\_ORDER** | Указывается путь к странице c процедурой оформления заказа. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Процедура оформления заказа](/user_help/store/sale/components_2/order/sale_order_full.php). |
| Показывать отложенные товары | **SHOW\_DELAY** | [Y|N] При отмеченной опции в корзине будут отображаться отложенные товары. |
| Показывать товары, недоступные для покупки | **SHOW\_NOTAVAIL** | [Y|N] При отмеченной опции будут отображаться товары, недоступные для покупки. |
| Показывать товары, на которые подписан покупатель | **SHOW\_SUBSCRIBE** | [Y|N] При отмеченной опции дополнительно будут показаны товары, на которые подписан покупатель. |

### Пример вызова

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

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх