|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Идентификатор резюме (Transcript ID) |

| Указывается идентификатор резюме студента. |
| **Дополнительные настройки** |

| |
| Устанавливать заголовок страницы |

| [Y|N] При отмеченной опции в качестве заголовка страницы будет установлено имя пользователя. |
| Формат имени |

```
<$APPLICATION->IncludeComponent("bitrix:learning.student.transcript","",Array(

		"TRANSCRIPT_ID" => $_REQUEST["TRANSCRIPT_ID"], 

		"SET_TITLE" => "Y", 

		"NAME_TEMPLATE" => "#LAST_NAME# #NAME_SHORT# #SECOND_NAME_SHORT#" 

	),

);?>


```