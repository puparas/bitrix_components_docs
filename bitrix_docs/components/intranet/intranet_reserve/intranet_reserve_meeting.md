# Бронирование переговорных (комплексный компонент)

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

Бронирование переговорных (комплексный компонент)

# Бронирование переговорных (комплексный компонент)

### Описание **intranet.reserve\_meeting**

Комплексный компонент выводит календарь занятости переговорных комнат, позволяет бронировать переговорные и управлять ими. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Бронирование переговорных*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается тип информационного блока, используемого для резервирования переговорных |
| Инфоблок | **IBLOCK\_ID** | Указывается инфоблок, используемый для хранения записей резервирования переговорных. |
| Группы пользователей, которые могут изменять переговорные | **USERGROUPS\_MODIFY** | Указываются группы пользователей, которым разрешено создавать и изменять переговорные. |
| Группы пользователей, которые могут резервировать переговорные | **USERGROUPS\_RESERVE** | Указываются группы пользователей, которые могут осуществлять резервирование переговорных комнат. |
| Группы пользователей, которые могут снимать резервирование переговорных | **USERGROUPS\_CLEAR** | Указываются группы пользователей, которые смогут отменять бронирование переговорных |
| Выходные дни недели | **WEEK\_HOLIDAYS** | Указываются выходные дни недели. Выбранные дни не будут отображаться в календаре переговорной, если в эти дни не зарезервированы переговорные. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включен режим поддержки ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить  следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - главная страница резервирования переговорных; * **meeting** - страница с графиком переговорной; * **modify\_meeting** - страница изменения переговорной; * **view\_item** - страница просмотра резервирования переговорной; * **reserve\_meeting** - страница резервирования переговорной; * **search** - страница поиска свободных переговорных. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| **Дополнительные настройки** | | |
| Устанавливать навигационную цепочку | **SET\_NAVCHAIN** | [Y|N] При отмеченной опции будет добавлен пункт с заголовком страницы в цепочку навигации. |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя | **SHOW\_LOGIN** | [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Шаблон пути к странице пользователя | **PATH\_TO\_USER** | Указывается шаблон пути к странице пользователя. |
| Страница отправки личного сообщения | **PM\_URL** | Указывается путь к странице отправки личного сообщения. |
| Шаблон пути к странице подразделения | **PATH\_TO\_CONPANY\_DEPARTMENT** | Указывается шаблон пути к странице подразделения компании. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты и времени, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Показывать год рождения | **SHOW\_YEAR** | Поле определяет кому показываеть год рождения:  * **всем** (**Y**); * **только мужчинам** (**M**); * **никому** (**N**). |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Список переговорных**. |
| Страница видеозвонка | **PATH\_TO\_VIDEO\_CALL** | Указывается шаблон пути к видеозвонку. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.reserve_meeting","",Array(
		"SEF_MODE" => "Y",
		"IBLOCK_TYPE" => "events",
		"IBLOCK_ID" => "17",
		"SET_NAVCHAIN" => "Y",
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"SHOW_LOGIN" => "Y",
		"PATH_TO_USER" => "/company/personal/user/#USER_ID#/",
		"PM_URL" => "/company/personal/messages/chat/#USER_ID#/",
		"PATH_TO_CONPANY_DEPARTMENT" => "/company/structure.php?set_filter_structure=Y&structure_UF_DEPARTMENT=#ID#",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"SHOW_YEAR" => "Y",
		"SET_TITLE" => "Y",
		"USERGROUPS_MODIFY" => array("1"),
		"USERGROUPS_RESERVE" => array("1"),
		"USERGROUPS_CLEAR" => array("1"),
		"WEEK_HOLIDAYS" => array("5", "6"),
		"PATH_TO_VIDEO_CALL" => "/company/personal/video/#USER_ID#/",
		"SEF_FOLDER" => "/",
		"SEF_URL_TEMPLATES" => Array(
			"index" => "index.php",
			"meeting" => "meeting/#meeting_id#/",
			"modify_meeting" => "meeting/#meeting_id#/modify/",
			"view_item" => "meeting/#meeting_id#/view/#item_id#/",
			"reserve_meeting" => "meeting/#meeting_id#/reserve/#item_id#/",
			"search" => "search/"
		),
		"VARIABLE_ALIASES" => Array(
			"index" => Array(),
			"meeting" => Array(),
			"modify_meeting" => Array(),
			"view_item" => Array(),
			"reserve_meeting" => Array(),
			"search" => Array(),
		)
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх