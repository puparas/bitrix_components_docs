|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Блог |

| Выбирается блог для сервиса идея. |
| Инфоблок, в котором хранится структура категорий |

| Выбирается инфоблок, в котором хранится структура категорий идей. |
| Группы пользователей, которые могут добавлять специальный ответ |

| Указывается группа пользователей, которая может модерировать сервис идей. |
| Статус по умолчанию для новой идеи |

| Указывается статус, который будет автоматически присвоен новым идеям. |
| **Внешний вид** |

| |
| Идей на странице |

| Указывается количество идей на странице. Остальные сообщения будут выведены с помощью постраничной навигации. |
| Комментариев к идее на странице |

| Указывается количество комментариев к идее на странице. |
| Использовать прямую постраничную навигацию для комментариев |

| [Y|N] При отмеченной опции список комментариев будет выводиться постранично с прямой навигацией. |
| Tегов в облаке тегов (0 - без ограничений) |

| Задается ограничение на количество отображаемых в облаке тегов. |
| Имя шаблона для постраничной навигации |

| Указывается имя шаблона для постраничной навигации. |
| Максимальная ширина изображения |

| Максимально допустимая ширина добавляемого в сообщение изображения (в пикселях). |
| Разрешить изменять размер визуального редактора |

| [Y|N] При отмеченной опции будет возможность менять размеры окна визуального редактора. |
| По умолчанию показывать невизуальный режим редактора |

| [Y|N] При отмеченной опции визуальный режим редактора не будет использоваться по умолчанию. |
| Высота визуального редактора по умолчанию (пикселей) |

| Значение высоты визуального редактора при загрузке (в пикселях) в форме редактирования идеи. |
| Высота визуального редактора по умолчанию (пикселей) в комментариях |

| Значение высоты визуального редактора в форме комментариев при загрузке (в пикселях). |
| **Управление адресами страниц** |

| |
| Включить поддержку ЧПУ |

| [Y|N] При отмеченной опции будет включена поддержка ЧПУ. Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Указывается путь к каталогу ЧПУ. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **index** - главная страница идей * **status\_code** - список идей со статусами 0го уровня * **category\_1** - общий список идей 1го уровня * **category\_1\_status** - список идей со статусами 1го уровня * **category\_2** - общий список идей 2го уровня * **category\_2\_status** - список идей со статусами 2го уровня * **user\_ideas** - общий список идей пользователя * **user\_ideas\_status** - список идей пользователя со статусами * **user** - профайл пользователя * **subscribe** -Email подписки пользователя * **edit** - редактирование идеи: * **post\_id** - идея детально: * **post\_rss** - адрес комментариев к сообщению в RSS формате * **rss** - адрес блога в RSS формате * **rss\_status** - адрес блога в RSS формате со статусом * **rss\_category** - адрес блога в RSS формате с категорией * **rss\_category\_status** - адрес блога в RSS формате с категорией и статусом * **rss\_user\_ideas** - адрес блога в RSS формате к идеям пользователя * **rss\_user\_ideas\_status** - адрес блога в RSS формате к идеям пользователя со статусом * **rss\_all** - сообщения всех блогов в RSS формате |  **SEF\_FOLDER** и **SEF\_URL\_TEMPLATES**.  Если режим поддержки ЧПУ **выключен**, то необходимо настроить параметр **VARIABLE\_ALIASES**     |  |  |  | | --- | --- | --- | | Имена переменных | **VARIABLE\_ALIASES** | Имена переменных для управления страницами. |  . |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| Время кэширования остальных страниц |

| Указывается время кеширования страниц, начиная со второй. |
| **Дополнительные настройки** |

| |
| Путь к папке со смайликами относительно корня сайта |

| Указывается путь к папке со смайликами относительно корня сайта. По умолчанию задано */bitrix/images/blog/smile/*. |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено название идеи. |
| Показывать навигацию (хлебные крошки) |

| [Y|N] При отмеченной опции в цепочку навигации будет добавлен пункт с названием блога. |
| Формат показа даты и времени |

| Указывается формат показа даты и времени. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |
| Отображение имени |

| Указывается шаблон для отображения ФИО пользователя социальной сети. По умолчанию - значение **Формат сайта** (т.е используются значение **Формат имени**, указанное в закладке **Параметры** страницы [Редактирование сайта](/user_help/settings/settings/sites/site_edit.php)). Указав пункт **другое->**, можно задать свой шаблон. Допустимы шаблоны: **#NAME#** - имя, **#LAST\_NAME#** - фамилия, **#SECOND\_NAME#** - отчество, **#NAME\_SHORT#**, **#LAST\_NAME\_SHORT#**, **#SECOND\_NAME\_SHORT#** - сокращенные до одной буквы имя, фамилия и отчество. |
| Показывать логин, если не задано имя |

| [Y|N] При отмеченной опции будет отображен логин пользователя, если не задано имя. |
| Разрешить вставку видео в комментарии |

| [Y|N] При отмеченной опции появится возможность вставки видеороликов в комментарий. |
| Запретить вставку ссылок в комментариях |

| Указывается, кому нельзя вставлять ссылки в комментарии (по умолчанию - **Никому**):   * Никому; * Анонимным пользователям; * Всем. |
| Использовать символьный код сообщений как идентификатор |

| [Y|N] При отмеченной опции транслитерация заголовка идеи будет использоваться как его идентификатор. |
| Использовать внешний сервис перевода для кода сообщений |

| [Y|N] При отмеченной опции для перевода символьного кода идей будет использоваться сервис перевода Bing. Параметр доступен при отмеченной опции **Использовать символьный код сообщений как идентификатор.** |
| Использовать рейтинги |

| [Y|N] При отмеченной опции будут использоваться рейтинги для оценки идей и комментариев к ним. |
| Шаблон рейтингов |

| Выбирается шаблон визуального отображения рейтингов. |
| Отключить уведомления в живую ленту |

| [Y|N] Опция позволяет отключить вывод идей в живую ленту.    Опция доступна только в **Битрикс24 в коробке**. |
| Отключить почтовые уведомления |

| [Y|N] Опция позволяет отключить почтовые уведомления о новых комментариях. |
| Отключить RSS |

| [Y|N] Опция позволяет отключить RSS. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(

	"bitrix:idea",

	".default",

	Array(

		"BLOG_URL" => "idea_s1",

		"IBLOCK_CATOGORIES" => "51",

		"POST_BIND_USER" => array(0=>"1",),

		"POST_BIND_STATUS_DEFAULT" => "15",

		"MESSAGE_COUNT" => "10",

		"COMMENTS_COUNT" => "10",

		"TAGS_COUNT" => "0",

		"DATE_TIME_FORMAT" => "d.m.y G:i",

		"NAV_TEMPLATE" => "",

		"IMAGE_MAX_WIDTH" => "770",

		"EDITOR_RESIZABLE" => "Y",

		"EDITOR_DEFAULT_HEIGHT" => "300",

		"EDITOR_CODE_DEFAULT" => "N",

		"COMMENT_EDITOR_DEFAULT_HEIGHT" => "200",

		"SEF_MODE" => "Y",

		"SEF_FOLDER" => "/services/idea/",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_TIME_LONG" => "604800",

		"PATH_TO_SMILE" => "/bitrix/images/blog/smile/",

		"SET_TITLE" => "Y",

		"SET_NAV_CHAIN" => "Y",

		"USE_ASC_PAGING" => "Y",

		"COMMENT_ALLOW_VIDEO" => "Y",

		"NO_URL_IN_COMMENTS" => "",

		"ALLOW_POST_CODE" => "Y",

		"USE_GOOGLE_CODE" => "Y",

		"SHOW_RATING" => "Y",

		"RATING_TEMPLATE" => "standart",

		"DISABLE_SONET_LOG" => "N",

		"DISABLE_EMAIL" => "N",

		"DISABLE_RSS" => "N",

		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",

		"SHOW_LOGIN" => "Y",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"status_0" => "status/#status_code#/",

			"category_1" => "category/#category_1#/",

			"category_1_status" => "category/#category_1#/status/#status_code#/",

			"category_2" => "category/#category_1#/#category_2#/",

			"category_2_status" => "category/#category_1#/#category_2#/status/#status_code#/",

			"user_ideas" => "user_idea/#user_id#/",

			"user_ideas_status" => "user_idea/#user_id#/status/#status_code#/",

			"user" => "user/#user_id#/",

			"user_subscribe" => "user/#user_id#/subscribe/",

			"post_edit" => "edit/#post_id#/",

			"post" => "#post_id#/",

			"post_rss" => "#blog#/rss/#type#/#post_id#/",

			"rss" => "#blog#/rss/#type#",

			"rss_status" => "rss/#type#/status/#status_code#/",

			"rss_category" => "rss/#type#/category/#category#/",

			"rss_category_status" => "rss/#type#/category/#category#/status/#status_code#/",

			"rss_user_ideas" => "rss/#type#/user/#user_id#/idea/",

			"rss_user_ideas_status" => "rss/#type#/user/#user_id#/idea/status/#status_code#/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"status_0" => Array(),

			"category_1" => Array(),

			"category_1_status" => Array(),

			"category_2" => Array(),

			"category_2_status" => Array(),

			"user_ideas" => Array(),

			"user_ideas_status" => Array(),

			"user" => Array(),

			"user_subscribe" => Array(),

			"post_edit" => Array(),

			"post" => Array(),

			"post_rss" => Array(),

			"rss" => Array(),

			"rss_status" => Array(),

			"rss_category" => Array(),

			"rss_category_status" => Array(),

			"rss_user_ideas" => Array(),

			"rss_user_ideas_status" => Array(),

		)

	)

);?> 


```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Филипп Болотов** 16.10.2012 15:36:23 |
| --- |
| Что бы подписать модератора Идей (пользователя, добавляющего специальный ответ) на email-уведомления о всех вновь добавляемых идея и комментариях к ним, следует выполнить в командной PHP-строке конструкцию:  |

| | --- | | ``` CModule::IncludeModule("blog");
 CModule::IncludeModule("idea");
 CIdeaManagment::getInstance()->Notification()->getEmailNotify()->Add("A", 12346);
 CIdeaManagment::getInstance()->Notification()->getEmailNotify()->Add("AI", 12346); ``` | где 123456 - идентификатор пользователя (модератора). |
|  |

```
<?$APPLICATION->IncludeComponent(

	"bitrix:idea",

	".default",

	Array(

		"BLOG_URL" => "idea_s1",

		"IBLOCK_CATOGORIES" => "51",

		"POST_BIND_USER" => array(0=>"1",),

		"POST_BIND_STATUS_DEFAULT" => "15",

		"MESSAGE_COUNT" => "10",

		"COMMENTS_COUNT" => "10",

		"TAGS_COUNT" => "0",

		"DATE_TIME_FORMAT" => "d.m.y G:i",

		"NAV_TEMPLATE" => "",

		"IMAGE_MAX_WIDTH" => "770",

		"EDITOR_RESIZABLE" => "Y",

		"EDITOR_DEFAULT_HEIGHT" => "300",

		"EDITOR_CODE_DEFAULT" => "N",

		"COMMENT_EDITOR_DEFAULT_HEIGHT" => "200",

		"SEF_MODE" => "Y",

		"SEF_FOLDER" => "/services/idea/",

		"CACHE_TYPE" => "A",

		"CACHE_TIME" => "3600",

		"CACHE_TIME_LONG" => "604800",

		"PATH_TO_SMILE" => "/bitrix/images/blog/smile/",

		"SET_TITLE" => "Y",

		"SET_NAV_CHAIN" => "Y",

		"USE_ASC_PAGING" => "Y",

		"COMMENT_ALLOW_VIDEO" => "Y",

		"NO_URL_IN_COMMENTS" => "",

		"ALLOW_POST_CODE" => "Y",

		"USE_GOOGLE_CODE" => "Y",

		"SHOW_RATING" => "Y",

		"RATING_TEMPLATE" => "standart",

		"DISABLE_SONET_LOG" => "N",

		"DISABLE_EMAIL" => "N",

		"DISABLE_RSS" => "N",

		"NAME_TEMPLATE" => "#NOBR##LAST_NAME# #NAME##/NOBR#",

		"SHOW_LOGIN" => "Y",

		"SEF_URL_TEMPLATES" => Array(

			"index" => "index.php",

			"status_0" => "status/#status_code#/",

			"category_1" => "category/#category_1#/",

			"category_1_status" => "category/#category_1#/status/#status_code#/",

			"category_2" => "category/#category_1#/#category_2#/",

			"category_2_status" => "category/#category_1#/#category_2#/status/#status_code#/",

			"user_ideas" => "user_idea/#user_id#/",

			"user_ideas_status" => "user_idea/#user_id#/status/#status_code#/",

			"user" => "user/#user_id#/",

			"user_subscribe" => "user/#user_id#/subscribe/",

			"post_edit" => "edit/#post_id#/",

			"post" => "#post_id#/",

			"post_rss" => "#blog#/rss/#type#/#post_id#/",

			"rss" => "#blog#/rss/#type#",

			"rss_status" => "rss/#type#/status/#status_code#/",

			"rss_category" => "rss/#type#/category/#category#/",

			"rss_category_status" => "rss/#type#/category/#category#/status/#status_code#/",

			"rss_user_ideas" => "rss/#type#/user/#user_id#/idea/",

			"rss_user_ideas_status" => "rss/#type#/user/#user_id#/idea/status/#status_code#/"

		),

		"VARIABLE_ALIASES" => Array(

			"index" => Array(),

			"status_0" => Array(),

			"category_1" => Array(),

			"category_1_status" => Array(),

			"category_2" => Array(),

			"category_2_status" => Array(),

			"user_ideas" => Array(),

			"user_ideas_status" => Array(),

			"user" => Array(),

			"user_subscribe" => Array(),

			"post_edit" => Array(),

			"post" => Array(),

			"post_rss" => Array(),

			"rss" => Array(),

			"rss_status" => Array(),

			"rss_category" => Array(),

			"rss_category_status" => Array(),

			"rss_user_ideas" => Array(),

			"rss_user_ideas_status" => Array(),

		)

	)

);?> 


```

``` CModule::IncludeModule("blog");
 CModule::IncludeModule("idea");
 CIdeaManagment::getInstance()->Notification()->getEmailNotify()->Add("A", 12346);
 CIdeaManagment::getInstance()->Notification()->getEmailNotify()->Add("AI", 12346); ```