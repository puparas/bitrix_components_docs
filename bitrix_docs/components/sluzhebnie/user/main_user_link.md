# Имя пользователя с тултипом

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

[Служебные](/user_help/components/sluzhebnie/index.php)

[navigation](/user_help/components/sluzhebnie/navigation/index.php)

[Безопасность](/user_help/components/sluzhebnie/security/index.php)

[Включаемые области](/user_help/components/sluzhebnie/included_regions/index.php)

[Поиск](/user_help/components/sluzhebnie/search/index.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

[Имя пользователя с тултипом](/user_help/components/sluzhebnie/user/main_user_link.php)
[Настраиваемая регистрация](/user_help/components/sluzhebnie/user/main_register.php)
[Параметры пользователя](/user_help/components/sluzhebnie/user/main_profile.php)
[Запрос согласия пользователя](/user_help/components/sluzhebnie/user/main_userconsent_request.php)
[Компонент для авторизации виджета Битрикс24.Онлайн-чат](/user_help/components/sluzhebnie/user/b24connector_openline_info.php)
[Пароли приложений](/user_help/components/sluzhebnie/user/main_app_passwords.php)
[Управление объединением профилей](/user_help/components/sluzhebnie/user/socserv_auth_split.php)
[Форма авторизации](/user_help/components/sluzhebnie/user/system_auth_form.php)
[Форма инициализации регистрации](/user_help/components/sluzhebnie/user/system_auth_initialize.php)
[Форма отписки от писем](/user_help/components/sluzhebnie/user/main_mail_unsubscribe.php)
[Форма подтверждения регистрации](/user_help/components/sluzhebnie/user/system_auth_confirmation.php)

[Статистика](/user_help/components/sluzhebnie/statistic/index.php)

[Соц. закладки и сети](/user_help/components/sluzhebnie/main_share.php)
[Упрощенный HTML-редактор](/user_help/components/sluzhebnie/fileman_light_editor.php)
[Форма обратной связи](/user_help/components/sluzhebnie/main_feedback.php)
[Элемент управления "Календарь"](/user_help/components/sluzhebnie/main_calendar.php)
[Элемент управления "Палитра"](/user_help/components/sluzhebnie/main_colorpicker.php)
[Элемент управления "Часы"](/user_help/components/sluzhebnie/main_clock.php)
[Журнал изменений](/user_help/components/sluzhebnie/event_list.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Пользователь](/user_help/components/sluzhebnie/user/index.php)

Имя пользователя с тултипом

# Имя пользователя с тултипом

### Описание **main.user.link**

Компонент выводит имя пользователя с всплывающей подсказкой (тултипом), который содержит информацию о пользователе социальной сети. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Служебные > Пользователь > Имя пользователя с тултипом*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Идентификатор пользователя | **ID** | Параметр содержит код, в котором передается идентификатор пользователя социальной сети. |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя | **SHOW\_LOGIN** | [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Отображать личное фото в списке | **USE\_THUMBNAIL\_LIST** | [Y|N] При отмеченной опции личное фото будет отображено в списке пользователей. |
| Показывать поля пользователя | **SHOW\_FIELDS** | Указываются пользовательские свойства, которые будут отображены в тултипе в публичной части. |
| Показывать доп. свойства | **USER\_PROPERTY** | Указываются дополнительные пользовательские свойства, которые будут отображены в тултипе в публичной части. |
| Путь к странице пользователя | **PATH\_TO\_SONET\_USER\_PROFILE** | Задается путь к странице профиля пользователя социальной сети. |
| **Внешний вид** | | |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт *(другое)->*, можно сформировать свой вариант на основании php-функции **date**. |
| **Шаблоны ссылок** | | |
| Шаблон пути к странице пользователя | **PROFILE\_URL** | Задается шаблон пути к странице профиля пользователя социальной сети. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Показывать год рождения | **SHOW\_YEAR** | Поле определяет кому показываеть год рождения:  * **всем** (**Y**); * **только мужчинам** (**M**); * **никому** (**N**). |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:main.user.link","",Array(
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "7200",
		"ID" => "",
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"SHOW_LOGIN" => "Y",
		"THUMBNAIL_LIST_SIZE" => "30",
		"THUMBNAIL_DETAIL_SIZE" => "100",
		"USE_THUMBNAIL_LIST" => "Y",
		"SHOW_FIELDS" => Array("PERSONAL_BIRTHDAY", "PERSONAL_ICQ", "PERSONAL_PHOTO", "PERSONAL_CITY", "WORK_COMPANY", "WORK_POSITION"),
		"USER_PROPERTY" => Array("UF_USER_CAR_DEMO"),
		"PATH_TO_SONET_USER_PROFILE" => "",
		"PROFILE_URL" => "",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"SHOW_YEAR" => "Y"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх