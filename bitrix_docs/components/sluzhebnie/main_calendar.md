|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Показывать элемент управления |

| [Y|N] Параметр служит для выбора способа отображения календаря:  * **Y** - показывать иконки календаря с полем ввода; * **N** - показывать только иконки календаря. |
| Имя формы |

| Указывается имя формы календаря. |
| Имя первого поля интервала |

| Указывается название переменной первого поля временного интервала. |
| Имя второго поля интервала |

| Указывается название переменной второго поля временного интервала. |
| Значение первого поля интервала |

| Указывается значение по умолчанию первого поля временного интервала. |
| Значение второго поля интервала |

| Указывается значение по умолчанию второго поля временного интервала. |
| Позволять вводить время |

| [Y|N] При отмеченной опции пользователь имеет возможность указать не только дату, но и время. |
| Скрывать поле для ввода времени |

| [Y|N] При отмеченной опции поле для ввода времени будет скрыто. |

### Пример вызова

```
<?$APPLICATION->IncludeComponent("bitrix:main.calendar","",Array(

     "SHOW_INPUT" => "Y",

     "FORM_NAME" => "",

     "INPUT_NAME" => "date_fld",

     "INPUT_NAME_FINISH" => "date_fld_finish",

     "INPUT_VALUE" => "",

     "INPUT_VALUE_FINISH" => "", 

     "SHOW_TIME" => "Y",

     "HIDE_TIMEBAR" => "Y"

	)

);?>


```

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 3  **c0013r** 10.09.2012 10:39:53 |
| --- |
| Для того, чтобы добавить какие-то атрибуты к полю ввода можно воспользоваться параметром компонента INPUT\_ADDITIONAL\_ATTR.  Например:   |

| | --- | | ``` <? 
 $APPLICATION->IncludeComponent('bitrix:main.calendar', '', Array(
       'SHOW_INPUT' => 'Y',
       'FORM_NAME' => '',
       'INPUT_NAME' => 'date_fld',
       'INPUT_NAME_FINISH" => 'date_fld_finish',
       'INPUT_VALUE' => '',
       'INPUT_VALUE_FINISH' => '', 
       'SHOW_TIME' => 'Y', 
       'HIDE_TIMEBAR' => 'Y', 
       'INPUT_ADDITIONAL_ATTR' => 'placeholder="дд.мм.гггг"'
    )
 );
 ?>
  ``` | |
|  |

```
<?$APPLICATION->IncludeComponent("bitrix:main.calendar","",Array(

     "SHOW_INPUT" => "Y",

     "FORM_NAME" => "",

     "INPUT_NAME" => "date_fld",

     "INPUT_NAME_FINISH" => "date_fld_finish",

     "INPUT_VALUE" => "",

     "INPUT_VALUE_FINISH" => "", 

     "SHOW_TIME" => "Y",

     "HIDE_TIMEBAR" => "Y"

	)

);?>


```

``` <? 
 $APPLICATION->IncludeComponent('bitrix:main.calendar', '', Array(
       'SHOW_INPUT' => 'Y',
       'FORM_NAME' => '',
       'INPUT_NAME' => 'date_fld',
       'INPUT_NAME_FINISH" => 'date_fld_finish',
       'INPUT_VALUE' => '',
       'INPUT_VALUE_FINISH' => '', 
       'SHOW_TIME' => 'Y', 
       'HIDE_TIMEBAR' => 'Y', 
       'INPUT_ADDITIONAL_ATTR' => 'placeholder="дд.мм.гггг"'
    )
 );
 ?>
  ```