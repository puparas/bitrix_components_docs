# Просмотр задачи

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

[Агрегатор библиотек документов (КП)](/user_help/components/content/webdav/index.php)

[Задачи 2.0 (КП)](/user_help/components/content/tasks/index.php)

[Задача](/user_help/components/content/tasks/tasks_task.php)
[Задачи](/user_help/components/content/tasks/tasks_list.php)
[Изменение шаблона](/user_help/components/content/tasks/template_edit.php)
[Просмотр задачи](/user_help/components/content/tasks/task_detail.php)
[Шаблоны](/user_help/components/content/tasks/templates_list.php)
[Тема (отзывы)](/user_help/components/content/tasks/topic_reviews.php)
[Канбан задач](/user_help/components/content/tasks/tasks_kanban.php)

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

[Фотогалерея](/user_help/components/content/photogallery/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

[Google Maps](/user_help/components/content/google_maps/index.php)

[Highload инфоблоки](/user_help/components/content/highload/index.php)

[RSS](/user_help/components/content/rss/index.php)

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Медиа](/user_help/components/content/media/index.php)

[Яндекс.Карты](/user_help/components/content/yandex_map/index.php)

[Обмен с 1С](/user_help/components/content/1c_exchange/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Задачи 2.0 (КП)](/user_help/components/content/tasks/index.php)

Просмотр задачи

# Просмотр задачи

### Описание **tasks.task.detail**

Компонент служит для отображения задачи.

В визуальном редакторе компонент расположен по пути: *Контент > Задачи 2.0 > Просмотр задачи*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Свойства задачи | **TASKS\_FIELDS\_SHOW** | Указываются поля, которые должны быть отображены при показе задач. |
| Тип задач | **TASK\_TYPE** | Указывается тип задач: **Для группы** (**group**) или **Для пользователя** (**user**). |
| **Шаблоны ссылок** | | |
| Путь к списку задач | **PATH\_TO\_GROUP\_TASKS** | Указывается путь к списку задач. |
| Путь к задаче | **PATH\_TO\_GROUP\_TASKS\_TASK** | Указывается путь к задаче. |
| Путь к представлению | **PATH\_TO\_GROUP\_TASKS\_VIEW** | Указывается путь к представлению задачи. |
| Путь к странице пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается путь к странице пользователя. |
| **Дополнительные настройки** | | |
| Путь к папке со смайликами для форума относительно корня сайта | **PATH\_TO\_FORUM\_SMILE** | Указывается путь к папке со смайлами. По умолчанию указано **/bitrix/images/forum/smile/**. |
| Выводить рейтинг | **SHOW\_RATING** | [Y|N] При отмеченной опции будет включен функционал рейтинга. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |
| Включить цепочку навигации | **SET\_NAVCHAIN** | [Y|N] При отмеченной опции будет показана цепочка навигации. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции на каждой странице будет установлен заголовок **Задача №<номер\_задачи>**. |
| Количество записей на странице | **ITEMS\_COUNT** | [Y|N] Параметр определяет количество задач отображаемых на одной странице. Остальные задачи будут выведены с помощью постраничной навигации. |
| **Псевдонимы переменных** | | |
| Имя переменной для кода задачи | **TASK\_VAR** | Поле содержит имя переменной для кода задачи. |
| Имя переменной для кода пользователя | **USER\_VAR** | Поле содержит имя переменной для кода пользователя. |
| Имя переменной для кода группы | **GROUP\_VAR** | Поле содержит имя переменной для кода группы. |
| Имя переменной для кода действия | **ACTION\_VAR** | Поле содержит имя переменной для кода действия. |
| Имя переменной для кода страницы | **PAGE\_VAR** | Поле содержит имя переменной для кода страницы. |

### Пример вызова

```

 <?$APPLICATION->IncludeComponent(
	"bitrix:tasks.task.detail",
	"",
	Array(
		"TASKS_FIELDS_SHOW" => array(),
		"TASK_TYPE" => "group",
		"TASK_VAR" => "task_var",
		"USER_VAR" => "user_var",
		"GROUP_VAR" => "grouop_var",
		"ACTION_VAR" => "action_var",
		"PAGE_VAR" => "page_var",
		"PATH_TO_GROUP_TASKS" => "/workgroups/group/#group_id#/tasks/",
		"PATH_TO_GROUP_TASKS_TASK" => "/workgroups/group/#group_id#/tasks/task/view/#task_id#/",
		"PATH_TO_GROUP_TASKS_VIEW" => "",
		"PATH_TO_FORUM_SMILE" => "/bitrix/images/forum/smile/",
		"URL_TEMPLATES_PROFILE_VIEW" => "",
		"SHOW_RATING" => "",
		"RATING_TYPE" => "",
		"SET_NAVCHAIN" => "Y",
		"SET_TITLE" => "Y",
		"ITEMS_COUNT" => "20"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх