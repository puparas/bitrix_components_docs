# Конструктор наборов

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

Конструктор наборов

**Недоступно в редакциях:**Стандарт, Старт

# Конструктор наборов

### Описание **catalog.set.constructor**

Компонент служит для отображения заданного набора и составления собственного набора товаров. Компонент содержит 2 шаблона: **.default** и **bootstrap\_v4**. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Конструктор наборов*.

Компонент относится к модулю [Торговый каталог](/user_help/store/catalog/index.php).

Компонент работает с одним инфоблоком (как и [catalog](https://dev.1c-bitrix.ru/user_help/components/content/catalog/catalog.php)).

На текущий момент не работает с товаром, имеющим торговые предложения (как единым целым).

При передаче ID торгового предложения компонент будет искать набор для торгового предложения. Если не найдет - будет искать набор для головного товара.

На текущий момент компонент не показывает групповые скидки (на набор в целом) - только на отдельные элементы набора.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE\_ID** | Тип инфоблока (нужен только при настройке компонента в визуальном редакторе). |
| Инфоблок | **IBLOCK\_ID** | ID инфоблока, которому принадлежит элемент (простой товар, комплект или торговое предложение). |
| ID элемента | **ELEMENT\_ID** | Указывается код, в котором передается идентификатор элемента. |
| **Внешний вид** | | |
| Число элементов набора, готовых к добавлению в корзину | **BUNDLE\_ITEMS\_COUNT** | Сколько товаров из набора сразу добавятся в корзину при нажатии "Купить набор". По умолчанию 3 элемента.  Пример: если в наборе 6 товаров, а в этом поле установлено значение - 3, то из предложенных 6 три автоматически попадают в корзину, а три покупатель может добавить самостоятельно. В корзину автоматически попадают те товары из набора, чье значение Сортировки в списке ниже, чем у других товаров. |
| Цветовая тема | **TEMPLATE\_THEME** | Задается цветовая схема для отображения элементов каталога. По умолчанию используется синяя схема (blue). |
| **Шаблоны ссылок** | | |
| URL, ведущий на страницу с корзиной покупателя | **BASKET\_URL** | Указывается путь к странице с корзиной покупателя. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа групп пользователей при кешировании. |
| **Цены** | | |
| Тип цены | **PRICE\_CODE** | Перечень кодов (НЕ ID - так же, как у каталожных компонент) типов цен, среди которых будет вычисляться минимальная. |
| Включать НДС в цену | **PRICE\_VAT\_INCLUDE** | [Y|N] При отмеченной опции цены будут показаны с учетом НДС. |
| Показывать цены в одной валюте | **CONVERT\_CURRENCY** | [Y|N] При установке флажка цены будут выводиться в одной валюте, даже если в каталоге они будут заданы в разных валютах. Если флажок не установлен, цены товаров набора будут показаны в валюте товара-владельца. При выборе данной опции становится доступным дополнительное поле.     |  |  |  | | --- | --- | --- | | Валюта, в которую будут сконвертированы цены | **CURRENCY\_ID** | Выбор валюты, в которой будут отображаться цены. | |
| Свойства предложений, добавляемые в корзину | **OFFERS\_CART\_PROPERTIES** | Из списка выбираются свойства, которые можно добавить в корзину. Для выбора нескольких свойств нужно использоать клавишу Ctrl. Данный параметр появляется при настройке компонента на инфоблок с поддержкой SKU. То есть, имеет смысл только для ситуации, когда в набор входят торговые предложения из одного инфоблока. Может быть настроен в визуальном редакторе, только если в IBLOCK\_ID указан инфоблок головного товара. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
   "bitrix:catalog.set.constructor",
   "",
   Array(
      "BASKET_URL" => "/personal/basket.php",
      "BUNDLE_ITEMS_COUNT" => "3",
      "CACHE_GROUPS" => "Y",
      "CACHE_TIME" => "36000000",
      "CACHE_TYPE" => "A",
      "CONVERT_CURRENCY" => "Y",
      "CURRENCY_ID" => "RUB",
      "ELEMENT_ID" => "4",
      "IBLOCK_ID" => "2",
      "IBLOCK_TYPE_ID" => "catalog",
      "OFFERS_CART_PROPERTIES" => array("COLOR_REF", "SIZES_SHOES", "SIZES_CLOTHES"),
      "PRICE_CODE" => array("BASE", "FULL", "RETAIL"),
      "PRICE_VAT_INCLUDE" => "Y",
      "TEMPLATE_THEME" => "blue" // параметр из дефолтного шаблона, означает цветовую тему
   )
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх