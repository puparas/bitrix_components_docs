# Тема (чтение)

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

Тема (чтение)

**Недоступно в редакциях:**Старт

# Тема (чтение)

### Описание **forum.topic.read**

Компонент выводит список сообщений темы форума. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |  |
| --- | --- | --- | --- |
| **Поле** | **Параметр** | **Описание** | |
| **Основные параметры** | | | |
| ID форума | **FID** | Указывается идентификатор форума, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["FID"]}**. | |
| ID темы | **TID** | Указывается идентификатор темы, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["TID"]}**. | |
| ID сообщения | **MID** | Указывается идентификатор сообщения, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["MID"]}**. | |
| Могут отправлять письмо (e-mail) из профиля | **SEND\_MAIL** | Указываются пользователи, которые могут отправлять письмо (e-mail) из профиля:  * **A** - никто; * **E** - авторизованные пользователи; * **U** - все пользователи, а для неавторизованных пользователей выводить поле CAPTCHA; * **Y** - все пользователи. | |
| **Шаблоны ссылок** | | | |
| Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#**. | |
| Страница чтения темы (с ID сообщения) | **URL\_TEMPLATES\_MESSAGE** | Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **message.php?FID=#FID#&TID=#TID#&MID=#MID#**. | |
| Страница списка тем | **URL\_TEMPLATES\_LIST** | Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php). | |
| Страница переноса сообщений | **URL\_TEMPLATES\_MESSAGE\_MOVE** | Указывается адрес страницы переноса сообщений форума. По умолчанию поле содержит **message\_move.php?FID=#FID#&TID=#TID#&MID\_ARRAY=#MID\_ARRAY#**. Такая страница может быть создана с помощью компонента [Сообщения (перемещение)](/user_help/components/obschenie/forum/forum_message_move.php). | |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). | |
| Страница создания новой темы | **URL\_TEMPLATES\_TOPIC\_NEW** | Указывается адрес страницы создания новой темы форума. По умолчанию поле содержит **topic\_new.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Тема (создание)](/user_help/components/obschenie/forum/forum_topic_new.php). | |
| Страница подписки | **URL\_TEMPLATES\_SUBSCR\_LIST** | Указывается адрес страницы подписки на форум. По умолчанию поле содержит **subscr\_list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Подписка (список)](/user_help/components/obschenie/forum/forum_subscribe_list.php). | |
| Страница переноса тем | **URL\_TEMPLATES\_TOPIC\_MOVE** | Указывается адрес страницы переноса темы форума. По умолчанию поле содержит **topic\_move.php?FID=#FID#&TID=#TID#**. Такая страница может быть создана с помощью компонента [Темы (перемещение)](/user_help/components/obschenie/forum/forum_topic_move.php). | |
| Страница списка форумов | **URL\_TEMPLATES\_INDEX** | Указывается адрес страницы со списком форумов. По умолчанию поле содержит **index.php**. Такая страница может быть создана с помощью компонента [Форумы (список)](/user_help/components/obschenie/forum/forum_index.php). | |
| Страница личных сообщений | **URL\_TEMPLATES\_PM\_EDIT** | Указывается адрес страницы со списком форумов. По умолчанию поле содержит **pm\_edit.php**. Такая страница может быть создана с помощью компонента [PM (изменение)](/user_help/components/obschenie/forum/forum_pm_edit.php). | |
| Страница отправки сообщения | **URL\_TEMPLATES\_MESSAGE\_SEND** | Указывается адрес страницы отправки сообщения. По умолчанию поле содержит **message\_send.php?UID=#UID#**. | |
| Страница RSS | **URL\_TEMPLATES\_RSS** | Указывается адрес страницы RSS форума. По умолчанию поле содержит **rss.php?TYPE=#TYPE#&MODE=#MODE#&IID=#IID#**. | |
| Страница сообщений пользователя | **URL\_TEMPLATES\_USER\_POST** | Указывается адрес страницы сообщений пользователя. По умолчанию поле содержит **user\_post.php?UID=#UID#&mode=#mode#**. | |
| **Настройки кеширования** | | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. | |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. | |
| **Дополнительные настройки** | | | |
| Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Указывается количество сообщений, отображаемых на одной странице. Все сообщения будут выведены с помощью постраничной навигации. | |
| Формат показа даты | **DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. | |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. | |
| Название шаблона для вывода постраничной навигации | **PAGE\_NAVIGATION\_TEMPLATE** | Задается название шаблона для вывода постраничной навигации. Если поле пусто, то используется шаблон по умолчанию. | |
| Количество страниц в постраничной навигации | **PAGE\_NAVIGATION\_WINDOW** | Задается количество отображаемых в навигации ссылок на страницы. Если количество страниц превышает заданное число, то в навигацию будет добавлено многоточие. | |
| Разрешать показывать все страницы форума | **PAGE\_NAVIGATION\_SHOW\_ALL** | [Y|N] При отмеченной опции будут показаны все страницы форума. | |
| Длина слова | **WORD\_LENGTH** | Задается максимально допустимая длина словообразующих символов, следующих друг за другом. Если длина слова превысит указанное число, то символы слова будут разбавлены разрывами (при просмотре сообщений разрывы не отображаются). | |
| Размер прикрепленного рисунка (px) | **IMAGE\_SIZE** | Указывается допустимый размер прикрепленного рисунка в пикселах. | |
| Показывать первое сообщение темы на каждой странице | **SHOW\_FIRST\_POST** | [Y|N] При отмеченной опции на каждой странице просмотра темы будет отображаться первое ее сообщение. | |
| Показывать навигацию (хлебные крошки) | **SET\_NAVIGATION** | [Y|N] При отмеченной опции в навигационную цепочку будет добавлен пункт с заголовком страницы. | |
| Использовать AJAX | **AJAX\_TYPE** | [Y|N] При отмеченной опции для компонента будет включен режим AJAX. | |
| Устанавливать теги и описание темы в свойства страницы | **SET\_PAGE\_PROPERTY** | [Y|N] Разрешает установку тегов и описания темы, указанных при создании темы в качестве тегов и описания для страницы. | |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено название просматриваемой темы. | |
| Как показывать прикрепленные рисунки (под сообщением) | **ATTACH\_MODE** | Задается форма отображения прикрепленных рисунков (под сообщением). Доступные формы:  * Миниатюра      При выборе формы **Миниатюра** станет доступно дополнительное поле:    |  |  |  |   | --- | --- | --- |   | Размер миниатюры рисунка (под сообщением, px) | **ATTACH\_SIZE** | Задается сторона квадрата, в который с сохранением пропорций будет включено изображение. Указывается в пикселях. | * Название | |
| Показывать RSS | **SHOW\_RSS** | [Y|N] При отмеченной опции на странице будет отображаться ссылка на RSS. | |
| Показывать ссылку «Имя» | **SHOW\_NAME\_LINK** | [Y|N] При отмеченной опции в форме сообщения будет показана ссылка «Имя» для вставки имени пользователя в создаваемое сообщение. | |
| Не индексировать ссылку на профиль | **SEO\_USER** | [Y|N] При отмеченной опции поисковые боты не смогут индексировать ссылки на профиль пользователя. | |
| Показывать опросы | **SHOW\_VOTE** | [Y|N] При отмеченной опции будет выведен опрос. | |
| Шаблон для опросов | **VOTE\_TEMPLATE** | Укажите шаблон для отображения опроса. | |
| **Настройки рейтинга** | | | |
| Включить рейтинг | **SHOW\_RATING** | Указывается включать ли вывод рейтинга:  * - по умолчанию; * **Y** - да; * **N** - нет. | **Примечание:** С версии **17.5.4** добавлена поддержка рейтингов с реакциями. |
| Рейтинг | **RATING\_ID** | Указывается какой будет использоваться рейтинг. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопки рейтинга:  * - по умолчанию; * **like** - Мне нравится (текстовый); * **like\_graphic** - Мне нравится (графический); * **standart\_text** - Нравится / Не нравится (текстовый); * **standart** - Нравится / Не нравится (графический). |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.topic.read","",Array(
		"SEND_MAIL" => "E",
		"SHOW_RSS" => "Y",
		"SHOW_NAME_LINK" => "Y",
		"SEO_USER" => "Y",
		"SHOW_VOTE" => "Y",
		"VOTE_TEMPLATE" => "light",
		"FID" => $_REQUEST["FID"],
		"TID" => $_REQUEST["TID"],
		"MID" => $_REQUEST["MID"],
		"URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#",
		"URL_TEMPLATES_MESSAGE" => "message.php?FID=#FID#&TID=#TID#&MID=#MID#",
		"URL_TEMPLATES_LIST" => "list.php?FID=#FID#",
		"URL_TEMPLATES_MESSAGE_MOVE" => "message_move.php?FID=#FID#&TID=#TID#&MID_ARRAY=#MID_ARRAY#",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"URL_TEMPLATES_TOPIC_NEW" => "topic_new.php?FID=#FID#",
		"URL_TEMPLATES_SUBSCR_LIST" => "subscr_list.php?FID=#FID#",
		"URL_TEMPLATES_TOPIC_MOVE" => "topic_move.php?FID=#FID#&TID=#TID#",
		"URL_TEMPLATES_INDEX" => "index.php",
		"URL_TEMPLATES_PM_EDIT" => "pm_edit.php",
		"URL_TEMPLATES_MESSAGE_SEND" => "message_send.php?UID=#UID#",
		"URL_TEMPLATES_RSS" => "rss.php?TYPE=#TYPE#&MODE=#MODE#&IID=#IID#",
		"URL_TEMPLATES_USER_POST" => "user_post.php?UID=#UID#&mode=#mode#",
		"PAGEN" => "1",
		"PATH_TO_SMILE" => "/bitrix/images/forum/smile/",
		"MESSAGES_PER_PAGE" => "10",
		"DATE_FORMAT" => "d.m.Y",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"PAGE_NAVIGATION_TEMPLATE" => "",
		"PAGE_NAVIGATION_WINDOW" => "11",
		"PAGE_NAVIGATION_SHOW_ALL" => "N",
		"WORD_LENGTH" => "50",
		"IMAGE_SIZE" => "300",
		"SHOW_FIRST_POST" => "N",
		"SET_NAVIGATION" => "Y",
		"AJAX_TYPE" => "Y",
		"SET_PAGE_PROPERTY" => "Y",
		"SET_TITLE" => "Y",
		"SHOW_RATING" => "Y",
		"RATING_ID" => "2",
		"RATING_TYPE" => "like",     
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх