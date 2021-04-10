# Programmers: Jordan DeGiacomo & Carson Synter
# Last DOM: 4/19/2021
# Course: CMPSC-310
# File name: chattingTraders.py

import pandas as pd

users = pd.read_csv('traders/users.tsv', sep= '\t') #
messages = pd.read_csv('traders/messages.tsv', sep= '\t')
discussions = pd.read_csv('traders/discussions.tsv', sep= '\t')
discussion_posts = pd.read_csv('traders/discussion_posts.tsv', sep= '\t')
