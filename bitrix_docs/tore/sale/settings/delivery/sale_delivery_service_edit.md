| Поле | Описание |
| --- |

|
| Закладка "Настройки обработчика" для настраиваемой службы доставки | |
| Валюта |

|
| Цена | Сумма, которая добавляется к стоимости товаров в заказе для оплаты услуг службы доставки.   Если валюта цены отличается от валюты заказа, то происходит автоматический пересчет в валюту заказа по текущему курсу системы. |
| Сроки доставки |

|
| Закладка "Настройки обработчика" для автоматизированной службы доставки | |
| Служба доставки |

|
| Описание | Описание обработчика службы доставки. Отображается только при редактировании существующей службы. |
| Наценка |

|
| Тип наценки | Тип наценки на стоимость доставки: в % или в выбранной на закладке **Общие настройки** валюте. |
| Закладка "Настройки" для службы доставки Почта России |

|
| Тип службы доставки | Тип службы доставки. Поле не редактируется. |
| Токен авторизации |

|
| Ключ авторизации | Ключ авторизации, полученный на сайте Почты России. |
| Точка сдачи |

|
| Показывать прецеденты невыкупа покупателя в форме заказа | При отмеченной опции будет выводиться информация о благонадёжности  получателя (есть ли прецеденты невыкупа). Актуально для отправлений с наложенным платежом. Опция доступна с версии модуля Интернет-магазин **v19.0.0**. |
| Длина (мм) |

|
| Ширина (мм) | Значение ширины груза по умолчанию. |
| Высота (мм) |

|
| Вес (г) | Вес груза по умолчанию. |
| Закладка "Настройки" для профиля службы доставки Почта России |

|
| Наименование типа профиля | Тип профиля службы доставки. Поле не редактируется. |
| Описание |

|
| Категория | Выбор категории профиля службы доставки. |
| Поддержка Он-лайн сервиса "Отправка" |

|
| Закладка "Настройки" для службы доставки СДЭК | |
| Тип службы доставки |

|
| Логин | Логин для запросов API калькуляции, полученный у СДЭК. |
| Пароль |

|
| Длина (мм) | Значение длины груза по умолчанию. |
| Ширина (мм) |

|
| Высота (мм) | Значение высоты груза по умолчанию. |
| Вес (г) |

|
| Закладка "Настройка тарифов" для службы доставки по группам местоположений | |
| Валюта |

|
| По умолчанию | Стоимость по умолчанию для данной доставки (т.е. стоимость доставки для тех местоположений, которые не вошли в группы). |
| *название\_группы\_местоположений* |

|
| Закладка "Настройки" для службы доставки СПСР-ЭКСПРЕСС | |
| Рассчитывать стоимость сразу |

|
| Вес отгрузки по умолчанию (грамм) | Указывается значение величины веса по умолчанию. |
| Страхование объявления / объявленная стоимость |

|
| Характер груза | Выбирается тип груза. |
| Логин |

|
| Пароль | Пароль аккаунта на сайте службы СПСР-ЭКСПРЕСС. |
| Индивидуальный клиентский номер |

|
| Закладка "Настройки" для службы доставки DPD | |
| Тип службы доставки |

|
| \*Клиентский номер в системе DPD (номер вашего договора с DPD) | Указывается номер договора с DPD, полученный у менеджера DPD. |
| \*Уникальный ключ для авторизации, полученный у сотрудника DPD |

|
| Место передачи груза DPD | Выбирается место передачи груза в DPD:  * **Склад интернет-магазина** * **Пункт приема DPD** |
| Длина (мм) |

|
| Ширина (мм) | Значение ширины груза по умолчанию. |
| Высота (мм) |

|
| Вес (г) | Вес груза по умолчанию. |

\* - поля, обязательные для заполнения.

### Профили

Данная закладка доступна только при редактировании параметров уже сохраненной любой автоматизированной службы доставки, службы доставки **Почта России**, **СДЭК**, **СПСР-ЭКСПРЕСС** и **DPD**.

| Поле | Описание |
| --- |

|
| кнопка *Добавить профиль* | Выполняет переход к [добавлению нового профиля](/user_help/store/sale/settings/delivery/sale_delivery_profile_edit.php) текущей службы доставки. |
| кнопка *Настроить* |

|
| *таблица со списком профилей* | | Поле | Описание | | --- | --- | | Действия | Действия над профилем:  * **Копировать** - переход к форме [добавления](/user_help/store/sale/settings/delivery/sale_delivery_profile_edit.php) нового профиля путем копирования параметров текущего; * **Редактировать** - переход к форме [редактирования](/user_help/store/sale/settings/delivery/sale_delivery_profile_edit.php) профиля; * **Удалить** - удаление профиля. | | ID | Идентификатор профиля службы доставки. | | Название | Название профиля. | | Активность | Признак активности профиля службы доставки. Покупателям интернет-магазина будут доступны только активные профили. | | Логотип | Логотип профиля службы доставки. | |

### Ограничения

На закладке задаются ограничения по использованию текущей службы доставки.

| Поле | Описание |
| --- |

|
| кнопка *Добавить ограничение* | Служит для добавления ограничения путем заполнения данных во всплывающей форме. Ограничения могут быть:  * исключить местоположения (профиль будет доступен для всех местоположений, кроме указанных); * по весу; * по группам пользователей; * по категории товара; * по конкретным товарам; * по максимальному размеру; * по максимальным размерам; * по местоположению (профиль будет доступен только для указанных местоположений); * по общей стоимости товаров; * по платёжным системам; * по публичной части (отображать ли профиль в публичной части сайта, либо же он доступен только в панели администратора); * по сайтам; * по типу плательщика. |
| кнопка *Настроить* |

|
| *таблица со списком ограничений* | | Поле | Описание | | --- | --- | | Действия | Действия над ограничением:  * **Редактировать** - редактирование параметров ограничения во всплывающем окне; * **Удалить** - удаление ограничения. | | ID | Идентификатор ограничения. | | Сортировка | Относительный "вес" ограничения. | | Тип ограничения | Тип ограничения. | | Параметры | Параметры ограничения. | |

### Дополнительные услуги

Данная закладка доступна для настраиваемых служб доставок, службы доставки **СДЭК**, **СПСР-ЭКСПРЕСС**, **DPD** и **по группам местоположений**.

Автоматизированная служба **ПЭК** также имеет закладку с названием **Дополнительные услуги**, но ее описание смотрите [ниже](#pek), поскольку она существенно отличается от текущей закладки.

| Поле | Описание |
| --- |

|
| кнопка *Добавить доп. услугу* | Выполняет переход к форме [добавления дополнительной услуги](/user_help/store/sale/settings/delivery/sale_delivery_eservice_edit.php). |
| кнопка *Настроить* |

|
| *таблица со списком услуг* | | Поле | Описание | | --- | --- | | Действия | Действия над услугой:  * **Редактировать** - переход к форме [редактирования](/user_help/store/sale/settings/delivery/sale_delivery_eservice_edit.php) дополнительной услуги; * **Удалить** - удаление дополнительной услуги. | | Идентификатор | Идентификатор услуги. | | Наименование | Название дополнительной услуги. | | Сортировка | Относительный "вес" услуги. | | Активность | Признак активности дополнительной услуги. Покупателям интернет-магазина будут доступны только активные услуги. | | Тип | Тип услуги: *список услуг*, *количественная услуга* или *единичная услуга*. | | Описание | Описание дополнительной услуги. | |

### Прочие закладки автоматизированных служб, службы доставки **Почта России**, **СДЭК**, **СПСР-ЭКСПРЕСС** и **DPD**

| Служба | Закладка |
| --- |

|
| DHL (USA) [dhlusa] | **Параметры отправлений**  | Поле | Описание | | --- | --- | | Тип упаковки | Выбирается один из возможных типов упаковки: *DHL Express Letter*, *DHL Other Packaging* или *Собственная упаковка*. | |
| UPS [ups] |

| Поле | Описание | | --- | --- | | CSV-файл с зонами доставки | Указывается адрес к CSV-файлу с зонами доставки. | | CSV-файл с тарифами доставки | Указывается адрес к CSV-файлу с тарифами доставки. | |
| Новая почта [ua\_post] |

| Поле | Описание | | --- | --- | | Тариф на услугу доставки по технологии "Склад-Склад" | | | Стоимость оформления | Стоимость оформления доставки. | | Цена за 1 кг | Цена за 1 кг заказа. | | Доплата к услуге "Склад-Склад" за услугу "Склад-Дверь" или "Дверь-Склад" | | | *весовые интервалы* | Для каждого весового интервала указывается стоимость доплаты. | | Тариф на услугу доставки "Дверь-Дверь" | | | *весовые интервалы* | Для каждого весового интервала указывается стоимость доставки по данной услуге. | | Комиссия за объявленную ценность | | | Размер комиссии % | Размер процента комиссии за объявленную ценность заказа. | | Минимальная сумма комиссии | Минимально взимаемая сумма комиссии. | |
| ПЭК [pecom] |