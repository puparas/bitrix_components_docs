| Поле | Описание |
| --- |

|
| ID | Идентификатор раздела в системе. **Поле отображается при редактировании существующего раздела.** |
| Создана |

|
| Изменена | Дата и время последнего изменения параметров раздела. **Поле отображается при редактировании существующего раздела.** |
| Раздел активен |

|
| Родительский раздел | Раздел, дочерним элементом которого является этот раздел. |
| \*Название |

|
| Изображение | Изображение, ассоциируемое с данным разделом информационного блока. Для выбора изображения используйте кнопку **Добавить файл** или воспользуйтесь необходимым пунктом меню кнопки :  * **Загрузить с компьютера** - загрузка изображения с локального компьютера; * **Выбрать из медиабиблиотеки** - выбор изображения из Медиабиблиотеки; * **Выбрать из структуры** - выбор изображения из структуры сайта; * **Вставить путь к файлу** - указывается путь к изображению на сервере; |
| Описание |

|
| Переключатель режима ввода текста | Задается режим ввода текста описания раздела инфоблока: **Text**, **HTML** или **Визуальный редактор**.    В текстовом режиме отсутствует возможность форматирования текста и вставки рисунков. Режим HTML позволяет использовать любое форматирование сообщения с помощью HTML-тегов. Визуальный редактор позволяет редактировать контент так, как он непосредственно будет выглядеть на сайте. |

\* - поля, обязательные для заполнения.

### SEO

По умолчанию все настройки SEO для раздела берутся из настроек для инфоблока (вышестоящего раздела), а с помощью данной закладки можно задать персональные настройки SEO для текущего раздела и всех его подразделов. Прежде, чем приступать к настройке того или иного шаблона, следует отметить расположенную рядом с его полем опцию **Изменить для этого раздела и его подразделов.**

| Поле | Описание |
| --- |

|
| Настройки для разделов/элементов | |
| Шаблон META TITLE |

|
| Шаблон META KEYWORDS | Задается шаблон, по которому будет создаваться мета-тег *KEYWORDS* для раздела/элементов раздела. Кнопка [...] служит для выбора данных, на основе которых будет создан шаблон. |
| Шаблон META DESCRIPTION |

|
| Заголовок раздела/товара | Задается шаблон для создания заголовка страницы просмотра раздела/элемента этого раздела. Вывод данного заголовка выполняется с помощью функции ShowTitle():    ``` <H1><?$APPLICATION->ShowTitle()?></H1> ```  Кнопка [...] служит для выбора данных, на основе которых будет создан шаблон. |
| Настройки для изображений разделов, детальных картинок разделов, картинок анонса элементов и для детальных картинок элементов |

|
| Шаблон ALT | Задается шаблон, по которому будет создаваться атрибут *ALT* для изображения. Кнопка [...] служит для выбора данных, на основе которых будет создан шаблон. |
| Шаблон TITLE |

|
| Шаблон имени файла | Задается шаблон, по которому будет создаваться имя файла с изображением. Кнопка [...] служит для выбора данных, на основе которых будет создан шаблон.   Имя файла будет формироваться с учетом следующих опций:   * **Привести к нижнему регистру** - при отмеченной опции имя файла будет создано в нижнем регистре; * **Транслитерировать** - при отмеченной опции будет выполнена транслитерация имени файла; * **Замена для пробельных символов после транслитерации** - задается символ, который будет использоваться вместо пробела после транслитерации имени файла. |
| Управление |

|
| Очистить кеш вычисленных значений | При отмеченной опции очищается кеш шаблонов и все вносимые изменения в настройках отображаются сразу. |

### Дополнительно, Доп. свойства, Доступ

  
  

### Закладка Дополнительно

| Поле | Описание |
| --- |

|
| Сортировка | Относительный "вес", влияющий на положение раздела в списке. |
| Внешний код |

|
| Символьный код | Мнемонический код раздела, состоящий из латинских символов. Используется при выборе разделов и элементов разделов для показа в публичной части сайта. |
| Детальная картинка |

``` <H1><?$APPLICATION->ShowTitle()?></H1> ```