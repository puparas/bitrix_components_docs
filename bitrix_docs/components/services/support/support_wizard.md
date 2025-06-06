# Техподдержка с мастером (комплексный компонент)

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

Техподдержка с мастером (комплексный компонент)

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Техподдержка с мастером (комплексный компонент)

### Описание **support.wizard**

Компонент служит для организации полноценного публичного интерфейса технической поддержки, создание обращения в котором выполняется с помощью специального мастера. Компонент является стандартным и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Техподдержка > Техподдержка с мастером*.

Компонент относится к модулю [Техподдержка](/user_help/service/support/index.php).

**Примечание**: мастер представляет собой информационный блок, а вопросы мастера являются разделами и элементами этого инфоблока.

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Тип инфоблока | **IBLOCK\_TYPE** | Указывается тип информационного блока. |
| Информационный блок | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор инфоблока, в котором хранится мастер техподдержки. |
| Свойство, в котором хранится тип вопроса | **PROPERTY\_FIELD\_TYPE** | Указывается свойство, в котором хранится тип вопроса. |
| Множественное свойство, в котором хранятся значения выпадающего списка | **PROPERTY\_FIELD\_VALUES** | Указывается множественное свойство, в котором хранятся значения выпадающего списка. |
| **Управление адресами страниц** | | |
| Идентификатор обращения | **VARIABLE\_ALIASES\_ID** | Указывается идентификатор обращения. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Дополнительные настройки** | | |
| Добавлять разделы мастера в навигационную цепочку | **INCLUDE\_IBLOCK\_INTO\_CHAIN** | [Y|N] При отмеченной опции разделы мастера техподдержки будут добавлены в навигационнную цепочку. |
| Количество обращений на одной странице | **TICKETS\_PER\_PAGE** | Указывается количество обращений, отображаемых на одной странице. |
| Количество сообщений на одной странице | **MESSAGES\_PER\_PAGE** | Указывается количество сообщений, отображаемых на одной странице. |
| Максимальная длина неразрывной строки | **MESSAGE\_MAX\_LENGTH** | Задается максимальная длина фразы без пробелов или символов перевода строки. |
| Направление для сортировки сообщений в обращении | **MESSAGE\_SORT\_ORDER** | Указывается направление сортировки сообщений в обращении. Сообщения сортируются по времени добавления:  * *asc* - по возрастанию; * *desc* - по убыванию. |
| Устанавливать заголовок страницы | **SET\_PAGE\_TITLE** | При выборе значения **Да** в качестве заголовка будет установлено **Список обращений**. В противном случае (значение **Нет**) заголовок установлен не будет. |
| Шаблон мастера | **TEMPLATE\_TYPE** | Укажите тему внешнего вида мастера: **Строгий** (**standard**) или **Изящный** (**.default**). |
| Показать результат работы мастера | **SHOW\_RESULT** | [Y|N] При отмеченной опции будет показан результат работы мастера. |
| Показывать поле ввода купона | **SHOW\_COUPON\_FIELD** | [Y|N] При отмеченной опции будет показано поле ввода купона. |
| Показывать пользовательские поля | **SET\_SHOW\_USER\_FIELD** | Выбираются пользовательские поля, которые должны быть показаны в форме создания/редактирования обращения. |
| **Привязка разделов мастера к категориям техподдержки** | | |
| Включить привязки | **SECTIONS\_TO\_CATEGORIES** | [Y|N] При отмеченной опции будет включена привязка разделов мастера к категориям техподдержки, станет активным дополнительное поле.     |  |  |  | | --- | --- | --- | | Список разделов для привязки | **SELECTED\_SECTIONS** | Указывается список разделов мастера техподдержки для привязки. | |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:support.wizard","",Array(  
		"IBLOCK_TYPE" => "services",   
		"IBLOCK_ID" => "11",   
		"PROPERTY_FIELD_TYPE" => "type",   
		"PROPERTY_FIELD_VALUES" => "values",   
		"AJAX_MODE" => "N",   

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх