# Канбан задач

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

Канбан задач

# Канбан задач

### Описание **tasks.kanban**

Компонент для отображения задач

В визуальном редакторе компонент находится в *Контент > Задачи 2.0 > Канбан задач*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Шаблоны ссылок** | | |
| Путь к списку задач группы | **PATH\_TO\_GROUP\_TASKS** | Прописывается путь к списку задач группы. |
| Путь к задаче группы | **PATH\_TO\_GROUP\_TASKS\_TASK** | Указывается путь к задаче группы. |
| Путь к списку задач пользователя | **PATH\_TO\_USER\_TASKS** | Указывается путь к списку задач пользователя. |
| Путь к задаче пользователя | **PATH\_TO\_USER\_TASKS\_TASK** | Прописывается путь к задаче пользователя. |
| Путь к профилю пользователя | **PATH\_TO\_USER\_PROFILE** | Указывается путь к профилю пользователя. |
| **Дополнительные настройки** | | |
| Персональный канбан | **PERSONAL** | [Y|N] Включение виртуальной онлайн-доски для работы с проектами. |
| Идентификатор пользователя | **USER\_ID** | Указывается ID пользователя. |
| Идентификатор группы | **GROUP\_ID** | Прописывается ID группы. |
| Идентификатор группы | **GROUP\_ID** | Указывается ID группы. |
| Количество записей на странице | **ITEMS\_COUNT** | Параметр определяет количество задач отображаемых на одной странице. Остальные задачи будут выведены с помощью постраничной навигации. |
| Отображение имени | **NAME\_TEMPLATE** | Выбор формата отображения фамилии и имени. Указывается шаблон для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е. используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Ширина превью | **PREVIEW\_WIDTH** | Задается ширина канбана, отображаемого в предварительном просмотре. |
| Высота превью | **PREVIEW\_HEIGHT** | Задается высота канбана, отображаемого в предварительном просмотре. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции на каждой странице будет установлен заголовок **<имя\_пользователя>: Задачи** или **Мои задачи**. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent(
	"bitrix:tasks.kanban",
	"",
	Array(
		"GROUP_ID" => "",
		"ITEMS_COUNT" => "20",
		"NAME_TEMPLATE" => "",
		"PATH_TO_GROUP_TASKS" => "",
		"PATH_TO_GROUP_TASKS_TASK" => "",
		"PATH_TO_USER_PROFILE" => "",
		"PATH_TO_USER_TASKS" => "",
		"PATH_TO_USER_TASKS_TASK" => "",
		"PERSONAL" => "N",
		"PREVIEW_HEIGHT" => "150",
		"PREVIEW_WIDTH" => "200",
		"SET_TITLE" => "Y",
		"USER_ID" => ""
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх