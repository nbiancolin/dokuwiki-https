# dokuwiki-https
 Python (pip) module to interface with dokuwiki over https (as opposed to XML-RPC)

get it on pypi!: https://pypi.org/project/dokuwiki-https/


## How to use:
1. log in to the wiki

```py
import dokuwiki-https as doku

#create a wiki object
wiki = doku.DokuWiki("https://myServer.com", "username", "password")

#call wiki.login() to get the login cookies
wiki.login()

#get page contents (returns one big string separated by '\n', exactly how it is on the web server)
content = wiki.getPage("myPage")

#write from an array of lines to a dokuwiki page (say the lines are in a list called lines)
content = ""
for line in lines:
    content += line

wiki.editPage("myPage", content)
```

Easy peasy right?

