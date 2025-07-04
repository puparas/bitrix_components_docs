| Поле | Описание |
| --- |

|
| Общие настройки | |
| Путь по умолчанию для экспортируемых файлов |

|
| Тип информационного блока для загрузки в формате CommerceML (из 1С) | Определяется в каталог какого типа будут выгружены данные из "1C". |
| Автоматически деактивировать товар при загрузке из CommerceML, если нет цены |

|
| Период экспорта в Яндекс.Маркет (часов) | Указывается с какой частотой данные каталогов, отмеченных в поле **Экспорт в Яндекс.Маркет** таблицы **Список информационных блоков**, экспортируются в **Яндекс.Маркет**.  Подробнее об автоматическом экспорте смотрите на странице [Автоматический экспорт каталогов в Яндекс.Маркет](/user_help/store/sale/settings/export/yandex_money.php) |
| Товары, которых нет в файле данных CommerceML |

|
| Файл кастомизированного агента экспорта в Яндекс.Маркет | Здесь можно задавать свой собственный обработчик вместо стандартного. |
| Экспорт / импорт из CSV |

|
| Доступные поля товара | Если в базе для каждого товара создано большое количество полей, содержащих значения свойств и параметров товара, то выбор конкретных полей при экспорте или импорте может оказаться затруднительным.  Указывается, какие поля из множества хранимых в базе будут доступны для выбора при экспорте. |
| Доступные поля цены |

|
| Количество уровней групп | Указывается, сколько уровней каталога будет доступно в файлах импорта / экспорта. |
| Доступные поля групп |

|
| Доступные валюты | Указываются валюты, доступные для экспорта и импорта. |

### Каталоги

Архитектура системы позволяет назначить статус торгового каталога любому информационному блоку. На данной закладке можно настроить любой из имеющихся информационных блоков на использование в качестве торгового каталога, а также выбрать информационные блоки для продажи контента и указать, данные из каких инфоблоков подлежат экспорту в **Яндекс.Маркет**. Функция взаимозависимая с закладкой **Торговый каталог** [формы редактирования инфоблока](http://dev.1c-bitrix.ru/user_help/content/iblock/iblock_edit.php). То есть задать информационному блоку свойства торгового каталога можно как в этой, так и в той закладке.

| Поле | Описание |
| --- |

|
| Перечень торговых каталогов | |
| Информационный блок |

|
| Является торговым каталогом | При отмеченной опции информационный блок будет настроен на использование в режиме торгового каталога. |
| Инфоблок торговых предложений |

|
| Продажа контента | При отмеченной опции контент информационного блока будет платным. |
| Экспортировать в Яндекс.Маркет |

|
| НДС | Указывается ставка НДС, которая будет использоваться как ставка НДС по умолчанию для товаров данного каталога.  Поле доступно для информационных блоков, которые являются торговым каталогом (отмечена опция **Является торговым каталогом**). |

### Продажа прав

На данной закладке Вы можете указать группы пользователей, права доступа к ресурсам сайта которых могут продаваться. Например, Вы можете осуществлять продажу прав на доступ к определённому разделу сайта, скачиванию файлов, управлению рекламой или любым другим ресурсам сайта и операциям над ними. При этом Вы можете определить период времени, в течение которого пользователь может работать с предоставленными ему правами.

В общем случае, чтобы организовать продажу прав доступа, необходимо выполнить следующую последовательность действий:

* на странице [Группы пользователей](/user_help/settings/users/group_admin.php) создать группу пользователей, наделенную необходимыми правами;* на странице настроек модуля **Торговый каталог** (закладка **Продажа прав**) разрешить продажу прав данной группе пользователей;* на странице [Список пользователей](/user_help/settings/users/user_admin.php) привязать пользователя, купившего право доступа, к соответствующей группе и задать период времени, на который осуществляется привязка.

| Поле | Описание |
| --- |

|
| Группа пользователей | Название группы пользователей. |
| Разрешена продажа |

|

### Доступ

Закладка позволяет настроить права на доступ к модулю **Торговый каталог** для всех имеющихся в системе групп пользователей.

| Поле | Описание |
| --- |

|
| По умолчанию | Уровень доступа групп пользователей, для которых установлено право "по умолчанию". |
| [группа\_пользователей] |

|
| Добавить право доступа | Ссылка, позволяющая добавить дополнительное право доступа для группы пользователей.. |

### Агент Яндекс.Маркет

Закладка позволяет просмотреть информацию о работе агента, либо в случае его отсутствия - добавить агент (для этого должен быть выбран экспортируемый в **Яндекс.Маркет** инфоблок).

| Кнопка | Описание |
| --- |

|
| Добавить агента | Добавление агента для экспорта. |

Стандартный агент теперь работает на UTF8-установках и пишет в журнал событий сообщения об ошибках (если они есть).

### Переиндексация данных

На закладке содержатся служебные процедуры для переиндексации скидок, переиндексации товаров и обновления остатков комплектов.

| Кнопка | Описание |
| --- |

|
| Запустить индексацию | Запуск процесса индексации скидок. |
| Запустить |

|
| Обновить остатки | Запуск процесса обновления остатков и доступности комплектов. |

### Очистка каталога

**Важно!** Закладка доступна только при выключенном складском учете.

Закладка служит для очистки доступного и зарезервированного количества товара в каталоге, обнуления остатков по складам. Таким образом, позволяет начать ведения учета с чистого листа.

| Кнопка | Описание |
| --- |

|
| Выберите каталог | Укажите каталог товаров, для которого должна быть проведена очистка доступного и/или зарезервированного количества. |
| Очистить поле "Доступное количество" |

|
| Очистить поле "Зарезервированное количество" | По кнопке **Очистить** выполняется очистка поля **Зарезервированное количество** для каждого товара в каталоге.    Если очистка поля уже выполнялась, то будет отображена дата и пользователь, который выполнял последнюю очистку. |
| Очистить остатки по складу |

|
| Выберите каталог | Укажите каталог товаров, для которого должна быть проведена очистка остатков по складам. |
| Выберите склад |