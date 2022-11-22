from absl import app
from absl import flags

import flags_b;

FLAGS = flags.FLAGS

flags.DEFINE_string('name','Jerry','Your name')


def main(_):
    print(f"name:{FLAGS.name}")
    print(f"salary:{FLAGS.salary}")
    


if __name__ == '__main__':
    app.run(main)