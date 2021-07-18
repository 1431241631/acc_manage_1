# import os
# import json
#
#
# def T(path):
#     paths = os.listdir(path)
#     for item in paths:
#         json_data = ''
#         with open(os.path.join(path, item), 'r', encoding='utf-8') as f:
#             data = f.read()
#             json_ = json.loads(data)
#             label = json_['text']
#             json_['text'] = label.replace('*', '-')
#             json_data = json_
#         with open(os.path.join(path, item), 'w', encoding='utf-8') as f:
#             f.write(json.dumps(json_data,ensure_ascii=False))
#
#
# T(r'C:\Users\14312\Desktop\data1')
