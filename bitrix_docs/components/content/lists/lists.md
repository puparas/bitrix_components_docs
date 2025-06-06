# Универсальные списки

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

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

[Фотогалерея](/user_help/components/content/photogallery/index.php)

[Фотогалерея 2.0](/user_help/components/content/photogallery2/index.php)

[Каталог](/user_help/components/content/catalog/index.php)

[Универсальные списки](/user_help/components/content/lists/index.php)

[Универсальные списки](/user_help/components/content/lists/lists.php)
[Списки](/user_help/components/content/lists/lists_lists.php)
[Список](/user_help/components/content/lists/lists_list.php)
[Разделы списка](/user_help/components/content/lists/lists_sections.php)
[Редактирование элемента](/user_help/components/content/lists/lists_element_edit.php)
[Настройки списка](/user_help/components/content/lists/lists_list_edit.php)
[Поля списка](/user_help/components/content/lists/lists_fields.php)
[Настройки поля списка](/user_help/components/content/lists/lists_field_edit.php)
[Навигационная цепочка](/user_help/components/content/lists/lists_element_navchain.php)
[Меню списков](/user_help/components/content/lists/lists_menu.php)
[Скачивание файла](/user_help/components/content/lists/lists_file.php)

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

Универсальные списки

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Универсальные списки

### Описание **lists**

Комплексный компонент позволяет вести полнофункциональную работу с универсальными списками, создавая физически только одну страницу. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Универсальные списки > Универсальные списки*.

Компонент относится к модулю [Универсальные списки](/user_help/content/lists/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE\_ID** | Указывается тип информационных блоков, в котором будут храниться универсальные списки. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **lists** - главная страница; * **list** - страница элементов и разделов; * **list\_sections** - страница управления разделами; * **list\_edit** - страница настроек списка; * **list\_fields** - страница с полями списка; * **list\_field\_edit** - страница настроек полей списка. * **element\_id** - страница редактирования элемента; * **document\_state\_id** - страница просмотра журнала бизнес-процесса; * **element\_id** - страница запуска бизнес-процесса; * **task\_id** - страница задачи бизнес-процесса. |  : **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:lists","",Array(
		"SEF_MODE" => "Y",
		"IBLOCK_TYPE_ID" => "lists",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"SEF_FOLDER" => "/",
		"SEF_URL_TEMPLATES" => Array(
			"lists" => "",
			"list" => "#list_id#/view/#section_id#/",
			"list_sections" => "#list_id#/edit/#section_id#/",
			"list_edit" => "#list_id#/edit/",
			"list_fields" => "#list_id#/fields/",
			"list_field_edit" => "#list_id#/field/#field_id#/",
			"list_element_edit" => "#list_id#/element/#section_id#/#element_id#/",
			"bizproc_log" => "#list_id#/bp_log/#document_state_id#/",
			"bizproc_workflow_start" => "#list_id#/bp_start/#element_id#/",
			"bizproc_task" => "#list_id#/bp_task/#section_id#/#element_id#/#task_id#/"
		),
		"VARIABLE_ALIASES" => Array(
			"lists" => Array(),
			"list" => Array(),
			"list_sections" => Array(),
			"list_edit" => Array(),
			"list_fields" => Array(),
			"list_field_edit" => Array(),
			"list_element_edit" => Array(),
			"bizproc_log" => Array(),
			"bizproc_workflow_start" => Array(),
			"bizproc_task" => Array(),
			
		)
	)
);?>

```

### Смотрите также

* [Универсальные списки (учебный курс "Контент-менеджер")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&CHAPTER_ID=02722)
* [Создание раздела списков и самих списков (учебный курс "Контент-менеджер")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=34&LESSON_ID=2955)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх