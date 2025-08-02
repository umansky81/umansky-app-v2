import streamlit as st
import pandas as pd
import os
import requests

st.write("Loaded API Key:", os.getenv("OPENWEATHER_API_KEY"))

