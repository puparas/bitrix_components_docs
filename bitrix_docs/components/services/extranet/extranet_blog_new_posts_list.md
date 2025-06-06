# Последние сообщения всех блогов экстранета

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

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Последние сообщения всех блогов экстранета](/user_help/components/services/extranet/extranet_blog_new_posts_list.php)
[Форма инициализации регистрации](/user_help/components/services/extranet/system_auth_initialize.php)
[Экстранет - создание группы (комплексный компонент)](/user_help/components/services/extranet/extranet_group_create.php)

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

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

Последние сообщения всех блогов экстранета

# Последние сообщения всех блогов экстранета

### Описание **extranet.blog.new\_posts.list**

Компонент выводит последние сообщения блогов сайта экстранета с постраничной навигацией. Компонент является стандартным и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Общение > Блоги > Последние сообщения всех блогов экстранета*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Группа блогов для отображения | **GROUP\_ID** | Указывается группа блогов, последние сообщения которых будут отображены. Если не указано, то выборка производится по всем группам блогов сайта экстранета. |
| **Внешний вид** | | |
| Количество результатов, выводимых на страницу | **MESSAGE\_PER\_PAGE** | Указывается число последних сообщений блогов, отображаемых на одной странице. Все последние сообщения блогов будут выведены с помощью постраничной навигации. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт *(другое)->*, можно сформировать свой вариант на основании php-функции **date**. |
| Имя шаблона для постраничной навигации | **NAV\_TEMPLATE** | Указывается имя шаблона для постраничной навигации. |
| **Шаблоны ссылок** | | |
| Шаблон пути к странице блога | **PATH\_TO\_BLOG** | Указывается шаблон пути к главной странице блога. |
| Шаблон пути к странице с сообщением блога | **PATH\_TO\_POST** | Указывается шаблон пути к странице детального просмотра сообщения блога. |
| Шаблон пути к странице пользователя блога | **PATH\_TO\_USER** | Указывается шаблон пути к странице профиля пользователя блога. |
| Шаблон пути к странице с сообщением блога группы | **PATH\_TO\_GROUP\_BLOG\_POST** | Указывается шаблон пути к странице с сообщением блога группы. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Путь к папке со смайликами относительно корня сайта | **PATH\_TO\_SMILE** | Указывается путь к папке со смайликами относительно корня сайта. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено . |
| Отображение имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя | **SHOW\_LOGIN** | [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Шаблон пути к странице пользователя соцсети | **PATH\_TO\_SONET\_USER\_PROFILE** | Указывается шаблон пути к странице пользователя соцсети. |
| Шаблон пути к чату с пользователем | **PATH\_TO\_MESSAGES\_CHAT** | Указывается шаблон пути к странице чата с пользователем. |
| Шаблон пути к странице подразделения | **PATH\_TO\_CONPANY\_DEPARTMENT** | Указывается шаблон пути к странице подразделения компании. |
| **Имена переменных** | | |
| Имя переменной для идентификатора блога | **BLOG\_VAR** | Указывается имя переменной, которой передается идентификатор блога. |
| Имя переменной для идентификатора сообщения блога | **POST\_VAR** | Указывается имя переменной, которой передается идентификатор сообщения блога. |
| Имя переменной для идентификатора пользователя блога | **USER\_VAR** | Указывается имя переменной, которой передается идентификатор пользователя блога. |
| Имя переменной для страницы | **PAGE\_VAR** | Указывается имя переменной, которой передается страница блога. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:extranet.blog.new_posts.list","",Array(
		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",
		"SHOW_LOGIN" => "Y",
		"PATH_TO_SONET_USER_PROFILE" => "/extranet/contacts/personal/user/#user_id#/",
		"PATH_TO_MESSAGES_CHAT" => "/extranet/contacts/personal/messages/chat/#user_id#/",
		"PATH_TO_VIDEO_CALL" => "/extranet/contacts/personal/video/#user_id#/",
		"PATH_TO_CONPANY_DEPARTMENT" => "/company/structure.php?set_filter_structure=Y&structure_UF_DEPARTMENT=#ID#",
		"MESSAGE_PER_PAGE" => "6",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"PATH_TO_BLOG" => "blog_blog.php?page=blog&blog=#blog#",
		"PATH_TO_POST" => "blog_post.php?page=post&blog=#blog&post_id=#post_id#",
		"PATH_TO_USER" => "blog_user.php?page=user&user_id=#user_id#",
		"PATH_TO_GROUP_BLOG_POST" => "",
		"PATH_TO_SMILE" => "/bitrix/images/blog/smile/",
		"BLOG_VAR" => "blog",
		"POST_VAR" => "post_id",
		"USER_VAR" => "user_id",
		"PAGE_VAR" => "page",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "86400",
		"GROUP_ID" => "1",
		"NAV_TEMPLATE" => "",
		"SET_TITLE" => "Y"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх