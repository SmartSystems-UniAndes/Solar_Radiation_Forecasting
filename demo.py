from demo_class import Demo

model_path = "models"
daily_folder = "daily_forecasting"
weekly_folder = "weekly_forecasting"

data_path = "data/GHI_sa.csv"

if __name__ == "__main__":
    demo = Demo(mode="weekly_forecasting",
                models_path=model_path,
                data_path=data_path,
                day_or_week=672*34)
    demo.run()
