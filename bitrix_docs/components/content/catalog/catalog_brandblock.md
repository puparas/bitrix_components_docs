# Бренды

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

Бренды

# Бренды

### Описание **catalog.brandblock**

Компонент служит для отображения брендов (или некоторых других данных) на странице с детальной информацией о товаре. Компонент стандартный, входит в дистрибутив модуля и содержит два шаблона: **.default** и **bootstrap\_v4**.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Бренды*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Идентификатор инфоблока | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор необходимого информационного блока. |
| Идентификатор элемента инфоблока | **ELEMENT\_ID** | Указывается код, в котором передается идентификатор элемента. Поле может быть оставлено пустым, если указан **Код элемента инфоблока**. |
| Код элемента инфоблока | **ELEMENT\_CODE** | Указывается код элемента. Поле может быть оставлено пустым, если указан **Идентификатор элемента инфоблока**. |
| Таблица брендов | **PROP\_CODE** | Указываются свойства типа "Справочник", в которых хранятся данные. |
| Показывать бренды так же и деактивированных товаров | **SHOW\_DEACTIVATED** | [Y|N] При отмеченной опции будут отображаться и те бренды, которые заданы для деактивированных товаров. |
| Выводить как список | **SINGLE\_COMPONENT** | [Y|N] При отмеченной опции бренды будут выводится списком в одну строку. |
| Количество элементов на странице | **ELEMENT\_COUNT** | Указывается количество выводимых брендов. |
| **Внешний вид** | | |
| Максимальная ширина изображения без описания (пикс) | **WIDTH** | Указывается максимальная ширина изображения, вставляемого в бренд без описания. |
| Максимальная высота изображения без описания (пикс) | **HEIGHT** | Указывается максимальная высота изображения, вставляемого в бренд без описания. |
| Максимальная ширина изображения с описанием (пикс) | **WIDTH\_SMALL** | Указывается максимальная ширина изображения, вставляемого в бренд с описанием. |
| Максимальная высота изображения с описанием (пикс) | **HEIGHT\_SMALL** | Указывается максимальная высота изображения, вставляемого в бренд с описанием. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.brandblock","",
Array(
		"IBLOCK_TYPE" => "books",
		"IBLOCK_ID" => "6",
		"ELEMENT_ID" => $_REQUEST["ELEMENT_ID"],
		"ELEMENT_CODE" => "",
		"PROP_CODE" => "PUBLISH",
		"SHOW_DEACTIVATED" => "N",
		"SINGLE_COMPONENT" => "N",
		"ELEMENT_COUNT" => "6",
		"WIDTH" => "120",
		"HEIGHT" => "45",
		"WIDTH_SMALL" => "80",
		"HEIGHT_SMALL" => "40",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "36000000",
		"CACHE_GROUPS" => "Y"
	),
false
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх