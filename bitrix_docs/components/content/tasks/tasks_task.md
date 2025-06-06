# Задача

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

Задача

# Задача

### Описание **tasks.task**

Компонент для создания, просмотра и редактирования задачи.

В визуальном редакторе компонент расположен по пути: *Контент > Задачи 2.0 > Задача*.

### Параметры

Существует параметр, не имеющий визуального отображения в форме настроек параметров компонента. С версии 20.6.0 (появление новых прав доступа) необходимо настраивать обязательный параметр компонента **ACTION**. Параметр может принимать значения `edit` или `view` в зависимости от того, на создание/редактирование или просмотр открывается задача.

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Выбрать связанные сущности | **SUB\_ENTITY\_SELECT** | Указываются сущности, которые будут связаны с задачей:  * Теги * Чек-лист * Напоминания * История изменений * Затраченное время * Шаблон повторения задачи * Зависимость в проекте * Связанные задачи * Данные планировщика задач |
| Выбрать дополнительные данные | **AUX\_DATA\_SELECT** | Выбираются дополнительные данные из списка:  * Время работы компании * Пользовательские поля * Шаблоны задач |
| **Источник данных** | | |
| Идентификатор задачи | **ID** | Прописывается ID задачи. |
| Идентификатор группы | **GROUP\_ID** | Указывается ID группы. |
| Идентификатор пользователя | **USER\_ID** | Указывается ID пользователя. |
| **Шаблоны ссылок** | | |
| Путь к задачам пользователя | **PATH\_TO\_USER\_TASKS** | Прописывается путь к списку задач пользователя. |
| Путь к списку задач | **PATH\_TO\_GROUP\_TASKS** | Прописывается путь к списку задач. |
| Путь к задаче | **PATH\_TO\_GROUP\_TASKS\_TASK** | Указывается путь к задаче. |
| Путь к профилю пользователя | **PATH\_TO\_USER\_PROFILE** | Указывается путь к профилю пользователя. |
| Путь к группе | **PATH\_TO\_GROUP** | Указывается путь к группе. |
| **Дополнительные настройки** | | |
| Включить цепочку навигации | **SET\_NAVCHAIN** | [Y|N] При отмеченной опции будет показана цепочка навигации. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции на каждой странице будет установлен заголовок **<имя\_пользователя>: Задачи** или **Мои задачи**. |
| Включить рейтинг | **SHOW\_RATING** | [Y|N] Включение функции отображения рейтинга. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |

### Пример вызова

```

 <?$APPLICATION->IncludeComponent(
	"bitrix:tasks.task",
	"",
	Array(
		"AUX_DATA_SELECT" => array(),
		"GROUP_ID" => "",
		"ID" => "",
		"PATH_TO_GROUP" => "",
		"PATH_TO_GROUP_TASKS" => "",
		"PATH_TO_GROUP_TASKS_TASK" => "",
		"PATH_TO_USER_PROFILE" => "",
		"PATH_TO_USER_TASKS" => "",
		"RATING_TYPE" => "",
		"REDIRECT_ON_SUCCESS" => "Y",
		"SET_NAVCHAIN" => "Y",
		"SET_TITLE" => "Y",
		"SHOW_RATING" => "Y",
		"SUB_ENTITY_SELECT" => array(),
		"ACTION"=>"edit",
		"USER_ID" => ""
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх