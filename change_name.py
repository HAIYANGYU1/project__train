
from absl import app
from absl import flags
import glob
import os
from tqdm import tqdm


flags.DEFINE_string('dirname','C:/Users/yhyxx/Desktop/AI/hhh/','path')


def main(_):
    # print(f"name:{flags.FLAGS.dirname}")

    images = glob.glob(f'{flags.FLAGS.dirname}*.jpg')

    for index,img in tqdm(enumerate(images)):
        
        new_name = f'{flags.FLAGS.dirname}{index}.jpg'

        basename = os.path.basename(img)
        old_name = f'{flags.FLAGS.dirname}{basename}'

        try:
            os.rename(old_name, new_name)
        except:
            pass



if __name__ == '__main__':
    app.run(main)
    


