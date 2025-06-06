# Форма добавления идеи

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

[Идеи](/user_help/components/services/ideas_manager/bitrix_idea.php)
[Форма добавления идеи](/user_help/components/services/ideas_manager/bitrix_idea_popup.php)

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

[Менеджер идей](/user_help/components/services/ideas_manager/index.php)

Форма добавления идеи

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Форма добавления идеи

### Описание **idea.popup**

Компонент позволяет добавить в публичную часть сайта кнопку, которая открывает форму добавления идеи во всплывающем окне.

В визуальном редакторе компонент расположен по пути: *Общение > Менеджер идей > Форма добавлении идеи (popup)*.

Компонент относится к модулю [Менеджер идей](/user_help/service/idea/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Блог | **BLOG\_URL** | Выбирается блог для сервиса идея. |
| Инфоблок, в котором хранится структура категорий | **IBLOCK\_CATEGORIES** | Выбирается инфоблок, в котором хранится структура категорий идей. |
| Путь к списку идей | **PATH\_IDEA\_INDEX** | Указывается путь к списку идей. |
| Путь к детальному описанию идеи | **PATH\_IDEA\_POST** | Указывается путь к детальному описанию идеи. |
| Путь к детальному описанию идеи | **PATH\_IDEA\_POST** | Указывается путь к детальному описанию идеи. |
| Цвет фона кнопки | **BUTTON\_COLOR** | Задается цвет фона кнопки отзывов в публичной части сайта. |
| Статус по умолчанию для новой идеи | **POST\_BIND\_STATUS\_DEFAULT** | Указывается статус, который будет автоматически присвоен новым идеям. |
| Шаблон формы авторизации | **AUTH\_TEMPLATE** | Задается название шаблона для формы авторизации. |
| Страница забытого пароля | **FORGOT\_PASSWORD\_URL** | Указывается адрес страницы восстановления пароля. |
| Страница регистрации | **REGISTER\_URL** | Указывается адрес страницы для регистрации нового пользователя. |
| **Внешний вид** | | |
| Количество категорий | **CATEGORIES\_CNT** | Указывается количество идей, отображаемых в форме. |
| Количество идей в категории | **MESSAGE** | Указывается количество идей, отображаемых в категории. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Указывается тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Дополнительные настройки** | | |
| Использовать рейтинги | **SHOW\_RATING** | [Y|N] При отмеченной опции будут использоваться рейтинги для оценки идей и комментариев к ним, станет доступно дополнительное поле.     |  |  |  | | --- | --- | --- | | Шаблон рейтингов | **RATING\_TEMPLATE** | Выбирается шаблон визуального отображения рейтингов. | |
| Отключить уведомления в живую ленту | **DISABLE\_SONET\_LOG** | [Y|N] Опция позволяет отключить вывод идей в живую ленту.   Опция доступна только в **Битрикс24 в коробке**. |
| Отключить почтовые уведомления | **DISABLE\_EMAIL** | [Y|N] Опция позволяет отключить почтовые уведомления о новых комментариях. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent(
	"bitrix:idea.popup",
	"",
	Array(
		"BLOG_URL" => "idea_s1",
		"IBLOCK_CATEGORIES" => "23",
		"PATH_IDEA_INDEX" => "/services/idea/",
		"PATH_IDEA_POST" => "/services/idea/#post_id#/",
		"BUTTON_COLOR" => "#3EA822",
		"POST_BIND_STATUS_DEFAULT" => "1",
		"CATEGORIES_CNT" => "4",
		"LIST_MESSAGE_COUNT" => "8",
		"AUTH_TEMPLATE" => "",
		"FORGOT_PASSWORD_URL" => "",
		"REGISTER_URL" => "",
		"CACHE_TYPE" => "A",
		"CACHE_TIME" => "3600",
		"SHOW_RATING" => "Y",
		"RATING_TEMPLATE" => "standart",
		"DISABLE_SONET_LOG" => "N",
		"DISABLE_EMAIL" => "N"
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх