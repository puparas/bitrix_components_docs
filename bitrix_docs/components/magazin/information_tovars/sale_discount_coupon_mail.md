# Генерация купона на товар для почты

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

[Процедура заказа](/user_help/components/magazin/zakaz/index.php)

[Рекомендуемые товары](/user_help/components/magazin/recommended/index.php)

[Список профилей текущего пользователя](/user_help/components/magazin/profiles/index.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Выбор товара для получения подарка](/user_help/components/magazin/information_tovars/sale_gift_main_products.php)
[Подарки к товарам в корзине](/user_help/components/magazin/information_tovars/sale_products_gift_basket.php)
[Подарки к товарам в корзине (устаревший)](/user_help/components/magazin/information_tovars/sale_gift_basket.php)
[Подарки к товарам конкретного раздела](/user_help/components/magazin/information_tovars/sale_products_gift_section.php)
[Подарки к выбранному товару](/user_help/components/magazin/information_tovars/sale_products_gift.php)
[Просмотренные товары](/user_help/components/magazin/information_tovars/catalog_products_viewed.php)
[Рекомендуемые товары](/user_help/components/magazin/information_tovars/catalog_recommended_products.php)
[Генерация купона на товар для почты](/user_help/components/magazin/information_tovars/sale_discount_coupon_mail.php)
[Персональные рекомендации (почта)](/user_help/components/magazin/information_tovars/sale_bigdata_personal_mail.php)
[Самые продаваемые товары](/user_help/components/magazin/information_tovars/sale_bestsellers.php)
[Сопутствующие заказу товары](/user_help/components/magazin/information_tovars/sale_bigdata_followup_mail.php)
[С этим товаром покупают](/user_help/components/magazin/information_tovars/sale_recommended_products.php)
[Подписка на товары](/user_help/components/magazin/information_tovars/catalog_product_subscribe.php)
[Список товаров на которые вы подписаны](/user_help/components/magazin/information_tovars/catalog_product_subscribe_list.php)
[Подарки к товарам конкретного раздела (устаревший)](/user_help/components/magazin/information_tovars/sale_gift_section.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

Генерация купона на товар для почты

**Недоступно в редакциях:**Стандарт, Старт

# Генерация купона на товар для почты

### Описание **sale.discount.coupon.mail**

Одностраничный компонент генерирует купон для правила корзины с соответствии с заданными параметрами. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Информация о товарах > Генерация купона на товар для почты*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Скидка** | | |
| Значение скидки | **DISCOUNT\_VALUE** | Указывается величина скидки для правила работы с корзиной. |
| Тип скидки | **DISCOUNT\_UNIT** | Выбирается тип скидки:  * **Perc** - процент; * **CurEach** - на каждый товар; * **CurAll** - на сумму товаров. |
| **Купон** | | |
| Тип купона | **COUPON\_TYPE** | Задается тип купона:  * **Order** - на один заказ; * **Basket** - на одну позицию заказа. |
| **Параметры** | | |
| Поле правила скидки "XML\_ID" | **DISCOUNT\_XML\_ID** | Указывается значение, которое будет подставлено в поле **Внешний код** правила работы с корзиной. По умолчанию в поле передается код выпуска рассылки. |
| Поле купона "Описание" | **COUPON\_DESCRIPTION** | Указывается значение, которое будет подставлено в поле **Комментарий** купона правила работы с корзиной. По умолчанию в поле передается email получателя рассылки. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.discount.coupon.mail",
	"",
	Array(
		"DISCOUNT_VALUE" => "10",
		"DISCOUNT_UNIT" => "Perc",
		"COUPON_TYPE" => "Order",
		"DISCOUNT_XML_ID" => "{#SENDER_CHAIN_CODE#}",
		"COUPON_DESCRIPTION" => "{#EMAIL_TO#}"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх