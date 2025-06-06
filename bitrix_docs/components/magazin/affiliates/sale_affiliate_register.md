# Регистрация аффилиата

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

[Аффилиатские планы](/user_help/components/magazin/affiliates/sale_affiliate_plans.php)
[Отчет аффилиата](/user_help/components/magazin/affiliates/sale_affiliate_account.php)
[Отчет по программе аффилиата](/user_help/components/magazin/affiliates/sale_affiliate_report.php)
[Регистрация аффилиата](/user_help/components/magazin/affiliates/sale_affiliate_register.php)
[Технические инструкции аффилиата](/user_help/components/magazin/affiliates/sale_affiliate_instructions.php)

[Корзина](/user_help/components/magazin/basket/index.php)

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

[Аффилиаты](/user_help/components/magazin/affiliates/index.php)

Регистрация аффилиата

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Регистрация аффилиата

Компонент является одностраничным и служит для создания страницы регистрации аффилиата.

### Описание **sale.affiliate.register**

Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Магазин > Аффилиаты > Регистрация аффилиата*.

Компонент относится к модулю [Интернет-магазин](/user_help/store/sale/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Путь к файлу с пользовательским соглашением | **AGREEMENT\_TEXT\_FILE** | Указывается путь к файлу с пользовательским соглашением. |
| **Согласие пользователя** | | |
| Запрашивать согласие | **USER\_CONSENT** | [Y|N] Установленный флажок включает механизм согласия пользователя. |
| Соглашение | **USER\_CONSENT\_ID** | Задается текст соглашения, которое отображается пользователю при заказе. |
| Галка по умолчанию проставлена | **USER\_CONSENT\_IS\_CHECKED** | Установка галочки автомаитчески устанавливает галочку в чекбоксе согласия пользователя. То есть согласие применяется одновременно с нажатием кнопки Оформить заказ. |
| Загружать текст сразу | **USER\_CONSENT\_IS\_LOADED** | Текст соглашения будет выводиться сразу. Если флажок не установлен, для просмотра текст нужно будет кликнуть по кнопке согласия. |
| **Дополнительные настройки** | | |
| Страница для перехода после регистрации | **REDIRECT\_PAGE** | Указывается путь к странице, на которую будет переведен пользователь после регистрации. Этот адрес не должен совпадать с адресом страницы, на которой расположен компонент. В противном случае будет зацикливание. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Регистрация аффилиата**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:sale.affiliate.register",
	"",
	Array(
		"AGREEMENT_TEXT_FILE" => "",
		"REDIRECT_PAGE" => $_REQUEST["REDIRECT_PAGE"],
		"SET_TITLE" => "Y",
		"USER_CONSENT" => "Y",
		"USER_CONSENT_ID" => "1",
		"USER_CONSENT_IS_CHECKED" => "Y",
		"USER_CONSENT_IS_LOADED" => "N"
	)
);?>



```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх