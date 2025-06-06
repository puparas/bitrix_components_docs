|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| Email получателя |

| Указывается email получателя сообщения. |
| ID получателя |

| Указывается идентификатор пользователя-получателя сообщения (почтового пользователя). |
| ID записи ЖЛ |

| Указывается идентификатор записи Живой ленты. |
| ID комментария |

| Указывается идентификатор комментария к сообщению Живой ленты. |
| URL сообщения |

```
<?EventMessageThemeCompiler::includeComponent(

    "bitrix:socialnetwork.log.entry.mail",

    "",

    Array(

        "EMAIL_TO" => "{#EMAIL_TO#}",

        "LOG_ENTRY_ID" => "{#LOG_ENTRY_ID#}",

        "RECIPIENT_ID" => "{#RECIPIENT_ID#}",

        "URL" => "{#URL#}"

    )

);?>


```

```
<?EventMessageThemeCompiler::includeComponent(

    "bitrix:socialnetwork.log.entry.mail",

    "",

    Array(

        "COMMENT_ID" => "{#COMMENT_ID#}",

        "EMAIL_TO" => "{#EMAIL_TO#}",

        "LOG_ENTRY_ID" => "{#LOG_ENTRY_ID#}",

        "RECIPIENT_ID" => "{#RECIPIENT_ID#}",

        "URL" => "{#URL#}"

    )

);?>


```