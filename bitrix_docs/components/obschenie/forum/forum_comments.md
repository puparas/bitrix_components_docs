# Комментарии

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

Комментарии

# Комментарии

### Описание **forum.comments**

Компонент выводит форму для комментариев. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Общение > Комментарии*.

Компонент относится к модулю [Форум](/user_help/service/forum/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип сущности | **ENTITY\_TYPE** | Двухсимвольный идентификатор типа комментируемой сущности. Пишется латиницей. Например, для задач тип сущности – TK. |
| Числовой ID сущности | **ENTITY\_ID** | Числовой идентификатор комментируемой сущности. Для задачи с ID, равной 348, это значение - 348. |
| Буквенно-числовой ID сущности (XML ID) | **ENTITY\_XML\_ID** | Бувенно-числовой ID комментируемой сущности, а именно XML ID. Используются символы [A-Z0-9\_]. Для задачи 348, это значение - TASKS\_348. |
| ID форума для комментариев | **FORUM\_ID** | Указывается форум, в котором будут храниться комментарии. |
| Права доступа | **PERMISSION** | Внешние права, которые переопределяют права пользователя на форуме: *A < E < I < Q < U < Y* (*A* - нет доступа, *E* - чтение, *I* - ответ, *Q* - модерирование, *U* - редактирование, *Y* - полный доступ). |
| Показывать пользовательские поля сообщения | **USER\_FIELDS** | Указываются пользовательские поля сообщения. |
| **Шаблоны ссылок** | | |
| Страница пользователя | **URL\_TEMPLATES\_PROFILE\_VIEW** | Указывается адрес страницы просмотра профиля пользователя. Такая страница может быть создана с помощью компонента [Пользователь (профиль)](/user_help/components/obschenie/forum/forum_user_profile_view.php). | |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Указывается количество сообщений, отображаемых на одной странице. Все сообщения будут выведены с помощью постраничной навигации. |
| Название шаблона для вывода постраничной навигации | **PAGE\_NAVIGATION\_TEMPLATE** | Задается название шаблона для вывода постраничной навигации. Если поле пусто, то используется шаблон по умолчанию. |
| Формат показа даты и времени | **DATE\_TIME\_FORMAT** | Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Формат имени | **NAME\_TEMPLATE** | Указывается шаблон для отображения ФИО пользователя. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Размер рисунков в тексте сообщения (px) | **IMAGE\_SIZE** | Задается сторона квадрата, в который с сохранением пропорций будет включено изображение. Указывается в пикселях. |
| Дополнительный размер рисунков в тексте сообщения (px) (используется для html-сжатия) | **IMAGE\_HTML\_SIZE** | Задается дополнительный размер изображения, используемый при html-сжатии. Указывается в пикселях. |
| По умолчанию показывать невизуальный режим редактора | **EDITOR\_CODE\_DEFAULT** | [Y|N] При отмеченной опции при создании или редактировании сообщения будет включен режим показа BB-кодов. (Пример: [B]сообщение[/B] вместо **сообщение**). |
| Подписывать автора элемента на новые комментарии | **SUBSCRIBE\_AUTHOR\_ELEMENT** | [Y|N] При отмеченной опции автор элемента будет подписан на новые комментарии. |
| Включить рейтинг | **SHOW\_RATING** | [Y|N] Указывается включать ли вывод рейтинга. |
| Сворачивать форму добавления отзыва | **SHOW\_MINIMIZED** | [Y|N] При отмеченной опции форма ввода отзыва будет свернута. |
| Использовать CAPTCHA | **USE\_CAPTCHA** | [Y|N] При отмеченной опции будет выводиться изображение и поле ввода **CAPTCHA** в форме добавления отзыва в публичной части. |
| Выводить сообщения в прямом порядке | **PREORDER** | [Y|N] При отмеченной опции сообщения будут отсортированы по возрастанию. |
| Обновлять статистику просмотра форума | **SET\_LAST\_VISIT** | [Y|N] При отмеченной опции будет обновляться статистика просмотра форума. |
| **Настройки редактора** | | |
| Позволить HTML-код | **ALLOW\_HTML** | [Y|N] При выборе данной опции в сообщения можно будет вставить код html . |
| Позволить ссылки | **ALLOW\_ANCHOR** | [Y|N] При выборе данной опции в сообщения можно будет вставить ссылки. |
| Позволить теги B, U, I, S | **ALLOW\_BIU** | [Y|N] При выборе данной опции в сообщениях можно будет использовать теги `B, U, I, S`. |
| Позволить изображения | **ALLOW\_IMG** | [Y|N] Разрешить использование изображений в тексте сообщения. Изображения располагаются на сторонних сайтах и подключаются на форуме (`<img src=...>`). |
| Позволить видео | **ALLOW\_VIDEO** | [Y|N] При выборе данной опции к сообщениям можно будет прикреплять видео. |
| Позволить списки | **ALLOW\_LIST** | [Y|N] При выборе данной опции в сообщениях можно использовать списки. |
| Позволить цитирование | **ALLOW\_QUOTE** | [Y|N] Возможность цитировать сообщение другого пользователя (`<quote>`). |
| Позволить коды | **ALLOW\_CODE** | [Y|N] Возможность использования кодов в сообщении (`<code>`). |
 Позволить таблицы | **ALLOW\_TABLE** | [Y|N] Разрешить использование таблиц (`<table>`). || Позволить шрифты | **ALLOW\_FONT** | [Y|N] Возможность изменения цвета текста и шрифт (`<font color=...>`). |
| Позволить смайлы | **ALLOW\_SMILES** | [Y|N] Возможность использования смайлов в сообщении. |
| Заменять символ перевода каретки на `<br>` | **ALLOW\_NL2BR** | [Y|N] Замена символа перевода каретки на `<br>` (доступно только при отмеченной опции `HTML-код`). |
| Позволить выравнивание | **ALLOW\_ALIGN** | [Y|N] Разрешить использование выравнивания текста. |
| Позволить упоминание пользователя | **ALLOW\_MENTION** | [Y|N] Разрешить упоминание пользователя в комментариях. |
|

  

С версии 23.300.0 модуля **Форум** в шаблоне компонента **.default** дополнились системные параметры:

* `$arParams['MAIN_POST_FORM_BUTTONS']` – дополнительные кнопки для компонента **main.post.form** в виде массива. Cписок возможных кнопок – `Copilot, UploadFile, MentionUser, Quote, SearchTag`.
* `$arParams['LHE']['copilotParams']` – параметры копилота `{{moduleId, contextId, category, invitationLineMode, contextParameters, isMentionUnavailable}}`.
* `$arParams['LHE']['isCopilotEnabled']` – доступен ли копилот.
* `$arParams['LHE']['isCopilotImageEnabledBySettings']` – доступна ли генерация изображений (в зависимости от настроек).
* `$arParams['LHE']['isCopilotTextEnabledBySettings']` – доступна ли генерация текстов (в зависимости от настроек).

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:forum.topic.reviews","",Array(
		"ALLOW_ALIGN" => "Y",
		"ALLOW_ANCHOR" => "Y",
		"ALLOW_BIU" => "Y",
		"ALLOW_CODE" => "Y",
		"ALLOW_FONT" => "Y",
		"ALLOW_HTML" => "Y",
		"ALLOW_IMG" => "Y",
		"ALLOW_LIST" => "Y",
		"ALLOW_MENTION" => "Y",
		"ALLOW_NL2BR" => "Y",
		"ALLOW_QUOTE" => "Y",
		"ALLOW_SMILES" => "Y",
		"ALLOW_TABLE" => "Y",
		"ALLOW_VIDEO" => "Y",
		"CACHE_TIME" => "0",
		"CACHE_TYPE" => "A",
		"DATE_TIME_FORMAT" => "d.m.Y H:i:s",
		"EDITOR_CODE_DEFAULT" => "Y",
		"ENTITY_ID" => "348",
		"ENTITY_TYPE" => "TK",
		"ENTITY_XML_ID" => "TASKS_348",
		"FORUM_ID" => "1",
		"IMAGE_HTML_SIZE" => "0",
		"IMAGE_SIZE" => "600",
		"MESSAGES_PER_PAGE" => "10",
		"NAME_TEMPLATE" => "",
		"PAGE_NAVIGATION_TEMPLATE" => "",
		"PERMISSION" => "Y",
		"PREORDER" => "Y",
		"SET_LAST_VISIT" => "N",
		"SHOW_MINIMIZED" => "Y",
		"SHOW_RATING" => "Y",
		"SUBSCRIBE_AUTHOR_ELEMENT" => "Y",
		"URL_TEMPLATES_PROFILE_VIEW" => "profile_view.php?UID=#UID#",
		"USER_FIELDS" => array("UF_FORUM_MES_URL_PRV","UF_TASK_COMMENT_TYPE"),
		"USE_CAPTCHA" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх