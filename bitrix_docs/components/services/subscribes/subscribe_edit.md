# Страница редактирования подписки

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

Страница редактирования подписки

**Недоступно в редакциях:**Старт

# Страница редактирования подписки

Компонент служит для создания страницы с формами для добавления или редактирования адреса подписки.

### Описание **subscribe.edit**

Если пользователь не авторизован на сайте, то в зависимости от настроек он сможет подписаться на рассылку, указав свой **e-mail** или перейти к редактированию параметров рассылки после ввода **e-mail** и кода подтверждения (пароля) подписки, который высылается на адрес электронной почты после оформления подписки. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент расположен по пути *Сервисы > Рассылки > Страница редактирования подписки*.

Компонент относится к модулю [Рассылки](/user_help/service/subscribe/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Источник данных** | | |
| Показать скрытые рубрики подписки | **SHOW\_HIDDEN** | [Y|N] При отмеченной опции в списке рассылок будут выведены все активные рассылки вне зависимости от опции **Выводить в списке публичных рассылок** в настройках рассылки. |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера **Назад** и **Вперед**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Дополнительные настройки** | | |
| Разрешить анонимную подписку | **ALLOW\_ANONYMOUS** | [Y|N] При отмеченной опции анонимные пользователи смогут подписываться на рассылку, лишь указав свой адрес электронной почты без необходимости регистрации на сайте. В случае неустановленной опции подписаться на рассылку анонимный пользователь не сможет. Только уже подписавшийся пользователь сможет редактировать параметры рассылки после ввода **e-mail** и кода подтверждения (пароль) подписки. |
| Показывать ссылки на авторизацию при анонимной подписке | **SHOW\_AUTH\_LINKS** | [Y|N] При отмеченной опции для анонимного пользователя при подписке на рассылку будут выведены формы для авторизации (если он зарегистрирован, то сможет авторизоваться) и форма для регистрации (пользователь сможет зарегистрироваться, если не имеет учетной записи на сайте). |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции заголовком страницы будет установлен:  * **Редактирование параметров подписки** при редактировании подписки; * **Добавление адреса подписки** при создании подписки. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:subscribe.edit","",Array(
		"AJAX_MODE" => "N", 
		"SHOW_HIDDEN" => "Y", 
		"ALLOW_ANONYMOUS" => "Y", 
		"SHOW_AUTH_LINKS" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600", 
		"SET_TITLE" => "Y", 
		"AJAX_OPTION_JUMP" => "N", 
		"AJAX_OPTION_STYLE" => "Y", 
		"AJAX_OPTION_HISTORY" => "N" 
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх