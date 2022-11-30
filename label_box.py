import json
from absl import flags
from absl import app
import cv2


# flags.mark_flag_as_required('model_dir')
flags.DEFINE_string('jsonname',None,'image_path')
flags.DEFINE_string('imgname',None,'image_path')


def main(_):
    with open(flags.FLAGS.jsonname) as f:
        json_file = json.load(f)
    img = cv2.imread(flags.FLAGS.imgname)
    
    for n in json_file["shapes"]:

        left,right = n["points"]
        left = (int(left[0]),int(left[1]))
        right = (int(right[0]),int(right[1]))
        
        cv2.rectangle(img,left,right,(0,255,0),thickness=2)

        x,y = left
        x = x 
        y = y - 10

        label_name = n["label"]
        cv2.putText(img,label_name,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),thickness=1)



    cv2.imshow('a',img)
    cv2.waitKey(0)

if __name__ == '__main__':
    app.run(main)