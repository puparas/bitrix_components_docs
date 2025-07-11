| **Поле** | Описание |
| --- |

|
| Создан | Дата, время и имя пользователя, создавшего заказ. |
| Последнее изменение |

|
| Сайт | Сайт, на котором был создан заказ. |
| Аффилиат |

|
| Статус заказа | Статус, в котором находится заказ. |
| Отмена заказа |

|

### Покупатель

| **Поле** | Описание |
| --- |

|
| Покупатель | Логин и Ф.И.О. пользователя. |
| Тип плательщика |

|
| Физическое лицо | |
| Личные данные |

|
| Ф.И.О. | Ф.И.О. покупателя. |
| E-Mail |

|
| Телефон | Номер телефона. |
| Данные для доставки |

|
| Индекс | Почтовый индекс |
| Местоположение |

|
| Город | Указан только в том случае, если его невозможно указать в поле **Местоположение**. |
| Адрес доставки |

|
| Комментарий | |
| Комментарий покупателя к заказу |

|
| Юридическое лицо | |
| Данные компании |

|
| Название компании  Юридический адрес  ИНН  КПП | Поля для ввода данных о компании. |
| Контактная информация |

|
| Контактное лицо | Контактное лицо. |
| E-Mail |

|
| Телефон  Факс | Поля для ввода телефона и факса компании. |
| Индекс |

|
| Город | Указан только в том случае, если его невозможно указать в поле **Местоположение**. |
| Местоположение |

|
| Адрес доставки | Адрес доставки заказа. |
| Комментарий |

|
| Комментарий покупателя к заказу | Если покупатель оставил комментарий, то он выводится в этом поле. |

### Отгрузка

Секция служит для добавления/редактирования документов по отгрузке товаров заказа. Каждый документ выделен в отдельный блок.

В шапке блока отгрузки доступны следующие ссылки:

* **Удалить** - удаление документа отгрузки;
* **Редактировать** - переход на страницу [редактирования](/user_help/store/sale/orders/sale_order_shipment_edit.php) документа отгрузки;
* **Свернуть/Развернуть** - отображение блока с документом отгрузки в более компактном или, наоборот, развернутом виде.

Под блоками с документами отгрузки доступна кнопка **Добавить отгрузку**. При ее нажатии открывается страница создания
[нового документа отгрузки](/user_help/store/sale/orders/sale_order_shipment_edit.php).

Каждый блок отгрузки имеет следующие поля, представленные в таблице ниже.

| Поле | Описание |
| --- |

|
| Служба доставки | Служба доставки товаров заказа. |
| Стоимость доставки |

|
| Офис отгрузки | Офис, с которого выполняется отгрузка. |
| Доставка разрешена |

|
| Отгрузка | Флаг отгрузки товаров заказа. |
| Статус документа |

|
| Идентификатор отправления | Идентификатор отправления заказа. |
| Номер документа отгрузки |

|
| Дата документа отгрузки | Дата создания документа отгрузки. |
| Состав отгрузки |

| Поле | Описание | | --- | --- | | № | Порядковый номер товарной позиции в отгрузке. | | Изображение | Изображение товара. | | Название | Название товара. Ссылка с названием позволяет перейти к просмотру товара в административной части сайта. | | Свойства | Свойства товара, передаваемые в заказ (например, ID, цвет, размер и т.д.). | | Количество к отгрузке | Количество товара, которое должно быть отгружено по текущему документу отгрузки. | | Склад | Склад, с которого будет выполняться отгрузка. | | Отгрузка | Количество товара, отгружаемого с конкретного склада.   **Примечание:** сумма значений в этом поле должна быть равна значению, указанному в поле **Количество к отгрузке**. | | Штрихкод | Штрихкод товара. | |

### Информация по оплатам

В секции отображается информация о том, какая сумма выставлена к оплате, сколько уже оплачено и сколько осталось оплатить. Кроме того, при наличии средств у покупателя на внутреннем счете, будет отображаться информация о величине остатка на нем.

#### Секция "Оплата"

Данная секция содержит информацию о документах по оплате заказа. Каждый документ представлен в виде отдельного блока.

В шапке блока оплаты доступны следующие ссылки:

* **Удалить** - удаление документа оплаты;
* **Редактировать** - переход на страницу [редактирования](/user_help/store/sale/orders/sale_order_payment_edit.php) документа оплаты;
* **Свернуть/Развернуть** - отображение блока с документом оплаты в более компактном или, наоборот, развернутом виде.

Под блоками с документами оплаты доступна кнопка **Добавить оплату**. При ее нажатии открывается страница создания [нового документа оплаты](/user_help/store/sale/orders/sale_order_payment_edit.php) заказа.

Каждый блок оплаты имеет следующие поля, представленные в таблице ниже.

| Поле | Описание |
| --- |

|
| Способ оплаты | Платежная система для оплаты заказа. |
| Сумма к оплате |

|
| *Статус\_оплаты* | Статус оплаты заказа (**Не оплачено** или **Оплачено**). |
| Номер документа прихода |

|
| Дата прихода | Устанавливается дата создания платежного документа. |
| Принять оплату на |

|

### Дополнительная информация

| Поле | Описание |
| --- |

|
| Ответственный | Пользователь, ответственный за выполнение заказа. |
| Офис |

|
| Комментарий менеджера | Комментарий менеджера по заказу. Комментарий не виден покупателю. |

### Состав заказа

| Поле | Описание |
| --- |

|
| Таблица с составом заказа | | Поле | Описание | | --- | --- | | Изображение | Изображение товара отображается вместе со свойствами товара. | | Название | Название товара. Ссылка с названием позволяет перейти к просмотру товара в административной части сайта. При наличии скидки на товар она отображается под названием товара, не использовать которую можно путем снятия соответствующего флага. | | Количество | Количество товара, приобретаемое покупателем. | | Остаток | Количество товара на складе. | | Цена | Стоимость данной позиции заказа в единичном экземпляре. | | Сумма | Общая стоимость данной позиции в заказе. |  В последней строке таблицы отображаются скидки, применяемые в заказе. При необходимости их можно отключить, сняв необходимые флаги. |
| Промокод |

|

### История изменений

Список записей об изменениях заказа с возможностью фильтрации.

**Форма поиска**

Поиск интересующих изменений заказа.

| Поле | Описание |
| --- |

|
| Пользователь | Поиск по пользователю, внесшему изменение. |
| Дата изменения |

|
| Операция | Поиск по проведенной операции с заказом. |
| Показывать ключевые операции |

|

Чтобы отобрать изменения заказа по заданным критериям поиска, нажмите кнопку **Найти**. Для отображения всех изменений заказа нажмите кнопку **Отменить**.

| Поле | Описание |
| --- |

|
| Дата изменения | Дата и время изменения заказа. |
| Пользователь |

|
| Операция | Операция, проведенная с заказом. |
| Описание |