|  |  |  |
| --- |

| --- |
| **Поле** |

| **Описание** |
| Email получателя |

| Указывается email получателя сообщения. |
| ID получателя |

| Указывается идентификатор пользователя-получателя сообщения (почтового пользователя). |
| ID сообщения |

| Указывается идентификатор сообщения блога. |
| ID комментария |

| Указывается идентификатор комментария к сообщению блога. |
| URL сообщения |

```
<?EventMessageThemeCompiler::includeComponent(

    "bitrix:socialnetwork.blog.post.comment.mail",

    "",

    Array(

        "COMMENT_ID" => "{#COMMENT_ID#}",

        "EMAIL_TO" => "{#EMAIL_TO#}",

        "POST_ID" => "{#POST_ID#}",

        "RECIPIENT_ID" => "{#RECIPIENT_ID#}",

        "URL" => "{#URL#}"

    )

);?>


```