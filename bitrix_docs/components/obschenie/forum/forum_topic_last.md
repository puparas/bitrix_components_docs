# Темы

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

Темы

**Недоступно в редакциях:**Старт

# Темы

### Описание **forum.topic.last**

Компонент выводит список тем (для использования вне форума). Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID форума | **FID** | Указываются форумы, которые будут отображены в списке. Если не выбран ни один форум, то будут показаны все форумы. |
| Показывать форумы других сайтов | **SHOW\_FORUM\_ANOTHER\_SITE** | [Y|N] При отмеченной опции администратору будут показаны форумы других сайтов.. |
| Поле для сортировки | **SORT\_BY** | Указывается порядок сортировки тем в списке:  * по заголовку - **Заголовок** (**TITLE**); * по автору - **Автор** (**USER\_START\_NAME**); * по количеству ответов - **Ответы** (**POSTS**); * по количеству просмотров - **Прочитано** (**VIEWS**); * по дате последнего сообщения - **Последнее сообщение** (**LAST\_POST\_DATE**). |
| Направление сортировки | **SORT\_ORDER** | Задается направление для сортировки тем:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Показывать вверху прикрепленные темы | **SORT\_BY\_SORT\_FIRST** | [Y|N] При отмеченной опции прикрепленные темы будут показаны вверху списка. |
| **Шаблоны ссылок** | | |
| Страница списка форумов | **URL\_TEMPLATES\_INDEX** | Указывается адрес страницы со списком форумов. По умолчанию поле содержит **index.php**. Такая страница может быть создана с помощью компонента [Форумы (список)](/user_help/components/obschenie/forum/forum_index.php). |
| Страница списка тем | **URL\_TEMPLATES\_LIST** | Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php). |
| Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница чтения сообщения | **URL\_TEMPLATES\_MESSAGE** | Указывается адрес страницы чтения сообщения форума. По умолчанию поле содержит **message.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [PM (чтение)](/user_help/components/obschenie/forum/forum_pm_read.php). |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| **Настройки кеширования** | | |
| Использовать тегированный кеш | **CACHE\_TAG** | [Y|N] При отмеченной опции будет использоваться тегированный кеш в компоненте. |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Список тем**. |
| Шаблон-разделитель для темы и форума | **SEPARATE** | Указывается шаблон-разделитель для темы и форума. Например, **в форуме «#FORUM#»**. |
| Показывать колонки | **SHOW\_COLUMNS** | Параметр служит для выбора полей, которые будут выведены для каждой темы в виде таблицы. В публичной части редактора поля выбираются, удерживая CTRL. В коде задаются в виде массива, например:    ``` "SHOW_COLUMNS" => Array("USER_START_NAME","POSTS","LAST_POST_DATE"), ``` |
| Показывать сортировку | **SHOW\_SORTING** | [Y|N] При отмеченной опции в публичной части будет доступна сортировка тем. |
| **Настройки вывода первого сообщения темы** | | |
| Сообщение темы | **SHOW\_TOPIC\_POST\_MESSAGE** | Выбор сообщения, которое будет отображаться первым. Доступные опции:  * не показывать * показывать первое сообщение темы      При выборе данной опции станут доступны дополнительные поля:    |  |  |  |   | --- | --- | --- |   | Максимальная длина сообщения | **TOPIC\_POST\_MESSAGE\_LENGHT** | Задается максимальное число символов, используемых для написания сообщения. |   | Размер рисунков в тексте сообщения (px) | **IMAGE\_SIZE** | Задается сторона квадрата, в который с сохранением пропорций будет включено изображение. |   | Позволить HTML-код | **ALLOW\_HTML** | При выборе данной опции в сообщения можно будет вставить код html . |   | Позволить ссылки | **ALLOW\_ANCHOR** | При выборе данной опции в сообщения можно будет вставить ссылки. |   | Позволить изображения | **ALLOW\_IMG** | Разрешить использование изображений в тексте сообщения. Изображения располагаются на сторонних сайтах и подключаются на форуме (`<img src=...>`) |   | Позволить видео | **ALLOW\_VIDEO** | При выборе данной опции к сообщениям можно будет прикреплять видео. |   | Позволить списки | **ALLOW\_LIST** | При выборе данной опции к сообщениям можно будет прикреплять видео. |   | Позволить цитирование | **ALLOW\_QUOTE** | Возможность цитировать сообщение другого пользователя (). |   | Позволить коды | **ALLOW\_CODE** | Возможность использования кодов в сообщении (`<code>`). |   | Позволить выравнивание | **ALLOW\_ALIGN** | Разрешить использование выравнивания текста. |   | Позволить таблицы | **ALLOW\_TABLE** | Разрешить использование таблиц (`<table>`). |   | Позволить шрифты | **ALLOW\_FONT** | Возможность изменения цвета текста и шрифт (`<font color=...>`). |   | Позволить смайлы | **ALLOW\_SMILES** | Возможность использования смайлов в сообщении. |   | Заменять символ перевода каретки на `<br>` | **ALLOW\_NL2BR** | замена символа перевода каретки на `<br>` (Доступно только при отмеченной опции `HTML-код`). | * показывать последнее сообщение темы      При выборе данной опции станут доступны дополнительные поля:    |  |  |  |   | --- | --- | --- |   | Максимальная длина сообщения | **TOPIC\_POST\_MESSAGE\_LENGHT** | Задается максимальное число символов, используемых для написания сообщения. |   | Размер рисунков в тексте сообщения (px) | **IMAGE\_SIZE** | Задается сторона квадрата, в который с сохранением пропорций будет включено изображение. |   | Позволить HTML-код | **ALLOW\_HTML** | При выборе данной опции в сообщения можно будет вставить код html . |   | Позволить ссылки | **ALLOW\_ANCHOR** | При выборе данной опции в сообщения можно будет вставить ссылки. |   | Позволить изображения | **ALLOW\_IMG** | Разрешить использование изображений в тексте сообщения. Изображения располагаются на сторонних сайтах и подключаются на форуме (`<img src=...>`) |   | Позволить видео | **ALLOW\_VIDEO** | При выборе данной опции к сообщениям можно будет прикреплять видео. |   | Позволить списки | **ALLOW\_LIST** | При выборе данной опции к сообщениям можно будет прикреплять видео. |   | Позволить цитирование | **ALLOW\_QUOTE** | Возможность цитировать сообщение другого пользователя (). |   | Позволить коды | **ALLOW\_CODE** | Возможность использования кодов в сообщении (`<code>`). |   | Позволить выравнивание | **ALLOW\_ALIGN** | Разрешить использование выравнивания текста. |   | Позволить таблицы | **ALLOW\_TABLE** | Разрешить использование таблиц (`<table>`). |   | Позволить шрифты | **ALLOW\_FONT** | Возможность изменения цвета текста и шрифт (`<font color=...>`). |   | Позволить смайлы | **ALLOW\_SMILES** | Возможность использования смайлов в сообщении. |   | Заменять символ перевода каретки на `<br>` | **ALLOW\_NL2BR** | замена символа перевода каретки на `<br>` (Доступно только при отмеченной опции `HTML-код`). | |
| **Настройки постраничной навигации** | | |
| Устанавливать постраничную навигацию | **SET\_NAVIGATION** | [Y|N] При отмеченной опции в навигационной цепочке будет отражен переход на страницу списка тем форума. |
| Количество тем на одной странице | **TOPICS\_PER\_PAGE** | Указывается количество тем форума, отображаемых на одной странице. Все темы будут выведены с помощью постраничной навигации. |
| Использовать обратную навигацию | **PAGER\_DESC\_NUMBERING** | [Y|N] При отмеченной опции будет использоваться обратная навигация. Для обратной навигации в системе происходит обратный отсчет страниц (последняя страница считается первой). Таким образом, постоянно меняется лишь последняя страница при добавлении нового элемента. Это верно, если новые элементы попадают всегда вверх списка (отсортированы по дате начала активности по убыванию). |
| Выводить всегда | **PAGER\_SHOW\_ALWAYS** | [Y|N] При отмеченной опции постраничная навигации будет выводиться, даже если все элементы помещаются на одной странице. |
| Название категорий | **PAGER\_TITLE** | Задается название категорий, по которым происходит перемещение при постраничной навигации (например, тема, сообщение и др.) |
| Название шаблона | **PAGER\_TEMPLATE** | Задается название шаблона для вывода постраничной навигации. Если поле пусто, то используется шаблон по умолчанию. |
| Показывать навигацию | **SHOW\_NAV** | Указывается способ отображения постраничной навигации по темам:  * **сверху** (**TOP**); * **снизу** (**BOTTOM**).  Если ничего не выбрано, то постраничная навигация выведена не будет. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.topic.last","",Array(
		"SHOW_NAV" => array("BOTTOM"),
		"SHOW_COLUMNS" => array("USER_START_NAME","POSTS","VIEWS","LAST_POST_DATE"),
		"SHOW_SORTING" => "Y",
		"SEPARATE" => "в форуме «#FORUM#»",
		"FID" => Array(),
		"SORT_BY" => "LAST_POST_DATE",
		"SORT_ORDER" => "DESC",
		"SORT_BY_SORT_FIRST" => "Y",
		"URL_TEMPLATES_INDEX" => "index.php",
		"URL_TEMPLATES_LIST" => "list.php?FID=#FID#",
		"URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#",
		"URL_TEMPLATES_MESSAGE" => "message.php?FID=#FID#&TID=#TID#&MID=#MID#",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"TOPICS_PER_PAGE" => "10",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"SHOW_FORUM_ANOTHER_SITE" => "Y",
		"SET_NAVIGATION" => "Y",
		"CACHE_TAG" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0",
		"SET_TITLE" => "Y",
		"PAGER_DESC_NUMBERING" => "Y",
		"PAGER_SHOW_ALWAYS" => "Y",
		"PAGER_TITLE" => "Темы",
		"PAGER_TEMPLATE" => ""
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх