| Кнопка | Описание |
| --- |

|
| Создать | Переход на страницу создания нового вопроса формы. |
| Копировать |

|
| Удалить вопрос | Удаление текущего вопроса. |

### Упрощённая форма редактирования

**Закладка "Свойства"**

| Поле | Описание |
| --- |

|
| Дата изменения | Дата последнего изменения вопроса. Поле отображается при редактировании существующего вопроса. |
| Активен |

|
| Порядок сортировки | Относительный "вес", определяющий положение вопроса в общем списке. |
| Изображение |

|
| Вопрос | Текст вопроса. |
| Поле ответа обязательно для заполнения |

|
| Тип поля для ответа | Тип поля для ответа на данный вопрос:  * **text** - однострочный текст; * **textarea**- многострочный текст; * **multiselect** - список вариантов с возможностью множественного выбора; * **dropdown** - список вариантов с возможностью одиночного выбора; * **radio** - набор radio кнопок (одиночный выбор); * **checkbox** - набор checkbox кнопок (множественный выбор); * **image** - поле для ввода изображения; * **date** - поля для ввода даты со встроенным календарем; * **file** - поле для добавления файла; * **password** - поле для ввода пароля; * **email** - поле для ввода электронного адреса; * **url** - поле для ввода адреса сайта; * **hidden** - скрытое поле. |
| Ответ |

| Поле | Описание | | --- | --- | | Варианты ответа | Вариант ответа на вопрос. | | Порядок | Относительный "вес", определяющий порядок следования вариантов ответа в списке. | | По умолчанию | Вариант ответа, отмеченный в этом поле, по умолчанию будет использоваться в качестве ответа на вопрос. | |

  
**Закладка "Валидаторы"** Добавление валидаторов для используемых полей ответов.

| Поле | Описание |
| --- |

|
| Доступные валидаторы для поля типа **<тип\_поля>** | Из выпадающего списка для поля указанного типа выбирается один из доступных валидаторов. Для его назначения служит кнопка **Добавить валидатор**, расположенная рядом с полем. |

  

**Закладка "Комментарий"**

Созданный служебный комментарий будет отображаться только в административном разделе.

### Полная форма. Свойства

| Поле | Описание |
| --- |

|
| Дата изменения | Дата последнего изменения вопроса. Поле отображается при редактировании существующего вопроса. |
| Активен |

|
| Порядок сортировки | Относительный "вес", определяющий положение вопроса в общем списке. |
| \* Символьный идентификатор |

|
| Обязателен | Признак обязательности ответа на данный вопрос. |

\* - Поля, обязательные для заполнения.

### Полная форма. Вопрос

| Поле | Описание |
| --- |

|
| Изображение | Изображение, которое будет показываться рядом с вопросом. |
| Текст вопроса |

|

### Полная форма. Ответ

Форма позволяет создать поля, используемые для ввода ответа на вопрос, либо создать возможные варианты ответов на вопрос.

| Поле | Описание |
| --- |

|
| ID | Идентификатор поля для ответа. |
| Текст [ ANSWER\_TEXT ] |

|
| Значение [ ANSWER\_VALUE ] | Дополнительный параметр, который может быть использован для идентификации конкретного ответа (например, в списках). |
| Тип поля |

|
| Ширина | Ширина полей типа **text**, **textarea**, **image**, **date**. Задается количеством столбцов. |
| Высота |

|
| Параметры | Данное поле может использоваться для вывода стиля элемента ввода, а также для задания специальных идентификаторов:  * **SELECTED** - при задании этого идентификатора поле ввода будет выделено; работает для полей следующих типов: **multiselect**, **dropdown**, **radio**. * **CHECKED** - при задании этого идентификатора поле ввода будет выделено; работает для полей следующих типов: **checkbox**. * **NOT\_ANSWER** - идентификатор используется для пометки тех пунктов элементов управления, которые не являются вариантами ответа на вопрос. В том случае, если этот идентификатора задан и если ответ на вопрос обязателен, выбор посетителем данного ответа не будет считаться ответом на обязательный вопрос формы. Работает для типов полей: **dropdown**, **radio**, **multiselect**, **checkbox**. * **NOW\_DATE -**выводит в поле типа **date** текущую дату. * **NOW\_TIME -**выводит в поле типа **date** текущее время. |
| Сорт. |

|
| Акт. | Признак активности поля. Для отображения в публичном разделе выбираются только активные варианты ответа. |
| Уд. |

|
| Для добавления дополнительных полей для ответа, нажмите на кнопку **Добавить ответ**. | |

### Полная форма. Валидаторы

Добавление валидаторов для используемых полей ответов.

| Поле | Описание |
| --- |

|
| Доступные валидаторы для поля типа **<тип\_поля>** | Выбирается один из доступных валидаторов. Для его назначения служит кнопка **Добавить валидатор**, расположенная рядом с полем. |
| Для добавления дополнительных валидаторов, нажмите на кнопку **Добавить валидатор**. |

|

### Полная форма. Результаты

Закладка служит для настройки параметров показа результатов ответа вопрос.

| Поле | Описание |
| --- |

|
| Показать в HTML-таблице результатов | Если отметить данный флаг, то ответы на данный вопрос будут отображены в HTML-таблице результатов формы. |
| Показать в Excel-таблице результатов |

|
| Заголовок столбца в таблице | Текст, который будет выводиться в таблице результатов в качестве заголовка столбца, содержащего ответы на данный вопрос. |

### Полная форма. Фильтр

| Поле | Описание |
| --- |