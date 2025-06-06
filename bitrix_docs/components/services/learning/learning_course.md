# Учебный курс (комплексный компонент)

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

[Учебный курс (комплексный компонент)](/user_help/components/services/learning/learning_course.php)
[Все материалы курса](/user_help/components/services/learning/learning_course_contents.php)
[Дерево курса](/user_help/components/services/learning/learning_course_tree.php)
[Детальный вывод курса](/user_help/components/services/learning/learning_course_detail.php)
[Список курсов](/user_help/components/services/learning/learning_course_list.php)
[Поиск по курсам](/user_help/components/services/learning/learning_search.php)
[Журнал студента](/user_help/components/services/learning/learning_student_gradebook.php)
[Отчет по курсам](/user_help/components/services/learning/learning_student_certificates.php)
[Профиль студента](/user_help/components/services/learning/learning_student_profile.php)
[Резюме студента](/user_help/components/services/learning/learning_student_transcript.php)
[Контрольный тест](/user_help/components/services/learning/learning_test.php)
[Самопроверка](/user_help/components/services/learning/learning_test_self.php)
[Список тестов](/user_help/components/services/learning/learning_test_list.php)
[Детальный вывод главы](/user_help/components/services/learning/learning_chapter_detail.php)
[Детальный вывод урока](/user_help/components/services/learning/learning_lesson_detail.php)

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

[Обучение](/user_help/components/services/learning/index.php)

Учебный курс (комплексный компонент)

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Учебный курс (комплексный компонент)

Комплексный компонент осуществляет полноценный вывод учебного курса. Компонент стандартный и входит в дистрибутив модуля.

### Описание **learning.course**

В визуальном редакторе компонент находится в *Компоненты > Сервисы > Обучение*.

Компонент относится к модулю [Обучение](/user_help/service/learning/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Идентификатор курса | **COURSE\_ID** | Указывается идентификатор курса. |
| **Управление адресами страниц** | | |
| Включить поддержку ЧПУ | **SEF\_MODE** | [Y|N] При отмеченной опции будет включена поддержка ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_FOLDER** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Адреса страниц | **SEF\_URL\_TEMPLATES** | Указываются адреса следующих страниц:  * **course.detail** - главная страница; * **lesson.detail** - страница урока; * **chapter.detail** - страница главы; * **test.self** - страница теста для самопроверки; * **test** - страница теста; * **test.list** - страница списка тестов; * **course.contents** - страница со всеми материалами курса; * **gradebook** - страница журнала. |  **SEF\_FOLDER**, **SEF\_URL\_TEMPLATES**. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. |
| **Дополнительные настройки** | | |
| Проверять право доступа | **CHECK\_PERMISSIONS** | [Y|N] При отмеченной опции будет проверяться право на доступ к курсу. |
| URL, ведущий на страницу с профилем пользователя | **PATH\_TO\_USER\_PROFILE** | Указывается шаблон пути со страницей профиля пользователя. |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено название курса. |
| **Настройки теста** | | |
| Количество вопросов в навигационной цепочке | **PAGE\_WINDOW** | Указывается количество вопросов, отображаемых в навигационной цепочке. |
| Показывать счетчик ограничения времени | **SHOW\_TIME\_LIMIT** | [Y|N] При отмеченной опции будет отображаться счетчик времени.  **Примечание:** если в настройках теста ограничение по времени не установлено, то счетчик не будет отображаться в любом случае. |
| Идентификатор вопроса | **PAGE\_NUMBER\_VARIABLE** | Задается имя переменной для идентификатора вопроса теста. |
| **Настройки списка тестов** | | |
| Количество тестов на странице | **TESTS\_PER\_PAGE** | Указывается количество тестов, выводимых на одной странице. Остальные тесты будут выведены с помощью постраничной навигации. |

### Пример вызова

```
<$APPLICATION->IncludeComponent("bitrix:learning.course","",Array(
		"SEF_MODE" => "Y", 
		"COURSE_ID" => "$_REQUEST[\"COURSE_ID\"]", 
		"CHECK_PERMISSIONS" => "Y", 
		"PAGE_WINDOW" => "10", 
		"SHOW_TIME_LIMIT" => "Y", 
		"PAGE_NUMBER_VARIABLE" => "PAGE", 
		"TESTS_PER_PAGE" => "20", 
		"SET_TITLE" => "Y", 
		"CACHE_TYPE" => "A", 
		"CACHE_TIME" => "3600", 
		"SEF_FOLDER" => "/", 
		"SEF_URL_TEMPLATES" => Array(
			"course.detail" => "course#COURSE_ID#/index",
			"lesson.detail" => "course#COURSE_ID#/lesson#LESSON_ID#/",
			"chapter.detail" => "course#COURSE_ID#/chapter#CHAPTER_ID#/",
			"test.self" => "course#COURSE_ID#/selftest#SELF_TEST_ID#/",
			"test" => "course#COURSE_ID#/test#TEST_ID#/",
			"test.list" => "course#COURSE_ID#/examination/",
			"course.contents" => "course#COURSE_ID#/contents/",
			"gradebook" => "course#COURSE_ID#/gradebook/"
		),
		"VARIABLE_ALIASES" => Array(
			"course.detail" => Array(),
			"lesson.detail" => Array(),
			"chapter.detail" => Array(),
			"test.self" => Array(),
			"test" => Array(),
			"test.list" => Array(),
			"course.contents" => Array(),
			"gradebook" => Array(),
		)
	)
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх