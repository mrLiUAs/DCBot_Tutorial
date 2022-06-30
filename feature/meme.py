def getMeme():
    import os
    import requests
    from pathlib import Path
    import json
    import random

    res = requests.get(os.getenv("memeurl"))

    if res.ok:
        data = json.loads(res.text)
        return random.choice(data)['src']
    else:
        raise Exception('not ok')