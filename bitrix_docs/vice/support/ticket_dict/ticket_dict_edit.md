# Создание и редактирование записи справочника

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

[Бизнес-процессы](/user_help/service/bizproc/index.php)

[Блоги](/user_help/service/blogs/index.php)

[Веб-мессенджер](/user_help/service/im/index.php)

[Веб-формы](/user_help/service/form/index.php)

[Видеоконференциии (КП)](/user_help/service/video/index.php)

[Внешние источники данных (КП)](/user_help/service/xdi/index.php)

[Интранет (КП)](/user_help/service/intranet/index.php)

[Календарь событий](/user_help/service/event_calendar/index.php)

[Конструктор отчетов (КП)](/user_help/service/report/index.php)

[Экстранет (КП)](/user_help/service/extranet/index.php)

[Контроллер](/user_help/service/controller/index.php)

[Менеджер идей](/user_help/service/idea/index.php)

[Опросы, голосования](/user_help/service/vote/index.php)

[Обучение](/user_help/service/learning/index.php)

[Подписка, рассылки](/user_help/service/subscribe/index.php)

[Почта](/user_help/service/mail/index.php)

[Рейтинги](/user_help/service/rating/index.php)

[Смайлы](/user_help/service/smile/index.php)

[Социальная сеть (КП)](/user_help/service/socialnetwork/index.php)

[Социальные сервисы](/user_help/service/socialservices/index.php)

[Стикеры](/user_help/service/stickers/index.php)

[Техподдержка](/user_help/service/support/index.php)

[Техподдержка. Настройки модуля](/user_help/service/support/settings.php)
[Рабочий стол](/user_help/service/support/ticket_desktop.php)
[Обращения](/user_help/service/support/ticket_list.php)
[Создание и редактирование обращения](/user_help/service/support/ticket_edit.php)
[Графики](/user_help/service/support/ticket_report_graph.php)
[Уровни поддержки](/user_help/service/support/ticket_sla_list.php)
[Создание и редактирование уровня поддержки](/user_help/service/support/ticket_sla_edit.php)
[Группы](/user_help/service/support/ticket_group_list.php)
[Создание и редактирование группы](/user_help/service/support/ticket_group_edit.php)
[Купоны спецобращений](/user_help/service/support/ticket_coupon_list.php)
[Создание и редактирование купона](/user_help/service/support/ticket_coupon_edit.php)
[Журнал использования купонов](/user_help/service/support/ticket_coupon_log.php)

[Справочники](/user_help/service/support/ticket_dict/index.php)

[Типы справочников техподдержки](/user_help/service/support/ticket_dict/ticket_dict_list.php)
[Создание и редактирование записи справочника](/user_help/service/support/ticket_dict/ticket_dict_edit.php)

[Расписания](/user_help/service/support/ticket_timetable/index.php)

[Учет рабочего времени (КП)](/user_help/service/timeman/index.php)

[Форум](/user_help/service/forum/index.php)

[CRM (КП)](/user_help/service/crm/index.php)

[Веб-аналитика](/user_help/statistic/index.php)

[Marketplace](/user_help/marketplace/index.php)

[Настройки](/user_help/settings/index.php)

[Компоненты](/user_help/components/index.php)

[Описание компонентов решений](/user_help/description_decisions/index.php)

[Дополнительно](/user_help/additional/index.php)

[Сервисы](/user_help/service/index.php)

[Техподдержка](/user_help/service/support/index.php)

[Справочники](/user_help/service/support/ticket_dict/index.php)

Создание и редактирование записи справочника

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование записи справочника

Форма предназначена для создания и редактирования записей справочников техподдержки, а именно:

* **Категории**;
* **Критичности**;
* **Статусы**;
* **Оценки ответов**;
* **Частые ответы**;
* **Источники**;
* **Сложность**.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Справочник | Открывает справочник для текущего типа записи. |
| Создать новую запись | Создает новую запись текущего типа в справочнике. |
| Удалить запись | Удаляет открытую запись.    Кнопка отображается только при редактировании существующей записи справочника. |

### Закладка Запись

| Поле | Описание |
| --- | --- |
| Тип | Тип записи справочника. |
| Сайты | Указываются сайты, в которых должна быть показана данная запись. |
| Порядок сортировки | Порядок сортировки при выводе. |
| \*Заголовок | Заголовок записи. |
| Символьный код | При использовании функции API **CTicket::SetTicket** есть возможность задавать в качестве параметра не **ID** типа записи справочника, а его символьные коды, что упрощает программирование. Данное поле может содержать именно этот символьный код. |
| Описание | Для типов категория, критичность, оценка, статус данное поле используется для всплывающей подсказки.     Для типа часто используемые ответы это поле используется для ввода тела ответа. |
| При создании нового обращения на сайте, выбирать по умолчанию в выпадающем списке | Флаг позволяет выбрать по умолчанию данное значение в веб-форме при создании нового обращения. Для одного типа записей справочника и одного сайта может быть только одна запись, для которой этот флаг будет установленным.     Поле доступно для модификации только для типов категория, критичность и источники. |
| Ответственный | Ответственный за обращение.     Поле доступно для модификации только для типов категория, критичность и источники. |

\* - поле, обязательное для заполнения.

### Закладка Статистика

Доступна только для типа категория.

| Как регистрировать новые обращения в техподдержку в модуле статистики | |
| --- | --- |
| **event1** | Идентификатор **event1** типа события для модуля **Веб-аналитика**. |
| **event2** | Идентификатор **event2** типа события для модуля **Веб-аналитика**. |
| **event3** | Дополнительный параметр события для модуля **Веб-аналитика**. |

### Смотрите также

* [Справочники (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2619)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх