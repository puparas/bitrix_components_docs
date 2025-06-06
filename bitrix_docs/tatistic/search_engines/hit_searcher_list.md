# Хиты поисковиков

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

[Веб-аналитика. Настройки модуля](/user_help/statistic/settings_va.php)
[Сводная статистика](/user_help/statistic/stat_list.php)
[Кто на сайте](/user_help/statistic/users_online.php)

[Посещаемость](/user_help/statistic/site_traffic/index.php)

[Рекламные кампании](/user_help/statistic/advertising_campaigns/index.php)

[События](/user_help/statistic/events/index.php)

[Поисковики](/user_help/statistic/search_engines/index.php)

[Поисковые фразы. Переходы с поисковиков](/user_help/statistic/search_engines/phrase_list.php)
[Поисковые системы](/user_help/statistic/search_engines/searcher_list.php)
[Круговая диаграмма индексации сайта](/user_help/statistic/search_engines/searcher_diagram_list.php)
[График индексации сайта](/user_help/statistic/search_engines/searcher_graph_list.php)
[Хиты поисковиков](/user_help/statistic/search_engines/hit_searcher_list.php)
[Динамика посещений сайта поисковиком](/user_help/statistic/search_engines/searcher_dynamic_list.php)
[Редактирование поисковика](/user_help/statistic/search_engines/searcher_edit.php)
[Автодетект](/user_help/statistic/search_engines/autodetect_list.php)

[Ссылающиеся сайты](/user_help/statistic/referer_sites/index.php)

[Посетители](/user_help/statistic/visitors/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Поисковики](/user_help/statistic/search_engines/index.php)

Хиты поисковиков

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Хиты поисковиков

На странице **Хиты поисковиков** (*Аналитика > Поисковики > Индексация > Хиты поисковиков*) представлены адреса страниц сайта, проиндексированные внешними поисковыми системами.

  

### Фильтр

| Поле | Описание |
| --- | --- |
| Поисковая система\* | ID или наименование поисковой системы для отображения. Для выбора можно воспользоваться выпадающим списком со всеми поисковыми системами, занесенными в базу данных. Это поле присутствует, даже если фильтр свернут. |
| ID\* | Поиск по маске ID записи в базе данных, содержащей адрес проиндексированной страницы. |
| Дата (DD.MM.YYYY): | Период времени, за который требуется отобразить данные по индексации. |
| Страница\* | Поиск по маске адреса проиндексированной страницы.   В выпадающем списке **(ошибка 404)** можно указать, отображать ли только запросы несуществующих страниц. |
| UserAgent\* | Отбор хитов поисковых систем по маске UserAgent (поле HTTP-заголовка UserAgent). |
| IP адрес\* | Отбор хитов поисковых систем по маске значения поля **IP адрес** (поиск по IP адресу поисковых систем на момент индексации той или иной страницы). |
| Логика между полями | Переключатель, определяющий механизм поиска записей:  * **И** - выводятся события, удовлетворяющие всем критериям фильтра.* **ИЛИ** - выводятся события, удовлетворяющие хотя бы одному критерию. |

\* - для данных полей вы можете воспользоваться [специальными логическими выражениями](https://dev.1c-bitrix.ru/api_help/main/general/filter.php).

Чтобы установить фильтр по заданным критериям поиска, нажмите на кнопку **Найти**. Для отображения всех хитов нажмите на кнопку **Отменить**.

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Настроить | Переход к диалогу настройки внешнего вида отчетной формы. |
| Excel | Экспорт данных из отображаемой таблицы в MS Excel. |

### Список хитов поисковиков

| Поле | Описание |
| --- | --- |
| ID | ID проиндексированной страницы. |
| Дата | Дата и время индексации страницы. |
| Поисковик | Поисковая система. Ссылка на идентификаторе открывает [список поисковых систем](/user_help/statistic/search_engines/searcher_list.php) с фильтром, установленным на эту систему. |
| UserAgent | UserAgent поисковой системы. |
| IP адрес | IP адрес поисковой системы на момент индексации страницы. Ссылка **Стоп-лист** открывает [форму для добавления в стоп-лист](/user_help/statistic/visitors/stoplist_edit.php) данного IP-адреса. |
| Страница | Адрес проиндексированной страницы. Ссылка на идентификаторе сайта открывает [форму редактирования сайта](/user_help/settings/settings/sites/site_edit.php). |

### Смотрите также

* [Хиты поисковиков (учебный курс "Продвижение сайта и Маркетинг")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=139&LESSON_ID=2117)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх