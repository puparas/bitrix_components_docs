# Ссылка на корзину

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

Ссылка на корзину

**Недоступно в редакциях:**Стандарт, Старт

# Ссылка на корзину

Одностраничный компонент, который отображает специальный блок корзины с набором в зависимости от настроек самого компонента информации.

### Описание **sale.basket.basket.line**

Компонент стандартный и входит в дистрибутив модуля. Поставляется с шаблонами: **.default** и **bootstrap\_v4**.

В визуальном редакторе компонент расположен по пути: *Магазин > Корзина > Ссылка на корзину*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Страница корзины | **PATH\_TO\_BASKET** | Указывается путь к странице с корзиной. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Страница оформления заказа | **PATH\_TO\_ORDER** | Указывается путь к странице оформления заказа. Если страница находится в текущей директории, то достаточно указать ее название. |
| Показывать количество товаров | **SHOW\_NUM\_PRODUCTS** | [Y|N] При отмеченной опции будет показано общее количество товара. |
| Показывать общую сумму по товару | **SHOW\_TOTAL\_PRICE** | [Y|N] При отмеченной опции будет выведена общая сумма по стоимости товаров, находящихся в корзине. |
| Выводить нулевые значения в пустой корзине | **SHOW\_EMPTY\_VALUES** | [Y|N] При отмеченной опции в пустой корзине будут выводится нулевые значения. |
| **Персональный раздел** | | |
| Отображать персональный раздел | **SHOW\_PERSONAL\_LINK** | [Y|N] При отмеченной опции будет выведена ссылка на персональный раздел. |
| Страница персонального раздела | **PATH\_TO\_PERSONAL** | Указывается путь к персональному разделу, где начальной страницей может быть список заказов, профили пользователя и т.д. |
| **Авторизация** | | |
| Добавить возможность авторизации | **SHOW\_AUTHOR** | [Y|N] При отмеченной опции будет доступна ссылка для авторизации на сайте; станут активны дополнительные поля     |  |  |  | | --- | --- | --- | | Страница регистрации | **PATH\_TO\_REGISTER** | Задается путь к странице регистрации на сайте. | | Страница авторизации | **PATH\_TO\_AUTHORIZE** | Задается путь к странице авторизации. | | Страница профиля | **PATH\_TO\_PROFILE** | Указывается путь к странице профиля покупателя. |  . |
| **Список товаров** | | |
| Показывать список товаров | **SHOW\_PRODUCTS** | [Y|N] При отмеченной опции в корзине будет выводится список добавленных товаров. Кроме того, становятся доступными дополнительные параметры     |  |  |  | | --- | --- | --- | | Показывать отложенные товары | **SHOW\_DELAY** | [Y|N] При отмеченной опции в корзине будут показаны отложенные товары. | | Показывать товары, недоступные для покупки | **SHOW\_NOTAVAIL** | [Y|N] При отмеченной опции в корзине будут показаны товары, недоступные в текущий момент для покупки. | | Выводить картинку товара | **SHOW\_IMAGE** | [Y|N] При отмеченной опции будет выводится изображение товара. | | Выводить цену товара | **SHOW\_PRICE** | [Y|N] При отмеченной опции для товара в корзине будет выведена цена. | | Выводить подытог по строке | **SHOW\_SUMMARY** | [Y|N] При отмеченной опции для каждой позиции в корзине будет выводится подытог. |  для показа списка товаров. |
| **Внешний вид** | | |
| Отображать корзину поверх шаблона | **POSITION\_FIXED** | [Y|N] При отмеченной опции специальный блок корзины будет отображен поверх других элементов сайта; станут активны дополнительные окна     |  |  |  | | --- | --- | --- | | Положение по горизонтали | **POSITION\_HORIZONTAL** | Выбирается положение блока корзины по горизонтали: справа или слева.   Параметр доступен, если отмечена опция **Отображать корзину поверх шаблона**. | | Положение по вертикали | **POSITION\_VERTICAL** | Выбирается положение блока корзины по горизонтали: вверху или внизу. |  . В противном случае детальная информация по содержимому корзины будет отображена на странице. |
| **Дополнительные настройки** | | |
| Не показывать на страницах корзины и оформления заказа | **HIDE\_ON\_BASKET\_PAGES** | [Y|N] При отмеченной опции компонент на страницах корзины и оформления заказа будет скрыт. Рекомендуется оставлять данную опцию включенной во избежание снижения производительности на этих страницах. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sale.basket.basket.line","",Array(
		"HIDE_ON_BASKET_PAGES" => "Y",
		"PATH_TO_BASKET" => SITE_DIR."personal/cart/",
		"PATH_TO_ORDER" => SITE_DIR."personal/order/make/",
		"PATH_TO_PERSONAL" => SITE_DIR."personal/",
		"PATH_TO_PROFILE" => SITE_DIR."personal/",
		"PATH_TO_REGISTER" => SITE_DIR."login/",
		"POSITION_FIXED" => "Y",
		"POSITION_HORIZONTAL" => "right",
		"POSITION_VERTICAL" => "top",
		"SHOW_AUTHOR" => "Y",
		"SHOW_DELAY" => "N",
		"SHOW_EMPTY_VALUES" => "Y",
		"SHOW_IMAGE" => "Y",
		"SHOW_NOTAVAIL" => "N",
		"SHOW_NUM_PRODUCTS" => "Y",
		"SHOW_PERSONAL_LINK" => "N",
		"SHOW_PRICE" => "Y",
		"SHOW_PRODUCTS" => "Y",
		"SHOW_SUMMARY" => "Y",
		"SHOW_TOTAL_PRICE" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 1  **Сергей Денисенко** 05.02.2021 15:43:25 |
| --- |
| можно передать параметр  "CUSTOM\_SITE\_ID" => "s1" для того чтоб использовать одну корзину на разных языковых/региональных версиях |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх