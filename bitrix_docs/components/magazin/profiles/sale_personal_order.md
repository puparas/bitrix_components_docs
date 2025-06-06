# Заказы пользователя (комплексный компонент)

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

Заказы пользователя (комплексный компонент)

**Недоступно в редакциях:**Стандарт, Старт

# Заказы пользователя (комплексный компонент)

Комплексный компонент отображает список заказов текущего пользователя с ссылками для перехода к просмотру детальной информации, отмене заказа, к оформлению повторного заказа.

### Описание **sale.personal.order**

Можно управлять адресами переходов по этим страницам с помощью настроек ЧПУ. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Персональный раздел > Заказы пользователя*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Не показывать свойства для типа плательщика *<название\_плательщика>* | **PROP\_*N*** | Для каждого типа плательщика *<название\_плательщика>* (*N* - идентификатор типа плательщика) задается массив свойств, которые не должны быть отображены. |
| **Внешний вид** | | |
| Формат показа даты | **ACTIVE\_DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **list** - страница со списком заказов; * **detail** - страница с подробной информацией о заказе; * **cancel** - страница отмены заказа. | | Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами. |  : **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** | | |
| Количество заказов на одной странице | **ORDERS\_PER\_PAGE** | Указывается количество заказов, отображаемых на одной странице. Все остальные заказы будут выведены с помощью постраничной навигации. |
| Страница подключения платежной системы | **PATH\_TO\_PAYMENT** | Указывается путь к странице подключения платежной системы. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Подключение платежной системы](/user_help/store/sale/components_2/order/sale_order_payment.php). Переход на эту страницу происходит по ссылке **Повторить оплату** на странице с детальной информацией по заказу. |
| Страница с корзиной | **PATH\_TO\_BASKET** | Указывается путь к странице с корзиной. Если страница находится в текущей директории, то достаточно указать ее название. Такая страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Мои заказы**. |
| Сохранять установки фильтра в сессии пользователя | **SAVE\_IN\_SESSION** | [Y|N] При отмеченной опции установки фильтра будут сохранены в сессии пользователя. |
| Имя шаблона для постраничной навигации | **NAV\_TEMPLATE** | Указывается имя шаблона для постраничной навигации. |
| Дополнительные свойства инфоблока | **CUSTOM\_SELECT\_PROPS** | Задаются коды свойств инфоблока, которые необходимо вывести при детальном просмотре заказа. Следует задавать для вывода только строковые и числовые типы свойств. |
| Перенести в историю заказы в статусах | **HISTORIC\_STATUSES** | Указываются статусы, которые будут использоваться при фильтрации по истории. Если заказ находится в одном из выбранных статусов, то в списке всех заказов он показан не будет, а будет доступен в истории заказов. |
| Цвет статуса *название\_статуса* | **STATUS\_COLOR\_*код\_статуса*** | Указывается цвет, которым будет выделен статус заказа. |
| Цвет отменённых заказов | **STATUS\_COLOR\_PSEUDO\_CANCELLED** | Указывается цвет, которым будет выделен статус отмененного заказа. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sale.personal.order","",Array(
		"STATUS_COLOR_N" => "green",
		"STATUS_COLOR_P" => "yellow",
		"STATUS_COLOR_F" => "gray",
		"STATUS_COLOR_PSEUDO_CANCELLED" => "red",
		"SEF_MODE" => "Y",
		"ORDERS_PER_PAGE" => 20,
		"PATH_TO_PAYMENT" => "payment.php",
		"PATH_TO_BASKET" => "basket.php",
		"SET_TITLE" => "Y",
		"SAVE_IN_SESSION" => "Y",
		"NAV_TEMPLATE" => "",
		"ACTIVE_DATE_FORMAT" => "d.m.Y",
		"PROP_1" => Array(),
		"PROP_2" => Array(),
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"CACHE_GROUPS" => "Y",
		"CUSTOM_SELECT_PROPS" => "",
		"HISTORIC_STATUSES" => "F",
		"SEF_FOLDER" => "/",
		"SEF_URL_TEMPLATES" => Array(
			"list" => "index.php",
			"detail" => "order_detail.php?ID=#ID#",
			"cancel" => "order_cancel.php?ID=#ID#"
		),
		"VARIABLE_ALIASES" => Array(
			"list" => Array(),
			"detail" => Array(
				"ID" => "ID"
			),
			"cancel" => Array(
				"ID" => "ID"
			),
		)
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх