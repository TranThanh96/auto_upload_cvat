for i in {58..71}
do

echo autopilot_00$i >> list_name_delete.txt
#python cli.py \
#--auth moderator:\#Cvat@1920 \
#--server-host camera.cvat.bigdataz.dev \
#--https delete \
#--name autopilot_00$i

done
