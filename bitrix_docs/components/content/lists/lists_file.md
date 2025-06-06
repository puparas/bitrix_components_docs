|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Источник данных** |

| |
| Тип инфоблока |

| Указывается тип информационных блоков, откуда будет использоваться информация. |
| Инфоблок |

| Для выбранного типа инфоблока указывается идентификатор информационного блока. |
| Раздел |

| Для выбранного инфоблока указывается идентификатор раздела. |
| Элемент |

| Указывается идентификатор элемента, к которому прикреплен файл. |
| Поле |

| Указывается идентификатор поля "Файл". |
| Файл |

```
 

<?$APPLICATION->IncludeComponent("bitrix:lists.file", ".default", array(

    "IBLOCK_TYPE_ID" => COption::GetOptionString("lists", "socnet_iblock_type_id"),

    "IBLOCK_ID" => $arResult["VARIABLES"]["list_id"],

    "SECTION_ID" => $arResult["VARIABLES"]["section_id"],

    "ELEMENT_ID" => $arResult["VARIABLES"]["element_id"],

    "FIELD_ID" => $arResult["VARIABLES"]["field_id"],

    "FILE_ID" => $arResult["VARIABLES"]["file_id"],

    "SOCNET_GROUP_ID" => $arResult["VARIABLES"]["group_id"],

    ),

    $component

);?>
```