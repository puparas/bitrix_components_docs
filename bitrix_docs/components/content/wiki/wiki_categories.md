# Категории

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

[Комплексный Wiki компонент](/user_help/components/content/wiki/wiki.php)
[Меню](/user_help/components/content/wiki/wiki_menu.php)
[Страница](/user_help/components/content/wiki/wiki_show.php)
[Редактирование](/user_help/components/content/wiki/wiki_edit.php)
[Категории](/user_help/components/content/wiki/wiki_categories.php)
[История](/user_help/components/content/wiki/wiki_history.php)
[Обсуждение](/user_help/components/content/wiki/wiki_discussion.php)
[Сравнение версий](/user_help/components/content/wiki/wiki_history_diff.php)

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

[Wiki](/user_help/components/content/wiki/index.php)

Категории

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Категории

### Описание **wiki.categories**

Компонент выводит список категорий. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути: *Контент > Wiki > Категории*.

Компонент относится к модулю [Wiki](/user_help/content/wiki/index.php).

### Параметры

| **Основные параметры** | | |
| --- | --- | --- |
| Тип информационного блока (используется только для проверки) | **IBLOCK\_TYPE** | Указывается тип информационных блоков, в котором будут храниться данные Wiki. Тип инфоблока создается при инсталляции дистрибутива или установке модуля. Если не создан, то требуется создание вручную. |
| Код информационного блока | **IBLOCK\_ID** | Указывается информационный блок, в котором будут храниться данные Wiki. Инфоблок создается при инсталляции дистрибутива или установке модуля. Если не создан, то требуется создание вручную. |
| Количество категорий на странице | **CATEGORY\_COUNT** | Задается число категорий, которое будет выводится на странице. Если число категорий превысит указанное число, начнется постраничная навигация. |
| **Шаблоны ссылок** | | |
| Шаблон пути к Wiki-странице | **PATH\_TO\_POST** | Указывается путь к главной странице Wiki. |
| **Дополнительные настройки** | | |
| Имя переменной для страницы | **VARIABLE\_ALIASES** | Указывается имя переменной в которой передается имя страницы |
| Имя переменной для операции | **VARIABLE\_ALIASES** | Указывается имя переменной, по которой определяется текущая операция на странице. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:wiki.categories",
	"",
	Array(
		"PATH_TO_POST" => "",
		"PAGE_VAR" => "title",
		"OPER_VAR" => "oper",
		"IBLOCK_TYPE" => "wiki",
		"IBLOCK_ID" => "",
		"CATEGORY_COUNT" => "20"
	)
);?>
```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх