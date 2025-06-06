# Подробная информация о заказе для почты

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

[Вывод полей заказа](/user_help/components/magazin/profiles/sale_business_value_mail.php)
[Добавление средств на счет текущего пользователя](/user_help/components/magazin/profiles/sale_account_pay.php)
[Заказы пользователя (комплексный компонент)](/user_help/components/magazin/profiles/sale_personal_order.php)
[Накопительные программы](/user_help/components/magazin/profiles/program.php)
[Отмена заказа](/user_help/components/magazin/profiles/sale_personal_order_cancel.php)
[Отмена подписки](/user_help/components/magazin/profiles/sale_personal_subscribe_cancel.php)
[Персональный раздел пользователя](/user_help/components/magazin/profiles/sale_personal_section.php)
[Пластиковые карты пользователя (комплексный компонент)](/user_help/components/magazin/profiles/sale_personal_cc.php)
[Подписки пользователя (комплексный компонент)](/user_help/components/magazin/profiles/sale_personal_subscribe.php)
[Подробная информация о заказе](/user_help/components/magazin/profiles/sale_personal_order_detail.php)
[Подробная информация о заказе для почты](/user_help/components/magazin/profiles/sale_personal_order_detail_mail.php)
[Профили пользователя (комплексный компонент)](/user_help/components/magazin/profiles/sale_personal_profile.php)
[Редактирование пластиковых карт](/user_help/components/magazin/profiles/sale_personal_cc_detail.php)
[Редактирование профиля](/user_help/components/magazin/profiles/sale_personal_profile_detail.php)
[Список заказов](/user_help/components/magazin/profiles/sale_personal_order_list.php)
[Список пластиковых карт текущего пользователя](/user_help/components/magazin/profiles/sale_personal_cc_list.php)
[Список подписок текущего пользователя](/user_help/components/magazin/profiles/sale_personal_subscribe_list.php)
[Список профилей текущего пользователя](/user_help/components/magazin/profiles/sale_personal_profile_list.php)
[Счета текущего пользователя](/user_help/components/magazin/profiles/sale_personal_account.php)

[Экспорт заказов](/user_help/components/magazin/export_zakaz/index.php)

[Информация о товарах](/user_help/components/magazin/information_tovars/index.php)

[Склады](/user_help/components/magazin/sklads/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Список профилей текущего пользователя](/user_help/components/magazin/profiles/index.php)

Подробная информация о заказе для почты

**Недоступно в редакциях:**Стандарт, Старт

# Подробная информация о заказе для почты

### Описание **sale.personal.order.detail.mail**

Одностраничный компонент выводит подробную информацию по заказу для почты. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Персональный раздел > Подробная информация о заказе для почты*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Идентификатор заказа | **ID** | Указывается идентификатор заказа или код, результатом которого является получение идентификатора заказа. |
| Показывать состав заказа | **SHOW\_ORDER\_BASKET** | [Y|N] При отмеченной опции будет отображено содержимое заказа. |
| Показывать общие данные заказа | **SHOW\_ORDER\_BASE** | [Y|N] При отмеченной опции будут отображены общие данные по заказу: статус заказа, на какую сумму, отменен или нет. |
| Показывать данные учетной записи | **SHOW\_ORDER\_USER** | [Y|N] При отмеченной опции будут отображены параметры учетной записи: имя, логин, e-mail. |
| Показывать параметры заказа | **SHOW\_ORDER\_PARAMS** | [Y|N] При отмеченной опции будет отображен блок "Параметры заказа". |
| Показывать личные данные | **SHOW\_ORDER\_BUYER** | [Y|N] При отмеченной опции будет отображен блок "Личные данные", содержащий информацию о покупателе. |
| Показывать данные для доставки | **SHOW\_ORDER\_DELIVERY** | [Y|N] При отмеченной опции будут показаны данные для доставки товара. |
| Показывать параметры доставки и оплаты | **SHOW\_ORDER\_PAYMENT** | [Y|N] При отмеченной опции будет отображена информация о платежной системе, службе доставки и оплачен ли заказ. |
| Показывать итоговую сумму | **SHOW\_ORDER\_SUM** | [Y|N] При отмеченной опции будет отображена итоговая сумма по заказу. |
| Выводимые колонки состава заказа | **CUSTOM\_SELECT\_PROPS** | Выбираются колонки, которые должны быть показаны в таблице содержимого заказа. |
| Не показывать свойства для типа плательщика **<название\_плательщика>** | **PROP\_<N>** | Для каждого типа плательщика **<название\_плательщика>** (**N** - идентификатор типа плательщика) задается массив свойств, которые не должны быть отображены. |
| **Внешний вид** | | |
| Формат показа даты | **ACTIVE\_DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Ограничение по ширине для анонсного изображения, px | **PICTURE\_WIDTH** | Указывается ширина (в пикселах) изображения товара при подробном просмотре заказа. |
| Ограничение по высоте для анонсного изображения, px | **PICTURE\_HEIGHT** | Указывается высота (в пикселах) изображения товара при подробном просмотре заказа. |
| Тип масштабирования | **PICTURE\_RESAMPLE\_TYPE** | Из выпадающего списка выбирается тип масштабирования изображений:  * С сохранением пропорций, улучшенная обработка; * С сохранением пропорций; * С обрезанием. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Страница со списком заказов | **PATH\_TO\_LIST** | Указывается путь к странице со списком заказов. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Список заказов](/user_help/store/sale/components_2/personal/sale_personal_order_list.php). |
| Страница отмены заказа | **PATH\_TO\_CANCEL** | Указывается путь к странице отмены заказа. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Отмена заказа](/user_help/store/sale/components_2/personal/sale_personal_order_cancel.php). Необходимо передавать идентификатор заказа в качестве параметра. |
| Страница подключения платежной системы | **PATH\_TO\_PAYMENT** | Указывается путь к странице подключения платежной системы. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Подключение платежной системы](/user_help/store/sale/components_2/order/sale_order_payment.php). |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.personal.order.detail.mail",
	"",
	Array(
		"ID" => "{#ORDER_ID#}",
		"SHOW_ORDER_BASKET" => "Y",
		"SHOW_ORDER_BASE" => "Y",
		"SHOW_ORDER_USER" => "Y",
		"SHOW_ORDER_PARAMS" => "Y",
		"SHOW_ORDER_BUYER" => "Y",
		"SHOW_ORDER_DELIVERY" => "Y",
		"SHOW_ORDER_PAYMENT" => "Y",
		"SHOW_ORDER_SUM" => "Y",
		"CUSTOM_SELECT_PROPS" => array("NAME", "DISCOUNT_PRICE_PERCENT_FORMATED", "PRICE_FORMATED", "QUANTITY"),
		"PROP_1" => array(),
		"PROP_2" => array(),
		"ACTIVE_DATE_FORMAT" => "d.m.Y",
		"PICTURE_WIDTH" => "110",
		"PICTURE_HEIGHT" => "110",
		"PICTURE_RESAMPLE_TYPE" => "1",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"PATH_TO_LIST" => "/personal/order/index.php",
		"PATH_TO_CANCEL" => "/personal/order/cancel.php?ORDER_ID=#ORDER_ID#",
		"PATH_TO_PAYMENT" => "/payment/payment.php"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх