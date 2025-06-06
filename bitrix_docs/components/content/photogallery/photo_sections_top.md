# Разделы с TOP'ом фотографий

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

[Фотогалерея (комплексный компонент)](/user_help/components/content/photogallery/photo.php)
[Разделы с TOP'ом фотографий](/user_help/components/content/photogallery/photo_sections_top.php)
[Фотографии раздела](/user_help/components/content/photogallery/photo_section.php)
[Фотография детально](/user_help/components/content/photogallery/photo_detail.php)
[Случайное фото](/user_help/components/content/photogallery/photo_random.php)

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

[Фотогалерея](/user_help/components/content/photogallery/index.php)

Разделы с TOP'ом фотографий

# Разделы с TOP'ом фотографий

### Описание **photo.sections.top**

Одностраничный компонент служит для вывода TOP'а фотографий, сгруппированных по разделам. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Фотогалерея > Разделы с TOP'ом фотографий*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

#### Описание параметров

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблока указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| **Источник данных** | | |
| Поля разделов | **SECTION\_FIELDS** | Указываются поля раздела, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу *Ctrl* либо в коде, указывая массив:  ``` Array("ID","CODE",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив) ничего отображаться не будет. |
| Свойства раздела | **SECTION\_USER\_FIELDS** | Указываются свойства раздела, которые будут отображены на странице. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, свойства не будут выведены. |
| По какому полю сортируем разделы | **SECTION\_SORT\_FIELD** | Указывается поле, по которому будет происходить сортировка разделов в TOP’е элементов:  * **SORT** - по индексу сортировки; * **TIMESTAMP\_X** - по дате изменения; * **NAME** - по названию; * **ID** - по идентификатору; * **DEPTH\_LEVEL** - по уровню вложенности папки.  Можно указать код любого другого поля. |
| Порядок сортировки разделов | **SECTION\_SORT\_ORDER** | Задается порядок сортировки разделов:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| По какому полю сортируем фотографии | **ELEMENT\_SORT\_FIELD** | Указывается поле, по которому будет происходить сортировка фотографий внутри каждого раздела:  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **ACTIVE\_FROM** – по дате активности с; * **ACTIVE\_TO** – по дате активности по. |
| Порядок сортировки фотографий в разделе | **ELEMENT\_SORT\_ORDER** | Задается порядок сортировки фотографий в разделе:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Имя выходящего массива для фильтрации | **FILTER\_NAME** | Задается имя переменной, в которой передается массив параметров из фильтра. Служит для определения выходящих из фильтра элементов. Поле может быть оставлено пустым, тогда используется значение по умолчанию. |
| Поля | **FIELD\_CODE** | Указываются поля, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства | **PROPERTY\_CODE** | Указываются свойства, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| **Внешний вид** | | |
| Максимальное количество выводимых разделов | **SECTION\_COUNT** | Задается максимальное количество выводимых разделов. |
| Максимальное количество фотографий, выводимых в каждом разделе | **ELEMENT\_COUNT** | Задается максимальное количество фотографий, выводимых в TOP’е элементов в каждом разделе. |
| Количество фотографий, выводимых в одной строке таблицы | **LINE\_ELEMENT\_COUNT** | Указывается количество фотографий, выводимых в одной строке таблицы. |
| **Шаблоны ссылок** | | |
| URL, ведущий на страницу с содержимым раздела | **SECTION\_URL** | Указывается адрес страницы с содержимым раздела. |
| URL, ведущий на страницу с содержимым элемента раздела | **DETAIL\_URL** | Указывается адрес страницы с содержимым элемента раздела. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Кешировать при установленном фильтре | **CACHE\_FILTER** | [Y|N] При отмеченной опции каждый результат, полученный из фильтра, будет кешироваться. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |

### Пример вызова

```
<$APPLICATION->IncludeComponent("bitrix:photo.sections.top","",Array(
		"IBLOCK_TYPE" => "gallery",
		"IBLOCK_ID" => 9,
		"SECTION_FIELDS" => array("ID"),
		"SECTION_USER_FIELDS" => array(),
		"SECTION_SORT_FIELD" => "sort",
		"SECTION_SORT_ORDER" => "asc",
		"ELEMENT_SORT_FIELD" => "sort",
		"ELEMENT_SORT_ORDER" => "asc",
		"FILTER_NAME" => "arrFilter",
		"FIELD_CODE" => Array(),
		"PROPERTY_CODE" => Array(),
		"SECTION_URL" => "section.php?SECTION_ID=#SECTION_ID#",
		"DETAIL_URL" => "detail.php?SECTION_ID=#SECTION_ID#&ELEMENT_ID=#ELEMENT_ID#",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => 3600,
		"CACHE_FILTER" => "N",
		"CACHE_GROUPS" => "Y",
		"SECTION_COUNT" => "20",
		"ELEMENT_COUNT" => "9",
		"LINE_ELEMENT_COUNT" => "3"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх