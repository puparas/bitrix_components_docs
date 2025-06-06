# Баннер

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

[Сервисы](/user_help/components/services/index.php)

[Видеоконференции (КП)](/user_help/components/services/video/index.php)

[Интранет (КП)](/user_help/components/services/intranet/index.php)

[Экстранет (КП)](/user_help/components/services/extranet/index.php)

[Контроллер](/user_help/components/services/controller/index.php)

[Частые вопросы](/user_help/components/services/faq/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

[Баннер](/user_help/components/services/advertising/advertising_banner.php)

[Техподдержка](/user_help/components/services/support/index.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

Баннер

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Баннер

Компонент выводит баннер заданного типа. Содержит 6 шаблонов: **bootstrap**, **.default**, **jssor**, **bootstrap\_v4**, **parallax** и **nivo**.
Компонент является стандартным и входит в дистрибутив модуля.

### Описание **advertising.banner**

В визуальном редакторе компонент расположен по пути *Сервисы > Реклама > Баннер*.

Компонент относится к модулю [Реклама](/user_help/marketing/advertising/index.php).

**Внимание!** Компонент не учитывает таргетинг по ключевым словам, для этого необходимо использовать функцию **`$APPLICATION->ShowBanner()`** (более подробную информацию по функции можно посмотреть на [странице документации для разработчиков](https://dev.1c-bitrix.ru/api_help/main/reference/cmain/showbanner.php)).

### Параметры

| Поле | Параметр | Описание | Примечание |
| --- | --- | --- | --- |
| **Основные параметры** | | | |
| Тип баннера | **TYPE** | Указывается один из типов баннера, созданных в системе. |  |
| Добавлять в ссылки noindex/nofollow | **NOINDEX** | [Y|N] При отмеченной опции ссылка перехода по баннеру данного типа заключаются в тэг **noindex**, а самой ссылке присваивается атрибут **nofollow**. HTML-тэг **noindex** используются для исключения из ранжирования в Яндексе и Рамблере заключенного в него текста. Атрибут **rel="nofollow"** используется для исключения индексации ссылки. Например:  ```  <noindex><a href="/ссылка_перехода_по_баннеру"  rel="nofollow"><img src="/upload/banners/10d/banner_100x100.gif" /></a></noindex>  ``` |  |
| Количество баннеров для показа | **QUANTITY** | Указывается максимальное количество баннеров, которое может показать шаблон компонента. |  |
| Шаблон слайдов по умолчанию | **DEFAULT\_TEMPLATE** | Выбирается шаблон для показа слайдов. Указанный шаблон будет использоваться только для баннеров типа **Изображение**. | Параметр недоступен в шаблоне **.default**. |
| Эффект переключения слайдов | **BS\_EFFECT** | Выбирается эффект переключения слайдов. | Параметр недоступен в шаблонах **.default** и **parallax**. |
| Длительность анимации (мсек.) | **ANIMATION\_DURATION** | Задается время анимации слайда баннера. | Параметр доступен только в шаблонах **jssor** и **nivo**. |
| Автоматически подключать библиотеку jQuery | **JQUERY** | [Y|N] При отмеченной опции для слайдера требуется подключение javascipt библиотеки jQuery. | Параметр доступен только в шаблоне **nivo**. |
| Автоматическая смена слайда | **BS\_CYCLING** | [Y|N] При отмеченной опции смена слайда будет выполняться автоматически. | Параметр недоступен в шаблонах **.default** и **parallax**. |
| Скорость смены слайдов (мсек.): | **BS\_INTERVAL** | Указывается время, через которое будет выполняться смена слайда. | Параметры доступны, если отмечена опция **Автоматическая смена слайда**. |
| Останавливать при наведении | **BS\_PAUSE** | [Y|N] При отмеченной опции смена слайдов выполняться не будет, если на баннер будет наведен курсор мыши. |
| Прокручивать в начало | **BS\_WRAP** | [Y|N] При отмеченной опции будет выполняться прокрутка к началу показа слайдов. | Параметр недоступен в шаблонах **.default** и **parallax**. |
| Навигация с помощью клавиатуры | **BS\_KEYBOARD** | [Y|N] При отмеченной опции возможно управление показом слайдов с помощью кнопок клавиатуры *вперед* и *назад*. | Параметр недоступен в шаблонах **.default**, **parallax** и **nivo**. |
| Показывать элементы навигации на слайде | **BS\_ARROW\_NAV** | [Y|N] При отмеченной опции элементы навигации будут показаны на слайде. | Параметр недоступен в шаблонах **.default** и **parallax**. |
| Показывать элемент постраничной навигации | **BS\_BULLET\_NAV** | [Y|N] При отмеченной опции будет отображаться элемент постраничной навигации. | Параметр недоступен в шаблонах **.default** и **parallax**. |
| Скрывать область с баннером на планшетах | **BS\_HIDE\_FOR\_TABLETS** | [Y|N] При отмеченной опции область с баннером не будет показываться при просмотре сайта на планшетах. | Параметр доступен только в шаблонах **bootstrap** и **bootstrap\_v4**. |
| Скрывать область с баннером на мобильном телефоне | **BS\_HIDE\_FOR\_PHONES** | [Y|N] При отмеченной опции область с баннером не будет показываться при просмотре сайта на мобильном телефоне. | Параметр доступен только в шаблонах **bootstrap** и **bootstrap\_v4**. |
| Масштабировать относительно ширины родителя | **SCALE** | [Y|N] При отмеченной опции будет выполняться масштабирование слайдов. | Параметр доступен только в шаблоне **jssor**. |
| Высота баннера, px | **HEIGHT** | Задается высота баннера (в пикселах). | Параметр доступен только в шаблоне **parallax**. |
| **Настройки кеширования** | | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |  |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |  |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:advertising.banner","",Array(  

	"TYPE" => "BOTTOM",   

	"NOINDEX" => "Y",   

	"QUANTITY" => "1",  

	"CACHE_TYPE" => "A",  

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Игорь Барковский** 24.03.2011 20:12:19 |
| --- |
| В последних версиях компонент уже учитывает таргетинг по желательным и обязательным ключевым словам. Если же вы хотите, чтобы таргетинг по ключевым словам работал для баннеров, размещаемых в хедере шаблона, то можно использовать отложенные функции, вида  php:  | Код | | --- | | ``` function ShowBanner ($arParams) {    if (CModule::IncludeModule('advertising'))    {       $bNoInd = $arParams["NOINDEX"] == "Y";       return $strBanner = CAdvBanner::Show($arParams["TYPE"], $bNoInd ? '<noindex>':'', $bNoInd ? '</noindex>':'');    } } ``` |   и размещать баннеры с помощью метода php:  | Код | | --- | | ``` $APPLICATION->AddBufferContent('ShowBanner', array("TYPE"=>"TOP_BANNER","NOINDEX"=>"Y")); ``` | |
|  |

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх