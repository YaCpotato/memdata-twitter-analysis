import streamlit as st
import numpy as np
import pandas as pd

data = pd.read_csv('./data/tweet_activity_metrics_yassh_i_20200829_20200926_en.csv')

data.head()