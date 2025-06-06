# Смена способа оплаты

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

[Смена способа оплаты](/user_help/components/magazin/zakaz/sale_order_payment_change.php)
[Калькулятор доставки (AJAX)](/user_help/components/magazin/zakaz/sale_ajax_delivery_calculator.php)
[Оформление заказа](/user_help/components/magazin/zakaz/sale_order_ajax.php)
[Подключение обработчика результата платежной системы](/user_help/components/magazin/zakaz/sale_order_payment_receive.php)
[Подключение платежной системы](/user_help/components/magazin/zakaz/sale_order_payment.php)
[Привязка к местоположению: выпадающие списки](/user_help/components/magazin/zakaz/sale_location_selector_steps.php)
[Привязка к местоположению: строка поиска](/user_help/components/magazin/zakaz/sale_location_selector_search.php)

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

[Процедура заказа](/user_help/components/magazin/zakaz/index.php)

Смена способа оплаты

**Недоступно в редакциях:**Стандарт, Старт

# Смена способа оплаты

### Описание **sale.order.payment.change**

Одностраничный компонент осуществляет смену платежной системы для оплаты заказа. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Процедура оформления заказа > Смена способа оплаты*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Дополнительные настройки** | | |
| Страница подключения платежной системы | **PATH\_TO\_PAYMENT** | Указывается путь к странице подключения платежной системы. |
| Устанавливать заголовок страницы | **SET\_TITLE** | При отмеченной опции будет устанавливаться заголовок страницы. |
| Исключить из списка платежных систем | **ELIMINATED\_PAY\_SYSTEMS** | Отмечаются платежные системы, которые необходимо исключить из списка. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.order.payment.change",
	"",
	Array(
		"ELIMINATED_PAY_SYSTEMS" => array("11","14"),
		"PATH_TO_PAYMENT" => "/personal/order/payment",
		"SET_TITLE" => "Y"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх