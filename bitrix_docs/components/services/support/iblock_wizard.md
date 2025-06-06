# Мастер создания обращения

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

[Техподдержка](/user_help/components/services/support/index.php)

[Техподдержка (комплексный компонент)](/user_help/components/services/support/support_ticket.php)
[Техподдержка с мастером (комплексный компонент)](/user_help/components/services/support/support_wizard.php)
[Создание нового, либо редактирование существующего обращения](/user_help/components/services/support/support_ticket_edit.php)
[Список обращений](/user_help/components/services/support/support_ticket_list.php)
[Мастер создания обращения](/user_help/components/services/support/iblock_wizard.php)

[Рабочий стол](/user_help/components/services/desktop.php)

[Общение](/user_help/components/obschenie/index.php)

[Магазин](/user_help/components/magazin/index.php)

[Служебные](/user_help/components/sluzhebnie/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Компоненты](/user_help/components/index.php)

[Сервисы](/user_help/components/services/index.php)

[Техподдержка](/user_help/components/services/support/index.php)

Мастер создания обращения

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Мастер создания обращения

### Описание **iblock.wizard**

Компонент формирует разделы мастера на основе секций [инфоблока](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2686 "Создание мастера в учебном курсе") и вопросы на основе элементов инфоблока. Компонент стандартный и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Техподдержка > Мастер создания обращения*.

Компонент относится к модулю [Техподдержка](/user_help/service/support/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается тип информационного блока. |
| Информационный блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор инфоблока, в котором хранится мастер техподдержки. |
| Свойство, в котором хранится тип вопроса | **PROPERTY\_FIELD\_TYPE** | Указывается свойство, в котором хранится тип вопроса. |
| Множественное свойство, в котором хранятся значения выпадающего списка | **PROPERTY\_FIELD\_VALUES** | Указывается множественное свойство, в котором хранятся значения выпадающего списка. |
| Страница, с которой пришли на мастер (для кнопки "Назад", может быть пустое) | **BACK\_URL** | Указывается адрес страницы, с которой пришли на мастер (для кнопки "Назад", поле может быть пустое). |
| Страница с формой редактирования сообщения | **NEXT\_URL** | Указывается адрес страницы с формой редактирования сообщения. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Дополнительные настройки** | | |
| Добавлять разделы мастера в навигационную цепочку | **INCLUDE\_IBLOCK\_INTO\_CHAIN** | [Y|N] При отмеченной опции разделы мастера техподдержки будут добавлены в навигационнную цепочку. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:iblock.wizard","",Array(
		"AJAX_MODE" => "N", 
		"IBLOCK_TYPE" => "services", 
		"IBLOCK_ID" => "11", 
		"PROPERTY_FIELD_TYPE" => "", 
		"PROPERTY_FIELD_VALUES" => "", 
		"BACK_URL" => "ticket_list.php", 
		"NEXT_URL" => "ticket_edit.php", 
		"INCLUDE_IBLOCK_INTO_CHAIN" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600", 
		"AJAX_OPTION_JUMP" => "N", 
		"AJAX_OPTION_STYLE" => "Y", 
		"AJAX_OPTION_HISTORY" => "N" 
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх