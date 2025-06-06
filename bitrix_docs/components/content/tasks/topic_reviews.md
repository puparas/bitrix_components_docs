# Тема (отзывы)

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

Тема (отзывы)

# Тема (отзывы)

### Описание **tasks.topic.reviews**

Компонент служит для создания отзыва к задаче.

В визуальном редакторе компонент расположен по пути: *Контент > Задачи 2.0 > Тема (отзывы)*.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID форума для отзывов | **FORUM\_ID** | Указывается идентификатор форума, в котором будут храниться отзывы пользователей. |
| ID элемента | **TASK\_ID** | Указывается идентификатор задачи, отзывы к которому будут создаваться. |
| Начинать тему текстом элемента | **POST\_FIRST\_MESSAGE** | [Y|N] Если опция отмечена, то при переходе по ссылке **Перейти к обсуждению на форуме** первым сообщением форума будет ссылка на обсуждаемый элемент (форма представления первого сообщения определяется параметром **POST\_FIRST\_MESSAGE\_TEMPLATE**). |
| Шаблон текста для первого сообщения темы | **POST\_FIRST\_MESSAGE\_TEMPLATE** | Указывается шаблон текста для первого сообщения темы. По умолчанию поле содержит **#IMAGE#[url=#LINK#]#TITLE#[/url]#BODY#**. |
| **Шаблоны ссылок** | | |
| Страница чтения темы форума | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. |
| Страница элемента инфоблока | **URL\_TEMPLATES\_DETAIL** | Указывается адрес страницы элемента инфоблока. |
| Страница пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Включить рейтинг | **SHOW\_RATING** | [Y|N] При отмеченной опции будет включен функционал рейтинга. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |
| Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Указывается количество сообщений, отображаемых на одной странице. Все сообщения будут выведены с помощью постраничной навигации. |
| Название шаблона для вывода постраничной навигации | **PAGE\_NAVIGATION\_TEMPLATE** | Задается название шаблона для вывода постраничной навигации. Если поле пусто, то используется шаблон по умолчанию. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Путь относительно корня сайта к папке со смайлами | **PATH\_TO\_SMILE** | Указывается путь к папке со смайлами относительно корня сайта. По умолчанию поле содержит **/bitrix/images/forum/smile/**. |
| Использовать CAPTCHA | **USE\_CAPTCHA** | [Y|N] При отмеченной опции будет выводиться изображение и поле ввода **CAPTCHA** в форме добавления отзыва в публичной части. |
| Выводить сообщения в прямом порядке | **PREORDER** | [Y|N] При отмеченной опции сообщения будут отсортированы по дате создания по возрастанию. |
| Показать ссылку на форум | **SHOW\_LINK\_TO\_FORUM** | [Y|N] При отмеченной опции на странице элемента будет отображена ссылка на форум обсуждения. |
| Максимальное количество файлов, прикрепленных к одному сообщению | **FILES\_COUNT** | Задается количество файлов, которое может быть прикреплено к сообщению. Данный параметр работает только в том случае, если в настройках соответствующего форума разрешено прикреплять файлы к сообщениям. |

### Пример вызова

```

  <?$APPLICATION->IncludeComponent(
	"bitrix:tasks.topic.reviews",
	"",
	Array(
		"SHOW_LINK_TO_FORUM" => "Y",
		"FILES_COUNT" => "2",
		"FORUM_ID" => "1",
		"TASK_ID" => $_REQUEST["ID"],
		"POST_FIRST_MESSAGE" => "Y",
		"POST_FIRST_MESSAGE_TEMPLATE" => "#IMAGE#[url=#LINK#]#TITLE#[/url]#BODY#",
		"URL_TEMPLATES_READ" => "",
		"URL_TEMPLATES_DETAIL" => "",
		"URL_TEMPLATES_PROFILE_VIEW" => "",
		"SHOW_RATING" => "",
		"RATING_TYPE" => "",
		"MESSAGES_PER_PAGE" => "10",
		"PAGE_NAVIGATION_TEMPLATE" => "",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"PATH_TO_SMILE" => "/bitrix/images/forum/smile/",
		"USE_CAPTCHA" => "Y",
		"PREORDER" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0"
	),
false
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх