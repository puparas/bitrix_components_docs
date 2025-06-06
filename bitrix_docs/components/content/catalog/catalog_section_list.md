# Структура разделов

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

Структура разделов

# Структура разделов

Компонент выводит список разделов инфоблока.

### Описание **catalog.section.list**

Компонент стандартный, входит в дистрибутив модуля и содержит 5 шаблонов: **store\_v3**, **.default**, **tree**, **store\_v3\_menu** и **bootstrap\_v4**.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Структура разделов*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |  |
| --- | --- | --- | --- |
| **Поле** | **Параметр** | **Описание** | **Примечание** |
| **Основные параметры** | | | |
| Тип инфо-блока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |  |
| Инфо-блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор необходимого информационного блока. |  |
| ID раздела | **SECTION\_ID** | Указывается код, в котором передается идентификатор раздела. |  |
| Код раздела | **SECTION\_CODE** | Указывается код раздела. |  |
| **Источник данных** | | | |
| Показывать количество элементов в разделе | **COUNT\_ELEMENTS** | [Y|N] При отмеченной опции будет показано количество элементов в разделе. |  |
| Показывать количество | **COUNT\_ELEMENTS\_FILTER** | Выбирается для каких товаров показывать количество: активных, доступных или всех. |  |
| Дополнительный фильтр для подсчета количества элементов в разделе | **ADDITIONAL\_COUNT\_ELEMENTS\_FILTER** | Задается имя переменной, в которую передается параметры дополнительного фильтра для подсчета количества элементов в разделе. |  |
| Скрывать разделы с нулевым количеством элементов | **HIDE\_SECTIONS\_WITH\_ZERO\_COUNT\_ELEMENTS** | [Y|N] При отмеченной опции разделы без элементов отображаться не будут. |  |
| Максимальная отображаемая глубина разделов | **TOP\_DEPTH** | Параметр определяет максимальную глубину отображаемых разделов. |  |
| Поля разделов | **SECTION\_FIELDS** | Указываются поля раздела, которые будут отображены на странице структуры разделов. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив:  ```  Array("ID","CODE",""), ```  При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже (т.е. если задан пустой массив) ничего отображаться не будет. |  |
| Свойства раздела | **SECTION\_USER\_FIELDS** | Указываются свойства раздела, которые будут отображены на странице. Заполняется из публичной части редактора, удерживая клавишу Ctrl либо в коде, указывая массив. При выборе пункта **(не выбрано)->** и без указания вычисления полей в строках ниже, свойства не будут выведены. |  |
| Имя массива со значениями фильтра разделов | **FILTER\_NAME** | Задается имя переменной, в которую передается массив параметров из фильтра. Если имя массива не указано, то будет использоваться значение по умолчанию. |  |
| **Внешний вид** (для шаблона **.default** и **bootstrap\_v4**) | | | |
| Вид списка подразделов | **VIEW\_MODE** | Определяется способ отображения списка подразделов: в виде списка (LINE), многоуровнего списка (LIST), текста (TEXT) или плитки (TILE). |  |
| Показывать название раздела | **SHOW\_PARENT\_NAME** | [Y|N] При отмеченной опции будет выводится название раздела (кроме раздела верхнего уровня). |  |
| **Внешний вид** (для шаблона **store\_v3**) | | | |
| Начальное смещение (скролл) блока разделов | **SECTIONS\_OFFSET\_MODE** | Выбирается вариант смещения блока разделов. |  |
| **Шаблоны ссылок** | | | |
| URL, ведущий на страницу с содержимым раздела | **SECTION\_URL** | Указывается путь к странице с содержимым раздела. |  |
| **Настройки кеширования** | | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |  |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |  |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |  |
| **Дополнительные настройки** | | | |
| Включать раздел в цепочку навигации | **ADD\_SECTIONS\_CHAIN** | [Y|N] При отмеченной опции название или заголовок (если задан в настройках SEO) раздела будет включен в цепочку навигации. |  |
| **Служебные параметры** (**не** отображаются в настройках компонента) | | | |
| Кастомная сортировка по произвольному числу параметров | **CUSTOM\_SECTION\_SORT** | Данный служебный параметр можно передать в вызове компонента. Тип параметра - массив. Структура массива соответствует ключу **$arOrder** метода [CIBlockSection::GetList](https://dev.1c-bitrix.ru/api_help/iblock/classes/ciblocksection/getlist.php). | Доступно с версии модуля **iblock** 20.0.400.  Параметр не используется в штатных шаблонах комплексного компонента [catalog](/user_help/components/content/catalog/catalog.php). |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.section.list","",
Array(
		"ADDITIONAL_COUNT_ELEMENTS_FILTER" => "additionalCountFilter",		
		"VIEW_MODE" => "TEXT",
		"SHOW_PARENT_NAME" => "Y",
		"IBLOCK_TYPE" => "",
		"IBLOCK_ID" => "",
		"SECTION_ID" => $_REQUEST["SECTION_ID"],
		"SECTION_CODE" => "",
		"SECTION_URL" => "",
		"COUNT_ELEMENTS" => "Y",
		"COUNT_ELEMENTS_FILTER" => "CNT_ACTIVE",
		"HIDE_SECTIONS_WITH_ZERO_COUNT_ELEMENTS" => "N",
		"TOP_DEPTH" => "2",
		"SECTION_FIELDS" => "",
		"SECTION_USER_FIELDS" => "",
		"ADD_SECTIONS_CHAIN" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000000",
		"CACHE_NOTES" => "",
		"CACHE_GROUPS" => "Y"
	)		
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 2  **Андрей Воробьев** 25.11.2013 12:15:00 |
| --- |
| Чтобы выбрать все пользовательские поля раздела укажите       | Код | | --- | | ```      "SECTION_USER_FIELDS" => array('UF_*'), ``` | |
|  |

| 7  **Роберт Басыров** 10.06.2009 14:10:16 |
| --- |
| Вывод разделов каталога в 2 колонки требует изменения в компоненте **bitrix:catalog.section.list**  В файле **result\_modifier.php**: |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх