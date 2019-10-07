'''
3.請說明造成以下兩者輸出的差異原因？
若輸入值維持不變讓Python輸出的結果和PHP一致你會如何修改（Python 3）？
'''
import json

input = {'banana': 1, 'apple': 2, 'orange': 3}

'''
PHP code:
$input = ['banana' => 1, 'apple' => 2, 'orange' => 3];
echo json_encode($input);

輸出結果為:
{"banana":1,"apple":2,"orange":3}
'''
print('PHP code的輸出:')
print('{"banana":1,"apple":2,"orange":3}')

'''
題目 Python code的輸出結果為:
{"banana": 1, "apple": 2, "orange": 3}
'''
print('原本Python code的輸出:')
print(json.dumps(input))

'''
答案 Python code的輸出結果為:
{"banana":1,"apple":2,"orange":3}
因為json.dumps在處理dic時會在key和value多一個" "空格
把', "'取代',"' 去除key的空格
把": "用":" 去除value的空格
'''
print('我的Python做法:')
print(json.dumps(input).replace(', "', ',"').replace('": ', '":'))
