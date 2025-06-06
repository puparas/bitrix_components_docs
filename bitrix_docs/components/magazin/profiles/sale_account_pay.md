# Добавление средств на счет текущего пользователя

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

Добавление средств на счет текущего пользователя

**Недоступно в редакциях:**Стандарт, Старт

# Добавление средств на счет текущего пользователя

### Описание **sale.account.pay**

Одностраничный компонент позволяет добавить средства на внутренний счет текущего пользователя. Компонент стандартный и входит в дистрибутив модуля. Доступен в редакции «Бизнес» и выше.

В визуальном редакторе компонент расположен по пути: *Магазин > Персональный раздел > Добавление средств на счет текущего пользователя*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Включить обновленную версию компонента | **REFRESHED\_COMPONENT\_MODE** | [Y|N] При отмеченной опции будет использоваться обновленная версия компонента. |
| **Дополнительные настройки (для старой версии компонента)** | | |
| Путь к корзине | **PATH\_TO\_BASKET** | Указывается путь к странице с корзиной от корня сайта. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Путь к странице оплат | **PATH\_TO\_PAYMENT** | Указывается путь к странице оплат от корня сайта. Если страница находится в текущей директории, то достаточно указать ее название. |
| Валюта для отображения | **SELL\_CURRENCY** | Из созданных в системе валют выбирается валюта, в которой будут отображаться денежные средства пользователя. |
| Выберите суммы для покупки | **SELL\_AMOUNT** | Указывается набор сумм, который будет доступен для пополнения счета. Полный набор сумм задается на [странице настроек модуля Интернет-магазин](/user_help/store/sale/module_settings.php). |
| Перенаправлять пользователя на текущую страницу после добавления в корзину | **REDIRECT\_TO\_CURRENT\_PAGE** | [Y|N] При отмеченной опции пользователь будет перенаправляться на данную страницу после добавление товара в корзину. |
| Имя переменной для покупки | **VAR** | Задается имя переменной, в которой будет передаваться сумма при зачислении на счет. |
| Callback-функция для разрешения доставки товара | **CALLBACK\_NAME** | Задайте имя Callback-функции. По умолчанию используется **PayUserAccountDeliveryOrderCallback**. Свою функцию можно добавить в файл **/bitrix/php\_interface/init.php**, при этом необходимо указать ее имя в параметрах компонента. Функция будет восприниматься как глобальная. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Пополнение счета**. |
| **Дополнительные настройки (для обновленной версии компонента)** | | |
| Путь к корзине | **PATH\_TO\_BASKET** | Указывается путь к странице с корзиной от корня сайта. Если страница находится в текущей директории, то достаточно указать ее название. Страница может быть создана с помощью компонента [Корзина](/user_help/store/sale/components_2/basket/sale_basket_basket.php). |
| Путь к странице оплат | **PATH\_TO\_PAYMENT** | Указывается путь к странице оплат от корня сайта. Если страница находится в текущей директории, то достаточно указать ее название. |
| Валюта для отображения | **SELL\_CURRENCY** | Из созданных в системе валют выбирается валюта, в которой будут отображаться денежные средства пользователя. |
| Тип пользователя | **PERSON\_TYPE** | Из созданных в системе типов плательщиков выбирается тот, для которого будет выполняться пополнение счета. |
| Исключить из списка платежных систем | **ELIMINATED\_PAY\_SYSTEMS** | Из созданных в системе платежных систем выбираются те, которые не должны быть доступны для пополнения счета. |
| Установка значения через заданную переменную | **SELL\_VALUES\_FROM\_VAR** | [Y|N] При отмеченной опции значение суммы к оплате будет устанавливаться через переменную. |
| Сумма к оплате\* | **SELL\_VAR\_PRICE\_VALUE** | Указывается переменная, через которую будет передаваться сумма для зачисления на счет. |
| Показать сумму на странице\* | **SELL\_SHOW\_RESULT\_SUM** | [Y|N] При отмеченной опции сумма будет показана на странице. |
| Показывать значения фиксированных платежей | **SELL\_SHOW\_FIXED\_VALUES** | [Y|N] При отмеченной опции будут отображаться значения фиксированных платежей. |
| Выберите суммы для покупки\*\* | **SELL\_TOTAL** | Задаются суммы фиксированных платежей. |
| Разрешить пользователю вводить сумму | **SELL\_USER\_INPUT** | [Y|N] При отмеченной опции пользователю будет доступно поле для ввода своей суммы платежа.    Параметр недоступен, если отмечена опция **Установка значения через заданную переменную**. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Пополнение счета**. |

\* - параметры доступны при отмеченной опции **Установка значения через заданную переменную**.

\*\* - параметр доступен при отмеченной опции **Показывать значения фиксированных платежей**.

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sale.account.pay",
	"",
	Array(
		"ELIMINATED_PAY_SYSTEMS" => array("2"),
		"PATH_TO_BASKET" => "/personal/cart",
		"PATH_TO_PAYMENT" => "/personal/order/payment",
		"PERSON_TYPE" => "1",
		"REFRESHED_COMPONENT_MODE" => "Y",
		"SELL_CURRENCY" => "RUB",
		"SELL_SHOW_FIXED_VALUES" => "Y",
		"SELL_TOTAL" => array("100","200","500","1000","5000",""),
		"SELL_USER_INPUT" => "Y",
		"SELL_VALUES_FROM_VAR" => "N",
		"SET_TITLE" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх