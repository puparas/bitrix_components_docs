| Поле | Описание |
| --- |

|
| Профиль | Указывается один из вариантов построения **CAPTCHA**. |
| Прозрачность текста в процентах от 0 до 100 |

|
| Нижняя граница случайного цвета фона | Указывается нижняя граница случайного цвета фона. |
| Верхняя граница случайного цвета фона |

|
| Количество кругов | Указывается количество кругов, которые будут показаны на изображениях **CAPTCHA**. |
| Нижняя граница случайного цвета круга |

|
| Верхняя граница случайного цвета круга | Указывается верхняя граница случайного цвета круга. |
| Линии поверх текста |

|
| Количество линий | Указывается количество линий, наносимых на изображения **CAPTCHA**. |
| Нижняя граница случайного цвета линии |

|
| Верхняя граница случайного цвета линии | Указывается верхняя граница случайного цвета линии. |
| Отступ текста слева |

|
| Размер шрифта | Параметр определяет размер шрифта текста, наносимых на изображения **CAPTCHA**. |
| Нижняя граница случайного цвета шрифта |

|
| Верхняя граница случайного цвета шрифта | Указывается верхняя граница случайного цвета шрифта. |
| Минимальный угол отклонения от вертикали |

|
| Максимальный угол отклонения от вертикали | Указывается максимальный угол отклонения букв текста от вертикали. |
| Минимальное расстояние между началами символов (при отрицательном значении максимальное расстояние наложения символов) |

|
| Максимальное расстояние между началами символов (при отрицательном значении минимальное расстояние наложения символов) | Указывается максимальное расстояние между началами символов (при отрицательном значении минимальное расстояние наложения символов). |
| Нелинейные искажения |

|
| Цвет границы | Указывается цвет границы изображений **CAPTCHA**. |
| Используемые шрифты |

|
| Допустимые символы (рекомендованный набор ABCDEFGHJKLMNPQRSTWXYZ23456789) | Указываются допустимые символы, отображаемые на изображениях **CAPTCHA** (рекомендованный набор ABCDEFGHJKLMNPQRSTWXYZ23456789). |

#### Смотрите также:

* [CAPTCHA (учебный курс "Администратор. Базовый")](https://dev.1c-bitrix.ru/learning/course/?COURSE_ID=35&CHAPTER_ID=02128&LESSON_PATH=3906.4503.2128)

Новинки документации в соцсетях:

#### Пользовательские комментарииПомните, что Пользовательские комментарии, несмотря на модерацию, не являются официальной документацией. Ответственность за их использование несет сам пользователь. Также Пользовательские комментарии не являются местом для обсуждения функционала. По подобным вопросам обращайтесь на [форумы](http://dev.1c-bitrix.ru/community/forums/group1/).

| 6  **Роберт Басыров** 21.05.2009 17:36:11 |
| --- |
| Использование Captcha в отдельной форме  Проверка полей после сабмита формы:   |

| | --- | | ``` include_once($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/classes/general/captcha.php"); 
 $cptcha = new CCaptcha(); 
 
 if(!strlen($_REQUEST["captcha_word"])>0){ 
    $err .= "! Не введен защитный код<br/>"; 
 } 
 elseif(!$cptcha -> CheckCode($_REQUEST["captcha_word"],$_REQUEST["captcha_sid"])){ 
    $err .= "! Код с картинки заполнен не правильно<br/>";    
 } 
 if(!strlen($err)>0): ``` |   Вывод Captcha в нужном месте формы:   | Код | | --- | | ``` <?/* CAPTCHA */ 
    $arResult["CAPTCHA_CODE"] = htmlspecialchars($GLOBALS["APPLICATION"]->CaptchaGetCode()); 
    if (true) 
    { 
       ?> 
       <tr> 
          <td colspan="2"><b>Защита</b></td> 
       </tr> 
       <tr> 
          <td></td> 
          <td> 
             <input type="hidden" name="captcha_sid" value="<?=$arResult["CAPTCHA_CODE"]?>" /> 
             <img src="/bitrix/tools/captcha.php?captcha_code=<?=$arResult["CAPTCHA_CODE"]?>" width="180" height="40" alt="CAPTCHA" /> 
          </td> 
       </tr> 
       <tr> 
          <td><span class="starrequired">*</span>Введите код с картинки:</td> 
          <td><input type="text" name="captcha_word" maxlength="50" value="" /></td> 
       </tr> 
       <? 
    } 
    /* CAPTCHA */?> ``` | |
|  |

``` include_once($_SERVER["DOCUMENT_ROOT"]."/bitrix/modules/main/classes/general/captcha.php"); 
 $cptcha = new CCaptcha(); 
 
 if(!strlen($_REQUEST["captcha_word"])>0){ 
    $err .= "! Не введен защитный код<br/>"; 
 } 
 elseif(!$cptcha -> CheckCode($_REQUEST["captcha_word"],$_REQUEST["captcha_sid"])){ 
    $err .= "! Код с картинки заполнен не правильно<br/>";    
 } 
 if(!strlen($err)>0): ```

``` <?/* CAPTCHA */ 
    $arResult["CAPTCHA_CODE"] = htmlspecialchars($GLOBALS["APPLICATION"]->CaptchaGetCode()); 
    if (true) 
    { 
       ?> 
       <tr> 
          <td colspan="2"><b>Защита</b></td> 
       </tr> 
       <tr> 
          <td></td> 
          <td> 
             <input type="hidden" name="captcha_sid" value="<?=$arResult["CAPTCHA_CODE"]?>" /> 
             <img src="/bitrix/tools/captcha.php?captcha_code=<?=$arResult["CAPTCHA_CODE"]?>" width="180" height="40" alt="CAPTCHA" /> 
          </td> 
       </tr> 
       <tr> 
          <td><span class="starrequired">*</span>Введите код с картинки:</td> 
          <td><input type="text" name="captcha_word" maxlength="50" value="" /></td> 
       </tr> 
       <? 
    } 
    /* CAPTCHA */?> ```