# %% load modules

import json
import time
from pathlib import Path
from datetime import date
from dateutil.relativedelta import relativedelta
import openai
import pandas as pd
import random


pd.set_option(
    "display.max_rows",
    8,
    "display.max_columns",
    None,
    "display.width",
    None,
    "display.expand_frame_repr",
    True,
    "display.max_colwidth",
    None,
)

openai.api_key = "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"

# %%


# %%

# TODO: add remaining questions
questions = {
    "aries": (
        """give me today's horoscope for someone whose astrological sign is aries - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "taurus": (
        """give me today's horoscope for someone whose astrological sign is taurus - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "gemini": (
        """give me today's horoscope for someone whose astrological sign is gemini - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "cancer": (
        """give me today's horoscope for someone whose astrological sign is cancer - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "leo": (
        """give me today's horoscope for someone whose astrological sign is leo - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "virgo": (
        """give me today's horoscope for someone whose astrological sign is virgo - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "libra": (
        """give me today's horoscope for someone whose astrological sign is libra - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "scorpio": (
        """give me today's horoscope for someone whose astrological sign is scorpio - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "sagittarius": (
        """give me today's horoscope for someone whose astrological sign is sagittarius - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "capricorn": (
        """give me today's horoscope for someone whose astrological sign is capricorn - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "aquarius": (
        """give me today's horoscope for someone whose astrological sign is aquarius - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
    "pisces": (
        """give me today's horoscope for someone whose astrological sign is pisces - [should be easy to read, have minimum 300 words, short sentences of less than 20 words, mostly in active voice]"""
    ),
}


# %%

n_reps = 30
temperature = 1.0  # 0 to 2 (1 is default)

outputfile = Path("HOROSCOPEdata.json")
gpt_responses = {}
for rep in range(n_reps):
    print(f"Rep {rep + 1} of {n_reps}.")
    dateused = date.today() + relativedelta(days=+rep)
    print(dateused.strftime("%d%b%Y"))

    temp = {}
    for question in questions:

        messages = [
            {
                "role": "user",
                "content": questions[question],
            },
        ]

        chat_completion = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo", messages=messages, temperature=temperature
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=temperature,
        )
        response = chat_completion.choices[0].message.content

        temp[question] = response

        time.sleep(21)
    gpt_responses[dateused.strftime("%d%b%Y")] = temp

with open(outputfile, "a+") as f:
    f.write(json.dumps(gpt_responses))

# %%


n_reps = 30

outputfile = Path("YOGAlinks.json")
gpt_responses = {}
for rep in range(n_reps):
    print(f"Rep {rep + 1} of {n_reps}.")
    dateused = date.today() + relativedelta(days=+rep)
    print(dateused.strftime("%d%b%Y"))

    temp = {}
    for question in questions:

        temp[question] = (
            "https://lqd.buw.mybluehost.me/yoga-" + str(random.randint(1, 68)) + "/"
        )

    gpt_responses[dateused.strftime("%d%b%Y")] = temp

with open(outputfile, "a+") as f:
    f.write(json.dumps(gpt_responses))

# %%
