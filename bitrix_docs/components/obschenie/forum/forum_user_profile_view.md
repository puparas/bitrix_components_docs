# Пользователь (профиль)

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

Пользователь (профиль)

**Недоступно в редакциях:**Старт

# Пользователь (профиль)

### Описание **forum.user.profile.view**

Компонент служит для просмотра профиля пользователя форума. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID пользователя | **UID** | Указывается код, в котором передается идентификатор пользователя форума. По умолчанию поле содержит **$\_REQUEST["UID"]**. |
| **Шаблоны ссылок** | | |
| Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница чтения сообщения | **URL\_TEMPLATES\_MESSAGE** | Указывается адрес страницы чтения сообщения форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница редактирования профиля | **URL\_TEMPLATES\_PROFILE** | Указывается адрес страницы редактирования профиля пользователя. По умолчанию поле содержит **profile.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (изменение профиля)](/user_help/components/obschenie/forum/forum_user_profile_edit.php). |
| Страница списка зарегистрированных пользователей форума | **URL\_TEMPLATES\_USER\_LIST** | Указывается адрес страницы списка зарегистрированных пользователей форума. По умолчанию поле содержит **user\_list.php**. Такая страница может быть создана с помощью компонента [Пользователь (список пользователей)](/user_help/components/obschenie/forum/forum_user_list.php). |
| Страница личных сообщений | **URL\_TEMPLATES\_PM\_LIST** | Указывается адрес страницы личных сообщений. По умолчанию поле содержит **pm\_list.php**. Такая страница может быть создана с помощью компонента [PM (список)](/user_help/components/obschenie/forum/forum_pm_list.php). |
| Страница отправки сообщения | **URL\_TEMPLATES\_MESSAGE\_SEND** | Указывается адрес страницы отправки сообщения. По умолчанию поле содержит **message\_send.php?TYPE=#TYPE#&UID=#UID#**. Такая страница может быть создана с помощью компонента [Письмо](/user_help/components/obschenie/forum/forum_message_send.php). |
| Страница создания (редактирования) личных сообщений | **URL\_TEMPLATES\_PM\_EDIT** | Указывается адрес страницы создания (редактирования) персонального сообщения. По умолчанию поле содержит **pm\_edit.php**. |
| Страница подписки | **URL\_TEMPLATES\_PM\_EDIT** | Указывается адрес страницы просмотра подписок пользователя. По умолчанию поле содержит **subscr\_list.php**. |
| Страница сообщений пользователя | **URL\_TEMPLATES\_USER\_POST** | Указывается адрес страницы просмотра сообщений пользователя. По умолчанию поле содержит **user\_post.php?UID=#UID#&mode=#mode#**. Такая страница может быть создана с помощью компонента [Пользователь (сообщения)](/user_help/components/obschenie/forum/forum_user_post.php). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| ID форума | **FID\_RANGE** | Указываются форумы, из которых будут выбраны для отображения темы и сообщения пользователя. |
| Формат показа даты | **DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Могут отправлять письмо (e-mail) из профиля | **SEND\_MAIL** | Указываются пользователи, которые могут отправлять письмо (e-mail) из профиля:  * **A** - никто; * **E** - авторизованные пользователи; * **U** - все пользователи, а для неавторизованных пользователей выводить поле CAPTCHA; * **Y** - все пользователи. |
| Могут видеть номер ICQ в профиле | **SEND\_ICQ** | Указываются пользователи, которые могут видет номер ICQ в профиле. |
| Показывать доп. свойства | **USER\_PROPERTY** | Указываются дополнительные пользовательские свойства, которые будут показаны на закладке с названием, заданным в параметре **USER\_PROPERTY\_NAME**. |
| Показывать навигацию | **SET\_NAVIGATION** | [Y|N] При отмеченной опции в навигационной цепочке будет отражен переход на страницу профиля пользователя. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено имя пользователя. |
| Название закладки с доп. свойствами | **USER\_PROPERTY\_NAME** | Указывается название закладки с дополнительными свойствами. |
| **Настройки рейтинга** | | |
| Выводить рейтинг | **SHOW\_RATING** | [Y|N] При отмеченной опции будет выведен рейтинг пользователя на форуме. |
| Рейтинг | **RATING\_ID** | Указывается рейтинг из списка. У каждого рейтинга свои настройки посчета. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопки рейтинга:  * - по умолчанию; * **standart** - Плюс / Минус; * **like** - Мне нравится;   Внимание! С версии **17.5.4** добавлена поддержка рейтингов с реакциями. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.user.profile.view","",Array(
	    "USER_PROPERTY_NAME" => "",
	    "UID" => $_REQUEST["UID"],
	    "URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#",
	    "URL_TEMPLATES_MESSAGE" => "message.php?FID=#FID#&TID=#TID#&MID=#MID#",
	    "URL_TEMPLATES_PROFILE" => "profile.php?UID=#UID#",
	    "URL_TEMPLATES_USER_LIST" => "user_list.php",
	    "URL_TEMPLATES_PM_LIST" => "pm_list.php",
	    "URL_TEMPLATES_MESSAGE_SEND" => "message_send.php?TYPE=#TYPE#&UID=#UID#",
	    "URL_TEMPLATES_PM_EDIT" => "pm_edit.php",
	    "URL_TEMPLATES_SUBSCR_LIST" => "subscr_list.php",
	    "URL_TEMPLATES_USER_POST" => "user_post.php?UID=#UID#&mode=#mode#",
	    "FID_RANGE" => array(),
	    "DATE_FORMAT" => "d.m.Y",
	    "DATE_TIME_FORMAT" => "d.m.Y H:i:s",
	    "SEND_MAIL" => "E",
	    "SEND_ICQ" => "A",
	    "USER_PROPERTY" => array(),
	    "SET_NAVIGATION" => "Y",
	    "CACHE_TYPE" => "A",
	    "CACHE_TIME" => "0",
	    "CACHE_NOTES" => "",
	    "SET_TITLE" => "Y",
	    "SHOW_RATING" => "Y",
	    "RATING_ID" => "",
	    "RATING_TYPE" => "like"		
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх