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
    # 9. What is the distribution of discussion categories by the number of posts? What is the most popular category? 
        # Deliverable: a pie chart, with the most popular category highlighted.
    # 10. Post activity delay is the time between user account creation and posting the first discussion message. What is the distribution of post activity delays in the most popular category? 
        # Deliverable: a histogram. Note: The most popular category shall be carried over from the previous question.
    # A box plot with whiskers that shows all appropriate statistics for message activity delays in EACH category, post activity delays, and activity ranges.
    # Finally, you shall write a short report that summarizes your findings in plain English language (for someone who knows neither CS nor Stats).
    # You shall be able to produce all deliverables in one program by applying appropriate transformations to one  DataFrame, assembled from the four tabular files (however, two- and three-way merges shall work, too).  The Y axis of all histograms shall be on the logarithmic scale.

import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

# Calculates the timestamp of the dataframe
def timestamp():
    to_days = (86400000) # 1000*60*60*24
    days = (
        max(users["memberSince"].max(), messages["sendDate"].max(), discussions["createDate"].max(), discussion_posts["createDate"].max()) - 
    
        min(users["memberSince"].min(), messages["sendDate"].min(), discussions["createDate"].min(), discussion_posts["createDate"].min())
    
        )  // to_days
    
    return days

# Open the data sets
users = pd.read_csv('traders/users.tsv', sep="\t")
messages = pd.read_csv('traders/messages.tsv', sep="\t")
discussions = pd.read_csv('traders/discussions.tsv', sep="\t")
discussion_posts = pd.read_csv('traders/discussion_posts.tsv', sep="\t")


# Deliverables (number of users, time span of the data base)
print(f"The number of users in the database is: {len(users)}")

print(f"The estimated time span of the database is: {timestamp()} days")

print(f"The number of discussion posts is: {len(discussion_posts)} days")

# Pie chart of message type
plot1 = plt.figure(1)
plt.pie(messages.groupby("type").size(), labels=("Friend Link Request","Direct Message"))
plt.title("Messages Based on Type")

# Pie chart of message range
plot2 = plt.figure(2) # figsize=(20,8)
plt.pie(discussions.groupby("discussionCategory").size().sort_values(0))
plt.title("Message Range")
plt.legend(discussions.groupby("discussionCategory").size().sort_values(0).index)

print(f"The number of discussion posts: {discussion_posts['id'].sum()}")

# Difference between first and last message
plot3 = plt.figure(3)
plt.hist( (messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min()) //86400000, 10, log=True )
plt.title("Message Range")
plt.xlabel("Activity Range (in days)")
plt.ylabel("Number of Users")

# Merging message and user data
activity_range = (pd.merge(users, messages, left_on="id", right_on='sender_id').groupby(["type", "sender_id"]).min()).reset_index() # attempt on 3

# Difference between account creation and activity
activity_range["delay"] = (activity_range["sendDate"] - activity_range["memberSince"]) // 86400000

# Plot friend link request and direct message delay
plot4 = plt.figure(4)
to_plot = [activity_range[activity_range["type"]== "FRIEND_LINK_REQUEST"]["delay"], activity_range[activity_range["type"]== "DIRECT_MESSAGE"]["delay"]]
plt.hist(to_plot, color = ["red", "skyblue"], log=True)
plt.title("Delay Times")
plt.xlabel("Delay Time (in days)")
plt.ylabel("Number of Users")
plt.legend(["Friend Link Request", "Direct Message"])

# Discussion categories
plot5 = plt.figure(5)
posts_w_category = pd.merge(discussion_posts, discussions, left_on= 'discussion_id', right_on= 'id').groupby('discussionCategory').size()
explode = [0] * len(posts_w_category)
explode[-1] = 0.1
plt.pie(posts_w_category.sort_values(), explode = tuple(explode))
plt.legend(posts_w_category.sort_values().index)


# 5: Ativity delay in most popular category
most_pop_cat = posts_w_category.sort_values().index[-1]
post_delay = pd.merge(users, discussion_posts, left_on="id", right_on='creator_id').groupby("id_x").min().reset_index()
post_delay["delay"] = (post_delay["createDate"] - post_delay["memberSince"]) // 86400000 # 1000*60*60*24
post_delay = post_delay.drop(columns=["memberSince", "id_y", "createDate", "creator_id"])

most_pop_disc = pd.merge(discussion_posts, discussions, left_on= 'discussion_id', right_on= 'id')
most_pop_disc = (most_pop_disc[most_pop_disc["discussionCategory"] == most_pop_cat])[["discussion_id", "discussionCategory"]]

# delay_w_category = pd.merge(most_pop_disc, post_delay, left_on='discussion_id', right_on='discussion_id')

delay_w_category = pd.merge(most_pop_disc, post_delay, left_on= 'discussion_id', right_on= 'discussion_id').groupby("id_x").first()
# delay_to_plot = [delay_w_category[], delay_w_category["delay"]

# plot4 = plt.figure(6)
# plt.hist(delay_w_category, log=True)
# plt.title("Activity Range")
# plt.xlabel("Delay Time (in days)")
# plt.ylabel("Number of Users")
# plt.legend(["Friend Link Request", "Direct Message"])

# plt.hist(b[b["type"]== "FRIEND_LINK_REQUEST"]["delay"], color = "red", log=True)
# plt.hist(b[b["type"]== "DIRECT_MESSAGE"]["delay"], color = "skyblue", log=True)

# delay_plot = plt.hist(b["delay"], b["delay"])



# messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min()


# If we need to convert each column to days right at the start
# users["memberSince"] = users["memberSince"] / to_milliseconds
# messages["sendDate"] = messages["sendDate"] / to_milliseconds
# discussions["createDate"] = discussions["createDate"] / to_milliseconds
# discussion_posts["createDate"] = discussion_posts["createDate"] / to_milliseconds

plt.show()
