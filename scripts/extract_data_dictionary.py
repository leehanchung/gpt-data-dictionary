#!/usr/bin/env python
import os
import sys
from pathlib import Path

import fire
import openai
from dotenv import load_dotenv

try:
    from gpt_data import data_dictionary
except ImportError:
    sys.path.append(str(Path.cwd()))
    from gpt_data import data_dictionary


load_dotenv()


# Using Anyscale Endpoints
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_API_KEY")


def main(*, csv_file: str):
    df = data_dictionary(csv_file=csv_file)
    df.to_csv("data_dictionary.csv", index=False)


if __name__ == "__main__":
    fire.Fire(main)
