# Статистика

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

Статистика

**Недоступно в редакциях:**Старт

# Статистика

### Описание **forum.statistic**

Компонент выводит статистику по форуму, информацию по посетителям. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Форум*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| ID форума | **FID** | Указывается идентификатор форума, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["FID"]}**. |
| ID темы | **TID** | Указывается идентификатор темы, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["TID"]}**. |
| SEO ID темы | **TITLE\_SEO** | Указывается символьный идентификатор темы, явно или в виде кода. По умолчанию поле содержит **={$\_REQUEST["TITLE\_SEO"]}**. |
| Период для отображения статистики (сек.) | **PERIOD** | Указывается период времени в секундах, за который показывается статистика форума. |
| Отображать в статистике | **SHOW** | Указываются данные, которые будут отображены в статистике:  * **STATISTIC** - статистика форумов; * **BIRTHDAY** - именинники; * **USERS\_ONLINE** - он-лайн пользователи. |
| Показывать администратору форумы других сайтов | **SHOW\_FORUM\_ANOTHER\_SITE** | [Y|N] При отмеченной опции администратору будут показаны форумы других сайтов. |
| Форумы | **FORUM\_ID** | Указываются форумы, информация по которым будет учтена в статистике. |
| **Шаблоны ссылок** | | |
| Страница профиля пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. По умолчанию поле содержит **profile\_view.php?UID=#UID#**. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Время кеширования списка пользователей на форуме | **CACHE\_TIME\_USER\_STAT** | Указывается время кеширование информации о списке пользователей форума в секундах. |
| **Дополнительные настройки** | | |
| Длина слова | **WORD\_LENGTH** | Задается максимально допустимая длина словообразующих символов, следующих друг за другом. Если длина слова превысит указанное число, то символы слова будут разбавлены разрывами (при просмотре сообщений разрывы не отображаются). |
 Не индексировать ссылку на профиль | **SEO\_USER** | [Y|N] При отмеченной опции поисковые боты не смогут индексировать ссылки на профиль пользователя. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.statistic","",Array(
		"SEO_USER" => "Y",
		"FID" => $_REQUEST["FID"],
		"TID" => $_REQUEST["TID"],
		"FORUM_ID" => array("1"),
		"TITLE_SEO" => $_REQUEST["TITLE_SEO"],
		"PERIOD" => "600",
		"SHOW" => array("STATISTIC","BIRTHDAY","USERS_ONLINE"),
		"SHOW_FORUM_ANOTHER_SITE" => "Y",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0",
		"CACHE_TIME_USER_STAT" => "600",
		"WORD_LENGTH" => "50"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх