|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| **Основные параметры** |

| |
| Тип инфоблока |

| Указывается тип информационного блока календаря событий. |
| Инфоблок |

```
<?$APPLICATION->IncludeComponent("bitrix:intranet.event_calendar","",Array(

		"IBLOCK_TYPE" => "events",

		"IBLOCK_ID" => "13",

		"ALLOW_SUPERPOSE" => "Y",

		"ALLOW_RES_MEETING" => "Y",	

	)

);?>


```