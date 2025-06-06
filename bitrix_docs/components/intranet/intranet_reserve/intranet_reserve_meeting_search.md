# Поиск переговорных

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

[Бронирование переговорных (комплексный компонент)](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting.php)
[Меню](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_menu.php)
[Переговорная](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_meeting.php)
[Поиск переговорных](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_search.php)
[Просмотр резервирования](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_view_item.php)
[Резервирование переговорной](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_reserve.php)
[Создание переговорной](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_add.php)
[Список переговорных](/user_help/components/intranet/intranet_reserve/intranet_reserve_meeting_list.php)

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

[Бронирование переговорных](/user_help/components/intranet/intranet_reserve/index.php)

Поиск переговорных

# Поиск переговорных

### Описание **intranet.reserve\_meeting.search**

Компонент служит для поиска переговорных. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Бронирование переговорных*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается тип информационного блока, используемого для резервирования переговорных. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор инфоблока, используемый для резервирования переговорных. |
| **Шаблоны ссылок** | | |
| Путь к графику переговорной | **PATH\_TO\_MEETING** | Указывается путь к странице с графиком переговорной от корня сайта. |
| Путь к странице резервирования переговорных | **PATH\_TO\_RESERVE\_MEETING** | Указывается путь к странице резервирования переговорной от корня сайта. |
| **Дополнительные настройки** | | |
| Устанавливать навигационную цепочку | **SET\_NAVCHAIN** | [Y|N] При отмеченной опции будет добавлен пункт с заголовком страницы в цепочку навигации. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Поиск переговорных**. |
| **Псевдонимы переменных** | | |
| Имя переменной для страницы | **PAGE\_VAR** | Указывается имя переменной, используемой для идентификации страницы. |
| Имя переменной для идентификатора переговорной | **MEETING\_VAR** | Указывается имя переменной, используемой для идентификации переговорной. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.reserve_meeting.search","",Array(
		"IBLOCK_TYPE" => "events",
		"IBLOCK_ID" => "16",
		"PAGE_VAR" => "",
		"MEETING_VAR" => "",
		"PATH_TO_MEETING" => "",
		"PATH_TO_RESERVE_MEETING" => "",
		"SET_NAVCHAIN" => "Y",
		"SET_TITLE" => "Y"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх