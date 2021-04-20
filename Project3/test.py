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




