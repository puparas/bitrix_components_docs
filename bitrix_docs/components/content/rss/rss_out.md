# RSS новости (экспорт)

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

[RSS новости (импорт)](/user_help/components/content/rss/rss_show.php)
[RSS новости (экспорт)](/user_help/components/content/rss/rss_out.php)

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

[RSS](/user_help/components/content/rss/index.php)

RSS новости (экспорт)

# RSS новости (экспорт)

Компонент предназначен для создания страницы, которая отдает выбранные новости вашего сайта в формате RSS.

### Описание **rss.out**

Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > RSS > RSS новости (экспорт)*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип информационного блока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Информационный блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, информация из которого будет экспортироваться. |
| Раздел | **SECTION\_ID** | Указывается числовой код, в котором передается идентификатор раздела. Поле может быть оставлено пустым, если указан **Код раздела**. |
| Код раздела | **SECTION\_CODE** | Указывается символьный код раздела, из которого будут выбраны новости. Поле может быть оставлено пустым, если указан **Раздел**. |
| Количество новостей для экспорта | **NUM\_NEWS** | Задается количество новостей для экспорта. |
| Количество дней для экспорта | **NUM\_DAYS** | Указывается количество дней для экспорта новостей. |
| **Источник данных** | | |
| Поле для первой сортировки новостей | **SORT\_BY1** | Поле для первой сортировки новостей:  * **ID** - по идентификатору; * **NAME** – по заголовку; * **ACTIVE\_FROM** – по дате начала активности; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** - по дате последнего изменения; * **CREATED** - по дате создания. |
| Направление для первой сортировки новостей | **SORT\_ORDER1** | Направление для первой сортировки новостей:  * **ASC** – по возрастанию; * **DECS** – по убыванию. |
| Поле для второй сортировки новостей | **SORT\_BY2** | Поле для второй сортировки новостей:  * **ID** - по идентификатору; * **NAME** – по заголовку; * **ACTIVE\_FROM** – по дате начала активности; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** - по дате последнего изменения; * **CREATED** - по дате создания. |
| Направление для второй сортировки новостей | **SORT\_ORDER2** | Направление для второй сортировки новостей:  * **ASC** – по возрастанию; * **DECS** – по убыванию. |
| Фильтр | **FILTER\_NAME** | Задается имя глобальной переменной для фильтрации новостей. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Кешировать при установленном фильтре | **CACHE\_FILTER** | [Y|N] При отмеченной опции каждый результат, полученный из фильтра, будет кешироваться. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Параметры RSS** | | |
| Время жизни (в минутах) | **RSS\_TTL** | Указывается количество минут, на которые канал может кешироваться перед обновлением ресурса. |
| Экспортировать в диалект Яндекса | **YANDEX** | [Y|N] При отмеченной опции новости будут экспортироваться в диалект Яндекса. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:rss.out","",Array(
		"IBLOCK_TYPE" => "news", 
		"IBLOCK_ID" => "3", 
		"SECTION_ID" => "", 
		"SECTION_CODE" => "", 
		"NUM_NEWS" => "20", 
		"NUM_DAYS" => "30", 
		"RSS_TTL" => "60", 
		"YANDEX" => "Y", 
		"SORT_BY1" => "ACTIVE_FROM", 
		"SORT_ORDER1" => "DESC", 
		"SORT_BY2" => "SORT", 
		"SORT_ORDER2" => "ASC", 
		"FILTER_NAME" => "", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600",
		"CACHE_GROUPS" => "Y", 
		"CACHE_FILTER" => "N"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 1  **Иван Салыгин** 18.05.2016 11:16:24 |
| --- |
| при выводе rss ленты раздела, если у вас есть подразделы, элементы подразделов по умолчанию не выводятся. лечится добавлением незадокументрованного параметра "INCLUDE\_SUBSECTIONS" => "Y" |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх