# Календарь

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

Календарь

# Календарь

### Описание **news.calendar**

Одностраничный компонент, который служит для формирования и вывода календаря новостей или событий. Настройки позволяют настраивать внешний вид календаря, указывать его тип, управлять шаблоном, кешированием и т.д. Компонент содержит два шаблона: **.default** и **compact**. Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Статьи и новости > Календарь*.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип информационного блока (используется только для проверки) | **IBLOCK\_TYPE** | Указывается один из созданных в системе типов информационного блока. |
| Код информационного блока | **IBLOCK\_ID** | Для выбранного типа инфоблока указывается идентификатор информационного блока, новости из которого будут выводиться. |
| Имя переменной для месяца | **MONTH\_VAR\_NAME** | Задается имя переменной, в которой передается номер месяца. |
| Имя переменной для года | **YEAR\_VAR\_NAME** | Задается имя переменной, в которой передается номер года. |
| Начало недели | **WEEK\_START** | Указывается день начала отсчета недели. |
| **Внешний вид** | | |
| Показывать переход по годам | **SHOW\_YEAR** | [Y|N] При отмеченной опции будет выведена ссылка на предыдущий год. |
| Показывать время новостей | **SHOW\_TIME** | [Y|N] При отмеченной опции рядом с названием элемента будет выведено время начала активности, если оно определено для элемента. |
| Длина заголовка (0 - не ограничивать) | **TITLE\_LEN** | Указывается длина заголовка новостей, выводимых в календаре (0 - не ограничивать). |
| Показывать текущий месяц и год | **SHOW\_CURRENT\_DATE** | [Y|N] При отмеченной опции будут выведены текущий месяц и год над календарем в правом углу. |
| Показывать выпадающий список месяцев | **SHOW\_MONTH\_LIST** | [Y|N] При отмеченной опции будет показан выпадающий список месяцев. В противном случае только ссылки на предыдущий и следующий месяцы. |
| Количество новостей в день (0 - не ограничивать) | **NEWS\_COUNT** | Указывается количество новостей, отображаемых в одной ячейки календаря за один день (0 - не ограничивать). Если число отлично от нуля, то будут выбраны элементы с меньшим временем начала активности. Если время не определено, то элементы будут выбраны по индексу сортировки. |
| **Шаблоны ссылок** | | |
| URL, ведущий на страницу с содержимым элемента раздела | **DETAIL\_URL** | Задается адрес, ведущий на страницу с содержимым элемента инфоблока в календаре. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера "Назад" и "Вперед". |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Поле даты | **DATE\_FIELD** | Указывается поле, по которому будет происходить сортировка новостей (событий) по датам:  * **DATE\_ACTIVE\_FROM** - **Дата активности с**; * **DATE\_ACTIVE\_TO** - **Дата активности по**; * **TIMESTAMP\_X** - **Время последнего изменения**; * **DATE\_CREATE** - **Дата создания**. |
| Тип календаря | **TYPE** | Указывается тип календаря:  * **Новостной** (**NEWS**) - освещает наступившие новости (события) (события текущего месяца будут выведены, даже если дата события еще не наступила); * **Событийный** (**EVENTS**) - освещает новости (события) ненаступившей даты. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет выведен текущий месяц и год. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:news.calendar","",Array(
		"AJAX_MODE" => "N", 
		"IBLOCK_TYPE" => "news", 
		"IBLOCK_ID" => "3", 
		"MONTH_VAR_NAME" => "month", 
		"YEAR_VAR_NAME" => "year", 
		"WEEK_START" => "1", 
		"DATE_FIELD" => "DATE_ACTIVE_FROM", 
		"TYPE" => "EVENTS", 
		"SHOW_YEAR" => "Y", 
		"SHOW_TIME" => "Y", 
		"TITLE_LEN" => "0", 
		"SET_TITLE" => "Y", 
		"SHOW_CURRENT_DATE" => "Y", 
		"SHOW_MONTH_LIST" => "Y", 
		"NEWS_COUNT" => "0", 
		"DETAIL_URL" => "", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600", 
		"AJAX_OPTION_JUMP" => "N", 
		"AJAX_OPTION_STYLE" => "Y", 
		"AJAX_OPTION_HISTORY" => "N", 
		"AJAX_OPTION_ADDITIONAL" => "" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх