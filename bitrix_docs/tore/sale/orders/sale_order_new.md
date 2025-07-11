| Поле | Описание |
| --- |

|
| **Добавить товар** и **Новый товар...** | По этим кнопкам вызываются окна добавления товара в создаваемый/редактируемый заказ. **Добавить товар** - добавление из существующего в каталоге товара. **Новый товар...** - возможность добавить произвольный, даже не существующий в каталоге товар.    **Примечание:** кнопка **Новый товар...** доступна только в том случае, если в настройках модуля [Интернет-магазин](/user_help/store/sale/settings_sale.php) отмечена опция **Разрешать добавлять новый товар в форме редактирования заказа**. |
| Таблица с составом заказа |

| Поле | Описание | | --- | --- | | Действия | Доступны следующие действия с позициями в заказе:  * **Изменить** - изменение параметров товара в форме, аналогичной форме **Новый товар...** * **Удалить** - удаление товарной позиции. заказа. | | Изображение | Изображение товара. | | Название | Название товара. Ссылка с названием позволяет перейти к просмотру товара в административной части сайта. | | Количество | Количество товара, приобретаемое покупателем. | | Остаток | Количество товара на складе. | | Свойства | Свойства товара, передаваемые в заказ (например, ID, цвет, размер и т.д.). | | Цена | Стоимость данной позиции заказа в единичном экземпляре. | | Сумма | Общая стоимость данной позиции в заказе. | |
| Промокод |

|

### Форма Новый товар

| Поле | Описание |
| --- |

|
| Код | Произвольный числовой код, который не должен повторятся в рамках списка товаров. |
| \*Наименование |

|
| Путь к странице с детальным описанием | Вводится путь к страничке с товаром (если есть) от корня сайта. |
| Внешний код каталога |

|
| Внешний код товара | Символьный код, используемый для связи с внешним источником данных. Например, для взаимодействия с 1С. |
| Тип цены |

|
| Свойства товара в заказе | Таблица со свойствами товара. новые строки добавляются по кнопке **Добавить**. |
| \*Количество |

|
| \*Цена | Цена товара в рублях. |
| Вес |

|
| \* - поля обязательные для заполнения | |

### Покупатель

| **Поле** | Описание |
| --- |

|
| При создании заказа доступна кнопка **Найти покупателя**, с помощью которой происходит выбор покупателя и все поля, либо их часть, заполнятся автоматически, согласно настройкам выбранного покупателя.  Для создания нового покупателя необходимо вручную заполнить все поля. | |
| \*Тип плательщика |

|
| Выбор профиля | Для существующего покупателя создается, либо выбирается профиль.  Поле доступно только при создании заказа. |
| Физическое лицо |

|
| Личные данные | |
| \*Ф.И.О. |

|
| \*E-Mail | Электронный адрес для уведомлений. |
| \*Телефон |

|
| Данные для доставки | |
| \*Индекс |

|
| \*Местоположение | Выбор местоположения. |
| Город |

|
| \*Адрес доставки | Адрес доставки заказа. |
| Комментарий |

|
| Комментарий покупателя к заказу | Если покупатель оставил комментарий, то он выводится в этом поле. |
| Юридическое лицо |

|
| Данные компании | |
| \*Название компании  Юридический адрес  ИНН  КПП |

|
| Контактная информация | |
| \*Контактное лицо |

|
| \*E-Mail | Электронный адрес для уведомлений. |
| Телефон  Факс |

|
| \*Индекс | Почтовый индекс. |
| Город |

|
| \*Местоположение | Выбор местоположения. |
| \*Адрес доставки |

|
| Комментарий | |
| Комментарий покупателя к заказу |

|

\* - поля, обязательные для заполнения.

### Финансовая информация о заказе

Данная секция доступна при создании заказа, при его редактировании она недоступна.

В секции отображается информация о том, какая сумма выставлена к оплате, сколько уже оплачено и сколько осталось оплатить. Кроме того, при наличии средств у покупателя на внутреннем счете, будет отображаться информация о величине остатка на счете и ссылка **Использовать внутренний счет**. Ссылка служит для создания документа об оплате через внутренний счет (т.е. при ее нажатии заполняться поля в секции **Оплата**).

### Отгрузка

Секция служит для создания/редактирования документов по отгрузке товаров заказа. Каждый документ выделен в отдельный блок.

**Примечание:** при создании заказа можно оформить только один документ отгрузки, т.е. изначально все товары попадают в одну отгрузку. Разделение отгрузки на части выполняется при просмотре существующего заказа.

При редактировании заказа в шапке блока отгрузки доступны следующие ссылки:

* **Удалить** - удаление документа отгрузки;
* **Редактировать** - переход на страницу [редактирования](/user_help/store/sale/orders/sale_order_shipment_edit.php) документа отгрузки;
* **Свернуть/Развернуть** - отображение блока с документом отгрузки в более компактном или, наоборот, развернутом виде.

Каждый блок отгрузки имеет следующие поля, представленные в таблице ниже.

| Поле | Описание |
| --- |

|
| \*Служба доставки | Выбор службы доставки. |
| Стоимость доставки |

|
| Офис отгрузки | Офис, с которого выполняется отгрузка. При создании заказа доступна ссылка **Добавить**, которая служит для перехода к добавлению в систему записи об офисе отгрузке. |
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

| Поле | Описание | | --- | --- | | № | Порядковый номер товарной позиции в отгрузке | | Изображение | Изображение товара. | | Название | Название товара. Ссылка с названием позволяет перейти к просмотру товара в административной части сайта. | | Свойства | Свойства товара, передаваемые в заказ (например, ID, цвет, размер и т.д.). | | Количество к отгрузке | Количество товара, которое должно быть отгружено по текущему документу отгрузки. | | Склад | Склад, с которого будет выполняться отгрузка. | | Отгрузка | Количество товара, отгружаемого с конкретного склада.   **Примечание:** сумма значений в этом поле должна быть равна значению, указанному в поле **Количество к отгрузке**. | | Штрихкод | Штрихкод товара. | |

\* - поля, обязательные для заполнения.

### Оплата

Данная секция содержит информацию о документах по оплате заказа. Каждый документ представлен в виде отдельного блока.

В шапке блока оплаты доступны следующие ссылки:

* **Удалить** - удаление документа оплаты;
* **Редактировать** - переход на страницу [редактирования](/user_help/store/sale/orders/sale_order_payment_edit.php) документа оплаты (недоступно при создании заказа);
* **Свернуть/Развернуть** - отображение блока с документом оплаты в более компактном или, наоборот, развернутом виде (недоступно при создании заказа).

В форме создания заказа под блоком с документом оплаты доступна кнопка **Добавить оплату**. При ее нажатии открывается страница создания [нового документа оплаты](/user_help/store/sale/orders/sale_order_payment_edit.php) заказа.

Каждый блок оплаты имеет следующие поля, представленные в таблице ниже.

| Поле | Описание |
| --- |

|
| \*Способ оплаты | Выбирается метод оплаты заказа. |
| Сумма к оплате |

|
| *Статус\_оплаты* | Статус оплаты заказа (**Не оплачено** или **Оплачено**). В форме создания заказа статус можно изменять. |
| Номер документа прихода |

|
| Дата прихода | Устанавливается дата создания платежного документа. |
| Принять оплату на |

|

\* - поля, обязательные для заполнения.

### Дополнительная информация

Добавление дополнительной информации к заказу.

| Поле | Описание |
| --- |

|
| Ответственный | Пользователь, ответственный за выполнение заказа.  При наведении курсора мыши на имя пользователя становится доступной ссылка **Изменить**. При ее нажатии открывается окно выбора пользователя, который будет ответственным за заказ. |
| Офис |

|
| Комментарий | |
| Комментарий менеджера |

|

### Статус заказа

| **Поле** | Описание |
| --- |

|
| Создан | Дата, время и имя пользователя, создавшего заказ. Поле доступно в режиме редактирования заказа. |
| Последнее изменение |

|
| Сайт | Сайт, на котором был создан заказ. Поле доступно в режиме редактирования заказа. |
| Аффилиат |