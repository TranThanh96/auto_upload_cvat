# CVat auo upload task, dump annotations ...

## Mapping task's name to task's ID
Lấy thông tin toàn bộ các task trên server CVAT (task name và task ID), lưu vào file lookup_table_name.json (file này sẽ được sử dụng để mapping giữa task name và task ID)
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https ls
~~~

## Create task
**Note**: Mới test khi upload local!

Tạo task và upload ảnh lên server. Một số tham số cần lưu ý:

* --label: đường dẫn đến file label json theo định dạng cvat
* --dir: Đường dẫn đến thư mục chứa ảnh cần gán nhãn
* --assignee: id assignee theo danh sách các user trên cvat tính từ 1 (mặc định un-assign)
* --name: tên task, nếu không cung cấp, tên task tự động lấy theo tên folder

~~~
python cli.py --auth moderator:#Cvat@1920 --server-host camera.cvat.bigdataz.dev --https create --labels label.json --resource_type local --dir temp/ --assignee 3 --name temp --annotation_path a.xml
~~~

## Dump annotation
Liệt kê toàn bộ các task cần dump annotation theo từng dòng trong file list_name_download.txt

update danh sách các task và ID tương ứng:
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https ls
~~~

Dump annotation, Toàn bộ file xml sẽ được lưu theo tên task trong folder download
~~~
python auto_download.py list_name_download.txt username:password
~~~


## Delete task
Liệt kê toàn bộ các task cần delete theo từng dòng trong file list_name_delete.txt

update danh sách các task và ID tương ứng:
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https ls
~~~

delete toàn bộ task được liệt kê trong list_name_delete.txt
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https delete --file_list_task_name list_name_delete.txt 
~~~

## Update label
Liệt kê toàn bộ các task cần update label theo từng dòng trong file list_name_update.txt

update danh sách các task và ID tương ứng:
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https ls
~~~

Dump label cho toàn bộ task được liệt kê trong list_name_update.txt
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https update_label --labels label.json --file_list_task_name list_name_update.txt 
~~~

## update annotation
Tạo folder chứa toàn bộ các file xml trùng tên với tên task cần upload.

update danh sách các task và ID tương ứng:
~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https ls
~~~

upload xml

~~~
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https update_anno --dir ./temp
~~~

