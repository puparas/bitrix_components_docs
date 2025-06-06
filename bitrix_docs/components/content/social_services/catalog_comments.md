# Комментарии к товарам

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

[Комментарии к товарам](/user_help/components/content/social_services/catalog_comments.php)
[Кнопки социальных сетей](/user_help/components/content/social_services/catalog_socnets_buttons.php)

[Сервисы](/user_help/components/services/index.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Контент](/user_help/components/content/index.php)

[Социальные сервисы](/user_help/components/content/social_services/index.php)

Комментарии к товарам

# Комментарии к товарам

### Описание **catalog.comments**

Компонент служит для отображения формы добавления комментариев к товару и обычно размещается на странице с детальной информацией о товаре. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Социальные сервисы > Комментарии к товарам*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Идентификатор инфоблока | **IBLOCK\_ID** | Для выбранного типа инфоблока указывается идентификатор инфоблока, к товарам которого будут добавляться комментарии. |
| Идентификатор товара | **ELEMENT\_ID** | Указывается код, в котором передается идентификатор товара. Поле может быть оставлено пустым, если указан **Код товара**. |
| Код товара | **ELEMENT\_CODE** | Указывается код товара. Поле может быть оставлено пустым, если указан **Идентификатор товара**. |
| Путь к комментируемому товару | **URL\_TO\_COMMENT** | Путь к детальной странице товара. |
| Ширина | **WIDTH** | Ширина блока с комментариями к товарам. |
| Количество показываемых комментариев | **COMMENTS\_COUNT** | Количество показываемых комментариев на странице (используется обратная постраничка). |
| **Внешний вид** | | |
| Цветовая тема | **TEMPLATE\_THEME** | Задается цветовая схема для отображения комментариев к товарам. По умолчанию используется синяя схема (blue). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Комментарии на сайте** | | |
| Использовать комментарии | **BLOG\_USE** | [Y|N] При отмеченной опции становится доступным функционал комментариев     |  |  |  | | --- | --- | --- | | Надпись на вкладке | **BLOG\_TITLE** | Надпись на вкладке с комментариями. | | Название блога латинскими буквами | **BLOG\_URL** | Задается код блога (латинскими символами), в котором будут храниться комментарии к товарам. | | Путь к улыбкам | **PATH\_TO\_SMILE** | Указывается путь к папке со смайлами относительно корня сайта. | | Уведомление по электронной почте | **EMAIL\_NOTIFY** | [Y|N] При отмеченной опции будет отправляться уведомление по электронной почте в случая добавления к товару комментария. | | Режим ajax | **AJAX\_POST** | [Y|N] При отмеченной опции в комментариях будет использоваться технология AJAX. | | Показывать администраторам ссылку на все комментарии пользователя | **SHOW\_SPAM** | [Y|N] При отмеченной опции администратор будет видеть ссылку на страницу со всеми комментариями каждого пользователя. | | Включить рейтинг | **SHOW\_RATING** | [Y|N] При установленной опции для комментариев будет доступен функционал рейтинга. | | Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопок рейтинга:  * по умолчанию; * Мне нравится (текстовый); * Мне нравится (графический); * Нравится / Не нравится (текстовый); * Нравится / Не нравится (графический).  Значение **По умолчанию** берется из настроек рейтингов. |  к товарам на основе блогов. |
| **Комментарии в Facebook\*** | | |
| Использовать Facebook\* | **FB\_USE** | [Y|N] При отмеченной опции отзывы о товаре можно будет оставлять с помощью Facebook\*, становятся активными дополнительные поля     |  |  |  | | --- | --- | --- | | Надпись на вкладке | **FB\_TITLE** | Надпись на вкладке с комментариями в Facebook\*. | | Идентификатор пользователя Facebook\* - модератора сообщений | **FB\_USER\_ADMIN\_ID** | Задается идентификатор (из аккаунта в Facebook\*) пользователя, который будет модератором комментариев к товарам. | | Идентификатор приложения Facebook\* (app\_id) | **FB\_APP\_ID** | Указывается идентификатор приложения Facebook\*, который можно получить с помощью ссылки *https://developers.facebook.com/setup*. | | Цветовая схема | **FB\_COLORSCHEME** | Задается цветовая схема для отображения блока с комментариями в Facebook\*: *light* - светлая или *dark* - темная. | | Сортировка | **FB\_ORDER\_BY** | Задается сортировка комментариев:  * *social* - социальная релевантность; * *reverse\_time* - по времени создания обратный; * *time* - по времени создания. |   \* Социальная сеть признана экстремистской и запрещена на территории Российской Федерации.   \* Социальная сеть признана экстремистской и запрещена на территории Российской Федерации. |
| **Комментарии В Контакте** | | |
| Использовать Вконтакте | **VK\_USE** | [Y|N] При отмеченной опции отзывы о товаре можно будет оставлять с помощью Вконтакте, станут доступны дополнительные поля     |  |  |  | | --- | --- | --- | | Надпись на вкладке | **VK\_TITLE** | Надпись на вкладке с комментариями ВКонтакте. | | Идентификатор приложения (API ID) | **VK\_API\_ID** | Указывается идентификатор приложения Вконтакте, который можно получить с помощью ссылки *http://vk.com/developers.php?o=-1&p=Comments*. |  . Компонент обращается к VKontakte только по протоколу https. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.comments","",
Array(
		"TEMPLATE_THEME" => "blue",
		"IBLOCK_TYPE" => "books",
		"IBLOCK_ID" => "6",
		"ELEMENT_ID" => $_REQUEST["ELEMENT_ID"],
		"ELEMENT_CODE" => "",
		"URL_TO_COMMENT" => "/e-store/books/element.php?ELEMENT_ID=#ELEMENT_ID#",
		"WIDTH" => "500",
		"COMMENTS_COUNT" => "4",
		"BLOG_USE" => "Y",
		"FB_USE" => "N",
		"VK_USE" => "N",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "0",
		"BLOG_TITLE" => "Комментарии",
		"BLOG_URL" => "catalog_comments",
		"PATH_TO_SMILE" => "/bitrix/images/blog/smile/",
		"EMAIL_NOTIFY" => "N",
		"AJAX_POST" => "N",
		"SHOW_SPAM" => "Y",
		"SHOW_RATING" => "Y",
		"RATING_TYPE" => "like_graphic",
		"FB_TITLE" => "Facebook",
		"FB_USER_ADMIN_ID" => "",
		"FB_APP_ID" => "",
		"FB_COLORSCHEME" => "dark",
		"FB_ORDER_BY" => "time",
		"VK_TITLE" => "Вконтакте",
		"VK_API_ID" => "API_ID"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх