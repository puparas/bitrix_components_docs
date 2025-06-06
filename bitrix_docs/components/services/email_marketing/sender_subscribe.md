# Форма подписки

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

[Форма подписки](/user_help/components/services/email_marketing/sender_subscribe.php)

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Реклама](/user_help/components/services/advertising/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

Форма подписки

**Недоступно в редакциях:**Стандарт, Старт

# Форма подписки

Компонент включается в дизайн сайта и служит формой для подписки на рассылки. Компонент стандартный и входит в дистрибутив модуля.

### Описание **sender.subscribe**

В визуальном редакторе компонент расположен по пути *Сервисы > Email-маркетинг > Форма подписки*.

Компонент относится к модулю [Email-маркетинг](/user_help/marketing/sender/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Определять подписку текущего пользователя | **USE\_PERSONALIZATION** | [Y|N] При включенной опции будут выделены только те рассылки, на которые подписан текущий пользователь. Иначе выбраны все рассылки. |
| Запрашивать подтверждение подписки по email | **CONFIRMATION** | [Y|N] При включенной опции подписчику отправляется письмо с ссылкой для подтверждения без авторизации. После перехода по ссылке подписчик будет подписан на выбранные подписки. |
| Скрыть список рассылок, и подписывать на все | **HIDE\_MAILINGS** | [Y|N] При включенной опции будут выбраны все рассылки. |
| **Источник данных** | | |
| Показать скрытые рассылки для подписки | **SHOW\_HIDDEN** | [Y|N] При включенной опции будут показываться подписки из **скрытых рубрик**, в настройках которых снята опция **Вывод в публичной части для подписки**. |
| **Согласие пользователя** | | |
| Запрашивать согласие | **USER\_CONSENT** | [Y|N] Установленный флажок включает механизм согласия пользователя. |
| Соглашение | **USER\_CONSENT\_ID** | Задается текст соглашения, которое отображается пользователю при заказе. |
| Галка по умолчанию проставлена | **USER\_CONSENT\_IS\_CHECKED** | Установка галочки автомаитчески устанавливает галочку в чекбоксе согласия пользователя. То есть согласие применяется одновременно с нажатием кнопки Оформить заказ. |
| Загружать текст сразу | **USER\_CONSENT\_IS\_LOADED** | Текст соглашения будет выводиться сразу. Если флажок не установлен, для просмотра текст нужно будет кликнуть по кнопке согласия. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленной опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера "Назад" и "Вперед". |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
|| **Дополнительные настройки** | | |
| --- | --- | --- |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено имя текущего раздела. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:sender.subscribe","",Array(
		"COMPONENT_TEMPLATE" => ".default",
		"USE_PERSONALIZATION" => "Y",
		"CONFIRMATION" => "Y",
		"SHOW_HIDDEN" => "Y",
		"AJAX_MODE" => "Y",
		"AJAX_OPTION_JUMP" => "Y",
		"AJAX_OPTION_STYLE" => "Y",
		"AJAX_OPTION_HISTORY" => "Y",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"SET_TITLE" => "Y"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх