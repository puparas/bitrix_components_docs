# Визуальная структура компании

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

Визуальная структура компании

# Визуальная структура компании

### Описание **intranet.structure.visual**

Компонент выводит визуальное представление древовидной структуры компании. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Корпоративный портал > Оргструктура > Визуальная структура компании*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Страница структуры компании | **DETAIL\_URL** | Указывается путь к странице структуры компании. |
| Страница профиля пользователя | **PROFILE\_URL** | Указывается путь к странице с профиля пользователя. |
| Страница отправки личного сообщения | **PM\_URL** | Указывается путь к странице отправки личного сообщения. |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя | **SHOW\_LOGIN** | [Y|N] При отмеченной опции будет выводиться логин, если не указано имя в профиле пользователя. |
| Выводить всплывающие информационные карточки пользователей | **USE\_USER\_LINK** | [Y|N] При отмеченной опции будут выводиться всплывающие информационные карточки сотрудников компании. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:intranet.structure.visual","",Array(
		"DETAIL_URL" => "/company/structure.php?set_filter_structure=Y&structure_UF_DEPARTMENT=#ID#",
		"PROFILE_URL" => "/company/personal/user/#ID#/",
		"PM_URL" => "/company/personal/messages/chat/#ID#/",
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"USE_USER_LINK" => "Y",
		"SHOW_LOGIN" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"PATH_TO_VIDEO_CALL" => "/company/personal/video/#USER_ID#/"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх