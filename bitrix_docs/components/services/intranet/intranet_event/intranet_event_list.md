# Список событий календаря

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

[Видеоконференции (КП)](/user_help/components/services/video/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

[Расчетные листки сотрудников](/user_help/components/services/intranet/payroll_1c.php)
[Интерфейс 1с 8.2](/user_help/components/services/intranet/intranet_1c82_interface.php)
[Импорт оргструктуры из 1С:ЗУП](/user_help/components/services/intranet/intranet_users_import_1c.php)
[Импорт оргструктуры из 1С:ЗУП (hrxml)](/user_help/components/services/intranet/intranet_users_import.1c_hrxml.php)

[Задачи 1.0](/user_help/components/services/intranet/intranet_tasks/index.php)

[Календарь событий](/user_help/components/services/intranet/intranet_event/index.php)

[Календарь событий](/user_help/components/services/intranet/intranet_event/intranet_event_calendar.php)
[Список событий календаря](/user_help/components/services/intranet/intranet_event/intranet_event_list.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Контроллер](/user_help/components/services/controller/index.php)

[Частые вопросы](/user_help/components/services/faq/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

...

[Сервисы](/user_help/components/services/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

[Календарь событий](/user_help/components/services/intranet/intranet_event/index.php)

Список событий календаря

# Список событий календаря

### Описание **intranet.event\_list**

Компонент выводит список ближайших событий календаря. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Контент > Календарь событий*.

**Внимание!** Компонент устарел, рекомендуется использовать новый компонент [Список событий календаря 2.0](/user_help/components/content/calendar/calendar_event_list.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Показывать события текущего пользователя | **B\_CUR\_USER\_LIST** | [Y|N] При отмеченной опции будут показаны события календаря текущего пользователя.   Если опция не отмечена (параметр принимает значение **N**), то необходимо настроить следущие параметры: **IBLOCK\_TYPE**, **IBLOCK\_ID** и **IBLOCK\_SECTION\_ID**. |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблока указывается идентификатор информационного блока, события календарей которого будут выводиться. |
| ID секции инфоблока | **IBLOCK\_SECTION\_ID** | В поле указывается код, в котором передается идентификатор календаря (раздела инфоблока), события которого будут отображены. |
| Дата инициализации | **INIT\_DATE** | Если в параметре указана дата, то список ближайших событий будет выведен для заданной даты. В противном случае список ближайших событий календаря будет отображен для текущей даты. |
| Показывать ближайшие события за количество месяцев | **FUTURE\_MONTH\_COUNT** | Указывается количество месяцев, за которые будут отображены ближайшие события. |
| Адрес страницы для детального просмотра | **DETAIL\_URL** | Указывается адрес страницы для детального просмотра события календаря. |
| Количество событий в списке | **EVENTS\_COUNT** | Указывается количество событий, которые будут отображены в списке ближайших событий. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```
<$APPLICATION->IncludeComponent("bitrix:intranet.event_list","",Array(
		"B_CUR_USER_LIST" => "N",
		"IBLOCK_TYPE" => "events",
		"IBLOCK_ID" => "13",
		"IBLOCK_SECTION_ID" => "",
		"INIT_DATE" => "--текущая дата--",
		"FUTURE_MONTH_COUNT" => "2",
		"DETAIL_URL" => "",
		"EVENTS_COUNT" => "5",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх