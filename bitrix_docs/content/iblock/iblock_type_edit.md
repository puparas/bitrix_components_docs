| Поле | Описание |
| --- |

|
| \*Идентификатор (ID) | Код, однозначно идентифицирующий тип инфоблоков в системе. Должен содержать только латинские символы. |
| Использовать древовидный классификатор элементов по разделам |

|
| Языкозависимые названия и заголовки объектов: | |
| |

| \*Название | Разделы | Элементы | | --- | --- | --- | --- | | [1] | [2] | [3] | [4] |  | Поле | Описание | | --- | --- | | [1] Язык | Список языков, используемых в системе. Названия типов, а также разделов и элементов информационных блоков указываются отдельно для каждого языка. | | [2] \*Название | Название типа инфоблоков для данного языка (например, Каталог). | | [3] Разделы | Название разделов инфоблоков данного типа для этого языка (например, Группы). | | [4] Элементы | Название элементов инфоблоков данного типа для этого языка (например, Товары). | | |

\* - поля, обязательные для заполнения.

### Дополнительно

| Поле | Описание |
| --- |

|
| Использовать экспорт в RSS | Если этот флаг установлен, содержимое инфоблоков данного типа может экспортироваться в RSS-файл и сохраняться в директории, указанной в поле **Путь к экспортируемым RSS файлам** в форме настроек модуля [Информационные блоки](/user_help/content/iblock/settings.php). |
| Сортировка |

|
| Файл для редактирования элемента, позволяющий модифицировать поля перед сохранением | Полный путь к файлу, отвечающему за обработку полей элементов инфоблоков данного типа при сохранении. Может быть использован для модификации данных перед сохранением элементов в административном разделе. **Важно!** Это поле предназначено только для использования разработчиками.См. [Пользовательские формы редактирования](https://dev.1c-bitrix.ru/user_help/content/iblock/settings.php#form) |
| Файл с формой редактирования элемента |

|

<!--
<h4>Кнопки управления

| Кнопка | Описание |
| --- |

|
| Сохранить | Сохранение внесённых изменений. Переход на страницу со [списком типов информационных блоков](/user_help/content/iblock/iblock_type_admin.php). |
| Применить |