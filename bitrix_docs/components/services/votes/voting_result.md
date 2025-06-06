# Результаты опроса

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

[Текущий опрос (комплексный компонент)](/user_help/components/services/votes/voting_current.php)
[Результаты опроса](/user_help/components/services/votes/voting_result.php)
[Список опросов](/user_help/components/services/votes/voting_list.php)
[Форма опроса](/user_help/components/services/votes/voting_form.php)

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

[Опросы, голосования](/user_help/components/services/votes/index.php)

Результаты опроса

**Недоступно в редакциях:**Старт

# Результаты опроса

Компонент выводит результаты опроса в виде диаграммы.
Диаграмма может быть представлена в трех видах: по умолчанию, гистограмма или круговая диаграмма. Компонент стандартный и входит в дистрибутив модуля.

В структуре визуального редактора компонент расположен по пути *Сервисы > Опросы, голосования > Результаты опроса*.

Компонент относится к модулю [Опросы, голосования](/user_help/service/vote/index.php).

Группа параметров **Дополнительно** отображается только в том случае, если параметр **VOTE\_ID** задан явно и для этого опроса созданы вопросы.

| Пример вызова компонента **voting.result** |
| --- |
| ``` <?$APPLICATION->IncludeComponent( 	"bitrix:voting.result", 	"", 	Array( 		"VOTE_ID" => "1", 		"VOTE_ALL_RESULTS" => "Y",         "NEED_SORT" => "Y", 		"CACHE_TYPE" => "A", 		"CACHE_TIME" => "1200", 		"CACHE_NOTES" => "", 		"QUESTION_DIAGRAM_1" => "histogram", 		"QUESTION_DIAGRAM_2" => "histogram" 	) );?>  ``` |

#### Секции настроек компонента:

- [Основные параметры](#main_settings)
- [Настройки кеширования](#сaching_settings)

#### Описание параметров

|  |  |  |
| --- | --- | --- |
| **Поле** | **Параметр** | **Описание** |
| **Основные параметры** | | |
| Идентификатор опроса | **VOTE\_ID** | Указывается идентификатор опроса. Задается явно или с помощью кода. |
| Показывать все результаты | **VOTE\_ALL\_RESULTS** | При отмеченной опции будут показаны все результаты. |
| Сортировать по количеству ответов | **NEED\_SORT** | Сортировка вариантов ответов по убыванию количества поданных голосов:  * **Y** - Сортировать; * **N** - Не сортировать. |
| **Настройки кеширования** | | |
| Тип кеширования | **CACHE\_TYPE** | Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) | **CACHE\_TIME** | Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |
| **Дополнительно** | | |
| Тип диаграммы для вопроса *<название\_вопроса>* | **QUESTION\_DIAGRAM\_*N*** | Для созданного в опросе вопроса *<название\_вопроса>* (*N* - идентификатор вопроса) указывается тип диаграммы: по умолчанию, гистограмма (**histogram**) или круговая диаграмма (**circle**). |
| Тема шаблона | **THEME*N*** | При установке шаблона компонента **main\_page (Встроенный шаблон)** в данном поле выбирается цветовое оформление. Доступные темы:  * бесцветная * зеленая * синяя |

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх