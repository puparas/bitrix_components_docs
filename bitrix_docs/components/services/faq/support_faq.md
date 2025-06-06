# FAQ (комплексный компонент)

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

[FAQ (комплексный компонент)](/user_help/components/services/faq/support_faq.php)
[Вопрос FAQ](/user_help/components/services/faq/support_faq_element_detail.php)
[Список вопросов FAQ](/user_help/components/services/faq/support_faq_element_list.php)
[Список категорий FAQ](/user_help/components/services/faq/support_faq_section_list.php)

[E-mail маркетинг](/user_help/components/services/email_marketing/index.php)

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

[Частые вопросы](/user_help/components/services/faq/index.php)

FAQ (комплексный компонент)

# FAQ (комплексный компонент)

### Описание **support.faq**

Комплексный компонент выводит FAQ категории и вопросы из инфоблока. Компонент является стандартным и входит в дистрибутив модуля.

Компонент относится к модулю [Информационные блоки](/user_help/content/iblock/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Настройки компонента** | | |
| Тип инфоблоков | **IBLOCK\_TYPE** | Тип информационного блока FAQ. |
| Список инфоблоков | **IBLOCK\_ID** | Для выбранного типа инфоблоков указывается идентификатор инфоблока, в котором будет храниться FAQ. |
| Список секций | **SECTION** | Указывается секция (категория FAQ), которая будет отображена на странице. Если ничего не указывать, то будет выведен весь список секций. |
| Показывать вложенные секции | **EXPAND\_LIST** | [Y|N] При отмеченной секции будут показаны вложенные секции. |
| **Настройки рейтингов** | | |
| Включить рейтинг | **SHOW\_RATING** | Указывается, будут ли использоваться рейтинги для оценки загруженных файлов.  * по умолчанию; * да; * нет.   Значение **по умолчанию** берется из настроек рейтингов. |
| Вид кнопок рейтинга | **RATING\_TYPE** | Указывается тип кнопок рейтинга:  * по умолчанию; * Мне нравится (текстовый); * Мне нравится (графический); * Нравится / Не нравится (текстовый); * Нравится / Не нравится (графический).   Значение **по умолчанию** берется из настроек рейтингов. |
| Шаблон пути к странице пользователя | **PATH\_TO\_USER** | Указывается шаблон пути к странице пользователя. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При установленном флаге включается поддержка ЧПУ и становятся доступными поля настройки адресов ЧПУ.     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **faq** - страница общего списка; * **section** - страница раздела; * **detail** - страница детального просмотра. | |
| **Управление режимом AJAX** | | |
| Включить режим AJAX | **AJAX\_MODE** | [Y|N] При установленной опции для компонента будет включен режим AJAX. |
| Включить прокрутку к началу компонента | **AJAX\_OPTION\_JUMP** | [Y|N] Если пользователь совершит AJAX-переход, то при установленой опции по окончании загрузки произойдет прокрутка к началу компонента. |
| Включить подгрузку стилей | **AJAX\_OPTION\_STYLE** | [Y|N] Если параметр принимает значение "Y", то при совершении AJAX-переходов будет происходить подгрузка и обработка списка стилей, вызванных компонентом. |
| Включить эмуляцию навигации браузера | **AJAX\_OPTION\_HISTORY** | [Y|N] Когда пользователь выполняет AJAX-переходы, то при включенной опции можно использовать кнопки браузера "Назад" и "Вперед". |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| Учитывать права доступа | **CACHE\_GROUPS** | [Y|N] При отмеченной опции будут учитываться права доступа при кешировании. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:support.faq","",Array(
		"IBLOCK_TYPE" => "services", 
		"IBLOCK_ID" => "17", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600",
		"CACHE_GROUPS" => "Y",     
		"AJAX_MODE" => "N", 
		"SEF_MODE" => "Y", 
		"SECTION" => "-", 
		"EXPAND_LIST" => "Y", 
		"AJAX_OPTION_JUMP" => "N", 
		"AJAX_OPTION_STYLE" => "Y", 
		"AJAX_OPTION_HISTORY" => "N", 
		"SEF_FOLDER" => "/", 
		"SEF_URL_TEMPLATES" => Array(
			"section" => "#SECTION_ID#/",
			"detail" => "#SECTION_ID#/#ELEMENT_ID#"
		),
		"SHOW_RATING" => "Y",
		"RATING_TYPE" => "like_graphic",
		"PATH_TO_USER" => "",
		"VARIABLE_ALIASES" => Array(
			"section" => Array(),
			"detail" => Array(),
			"faq" => Array(),
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх