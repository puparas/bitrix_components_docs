# PM (изменение)

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

PM (изменение)

**Недоступно в редакциях:**Старт

# PM (изменение)

### Описание **forum.pm.edit**

Компонент служит для создания нового или редактирования существующего персонального сообщения. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID сообщения | **MID** | Указывается код, в котором передается идентификатор сообщения. По умолчанию поле содержит **$\_REQUEST["MID"]**. |
| ID папки пользователя | **FID** | Указывается код, в котором передается идентификатор папки пользователя с личными сообщениями. По умолчанию поле содержит **$\_REQUEST["FID"]**. |
| ID пользователя | **UID** | Указывается код, в котором передается идентификатор пользователя. По умолчанию поле содержит **$\_REQUEST["UID"]**. |
| Тип сообщения | **MODE** | Указывается тип сообщения. Возможные варианты зачения параметра:  * **REPLY** - ответ; * **EDIT** - редактирование; * **NEW** - новое сообщение. |
| **Шаблоны ссылок** | | |
| Страница списка персональных сообщений | **URL\_TEMPLATES\_PM\_LIST** | Указывается адрес страницы со списком персональных сообщений. По умолчанию поле содержит **pm\_list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [PM (список)](/user_help/components/obschenie/forum/forum_pm_list.php). |
| Страница чтения персонального сообщения | **URL\_TEMPLATES\_PM\_READ** | Указывается адрес страницы чтения персонального сообщения. По умолчанию поле содержит **pm\_read.php?MID=#MID#**. Такая страница может быть создана с помощью компонента [PM (чтение)](/user_help/components/obschenie/forum/forum_pm_read.php). |
| Страница редактирования (создания) персонального сообщения | **URL\_TEMPLATES\_PM\_EDIT** | Указывается адрес страницы редактирования (создания) персонального сообщения. По умолчанию поле содержит **pm\_edit.php?MID=#MID#**. |
| Страница поиска пользователя | **URL\_TEMPLATES\_PM\_SEARCH** | Указывается адрес страницы поиска пользователя. По умолчанию поле содержит **pm\_search.php?MID=#MID#**. Такая страница может быть создана с помощью компонента [PM (поиск)](/user_help/components/obschenie/forum/forum_pm_search.php). |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| По умолчанию показывать невизуальный режим редактора | **EDITOR\_CODE\_DEFAULT** | [Y|N] При отмеченной опции при создании или редактировании сообщения будет включен режим показа BB-кодов. (Пример: [B]сообщение[/B] вместо **сообщение**). |
| Показывать навигацию | **SET\_NAVIGATION** | [Y|N] При отмеченной опции будет добавлен пункт с заголовком страницы в цепочку навигации. |
| Формат имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. | |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено:  * **Новое** при создании нового сообщения и при ответе на сообщение; * **<тема\_сообщения> (редактирование)** при изменении сообщения. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.pm.edit","",Array(
		"MID" => $_REQUEST["MID"],
		"FID" => $_REQUEST["FID"],
		"UID" => $_REQUEST["UID"],
		"MODE" => $_REQUEST["MODE"],
		"URL_TEMPLATES_PM_LIST" => "pm_list.php?FID=#FID#",
		"URL_TEMPLATES_PM_READ" => "pm_read.php?MID=#MID#",
		"URL_TEMPLATES_PM_EDIT" => "pm_edit.php?MID=#MID#",
		"URL_TEMPLATES_PM_SEARCH" => "pm_search.php?MID=#MID#",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"NAME_TEMPLATE" => "",
		"SET_NAVIGATION" => "Y",
		"EDITOR_CODE_DEFAULT" => "N",    
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0",
		"SET_TITLE" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх