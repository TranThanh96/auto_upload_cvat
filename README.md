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
python cli.py --auth username:password --server-host camera.cvat.bigdataz.dev --https create --labels label.json --resource_type local --dir temp/ --assignee 3 --name temp
~~~

## Dump annotation
Liệt kê toàn bộ các task cần dump annotation theo từng dòng trong file list_name_download.txt

~~~
python auto_download.py list_name_download.txt username:password
~~~

Toàn bộ file xml sẽ được lưu theo tên task trong folder download

## Delete task
Updating...

## Update annotation
Updating...