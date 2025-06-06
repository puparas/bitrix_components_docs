# Создание и редактирование группы

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

Создание и редактирование группы

**Недоступно в редакциях:**Малый бизнес, Стандарт, Старт

# Создание и редактирование группы

Форма предназначена для создания новой группы техподдержки или изменения параметров уже существующей группы.

  

### Контекстная панель

| Кнопка | Описание |
| --- | --- |
| Список групп | Переход на страницу со [списком групп пользователей техподдержки](/user_help/service/support/ticket_group_list.php). |

### Закладка Группа

Закладка предназначена для настройки основных параметров группы.

| Поле | Описание |
| --- | --- |
| \*Название группы | Указывается название группы пользователей техподдержки. |
| Сортировка | Задается индекс сортировки группы. |
| XML\_ID | Указывается XML-идентификатор (набор произвольных чисел и латинских букв). Позволяет не привязываться к **ID** группы в имеющейся базе данных. В отличие от обычного идентификатора **ID** не меняется при переносе базы. Необходим для использования при разработке собственных скриптов. |
| Группа сотрудников поддержки | При отмеченной опции создаваемая группа будет относится к группе сотрудников техподдержки. Если опция не отмечена то создаваемая группа будет относится к клиентской группе. |

\* - поля, обязательные для заполнения.

### Закладка Пользователи

На закладке производится набор пользователей в группу.

| Поле | Описание |
| --- | --- |
| Пользователь | Идентификатор и логин пользователя, состоящего в группе. |
| Может видеть сообщения группы | При отмеченной опции пользователь сможет видеть сообщения, написанные другим пользователем этой группы. |
| Получает уведомления о новых обращениях в группе | При отмеченной опции пользователь будет получать уведомления о новых обращениях в группе. |
| Получает уведомления о обновлении обращений в группе | При отмеченной опции пользователь будет получать уведомления об обновлении обращений в группе. |
| Кнопка **Добавить** | Вызов всплывающего окна со списком пользователей для добавления их в группу. |

  
Для удаления пользователя из группы достаточно удалить его **ID** из строки.

### Смотрите также

* [Группы (учебный курс "Администратор. Модули")](https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=41&LESSON_ID=2628)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

© «Битрикс», 2001-2025, «1С-Битрикс», 2025

Наверх