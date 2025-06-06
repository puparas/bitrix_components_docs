# Карта сайта

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

[Wiki](/user_help/components/content/wiki/index.php)

[Валюты](/user_help/components/content/currency/index.php)

[Добавление элементов](/user_help/components/content/adding/index.php)

[Инфоблоки](/user_help/components/content/infoblocks/index.php)

[Календарь событий](/user_help/components/content/calendar/index.php)

[Карта сайта](/user_help/components/content/sitemap/index.php)

[Карта сайта](/user_help/components/content/sitemap/main_map.php)

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

Карта сайта

# Карта сайта

С помощью данного компонента осуществляется показ карты сайта.

### Описание **main.map**

Компонент стандартный и входит в дистрибутив модуля. Карта строится на основе [настроек Главного модуля](/user_help/settings/settings/settings.php), секция Карта сайта.

В визуальном редакторе компонент расположен по пути: *Контент > Карта сайта > Карта сайта*.

Компонент относится к [Главному модулю](/user_help/settings/settings/index.php).

**Примечание**: Если в настройках сайта (*Настройки > Настройки продукта > Сайты > Список сайтов > [\_ имя сайта \_](/user_help/settings/settings/sites/site_edit.php)*) не совсем верно указана папка сайта (например, нет закрывающего слеша), то компонент не сможет создать карту сайта.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка будет установлено **Карта сайта**. |
| **Настройки компонента** | | |
| Максимальный уровень вложенности (0 - без вложенности) | **LEVEL** | Параметр определяет максимальный уровень вложенности разделов при показе в карте сайта (0 - без вложенности). Если число в этом поле более чем 4, то рекомендуется еще раз продумать структуру сайта. |
| Количество колонок | **COL\_NUM** | Указывается количество колонок карты сайта. Это число во многом зависит от дизайна сайта, используемого уровня вложенности, структуры сайта. Перенос пунктов карты по колонкам происходит на базе пунктов меню первого уровня. То есть, если один из пунктов меню имеет структуру намного более глубокую, чем другие пункты, то при выборе глубокого уровня вложенности на карте сайта вы можете получить длинную колонку этого пунтка и короткие колонки с другими пунктами. |
| Показывать описания | **SHOW\_DESCRIPTION** | [Y|N] При отмеченной опции будут выведены описания разделов, если они заданы. Описания разделов информационных блоков не отображаются. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.map","",Array(
		"LEVEL" => "3", 
		"COL_NUM" => "1", 
		"SHOW_DESCRIPTION" => "Y", 
		"SET_TITLE" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх