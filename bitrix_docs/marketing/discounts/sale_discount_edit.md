| Поле | Описание | |
| --- |

| --- |
| ID |

| |
| Активность |

| |
| \*Сайт |

| |
| Название |

| |
| Период активности |

| |
| Приоритет применимости |

| |
| Индекс сортировки |

| |
| Прекратить применение скидок на текущем уровне приоритетов |

|  |
| Прекратить дальнейшее применение правил |

|

\* - поля, обязательные для заполнения.

### Действия и условия

| Поле | Описание |
| --- |

|
| Действия | |
| В данной секции для выбранного действия настраиваются условия применения правила. |

|
| Добавить действие | Выбирается действие:  * **Изменить стоимость товаров в корзине**. Применить:   + **скидку** – укажите величину скидки в процентах или в валюте магазина (RUB, USD и т.д.), на которую будет уменьшена стоимость заказа или товаров;   + **наценку** – укажите величину наценки в процентах или в валюте магазина, на которую будет увеличена стоимость заказа или товаров;   + **фиксированную цену распродажи** – укажите фиксированную стоимость товара. Может быть применено только в валюте магазина для каждого товара. При выборе процентов или общей суммы товаров – правило не сохранится и будет показана ошибка. * **Изменить стоимость доставки**. Применить к стоимости доставки:   + **скидку** – укажите величину скидки в процентах или в валюте магазина, на которую будет уменьшена стоимость доставки. Скидка не применится, если стоимость доставки меньше указанной суммы в валюте;   + **скидку не более** – укажите величину скидки      в валюте магазина        В процентах ограничение «не более» не имеет смысла и будет работать как обычная скидка.     . Если стоимость доставки окажется меньше этой суммы, то доставка станет бесплатной;   + **наценку** – укажите величину наценки в процентах или в валюте магазина, на которую будет увеличена стоимость доставки. * **Предоставить подарок** – выберите товары, из которых клиенту будет предложен на выбор товар в подарок, т.е. со скидкой 100%. |
| все условия |

|
| выполнено(ы) | Указывается требуемое выполнение выбранных условий:  * **выполнено(ы);** * **не выполнено(ы)**. |
| Добавить условие |

| Штатные условия | | --- | | **Параметры в корзине**  * **Товар в корзине** - выбор конкретного товара или торгового предложения. * **Название товара в корзине** - полное наименование товара. * **Стоимость позиции** - суммарная стоимость (цена \* количество) товара для позиции в корзине (пример: несколько одинаковых футболок). * **Цена товара** - стоимость единицы товара. * **Количество товара** - количество в шт. для позиции в корзине. * **Вес позиции** - суммарный вес (вес единицы товара \* количество) для позиции в корзине. * **Вес товара** - вес единицы товара. * **Были применены правила корзины** - варианты: да или нет. Применять правило, если другие правила корзины уже были применены, или нет. * **Свойства товара в корзине** - правило применяется, если выбранное свойство товара имеет указанный тип.    **Поля и характеристики [товара в инфоблоке](/user_help/store/catalog/products/cat_product_edit.php)**  * **Товар** - выбор конкретного товара или торгового предложения. * **Инфоблок** - выбор конкретного инфоблока. * **Раздел** - раздел, к которому привязан товар. * **Символьный код** - символьный код товара. * **Внешний код** - код, используемый для связи элемента инфоблока с внешним источником данных. * **Название** - название товара, как оно отображается в публичной части. * **Начало активности** - начало периода активности товара. * **Окончание активности** - окончание периода активности товара. * **Сортировка** - вес сортировки товара (чем меньше вес сортировки, тем выше отображается товар). * **Описание для анонса** - краткое описание товара. * **Детальное описание** - подробное описание товара. * **Дата создания** - дата создания товара. * **Автор** - пользователь, создавший товар. * **Дата изменения** - дата изменения товара. * **Изменивший** - пользователь, изменивший товар. * **Теги** - слова или словосочетания, с помощью которых формируется поиск по тегам. * **Количество товара на складе** - остаток товара на складах в данный момент. * **Вес товара** - вес единицы товара. * **НДС** - размер ставки НДС. * **НДС включен в цену** - варианты: да или нет. * **Тип цен** - выбор из доступных типов цен товара.   **Примечание**: Также в качестве условия можно использовать свойства    При создании и товаров, и торговых предложений необходимо указать их свойства (например, артикул, производитель, материал, цвет, размеры, масса и т.д.).   инфоблока товаров или торговых предложений. | |
| Дополнительные условия |

|
| все условия | Указываются необходимые условия:  * **все условия;** * **любое из условий**. |
| выполнено(ы) |

|
| Добавить условие | Выбирается условие или группа условий. | Штатные условия | | --- | | **Дополнительные условия**  * **Сумма оплаченных заказов** - сумма ранее оплаченных заказов (можно указать период). * **Количество товаров** - суммарное количество всех товаров в корзине. * **Общая стоимость товаров** - общая стоимость всех товаров с учетом уже примененных правил корзины. * **Общая исходная стоимость товаров** - общая стоимость всех товаров до применения правил корзины. * **Товары** - в корзине/заказе есть/отсутствуют товары, удовлетворяющие указанным условиям. * **Количество позиций** - необходимоe для действия правила количество различных позиций товара в корзине.    **Параметры заказа**  * **Общая сумма заказа с доставками и налогами** - общая сумма заказа, включая НДС и стоимость доставки. * **Тип плательщика** - тип плательщика, оформляющего заказ. * **Платежная система** - выбранная платёжная система. * **Служба доставки** - выбранная служба доставки. * **Общий вес заказа** - суммарный вес всех товаров заказа.    **Предыдущий оплаченный заказ**  * **Общая сумма заказа с доставками и налогами** - общая сумма заказа, включая НДС и стоимость доставки. * **Тип плательщика** - тип плательщика, оформляющего заказ. * **Платежная система** - выбранная платёжная система. * **Служба доставки** - выбранная служба доставки. * **Общий вес заказа** - суммарный вес всех товаров заказа.    **Пользователь**  * **Пользователь** - конкретный пользователь сайта. * **Группы** - группа пользователей сайта. | |

### Ограничения

| Поле | Описание |
| --- |

|
| Группы пользователей, на которые распространяется правило | В данном поле выбираются группы пользователей, имеющие право на применение данного правила. Если ни одна группа не выбрана, то правило будет доступно для пользователей всех групп. |

### Купоны

| Поле | Описание |
| --- |

|
| Создать купоны при сохранении правила | Опция доступна только при создании нового правила и, если она отмечена, то становятся доступными дополнительные поля.     * **Число купонов** - число купонов выбранного ниже типа для данного правила. * **Период активности** - указывается период активности купона:   + Без ограничений - время действия купона неограничено;   + Интервал - указывается дата начала и окончания действия купона.Обратите внимание, что в купоне в первую очередь учитывается период активности самого правила. * **Тип купонов** - указывается тип купонов правила:   + на одну позицию заказа;   + на один заказ;   + многоразовый купон. * **Максимальное число использований** - указывается количество, определяющее сколько раз может быт применен многоразовый купон. || В форме редактирования правила выводится [список купонов](/user_help/marketing/discounts/sale_discount_coupons.php). На закладке можно добавить новые купоны к правилу по кнопке **Добавить** или с помощью одноименной кнопки обновить список купонов. | |

### Дополнительно

| Поле | Описание |
| --- |

|
| Внешний код | Символьный код, используемый для связи правила с внешним источником данных. |

<!--
<h2>Кнопки управления

| Кнопка | Описание |
| --- |

|
| Сохранить | Сохранение внесённых изменений. Переход на страницу со списком правил. |
| Применить |