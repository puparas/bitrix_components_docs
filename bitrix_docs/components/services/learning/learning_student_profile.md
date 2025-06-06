# Профиль студента

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

Профиль студента

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Профиль студента

### Описание **learning.student.profile**

Компонент отображает результаты прохождения тестов. Компонент является стандартным и входит в дистрибутив модуля.

В визуальном редакторе компонент находится в *Компоненты > Сервисы > Обучение*.

Компонент относится к модулю [Обучение](/user_help/service/learning/index.php).

### Параметры

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| URL, ведущий на страницу c результатами сертификации | **TRANSCRIPT\_DETAIL\_TEMPLATE** | Указывается путь к странице с результатами сертификации. |
| **Дополнительные настройки** | | |
| Устанавливать заголовок страницы | **SET\_TITLE** | [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено **Анкета специалиста**. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:learning.student.profile","",Array(
		"TRANSCRIPT_DETAIL_TEMPLATE" => "certification/?TRANSCRIPT_ID=#TRANSCRIPT_ID#", 
		"SET_TITLE" => "Y" 
	),
);?>

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх