|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| URL, ведущий на страницу c результатами сертификации |

| Указывается путь к странице с результатами сертификации. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

```
<?$APPLICATION->IncludeComponent("bitrix:learning.student.profile","",Array(

		"TRANSCRIPT_DETAIL_TEMPLATE" => "certification/?TRANSCRIPT_ID=#TRANSCRIPT_ID#", 

		"SET_TITLE" => "Y" 

	),

);?>


```