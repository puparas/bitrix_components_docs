# Список сотрудников

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

[Бронирование переговорных](/user_help/components/intranet/intranet_reserve/index.php)

[Оргструктура](/user_help/components/intranet/intranet_search/index.php)

[Поиск сотрудника (комплексный компонент)](/user_help/components/intranet/intranet_search/intranet_search.php)
[Структура компании (комплексный компонент)](/user_help/components/intranet/intranet_search/intranet_structure.php)
[Визуальная структура компании](/user_help/components/intranet/intranet_search/intranet_structure_visual.php)
[Список сотрудников](/user_help/components/intranet/intranet_search/intranet_structure_list.php)
[Форма поиска](/user_help/components/intranet/intranet_search/intranet_structure_selector.php)

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

[Оргструктура](/user_help/components/intranet/intranet_search/index.php)

Список сотрудников

# Список сотрудников

### Описание **intranet.structure.list**

Компонент выводит список сотрудников, удовлетворяющих внешнему фильтру. Компонент содержит два шаблона: (**.default**) и (**.list**).Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Оргструктура*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Выводить только синхронизируемых с 1С пользователей | **FILTER\_1C\_USERS** | [Y|N] При отмеченной опции будут выводиться только синхронизируемые с 1С пользователи. |
| Фильтр по подразделениям | **FILTER\_SECTION\_CURONLY** | Указывается тип фильтра по подразделениям:  * **прямой** (**Y**); * **рекурсивный** (**N**). |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Выводить уведомление при пустом списке | **SHOW\_ERROR\_ON\_NULL** | [Y|N] При отмеченной опции будет выводиться уведомление при пустом списке. |
| Количество пользователей на страницу | **USERS\_PER\_PAGE** | Поле определяет количество пользователей, отображаемых на одной странице. Весь список будет отображен с помощью постраничной навигации. |
| Подпись постраничной навигации | **NAV\_TITLE** | Указывается подпись для постраничной навигации. |
| Показывать постраничную навигацию над списком | **SHOW\_NAV\_TOP** | [Y|N] При отмеченной опции постраничная навигация будет показываться над списком. |
| Показывать постраничную навигацию под списком | **SHOW\_NAV\_BOTTOM** | [Y|N] При отмеченной опции постраничная навигация будет показываться под списком. |
| Показывать список при пустом фильтре | **SHOW\_UNFILTERED\_LIST** | [Y|N] Если условия поиска не заданы, то при отмеченной опции будет выведен весь список сотрудников. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Вывести руководителя при фильтре по подразделению | **SHOW\_DEP\_HEAD\_ADDITIONAL** | [Y/N] При отмеченной опции в фильтре по подразделению будет отображен руководитель подразделения. |
| Параметры для вывода в списке | **USER\_PROPERTY** | Указываются поля пользователей, которые будут показаны в визитных карточках сотрудников. |
| Параметры для вывода в Excel | **USER\_PROPERTY\_EXCEL** | Указываются поля пользователей, которые должны быть выгружены при выполнении экспорта пользователей в MS Excel. |
| Страница отправки личного сообщения | **PM\_URL** | Указывается путь к странице отправки личного сообщения.   Данное поле доступно только для шаблона **.list**. |
| Дополнительные поля для вывода | **USER\_PROPERTY** | Указываются, какие поля будут выводиться в списке сотрудников, удовлетворяющих внешнему фильтру.   Данное поле доступно только для шаблона **.list**. |
| **Параметры фильтра** | | |
| Имя фильтра | **FILTER\_NAME** | Указывается имя фильтра. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.structure.list","",Array(
		"USER_PROPERTY" => Array("FULL_NAME", "EMAIL", "PERSONAL_PHONE", "WORK_POSITION", "UF_DEPARTMENT"),
		"USER_PROPERTY_EXCEL" => Array("FULL_NAME", "EMAIL", "PERSONAL_PHONE", "WORK_POSITION", "UF_DEPARTMENT"),
		"FILTER_NAME" => "users",
		"FILTER_1C_USERS" => "Y",
		"FILTER_SECTION_CURONLY" => "N",
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"SHOW_ERROR_ON_NULL" => "Y",
		"USERS_PER_PAGE" => "10",
		"NAV_TITLE" => "Сотрудники",
		"SHOW_NAV_TOP" => "Y",
		"SHOW_NAV_BOTTOM" => "Y",
		"SHOW_UNFILTERED_LIST" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх