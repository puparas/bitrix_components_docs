| Поле | Описание |
| --- |

|
| Действия | Колонка доступна только для тех каталогов, для которых необходимо создать фасетные индексы. Доступные действия:  * **Создать** - переход к форме [создания](/user_help/content/iblock/iblock_reindex.php) фасетных индексов. |
| ID |

|
| Название | Название торгового каталога. |
| Состояние |

|

### Смотрите также

* [Фасетный поиск: улучшаем работу каталога товаров](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=42&LESSON_ID=5364)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Юрий Гранд** 30.03.2020 14:40:00 |
| --- |
| Для переиндексации элемента можно использовать метод:  |

| | --- | | ``` \Bitrix\Iblock\PropertyIndex\Manager::updateElementIndex($IBLOCK_ID,$PRODUCT_ID); ``` | |
|  |

| 3  **Владислав Морсин** 17.04.2015 21:38:47 |
| --- |
| Для удаления фасетного индекса инфоблока надо выполнить:   |

| | --- | | ``` CModule::IncludeModule('iblock');
 Bitrix\Iblock\PropertyIndex\Manager::DeleteIndex($iblockId);
 Bitrix\Iblock\PropertyIndex\Manager::markAsInvalid($iblockId); ``` | \*\*\*\*\*\*\*\*\*\*\* От разработчика: | Цитата | | --- | | Вместо DeleteIndex (в этом случае) лучше использовать dropIfExists. | |
|  |

``` \Bitrix\Iblock\PropertyIndex\Manager::updateElementIndex($IBLOCK_ID,$PRODUCT_ID); ```

``` CModule::IncludeModule('iblock');
 Bitrix\Iblock\PropertyIndex\Manager::DeleteIndex($iblockId);
 Bitrix\Iblock\PropertyIndex\Manager::markAsInvalid($iblockId); ```