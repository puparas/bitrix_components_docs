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

[Веб-Сервис](/user_help/components/services/web_service/index.php)

[Веб-формы](/user_help/components/services/web_forms/index.php)

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

[Обучение](/user_help/components/services/learning/index.php)

[Опросы, голосования](/user_help/components/services/votes/index.php)

[Рассылки](/user_help/components/services/subscribes/index.php)

[Список новостей](/user_help/components/services/subscribes/subscribe_news.php)
[Страница рассылок](/user_help/components/services/subscribes/subscribe_index.php)
[Страница редактирования подписки](/user_help/components/services/subscribes/subscribe_edit.php)
[Упрощенное редактирование подписки](/user_help/components/services/subscribes/subscribe_simple.php)
[Форма подписки](/user_help/components/services/subscribes/subscribe_form.php)

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

[Рассылки](/user_help/components/services/subscribes/index.php)

Форма подписки

**Недоступно в редакциях:**Старт

# Форма подписки

Компонент служит для построения включаемой в дизайн сайта формы для подписки на рассылки.

### Описание **subscribe.form**

Право на подписку имеют как зарегистрированные, так и анонимные пользователи (в случае наличия установленной опции в настройках модуля Подписка, рассылка). Компонент стандартный и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Сервисы > Рассылки > Форма подписки*.

Компонент относится к модулю [Рассылки](/user_help/service/subscribe/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Определять подписку текущего пользователя | **USE\_PERSONALIZATION** | [Y|N] При отмеченной опции будут определяться имеющиеся подписки текущего пользователя. |
| **Источник данных** | | |
| Показать скрытые рубрики подписки | **SHOW\_HIDDEN** | [Y|N] При отмеченной опции в списке рассылок будут выведены все активные рассылки вне зависимости от опции **Выводить в списке публичных рассылок** в настройках рассылки. |
| **Шаблоны ссылок** | | |
| Страница редактирования подписки (доступен макрос #SITE\_DIR#) | **PAGE** | Указывается путь от корня сайта (**#SITE\_DIR#**) к странице редактирования подписки. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:subscribe.form","",Array(
		"USE_PERSONALIZATION" => "Y", 
		"PAGE" => "#SITE_DIR#personal/subscribe/subscr_edit.php", 
		"SHOW_HIDDEN" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх