# Тема (создание)

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

[Бизнес-процесс](/user_help/components/obschenie/buziness_process/index.php)

[Блоги](/user_help/components/obschenie/blogs/index.php)

[Социальная сеть](/user_help/components/obschenie/social_network/index.php)

[Форум](/user_help/components/obschenie/forum/index.php)

[Форум (комплексный компонент)](/user_help/components/obschenie/forum/forum_composite.php)
[Письмо](/user_help/components/obschenie/forum/forum_message_send.php)
[Подписка (список)](/user_help/components/obschenie/forum/forum_subscribe_list.php)
[Поиск](/user_help/components/obschenie/forum/forum_search.php)
[Пользователь (изменение профиля)](/user_help/components/obschenie/forum/forum_user_profile_edit.php)
[Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php)
[Пользователь (сообщения)](/user_help/components/obschenie/forum/forum_user_post.php)
[Пользователь (список пользователей)](/user_help/components/obschenie/forum/forum_user_list.php)
[PM (изменение)](/user_help/components/obschenie/forum/forum_pm_edit.php)
[PM (папки)](/user_help/components/obschenie/forum/forum_pm_folder.php)
[PM (поиск)](/user_help/components/obschenie/forum/forum_pm_search.php)
[PM (список)](/user_help/components/obschenie/forum/forum_pm_list.php)
[PM (чтение)](/user_help/components/obschenie/forum/forum_pm_read.php)
[Помощь](/user_help/components/obschenie/forum/forum_help.php)
[Правила](/user_help/components/obschenie/forum/forum_rules.php)
[Сообщения (перемещение)](/user_help/components/obschenie/forum/forum_message_move.php)
[Сообщения (проверка)](/user_help/components/obschenie/forum/forum_message_approve.php)
[Статистика](/user_help/components/obschenie/forum/forum_statistic.php)
[Темы](/user_help/components/obschenie/forum/forum_topic_last.php)
[Комментарии к инфоблоку](/user_help/components/obschenie/forum/forum_topic_reviews.php)
[Тема (создание)](/user_help/components/obschenie/forum/forum_topic_new.php)
[Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php)
[Темы (новые)](/user_help/components/obschenie/forum/forum_topic_active.php)
[Темы (перемещение)](/user_help/components/obschenie/forum/forum_topic_move.php)
[Темы (поиск)](/user_help/components/obschenie/forum/forum_topic_search.php)
[Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php)
[Форма создания сообщения](/user_help/components/obschenie/forum/forum_post_form.php)
[Форумы (список)](/user_help/components/obschenie/forum/forum_index.php)
[Шаблоны](/user_help/components/obschenie/forum/forum_interface.php)
[RSS форума](/user_help/components/obschenie/forum/forum_rss.php)
[Комментарии](/user_help/components/obschenie/forum/forum_comments.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Форум](/user_help/components/obschenie/forum/index.php)

Тема (создание)

**Недоступно в редакциях:**Старт

# Тема (создание)

### Описание **forum.topic.new**

Компонент служит для сохранения новой темы форума. Он ничего не выводит. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID форума | **FID** | Указывается идентификатор форума, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["FID"]}**. |
| ID темы | **TID** | Указывается идентификатор темы, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["TID"]}**. |
| Действие над сообщением | **MESSAGE\_TYPE** | Указывается переменная, в которой будет содержаться код действия над сообщением. По умолчанию поле содержит **={$\_REQUEST["MESSAGE\_TYPE"]}**. |
| **Шаблоны ссылок** | | |
| Страница списка форумов | **URL\_TEMPLATES\_INDEX** | Указывается адрес страницы со списком форумов. По умолчанию поле содержит **index.php**. Такая страница может быть создана с помощью компонента [Форумы (список)](/user_help/components/obschenie/forum/forum_index.php). |
| Страница списка тем | **URL\_TEMPLATES\_LIST** | Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php). |
| Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница чтения сообщения | **URL\_TEMPLATES\_MESSAGE** | Указывается адрес страницы чтения сообщения форума. По умолчанию поле содержит **message.php?FID=#FID#&TID=#TID#&MID=#MID#**. |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. | |
| Показывать навигацию | **SET\_NAVIGATION** | [Y|N] При отмеченной опции в навигационную цепочку будет добавлен пункт с заголовком страницы. |
| Использовать AJAX | **AJAX\_TYPE** | [Y|N] При отмеченной опции для компонента будет включен режим AJAX. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Новая тема**. |
| Показывать теги | **SHOW\_TAGS** | [Y|N] При отмеченной опции будут показаны теги. |
| **Настройки опросов** | | |
| Показывать опросы | **SHOW\_VOTE** | [Y|N] При отмеченной опции будет выведена форма создания опроса. Создание опроса доступно только при создании новой темы на форуме. При выборе данной опции станут активны дополнительные поля.     |  |  |  | | --- | --- | --- | | Группа опросов | **VOTE\_CHANNEL\_ID** | Указывается группа опросов, в которой будет создан опрос. | | Группа пользователей, которым разрешено создавать опросы | **VOTE\_GROUP\_ID** | Задаются группы пользователей, которым разрешено создавать опросы на форуме. | |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.topic.new","",Array(
		"SHOW_TAGS" => "Y",
		"FID" => $_REQUEST["FID"],
		"MID" => $_REQUEST["MID"],
		"MESSAGE_TYPE" => $_REQUEST["MESSAGE_TYPE"],
		"URL_TEMPLATES_INDEX" => "index.php",
		"URL_TEMPLATES_LIST" => "list.php?FID=#FID#",
		"URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#",
		"URL_TEMPLATES_MESSAGE" => "message.php?FID=#FID#&TID=#TID#&MID=#MID#",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"NAME_TEMPLATE" => "",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"SET_NAVIGATION" => "Y",
		"AJAX_TYPE" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0",
		"SET_TITLE" => "Y",
		"SHOW_VOTE" => "Y",
		"VOTE_CHANNEL_ID" => "2",
		"VOTE_GROUP_ID" => ""
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх