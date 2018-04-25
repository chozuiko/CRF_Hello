import deepnlp
# Download all the modules
deepnlp.download()

# Download specific module
deepnlp.download('segment')
deepnlp.download('pos')
deepnlp.download('ner')
deepnlp.download('parse')

# Download module and domain-specific model
deepnlp.download(module = 'pos', name = 'en')
deepnlp.download(module = 'ner', name = 'zh_entertainment')