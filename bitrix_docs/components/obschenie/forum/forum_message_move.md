# Сообщения (перемещение)

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

Сообщения (перемещение)

**Недоступно в редакциях:**Старт

# Сообщения (перемещение)

### Описание **forum.message.move**

Компонент служит для перемещения сообщений форума. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID форума | **FID** | Указывается идентификатор форума, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["FID"]}**. |
| ID темы | **TID** | Указывается идентификатор темы, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["TID"]}**. |
| ID сообщения | **MID** | Указывается идентификатор сообщения, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["MID"]}**. |
| Могут отправлять письмо (e-mail) из профиля | **SEND\_MAIL** | Указываются пользователи, которые могут отправлять письмо (e-mail) из профиля:  * **A** - никто; * **E** - авторизованные пользователи; * **U** - все пользователи, а для неавторизованных пользователей выводить поле CAPTCHA; * **Y** - все пользователи. |
| **Шаблоны ссылок** | | |
| Страница списка форумов | **URL\_TEMPLATES\_INDEX** | Указывается адрес страницы со списком форумов. По умолчанию поле содержит **index.php**. Такая страница может быть создана с помощью компонента [Форумы (список)](/user_help/components/obschenie/forum/forum_index.php). |
| Страница списка тем | **URL\_TEMPLATES\_LIST** | Указывается адрес страницы со списком тем форума. По умолчанию поле содержит **list.php?FID=#FID#**. Такая страница может быть создана с помощью компонента [Темы (список)](/user_help/components/obschenie/forum/forum_topic_list.php). |
| Страница чтения темы | **URL\_TEMPLATES\_READ** | Указывается адрес страницы чтения темы форума. По умолчанию поле содержит **read.php?FID=#FID#&TID=#TID#&MID=#MID#**. Такая страница может быть создана с помощью компонента [Тема (чтение)](/user_help/components/obschenie/forum/forum_topic_read.php). |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| Страница поиска темы форума | **URL\_TEMPLATES\_TOPIC\_SEARCH** | Указывается адрес страницы поиска темы форума. По умолчанию поле содержит **topic\_search.php**. Такая страница может быть создана с помощью компонента [Темы (поиск)](/user_help/components/obschenie/forum/forum_topic_search.php). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Длина слова | **WORD\_LENGTH** | Задается максимально допустимая длина словообразующих символов, следующих друг за другом. Если длина слова превысит указанное число, то символы слова будут разбавлены разрывами (при просмотре сообщений разрывы не отображаются). |
| Размер прикрепленного рисунка (px) | **IMAGE\_SIZE** | Указывается размер прикрепляемых изображений. |
| Формат показа даты | **DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Показывать навигацию | **SET\_NAVIGATION** | [Y|N] При отмеченной опции в навигационной цепочке будет отражен переход на страницу переноса сообщения. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Перенос сообщений**. |
| Использовать внешний сервис для перевода названия темы (seo) | **SEO\_USE\_AN\_EXTERNAL\_SERVICE** | [Y|N] При отмеченной опции название темы будет переведено автоматически внешним сервером. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.message.move","",Array(
		"SEND_MAIL" => "E",
		"FID" => $_REQUEST["FID"],
		"TID" => $_REQUEST["TID"],
		"MID" => $_REQUEST["MID"],
		"URL_TEMPLATES_INDEX" => "index.php",
		"URL_TEMPLATES_LIST" => "list.php?FID=#FID#",
		"URL_TEMPLATES_READ" => "read.php?FID=#FID#&TID=#TID#&MID=#MID#",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"URL_TEMPLATES_TOPIC_SEARCH" => "topic_search.php",
		"WORD_LENGTH" => "50",
		"IMAGE_SIZE" => "300",
		"DATE_FORMAT" => "d.m.Y",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"SET_NAVIGATION" => "Y",
		"SET_TITLE" => "Y",
		"SEO_USE_AN_EXTERNAL_SERVICE" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0"
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх