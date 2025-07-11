|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается один из созданных в системе типов информационного блока. |
| Инфоблок |

| Для выбранного типа инфоблока указывается идентификатор информационного блока, фотографии из которого будут выводиться. |
| **Источник данных** |

| |
| Поля разделов |

| Указываются поля раздела, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу *Ctrl* либо в коде, указывая массив:  ``` Array("ID","CODE",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив) ничего отображаться не будет. |
| Свойства раздела |

| Указываются свойства раздела, которые будут отображены на странице. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, свойства не будут выведены. |
| По какому полю сортируем разделы |

| Указывается поле, по которому будет происходить сортировка разделов в TOP’е элементов:  * **SORT** - по индексу сортировки; * **TIMESTAMP\_X** - по дате изменения; * **NAME** - по названию; * **ID** - по идентификатору; * **DEPTH\_LEVEL** - по уровню вложенности папки.  Можно указать код любого другого поля. |
| Порядок сортировки разделов |

| Задается порядок сортировки разделов:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| По какому полю сортируем фотографии |

| Указывается поле, по которому будет происходить сортировка фотографий внутри каждого раздела:  * **SHOWS** – по количеству просмотров в среднем; * **SORT** – по индексу сортировки; * **TIMESTAMP\_X** – по дате последнего изменения; * **NAME** – по названию; * **ID** – по идентификатору; * **ACTIVE\_FROM** – по дате активности с; * **ACTIVE\_TO** – по дате активности по. |
| Порядок сортировки фотографий в разделе |

| Задается порядок сортировки фотографий в разделе:  * **ASC** – **По возрастанию**; * **DESC** – **По убыванию**. |
| Имя выходящего массива для фильтрации |

| Задается имя переменной, в которой передается массив параметров из фильтра. Служит для определения выходящих из фильтра элементов. Поле может быть оставлено пустым, тогда используется значение по умолчанию. |
| Поля |

| Указываются поля, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив), на странице списка будут выведены поля по умолчанию. |
| Свойства |

| Указываются свойства, которые будут отображены на странице TOP'а элементов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, на странице детального просмотра свойства не будут выведены. |
| **Внешний вид** |

| |
| Максимальное количество выводимых разделов |

| Задается максимальное количество выводимых разделов. |
| Максимальное количество фотографий, выводимых в каждом разделе |

| Задается максимальное количество фотографий, выводимых в TOP’е элементов в каждом разделе. |
| Количество фотографий, выводимых в одной строке таблицы |

| Указывается количество фотографий, выводимых в одной строке таблицы. |
| **Шаблоны ссылок** |

| |
| URL, ведущий на страницу с содержимым раздела |

| Указывается адрес страницы с содержимым раздела. |
| URL, ведущий на страницу с содержимым элемента раздела |

| Указывается адрес страницы с содержимым элемента раздела. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. |
| Кешировать при установленном фильтре |

| [Y|N] При отмеченной опции каждый результат, полученный из фильтра, будет кешироваться. |
| Учитывать права доступа |

``` Array("ID","CODE",""), ```

``` Array("NAME","PREVIEW_TEXT","PREVIEW_PICTURE","DETAIL_TEXT",""), ```

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