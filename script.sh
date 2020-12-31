# for i in {1..100}
# do

# echo bpo_autopilot_us_$(printf "%04d" $i)
# echo $(( 9 + (($i - 1) / 5 )))
i=100
python cli.py \
--auth moderator:\#Cvat@1920 \
--server-host camera.cvat.bigdataz.dev \
--https create \
--labels label_us.json \
--resource_type local \
--dir /media/workstation/Smart_Camera/annotation_images/US/bpo/bpo_autopilot_us_$(printf "%04d" $i) \
--assignee $(( 9 + (($i - 1) / 5 ))) \
--name bpo_autopilot_us_$(printf "%04d" $i) \
--annotation_path /media/workstation/Smart_Camera/auto_upload_cvat/lightsign/US/bpo_autopilot_us_$(printf "%04d" $i).xml
# done
