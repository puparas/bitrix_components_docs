# Фильтр по элементам

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

[Структура разделов](/user_help/components/content/catalog/catalog_section_list.php)
[Элементы раздела](/user_help/components/content/catalog/catalog_section.php)
[Каталог (комплексный компонент)](/user_help/components/content/catalog/catalog.php)
[Поиск по каталогу](/user_help/components/content/catalog/catalog_search.php)
[Бренды](/user_help/components/content/catalog/catalog_brandblock.php)
[Элемент каталога детально](/user_help/components/content/catalog/catalog_element.php)
[Список сравниваемых элементов каталога](/user_help/components/content/catalog/catalog_compare_list.php)
[Таблица сравнения](/user_help/components/content/catalog/catalog_compare_result.php)
[Умный фильтр](/user_help/components/content/catalog/smart_filter.php)
[Фильтр по элементам](/user_help/components/content/catalog/catalog_filter.php)
[Список информационных блоков заданного типа](/user_help/components/content/catalog/catalog_main.php)
[top элементов каталога](/user_help/components/content/catalog/catalog_top.php)
[top элементов каталога по параметру (магазин) - не поддерживается с версии 12.5](/user_help/components/content/catalog/store_catalog_top.php)
[Конструктор наборов](/user_help/components/content/catalog/catalog_set_constructor.php)
[Разделы с top'ом элементов](/user_help/components/content/catalog/catalog_sections_top.php)
[Список связанных элементов](/user_help/components/content/catalog/catalog_link_list.php)

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

[Каталог](/user_help/components/content/catalog/index.php)

Фильтр по элементам

# Фильтр по элементам

### Описание **catalog.filter**

Компонент выводит форму фильтра для фильтрации элементов информационных блоков.

Компонент содержит 3 шаблона: **.default**, **flat** и **bootstrap\_v4**. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Фильтр по элементам*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфо-блока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфо-блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, элементы которого будут отфильтрованы. |
| Имя входящего массива для дополнительной фильтрации элементов | **PREFILTER\_NAME** | Задается имя переменной, в которую передается массив параметров из дополнительного фильтра. Если имя массива не указано, то будет использоваться значение по умолчанию. |
| Имя выходящего массива для фильтрации | **FILTER\_NAME** | Задается имя переменной, в которую передается массив параметров из фильтра. Если имя массива не указано, то будет использоваться значение по умолчанию. |
| Поля | **FIELD\_CODE** | Указываются дополнительные поля элементов инфоблока, по которым будет возможна фильтрация. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания полей в строках (т.е. если задан пустой массив), будут выведены поля по умолчанию. |
| Свойства | **PROPERTY\_CODE** | Указываются свойства инфоблока, которые будут отображены при показе в качестве полей фильтра. При выборе пункта **(не выбрано)->** и без указания кодов свойств в строках, свойства выведены не будут.   Значения свойств типа "Список" отображаются в фильтре в соответствии с настройками, заданными в форме редактирования самого свойства (поле "Внешний вид"). |
| Поля предложений | **OFFERS\_FIELD\_CODE** | Выбираются поля предложений. С помощью клавиши Ctrl можно выбрать несколько значений. Данный параметр появляется при настройке компонента на инфоблок с поддержкой SKU. |
| Свойства предложений | **OFFERS\_PROPERTY\_CODE** | Указываются свойства предложений. Можно добавлять свои. Данный параметр появляется при настройке компонента на инфоблок с поддержкой SKU. |
| **Внешний вид** | | |
| Высота списков множественного выбора | **LIST\_HEIGHT** | Указывается высота множественных списков выбора, отображаемых в фильтре. |
| Ширина однострочных текстовых полей ввода | **TEXT\_WIDTH** | Указывается ширина текстового поля ввода в форме фильтра. |
| Ширина полей ввода для числовых интервалов | **NUMBER\_WIDTH** | Указывается ширина полей ввода для числовых интервалов в форме фильтра. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** | | |
| Сохранять установки фильтра в сессии пользователя | **SAVE\_IN\_SESSION** | [Y|N] При отмеченной опции установки фильтра будут сохраняться в сессии пользователя. |
| Имя массива с переменными для построения ссылок в постраничной навигации | **PAGER\_PARAMS\_NAME** | Задается имя переменной, в которой передается массив с переменными для построения ссылок компонентом постраничной навигации. |
| **Цены** | | |
| Тип цены | **PRICE\_CODE** | Указывается тип цены для выводимых элементов. Если не задан ни один из типов, то цена товара и кнопки **Купить** и **В корзину** показаны не будут. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent (
"bitrix:catalog.filter",
	"",
	Array(
		"IBLOCK_TYPE" => "news",
		"IBLOCK_ID" => "2",
		"FILTER_NAME" => "arrFilter",
		"FIELD_CODE" => array(),
		"PROPERTY_CODE" => array(),
		"OFFERS_FIELD_CODE" => array(),
		"OFFERS_PROPERTY_CODE" => array(),
		"PRICE_CODE" => array(),
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000000",
		"CACHE_GROUPS" => "Y",
		"LIST_HEIGHT" => "5",
		"TEXT_WIDTH" => "20",
		"NUMBER_WIDTH" => "5",
		"SAVE_IN_SESSION" => "N",
		"PREFILTER_NAME" => "preFilter",
		"PAGER_PARAMS_NAME" => "arrPager"
	),
false
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Роберт Басыров** 14.05.2009 18:45:20 |
| --- |
| Для изменения ширины выпадающего списка в шаблоне компонента создайте файл style.css и в него добавьте:   | Код | | --- | | ``` .data-table select {      width: 100px !important;  }  ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх