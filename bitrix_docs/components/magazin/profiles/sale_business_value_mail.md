# Вывод полей заказа

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

Вывод полей заказа

**Недоступно в редакциях:**Стандарт, Старт

# Вывод полей заказа

### Описание **sale.business.value.mail**

Компонент выводит список полей заказа по коду заказа. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Магазин > Персональный раздел > Вывод полей
заказа*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Источник данных | **PROVIDER** | Указывается источник для вывода данных из заказа. |
| Группа полей | **GROUP** | В случае, если выбранный источник данных содержит несколько групп полей, то в параметре следует указать ту группу, данные из которой необходимо выводить. |
| Поля | **FIELD** | Задается перечень необходимых полей для вывода. |
| **Дополнительные настройки** | | |
| Код заказа | **ORDER\_ID** | Указывается код заказа, список полей которого должен быть выведен. |
| Выводить название поля | **DISPLAY\_NAME** | [Y|N] При отмеченной опции будет выводиться название поля. |
| Выводить пустые поля | **DISPLAY\_EMPTY** | [Y|N] При отмеченной опции выбранные поля заказа будут выводиться даже в том случае, если они пусты. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.business.value.mail",
	"",
	Array(
		"DISPLAY_EMPTY" => "N",
		"DISPLAY_NAME" => "Y",
		"FIELD" => array("NAME","SECOND_NAME","EMAIL"),
		"GROUP" => "CLIENT",
		"ORDER_ID" => "{#ORDER_ID#}",
		"PROVIDER" => "USER"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх