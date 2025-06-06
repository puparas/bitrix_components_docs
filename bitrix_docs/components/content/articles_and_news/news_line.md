# Лента

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

[Новости (комплексный компонент)](/user_help/components/content/articles_and_news/news.php)
[Список новостей](/user_help/components/content/articles_and_news/news_list.php)
[Новость детально](/user_help/components/content/articles_and_news/news_detail.php)
[Лента](/user_help/components/content/articles_and_news/news_line.php)
[Список новостей для почты](/user_help/components/content/articles_and_news/news_list_mail.php)
[Календарь](/user_help/components/content/articles_and_news/news_calendar.php)
[Все новости](/user_help/components/content/articles_and_news/news_index.php)

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

[Статьи и новости](/user_help/components/content/articles_and_news/index.php)

Лента

# Лента

### Описание **news.line**

Одностраничный компонент, осуществляющий вывод списка элементов инфоблоков с датой и заголовком со ссылкой на страницу с подробной информацией. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Статьи и новости > Лента*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип информационного блока (используется только для проверки) | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Код информационного блока | **IBLOCKS** | Для выбранного типа инфоблока указывается идентификатор информационного блока, новости из которого будут выводиться. |
| Количество новостей на странице | **NEWS\_COUNT** | Указывается количество новостей, отображаемых на одной странице. |
| **Источник данных** | | |
| Поля | **FIELD\_CODE** | Данные элемента, которые могут выводиться в ленте новостей. (Требуется кастомизация шаблона.)  * **ID** – ID; * **CODE** – символьный код; * **XML\_ID** – XML\_ID; * **NAME** – название; * **TAGS** – теги; * **SORT** – сортировка; * **PREVIEW\_TEXT** – текст анонса; * **PREVIEW\_PICTURE** – картинка анонса; * **DETAIL\_TEXT** – детальный текст; * **DETAIL\_PICTURE** – детальная картинка. * **DATE\_ACTIVE\_FROM** – начало активности (дата); * **ACTIVE\_FROM** – начало активности (время); * **DATE\_ACTIVE\_TO** – окончание активности (дата); * **ACTIVE\_TO** – окончание активности (время); * **SHOW\_COUNTER** – количество показов; * **SHOW\_COUNTER\_START** – дата первого показа; * **IBLOCK\_TYPE\_ID** – тип информаионного блока; * **IBLOCK\_ID** – ID информационного блока; * **IBLOCK\_CODE** – символьный код информационного блока; * **IBLOCK\_NAME** – название информационного блока; * **IBLOCK\_EXTERNAL\_ID** – внешний код информационного блока; * **DATE\_CREATE** – дата создания; * **CREATED\_BY** – кем создан (ID); * **CREATED\_USER\_NAME** – дата изменения; * **MODIFIED\_BY** – кем изменен (ID); * **USER\_NAME** – кем изменен (имя). |
| Поле для первой сортировки новостей | **SORT\_BY1** | Поле для первой сортировки новостей:  * **ID** – по идентификатору; * **NAME** – по заголовку; * **ACTIVE\_FORM** – по дате начала активности; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения.  Выбрав пункт **(другое)->**, можно сформировать свой вариант поля для первой сортировки новостей. |
| Направление для первой сортировки новостей | **SORT\_ORDER1** | Задается направление для первой сортировки новостей:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Поле для второй сортировки новостей | **SORT\_BY2** | Поле для второй сортировки новостей:  * **ID** – по идентификатору; * **NAME** – по заголовку; * **ACTIVE\_FORM** – по дате начала активности; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения.  Выбрав пункт **(другое)->**, можно сформировать свой вариант поля для второй сортировки новостей. |
| Направление для второй сортировки новостей | **SORT\_ORDER2** | Задается направление для второй сортировки новостей:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| **Шаблоны ссылок** | | |
| URL, ведущий на страницу с содержимым элемента раздела | **DETAIL\_URL** | Задается адрес, ведущий на страницу с детальной информацией элемента раздела (по умолчанию - из настроек инфоблока). |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** | | |
| Формат показа даты | **ACTIVE\_DATE\_FORMAT** | Указывается формат показа даты. В выпадающем списке перечислены все возможные варианты показа даты, формируемые внутри компонента. Выбрав пункт **(другое)->**, можно сформировать свой вариант на основании php-функции **date**. |

### Пример вызова

```

<?$APPLICATION->IncludeComponent("bitrix:news.line","",Array(
		"IBLOCK_TYPE" => "news",
		"IBLOCKS" => Array("3"),
		"NEWS_COUNT" => "20",
		"FIELD_CODE" => Array("ID", "CODE"),
		"SORT_BY1" => "ACTIVE_FROM",
		"SORT_ORDER1" => "DESC",
		"SORT_BY2" => "SORT",
		"SORT_ORDER2" => "ASC",
		"DETAIL_URL" => "news_detail.php?ID=#ELEMENT_ID#",
		"ACTIVE_DATE_FORMAT" => "d.m.Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "300",
		"CACHE_GROUPS" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх