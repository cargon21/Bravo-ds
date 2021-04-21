# All files are TAB-separated. All times in the tables are expressed in milliseconds, starting on midnight, January 1, 1970. You shall convert the times to days (24hr).

# You shall produce the following deliverables:
    # Simple descriptive statistics:
    # 1. How many users are in the database? 
        # Deliverable: A number. 
    # 2. What is the time span of the database? 
        # Deliverable: The difference between the largest and the smallest timestamps in the database, a number. 
    # 3. How many messages of each type have been sent? 
        # Deliverable: A pie chart. 
    # 4. How many discussions of each type have been started? 
        # Deliverable: A pie chart. 
    # 5. How many discussion posts have been posted? 
        # Deliverable: A number.
    # 6. Activity range is the time between the first and the last message (in ANY category) sent by the same user. 
    # 7. What is the distribution of activity ranges? 
        # Deliverable: a histogram. 
    # 8. Message activity delay is the time between user account creation and sending the first user message in a specific category. What is the distribution of message activity delays in EACH category? 
        # Deliverable: a histogram for each category (ideally all histograms shall be in the same chart, semi-transparent, with legend).
    # What is the distribution of discussion categories by the number of posts? What is the most popular category? 
        # Deliverable: a pie chart, with the most popular category highlighted.
    # Post activity delay is the time between user account creation and posting the first discussion message. What is the distribution of post activity delays in the most popular category? 
        # Deliverable: a histogram. Note: The most popular category shall be carried over from the previous question.
    # A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.
    # Finally, you shall write a short report that summarizes your findings in plain English language (for someone who knows neither CS nor Stats).
    # You shall be able to produce all deliverables in one program by applying appropriate transformations to one  DataFrame, assembled from the four tabular files (however, two- and three-way merges shall work, too).  The Y axis of all histograms shall be on the logarithmic scale.

import pandas as pd
import matplotlib.pyplot  as plt 

def timestamp():
    to_days = (1000*60*60*24)
    days = (
        max(users["memberSince"].max(), messages["sendDate"].max(), discussions["createDate"].max(), discussion_posts["createDate"].max()) - 
    
        min(users["memberSince"].min(), messages["sendDate"].min(), discussions["createDate"].min(), discussion_posts["createDate"].min())
    
        )  // to_days
    
    return days

users = pd.read_csv('traders/users.tsv', sep="\t")
messages = pd.read_csv('traders/messages.tsv', sep="\t")
discussions = pd.read_csv('traders/discussions.tsv', sep="\t")
discussion_posts = pd.read_csv('traders/discussion_posts.tsv', sep="\t")


# If we need to convert each column to days right at the start
# users["memberSince"] = users["memberSince"] / to_milliseconds
# messages["sendDate"] = messages["sendDate"] / to_milliseconds
# discussions["createDate"] = discussions["createDate"] / to_milliseconds
# discussion_posts["createDate"] = discussion_posts["createDate"] / to_milliseconds

print(f"The number of users in the database is: {len(users)}")

print(f"The estimated time span of the database is: {timestamp()} days")

print(f"The estimated time span of the database is: {len(discussions)} days")

plot1 = plt.figure(1)
m_plot = plt.pie(messages.groupby("type").size())

plot2 = plt.figure(2)
d_plot = plt.pie(discussions.groupby("discussionCategory").size())

print(f"The number of discussion posts: {discussion_posts['id'].sum()}")

plot3 = plt.figure(3)
h_plot = plt.hist( messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min(), 8)

a = pd.merge(users, messages.groupby(["sender_id", "type"]).min(), left_on="id", right_on='sender_id') # attempt on 3
b = pd.merge(users, messages, left_on="id", right_on='sender_id').groupby(["sender_id", "type"]).min() # attempt on 3

b["delay"] = b["sendDate"] - b["memberSince"]



plt.show()

messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min()




