| Параметр | Описание |
| --- |

|
| **Найти** | Поле, позволяющее найти события по их основным параметрам: **идентификатору**, **event1** или **event2**.   Это поле присутствует, даже если фильтр свернут. |
| ID\* |

|
| event1\* | Идентификатор типа события – **event1.** |
| event2\* |

|
| Наименование\* | Наименование типа события. |
| Описание\* |

|
| Первое (DD.MM.YYYY) | Интервал для поля **Первое** (дата первого события данного типа). |
| Последнее (DD.MM.YYYY) |

|
| Период (DD.MM.YYYY) | Временной интервал, за который вы хотите вывести количество событий соответствующих типов. |
| Всего событий |

|
| Денежная сумма | Интервал для фильтрации суммы денег по всем событиям того или иного типа за все время (столбец **Всего**). |
 Сколько дней хранить каждое событие | Фильтр по интервалу количества дней, отводимых для хранения искомых типы событий (в случае, если это количество задано, а не используется по умолчанию). || Сколько дней хранить динамику типа события | Фильтр по интервалу количества дней, отводимых для хранения динамики искомых типы событий (в случае, если это количество задано, а не используется по умолчанию). |
| Включить в отчет по рекламе |

|
| Включить в круговую диаграмму и график по умолчанию | Позволяет выбрать типы событий с определённым значением флага  **Включить в круговую диаграмму и график по умолчанию**. |

\* - для данных полей вы можете воспользоваться [специальными логическими выражениями](https://dev.1c-bitrix.ru/api_help/main/general/filter.php).

Чтобы установить фильтр по заданным критериям поиска, нажмите на кнопку **Найти**. Для отображения всех типов событий нажмите на кнопку **Отменить**.

### Контекстная панель

| Кнопка | Описание |
| --- |

|
| Добавить | Открывает форму создания нового типа событий. |
| Группировка |

|
| Диаграмма | Открывает форму с [круговой диаграммой типов событий](/user_help/statistic/events/type/event_diagram_list.php). |
| Графики |

|
| Настроить | Позволяет перейти к диалогу настройки внешнего вида отчетной формы. |
| Excel |

|

### Типы событий

| Поле | Описание |
| --- |

|
| Колонка флажков | Поле предназначено для выбора событий, к которым предполагается применить какое-либо действие из панели действий, расположенной ниже таблицы кампаний.  Эта колонка присутствует только в несгруппированной таблице. |
| Меню действий |

|
| ID | Идентификатор типа события.  Эта колонка присутствует только в несгруппированной таблице. |
| Наименование |

|
| event1 | Идентификатор типа события – **event1**.   Эта колонка присутствует, если таблица не сгруппирована или сгруппирована по **event1**. |
| event2 |

|
| Сегодня | Количество событий данного типа за текущий день. |
| Вчера |

|
| Позавчера | Количество событий данного типа за позавчерашний день. |
| Всего |

|
| Первое | Дата первого события данного типа. |
| Последнее |