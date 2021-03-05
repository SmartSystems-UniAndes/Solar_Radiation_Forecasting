import argparse

from demo_class import Demo


def get_parser():
    parser = argparse.ArgumentParser(description="Fault classification for PV panels Demo")
    parser.add_argument(
        "--models_path",
        default="models",
        help="Path with the models files (must contain for daily and for weekly forecasting."
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

    demo = Demo(mode=args.mode,
                models_path=args.models_path,
                data_path=args.data_path,
                day_or_week=int(args.day_or_week))
    demo.run()
