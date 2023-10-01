from utils import parse_args, create_experiment_dirs, calculate_flops
from model import MobileNet
from backend.app.mobileNet.train3 import Train
from data_loader import DataLoader
from summarizer import Summarizer
import tensorflow as tf


def main():
    
    config_args = {
        "experiment_dir": "test_experiment",
        "num_epochs": 2,
        "num_classes": 2,
        "batch_size": 10,
        "width_multiplier": 1.0,
        "shuffle": True,
        "l2_strength": 4e-5,
        "bias": 0.0,
        "learning_rate": 1e-3,
        "batchnorm_enabled": True,
        "dropout_keep_prob": 0.999,
        "pretrained_path": "pretrained_weights/mobilenet_v1.pkl",
        "max_to_keep": 4,
        "save_model_every": 5,
        "test_every": 5,
        "to_train": False,
        "to_test": True
        }


    _, config_args.summary_dir, config_args.checkpoint_dir = create_experiment_dirs(config_args.experiment_dir)

    tf.reset_default_graph()
    config = tf.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

    data = DataLoader(config_args.batch_size, config_args.shuffle)
    config_args.img_height, config_args.img_width, config_args.num_channels, \
    config_args.train_data_size, config_args.test_data_size = data.load_data()
    model = MobileNet(config_args)

    summarizer = Summarizer(sess, config_args.summary_dir)
    trainer = Train(sess, model, data, summarizer)

    if config_args.to_train:
        trainer.train()

    if config_args.to_test:
        trainer.test('val')
