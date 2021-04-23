import argparse

from demo_class import Demo
import tensorflow as tf

def get_parser():
    parser = argparse.ArgumentParser(description="Solar Radiation Forecasting Demo")
    parser.add_argument(
        "--models_path",
        default="models",
        help="Path with the models files."
    )
    parser.add_argument(
        "--daily_folder_name",
        default="daily_forecasting",
        help="Folder name where are saved the .json and .h5 model files for daily forecasting."
    )
    parser.add_argument(
        "--weekly_folder_name",
        default="weekly_forecasting",
        help="Folder name where are saved the .json and .h5 model files for weekly forecasting."
    )
    parser.add_argument(
        "--data_path",
        default="data/GHI_sa.csv",
        help="Path where are saved the dataset."
    )
    parser.add_argument(
        "--mode",
        default="daily_forecasting",
        help="Mode to use (daily_forecasting, weekly_forecasting)."
    )
    parser.add_argument(
        "--day_or_week",
        default=1416,
        help="Day or week to forecasting. (day * 24 hours), (week * 672 hours)"
    )
    return parser


if __name__ == "__main__":
    args = get_parser().parse_args()
    
    gpu = tf.config.list_physical_devices('GPU')[0]
    try:
        tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpu), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        print(e)
    
    demo = Demo(mode=args.mode,
                models_path=args.models_path,
                data_path=args.data_path,
                day_or_week=int(args.day_or_week))
    demo.run()
