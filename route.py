from eve import eve

app = Eve()


if __name__ == '__main__':
    app.run()
{
    "_info": {
        "server": "Eve",
        "version": "a.b.c",
        "api_version": "x.y.z"
    },
    "_links": {
        "child": [
            {
                "href": "people",
                "title": "people"
            }
        ]
    }
}
