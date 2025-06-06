# Умный фильтр

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

Умный фильтр

# Умный фильтр

Компонент подготавливает фильтр для выборки из инфоблока и выводит форму фильтра для фильтрации элементов.

### Описание **catalog.smart.filter**

Компонент должен подключаться перед компонентом вывода элементов каталога, иначе список элементов фильтроваться не будет. Компонент стандартный, входит в дистрибутив модуля и содержит четыре шаблона: **.default**, **bootstrap\_v4**, **visual\_horizontal** и **visual\_vertical** (последние два шаблона не поддерживаются, остались для сохранения совместимости).

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Умный фильтр*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

**Внимание!** В префильтре нельзя использовать вызов [CIBlockElement::SubQuery](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblockelement/SubQuery.php "Описание метода в документации для разработчиков").

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, элементы которого будут отфильтрованы. |
| ID раздела инфоблока | **SECTION\_ID** | Указывается идентификатор раздела, фильтрация элементов которого должна выполняться. Можно не указывать, если задан **Код раздела**.    **Примечание:** при включенном режиме ЧПУ параметр настраивается в секции **Управление адресами страниц**. |
| Код раздела | **SECTION\_CODE** | Указывается код раздела, фильтрация элементов которого должна выполняться. Можно не указывать, если задан **ID раздела инфоблока**. |
| Имя входящего массива для дополнительной фильтрации элементов | **PREFILTER\_NAME** | Задается имя переменной, в которую передается массив параметров из дополнительного фильтра. Если имя массива не указано, то будет использоваться значение по умолчанию. |
| Имя выходящего массива для фильтрации | **FILTER\_NAME** | Задается имя переменной, в которую передается массив параметров из фильтра. Если имя массива не указано, то будет использоваться значение по умолчанию. |
| Не отображать недоступные товары | **HIDE\_NOT\_AVAILABLE** | [Y|N] При отмеченной опции будут скрыты товары, для которых общее количество на складах меньше либо равно нулю, включен количественный учет и не разрешена покупка при отсутствии товара. |
| **Внешний вид** | | |
| Цветовая тема | **TEMPLATE\_THEME** | Задается цветовая схема для отображения фильтра. По умолчанию используется синяя схема (blue). |
| Вид отображения умного фильтра | **FILTER\_VIEW\_MODE** | Задается вид отображения умного фильтра: вертикальный (VERTICAL) или горизонтальный (HORIZONTAL). |
| Позиция для отображения всплывающего блока с информацией о фильтрации | **POPUP\_POSITION** | Задается позиция отображения всплывающего блока: **слева** (left) или **справа** (right). |
| Показывать количество | **DISPLAY\_ELEMENT\_COUNT** | [Y|N] При отмеченной опции в всплывающем блоке будет показано количество отобранных элементов в соответствии с условиями фильтрации. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции включается поддержка ЧПУ и становятся доступными поля настройки ЧПУ. |
| Правило для обработки | **SEF\_RULE** | Указывается правило обработки вызова умного фильтра. Для создания правила следует использовать шаблоны, доступные по кнопке **[...]**.    Например, компонент умного фильтра расположен на странице */examples/books/section.php*, тогда правило может быть задано следующим образом:  ```  /examples/books/#SECTION_ID#/filter/#SMART_FILTER_PATH#/apply/  ```  где `/filter/`, `/apply/` - выражения-ограничители, обязательно присутствующие в правиле (могут быть заменены на любые другие слова). |
| ID раздела инфоблока | **SECTION\_ID** | Указывается ID раздела инфоблока. Можно не задавать, если указан **Код раздела** или **Путь из символьных кодов раздела**.    **Примечание:** при отключенном режиме ЧПУ параметр настраивается в секции **Источник данных**. |
| Код раздела | **SECTION\_CODE** | Указывается символьный код раздела инфоблока. Можно не задавать, если указан **ID раздела инфоблока** или **Путь из символьных кодов раздела**.    **Примечание:** при отключенном режиме ЧПУ параметр настраивается в секции **Источник данных**. |
| Путь из символьных кодов раздела | **SECTION\_CODE\_PATH** | Задается путь из символьных кодов раздела инфоблока. Можно не задавать, если указан **Код раздела** или **ID раздела инфоблока**. |
| Блок ЧПУ умного фильтра | **SMART\_FILTER\_PATH** | Задается блок с параметрами фильтрации. По умолчанию подставляется значение *={$\_REQUEST["SMART\_FILTER\_PATH"]}*. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |
| **Дополнительные настройки** | | |
| Сохранять установки фильтра в сессии пользователя | **SAVE\_IN\_SESSION** | [Y|N] При отмеченной опции установки фильтра будут сохраняться в сессии пользователя. |
| Имя массива с переменными для построения ссылок в постраничной навигации | **PAGER\_PARAMS\_NAME** | Задается имя переменной, в которой передается массив с переменными для построения ссылок компонентом постраничной навигации. |
| **Цены** | | |
| Тип цены | **PRICE\_CODE** | Указывается тип цены для фильтрации элементов. |
| Показывать цены в одной валюте | **CONVERT\_CURRENCY** | [Y|N] При отмеченной опции цены в фильтре будут отображаться в одной валюте, даже если для товаров они будут заданы в разных валютах. Будет доступно для заполнения дополнительное поле.     |  |  |  | | --- | --- | --- | | Валюта, в которую будут сконвертированы цены | **CURRENCY\_ID** | Выбор валюты, в которой будут отображаться цены. |     **Примечание:** конвертация цен в умном фильтре работает только при созданном фасетном индексе. |
| **Поддержка Яндекс Островов (экспорт фильтра в XML)** | | |
| Включить поддержку Яндекс Островов | **XML\_EXPORT** | [Y|N] При отмеченной опции будет включена поддержка Яндекс Островов. |
| Заголовок | **SECTION\_TITLE** | Указывается поле, которое будет использоваться в качестве заголовка раздела. |
| Описание | **SECTION\_DESCRIPTION** | Задается поле, которое будет использоваться в качестве описания раздела. |

**Примечание:** в компоненте имеется специальный параметр **SHOW\_ALL\_WO\_SECTION**, принимающий значения **Y|N**. Если задано значение **Y**, то будут отображены все элементы инфоблока, если не указан раздел.

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:catalog.smart.filter", 
	".default", 
	array(
		"COMPONENT_TEMPLATE" => ".default",
		"IBLOCK_TYPE" => "books",
		"IBLOCK_ID" => "6",
		"SECTION_ID" => "10",
		"SECTION_CODE" => "",
		"FILTER_NAME" => "arrFilter",
		"HIDE_NOT_AVAILABLE" => "N",
		"TEMPLATE_THEME" => "blue",
		"FILTER_VIEW_MODE" => "horizontal",
		"DISPLAY_ELEMENT_COUNT" => "Y",
		"SEF_MODE" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000000",
		"CACHE_GROUPS" => "Y",
		"SAVE_IN_SESSION" => "N",
		"INSTANT_RELOAD" => "Y",
		"PAGER_PARAMS_NAME" => "arrPager",
		"PRICE_CODE" => array(
			0 => "BASE",
		),
		"CONVERT_CURRENCY" => "Y",
		"XML_EXPORT" => "N",
		"SECTION_TITLE" => "-",
		"SECTION_DESCRIPTION" => "-",
		"POPUP_POSITION" => "left",
		"SEF_RULE" => "/examples/books/#SECTION_ID#/filter/#SMART_FILTER_PATH#/apply/",
		"SECTION_CODE_PATH" => "",
		"SMART_FILTER_PATH" => $_REQUEST["SMART_FILTER_PATH"],
		"CURRENCY_ID" => "RUB"
	),
	false
);?>

```

### Смотрите также

* [Настройка отображения свойств в умном фильтре](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=42&LESSON_ID=5371)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 12  **Андрей Шварёв** 26.12.2015 13:32:50 |
| --- |
| Фильтр генерирует url вида arFilter\_<ид свойства>\_<некий код>.  **Задача:** взяв параметры фильтра из урл, использовать их для своих компонентов и фильтраций.  <некий код> = abs( crc32( "значение свойства" ) ) - т.е. это просто crc32 сумма от строки, взятая по модулю. |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх