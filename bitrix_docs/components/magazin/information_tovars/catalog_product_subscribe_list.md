# Список товаров на которые вы подписаны

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

Список товаров на которые вы подписаны

**Недоступно в редакциях:**Стандарт, Старт

# Список товаров на которые вы подписаны

Компонент служит для отображения списка товаров, на которые подписан пользователь. Компонент стандартный и входит в дистрибутив модуля.

### Описание **catalog.product.subscribe.list**

В визуальном редакторе компонент расположен по пути *Магазин > Информация о товарах > Список товаров на которые вы подписаны*.

Компонент относится к модулю [Торговый каталог](/user_help/store/catalog/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительные настройки** | | |
 Количество элементов, выводимых в одной строке | **LINE\_ELEMENT\_COUNT** | Указывается количество элементов выводимых в одной строке на странице. || **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:catalog.product.subscribe.list",
	"",
	Array(
		"CACHE_TIME" => "3600",
		"CACHE_TYPE" => "A",
		"LINE_ELEMENT_COUNT" => "3"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх