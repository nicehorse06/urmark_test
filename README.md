2.請問依序列印 list 1-3 結果是如何？為何？ ( Python 3 ) :
```
def add_val_to_list (val, list=[]):  
	list.append(val)
	return list

list1 = add_val_to_list( 321 )
list2 = add_val_to_list( 123 ,[])
list3 = add_val_to_list( 'a' )
```

3.請說明造成以下兩者輸出的差異原因？若輸入值維持不變讓Python輸出的結果和PHP一致你會如何修改（Python 3）？

PHP
```
$input = ['banana' => 1, 'apple' => 2, 'orange' => 3];
echo json_encode($input);
```
Python

```
import json
input = {'banana': 1, 'apple': 2, 'orange': 3}
print(json.dumps(input))
```
