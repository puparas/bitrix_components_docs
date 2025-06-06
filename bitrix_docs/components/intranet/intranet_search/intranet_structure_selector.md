# Форма поиска

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

Форма поиска

# Форма поиска

### Описание **intranet.structure.selector**

Компонент выводит форму фильтрации списка сотрудников. Компонент содержит шаблоны: (**.default**), (**.alphabet**), (**.include\_area**), (**online**), (**.sections**). Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Оргструктура*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Страница списка пользователей | **LIST\_URL** | Указывается путь к странице со списком пользователей. |
| **Параметры фильтра** | | |
| Имя фильтра | **FILTER\_NAME** | Указывается имя фильтра. |
| Выбор подразделения для фильтрации | **FILTER\_DEPARTMENT\_SINGLE** | Указывается способ выбора подразделения(ий) в форме поиска:  * **одинарный** (**Y**) - в выпадающем списке можно выбрать только одно подразделение; * **множественный** (**N**) - поле позволяет выбирать несколько подразделений. |
| Запоминать фильтр в сессии | **FILTER\_SESSION** | [Y|N] При отмеченной опции введенные значения в поля формы поиска будут запоминаться системой. |
| **Дополнительно (данный список настроек доступен для шаблона **.sections**)** | | |
| Количество колонок | **COLUMNS** | Указывается количество колонок в секции. |
| Количество колонок на первой странице | **COLUMNS\_FIRST** | Указывается количество колонок на первой странице. |
| Максимальная глубина дерева (0 - все) | **MAX\_DEPTH** | Указывается максимальная глубина дерева. |
| Максимальная глубина дерева на первой странице (0 - все) | **MAX\_DEPTH\_FIRST** | Указывается максимальная глубина дерева на первой странице. |
| Выводить информацию о подразделении | **SHOW\_SECTION\_INFO** | [Y|N] При отмеченной опции в результах поиска будет выводиться информация о подразделении. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:intranet.structure.selector","sections",Array(
		"COLUMNS" => "2",
		"COLUMNS_FIRST" => "2",
		"MAX_DEPTH" => "2",
		"MAX_DEPTH_FIRST" => "0",
		"SHOW_SECTION_INFO" => "Y",
		"LIST_URL" => "users_list.php", 
		"FILTER_NAME" => "users", 
		"FILTER_DEPARTMENT_SINGLE" => "Y", 
		"FILTER_SESSION" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх