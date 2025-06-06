|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Показывать кнопку |

| [Y|N] При отмеченной опции кнопки компонента будут отображены на странице. |
| Идентификатор |

| Идентификатор компонента. |
| Название |

| Имя компонента, которое будет отображаться в публичной части. |
| Обработчик события выбора |

| Обработчик, который будет использовать данный компонент. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.colorpicker","",Array(  
		"SHOW_BUTTON" => "Y",  
		"ID" => "123",  
		"NAME" => "Выбор цвета",  
		"ONSELECT" => ""  
	),  

```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 0  **Антон Долганин** 19.08.2010 01:03:54 |
| --- |
| Пример использования:   |

| | --- | | ``` 
 <sc ript type="text/javascript">
 function OnSelectBGColor(color, objColorPicker)
 {
    alert(color);
 }
 </script>
 
 <?$APPLICATION->IncludeComponent(
    "bitrix:main.colorpicker",
    "",
    Array(
       "SHOW_BUTTON" => "Y",
       "ID" => "color_bg_picker",
       "NAME" => "Выбор цвета",
       "ONSELECT" => "OnSelectBGColor"
    ),
 $component, array("HIDE_ICONS" => "Y")
 );?>
  ``` | |
|  |

```
<?$APPLICATION->IncludeComponent("bitrix:main.colorpicker","",Array(  
		"SHOW_BUTTON" => "Y",  
		"ID" => "123",  
		"NAME" => "Выбор цвета",  
		"ONSELECT" => ""  
	),  

```

``` 
 <sc ript type="text/javascript">
 function OnSelectBGColor(color, objColorPicker)
 {
    alert(color);
 }
 </script>
 
 <?$APPLICATION->IncludeComponent(
    "bitrix:main.colorpicker",
    "",
    Array(
       "SHOW_BUTTON" => "Y",
       "ID" => "color_bg_picker",
       "NAME" => "Выбор цвета",
       "ONSELECT" => "OnSelectBGColor"
    ),
 $component, array("HIDE_ICONS" => "Y")
 );?>
  ```