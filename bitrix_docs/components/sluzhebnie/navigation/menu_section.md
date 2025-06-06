|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Включить режим совместимости с поддержкой ЧПУ |

| [Y|N] При отмеченной опции включается режим поддержки ЧПУ.   Если режим поддержки ЧПУ **включен**, то необходимо настроить следующие параметры:     |  |  |  | | --- | --- | --- | | Каталог ЧПУ (относительно корня сайта) | **SEF\_BASE\_URL** | Каталог ЧПУ: путь до папки, с которой работает компонент. Этот путь может как совпадать с физическим путём, так и не совпадать. | | Шаблон URL, ведущий на страницу с содержимым раздела | **SECTION\_PAGE\_URL** | Указывается шаблон пути, ведущий на страницу с содержимым раздела. | | Шаблон URL, ведущий на страницу с элементом | **DETAIL\_PAGE\_URL** | Указывается шаблон пути, ведущий на страницу с элементом. |  **SEF\_BASE\_URL**, **SECTION\_PAGE\_URL**, **DETAIL\_PAGE\_URL**. |
| Тип информационного блока |

| Указывается идентификатор типа информационного блока. |
| Код информационного блока |

| Для выбранного типа инфоблоков указывается идентификатор (код) инфоблока, на основе которого будет строиться меню. |
| **Источник данных** |

| |
| Сколько уровней вложенности выводить |

| Задается глубина вложений, согласно которой будет строиться меню. |
| **Настройки кеширования** |

| |
| Тип кеширования |

| Тип кеширования:  * **A** - Авто + Управляемое: автоматически обновляет кеш компонентов в течение заданного времени или при изменении данных; * **Y** - Кешировать: для кеширования необходимо определить время кеширования; * **N** - Не кешировать: кеширования нет в любом случае. |
| Время кеширования (сек.) |

| Время кеширования, указанное в секундах. По умолчанию поле содержит 3600 сек. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:menu.sections","",Array(

		"IS_SEF" => "Y", 

		"SEF_BASE_URL" => "/catalog/phone/", 

		"SECTION_PAGE_URL" => "#SECTION_ID#/", 

		"DETAIL_PAGE_URL" => "#SECTION_ID#/#ELEMENT_ID#", 

		"IBLOCK_TYPE" => "news", 

		"IBLOCK_ID" => "1", 

		"DEPTH_LEVEL" => "1", 

		"CACHE_TYPE" => "A", 

		"CACHE_TIME" => "3600" 

	)

);?>


```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 4  **Александр Щербаков** 01.09.2015 10:02:01 |
| --- |
| Живой пример для файла меню, например **.catalog.menu\_ext.php** (в модуле bitrix:menu должно быть «USE\_EXT» ⇒ «Y»)  |

| | --- | | ``` 
 <?
 if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
 
 global $APPLICATION;
 $aMenuLinksExt = array();
 
 if(CModule::IncludeModule('iblock'))
 {
    $arFilter = array(
       "TYPE" => "catalog",
       "SITE_ID" => SITE_ID,
    );
 
    $dbIBlock = CIBlock::GetList(array('SORT' => 'ASC', 'ID' => 'ASC'), $arFilter);
    $dbIBlock = new CIBlockResult($dbIBlock);
 
    if ($arIBlock = $dbIBlock->GetNext())
    {
       if(defined("BX_COMP_MANAGED_CACHE"))
          $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_".$arIBlock["ID"]);
 
       if($arIBlock["ACTIVE"] == "Y")
       {
          $aMenuLinksExt = $APPLICATION->IncludeComponent("bitrix:menu.sections", "", array(
             "IS_SEF" => "Y",
             "SEF_BASE_URL" => "",
             "SECTION_PAGE_URL" => $arIBlock['SECTION_PAGE_URL'],
             "DETAIL_PAGE_URL" => $arIBlock['DETAIL_PAGE_URL'],
             "IBLOCK_TYPE" => $arIBlock['IBLOCK_TYPE_ID'],
             "IBLOCK_ID" => $arIBlock['ID'],
             "DEPTH_LEVEL" => "3",
             "CACHE_TYPE" => "N",
          ), false, Array('HIDE_ICONS' => 'Y'));
       }
    }
 
    if(defined("BX_COMP_MANAGED_CACHE"))
       $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_new");
 }
 
 $aMenuLinks = array_merge($aMenuLinks, $aMenuLinksExt);
 ?>
  ``` | |
|  |

```
<?$APPLICATION->IncludeComponent("bitrix:menu.sections","",Array(

		"IS_SEF" => "Y", 

		"SEF_BASE_URL" => "/catalog/phone/", 

		"SECTION_PAGE_URL" => "#SECTION_ID#/", 

		"DETAIL_PAGE_URL" => "#SECTION_ID#/#ELEMENT_ID#", 

		"IBLOCK_TYPE" => "news", 

		"IBLOCK_ID" => "1", 

		"DEPTH_LEVEL" => "1", 

		"CACHE_TYPE" => "A", 

		"CACHE_TIME" => "3600" 

	)

);?>


```

``` 
 <?
 if(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true)die();
 
 global $APPLICATION;
 $aMenuLinksExt = array();
 
 if(CModule::IncludeModule('iblock'))
 {
    $arFilter = array(
       "TYPE" => "catalog",
       "SITE_ID" => SITE_ID,
    );
 
    $dbIBlock = CIBlock::GetList(array('SORT' => 'ASC', 'ID' => 'ASC'), $arFilter);
    $dbIBlock = new CIBlockResult($dbIBlock);
 
    if ($arIBlock = $dbIBlock->GetNext())
    {
       if(defined("BX_COMP_MANAGED_CACHE"))
          $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_".$arIBlock["ID"]);
 
       if($arIBlock["ACTIVE"] == "Y")
       {
          $aMenuLinksExt = $APPLICATION->IncludeComponent("bitrix:menu.sections", "", array(
             "IS_SEF" => "Y",
             "SEF_BASE_URL" => "",
             "SECTION_PAGE_URL" => $arIBlock['SECTION_PAGE_URL'],
             "DETAIL_PAGE_URL" => $arIBlock['DETAIL_PAGE_URL'],
             "IBLOCK_TYPE" => $arIBlock['IBLOCK_TYPE_ID'],
             "IBLOCK_ID" => $arIBlock['ID'],
             "DEPTH_LEVEL" => "3",
             "CACHE_TYPE" => "N",
          ), false, Array('HIDE_ICONS' => 'Y'));
       }
    }
 
    if(defined("BX_COMP_MANAGED_CACHE"))
       $GLOBALS["CACHE_MANAGER"]->RegisterTag("iblock_id_new");
 }
 
 $aMenuLinks = array_merge($aMenuLinks, $aMenuLinksExt);
 ?>
  ```