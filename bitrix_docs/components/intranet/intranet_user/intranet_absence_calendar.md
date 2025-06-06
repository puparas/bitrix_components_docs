# Календарь отсутствий

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

[HR](/user_help/components/intranet/intranet_user/index.php)

[Календарь отсутствий](/user_help/components/intranet/intranet_user/intranet_absence_calendar.php)
[Отсутствующие сотрудники](/user_help/components/intranet/intranet_user/intranet_structure_informer_absent.php)
[Доска почета](/user_help/components/intranet/intranet_user/intranet_structure_honour.php)
[Доска почета пользователя](/user_help/components/intranet/intranet_user/intranet_structure_honour_user.php)
[Отсутствия пользователя](/user_help/components/intranet/intranet_user/intranet_absence_user.php)
[Кадровые изменения](/user_help/components/intranet/intranet_user/intranet_structure_events.php)
[Новые сотрудники](/user_help/components/intranet/intranet_user/intranet_structure_informer_new.php)
[Дни рождения](/user_help/components/intranet/intranet_user/intranet_structure_birthday_nearest.php)

[Бронирование переговорных](/user_help/components/intranet/intranet_reserve/index.php)

[Оргструктура](/user_help/components/intranet/intranet_search/index.php)

[Собрания и планерки](/user_help/components/intranet/meetings/index.php)

[Учет рабочего времени](/user_help/components/intranet/timeman/index.php)

[Руководство подразделениями](/user_help/components/intranet/intranet_structure_head_user.php)

[Сайты 24](/user_help/components/landing/index.php)

[Контент](/user_help/components/content/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Корпоративный портал (КП)](/user_help/components/intranet/index.php)

[HR](/user_help/components/intranet/intranet_user/index.php)

Календарь отсутствий

# Календарь отсутствий

### Описание **intranet.absence.calendar**

Компонент выводит график отсутствий сотрудников в виде календаря. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > HR*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Начальное представление | **VIEW\_START** | Указывается закладка календаря графика отсутствий, которая будет открыта при обращении к графику:  * **день** (**day**); * **неделя** (**week**); * **месяц** (**month**). |
| Отображаемые элементы управления | **FILTER\_CONTROLS** | Указываются элементы, которые будут отображены на панели управления графиком отсутствий:  * **переход к дате** (**DATEPICKER**); * **типы отсутствий** (**TYPEFILTER**); * **только отсутствующие** (**SHOW\_ALL**); * **подразделения** (**DEPARTMENT**). |
| Первый день недели | **FIRST\_DAY** | Указывается первый день недели. |
| Начало рабочего дня (час) | **DAY\_START** | Указывается время (час) начала рабочего дня. |
| Конец рабочего дня (час) | **DAY\_FINISH** | Указывается время (час) окончания рабочего дня. |
| Показывать нерабочее время в дневном представлении | **DAY\_SHOW\_NONWORK** | [Y|N] При отмеченной опции нерабочее время будет показано в дневном представлении. |
| Формат показа даты | **DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат показа даты/времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.absence.calendar","",Array(
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"VIEW_START" => "month",
		"FILTER_CONTROLS" => Array("DATEPICKER", "TYPEFILTER", "DEPARTMENT"),
		"FIRST_DAY" => "1",
		"DAY_START" => "9",
		"DAY_FINISH" => "18",
		"DAY_SHOW_NONWORK" => "Y"
		"DATE_FORMAT" => "d.m.Y",
		"DATETIME_FORMAT" => "d.m.Y H:i:s"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх