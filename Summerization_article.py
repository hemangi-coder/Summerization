import pycurl, json
import io

def summerize_by_paste_article(text,summary_length,title):
    b_obj = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'https://api.agolo.com/nlp/v0.2/summarize')
    c.setopt(pycurl.HTTPHEADER,
             ['Content-Type:application/json', 'Ocp-Apim-Subscription-Key: 2f56b03810534f6885d376164e232b18'])
    data = json.dumps(
        {
            "summary_length": summary_length,
            "articles": [
                {
                    "text":text,
                    "title": title,
        "metadata": {
         "id": "PostmanAPIPortalProxyText2", "key2": "value2",
        "key3": ["value3_1", "value3_2"]}
    }
    ]}
    )
    c.setopt(pycurl.POST, 1)
    c.setopt(c.WRITEDATA, b_obj)
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.SSL_VERIFYHOST, 0)
    c.perform()
    dict_str = json.loads(b_obj.getvalue().decode("UTF-8"))
    #print(dict_str['title'])
    #l = dict_str['summary'][0]['sentences']
    #for i in l:
    #    print(i)
    c.close()
    return dict_str
