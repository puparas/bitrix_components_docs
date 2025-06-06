# Список сравниваемых элементов каталога

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

Список сравниваемых элементов каталога

# Список сравниваемых элементов каталога

### Описание **catalog.compare.list**

Компонент выводит список сравниваемых элементов каталога в виде небольшой таблицы.
Он предоставляет возможность удаления элемента из списка и возможность сравнения элементов.
Компонент стандартный, входит в дистрибутив модуля и содержит два шаблона: **.default** и **bootstrap\_v4**.

В визуальном редакторе компонент расположен по пути *Контент > Каталог > Список сравниваемых элементов каталога*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационных блоков. |
| Инфоблок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор информационного блока, элементы которого будут отфильтрованы. |
| **Внешний вид** | | |
| Отображать список сравнения поверх страницы | **POSITION\_FIXED** | [Y|N] При отмеченной опции список сравнения будет отображен поверх страницы. |
| Положение на странице | **POSITION** | Выберите положение списка сравнения на странице: вверху слева, вверху справа, внизу слева или внизу справа. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Дополнительные настройки** | | |
| URL, ведущий на страницу с содержимым элемента раздела | **DETAIL\_URL** | Указывается путь к странице с детальным описанием элемента раздела. |
| URL страницы с таблицей сравнения | **COMPARE\_URL** | Указывается путь к странице с таблицей сравнения элементов текущего инфоблока. |
| Уникальное имя для списка сравнения | **NAME** | Задается имя переменной, в которой передается список сравниваемых элементов. По умолчанию **CATALOG\_COMPARE\_LIST**. |
| **Настройки действий** | | |
| Название переменной, в которой передается действие | **ACTION\_VARIABLE** | Задается имя переменной, в которой передается действие. Значение поля по умолчанию **action**. Значение параметра должно быть уникальным среди всех используемых компонентов на одной странице. |
| Название переменной, в которой передается код товара для покупки | **PRODUCT\_ID\_VARIABLE** | Задается имя переменной, в которой будет передаваться идентификатор товара. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:catalog.compare.list","",
Array(
		"AJAX_MODE" => "Y",
		"IBLOCK_TYPE" => "books",
		"IBLOCK_ID" => "6",
		"POSITION_FIXED" => "Y",
		"POSITION" => "top left",
		"DETAIL_URL" => "",
		"COMPARE_URL" => "compare.php",
		"NAME" => "CATALOG_COMPARE_LIST",
		"AJAX_OPTION_JUMP" => "N",
		"AJAX_OPTION_STYLE" => "Y",
		"AJAX_OPTION_HISTORY" => "N",
		"ACTION_VARIABLE" => "action",
		"PRODUCT_ID_VARIABLE" => "id"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх