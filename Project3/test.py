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


# Deliverables
print(f"The number of users in the database is: {len(users)}")

print(f"The estimated time span of the database is: {timestamp()} days")

print(f"The estimated time span of the database is: {len(discussions)} days")

# Plots the size of each type
plot1 = plt.figure(1)
plt.pie(messages.groupby("type").size(), labels=("Friend Link Request","Direct Message"))
plt.title("Messages Based on Type")


plot2 = plt.figure(2) # figsize=(20,8)
plt.pie(discussions.groupby("discussionCategory").size().sort_values(0))
plt.title("Message Range")
plt.legend(discussions.groupby("discussionCategory").size().sort_values(0).index)

print(f"The number of discussion posts: {discussion_posts['id'].sum()}")


plot3 = plt.figure(3)
plt.hist( (messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min()) //86400000, 10, log=True )
plt.title("Message Range")
plt.xlabel("Activity Range (in days)")
plt.ylabel("Number of Users")

a = pd.merge(users, messages.groupby(["type", "sender_id"]).min(), left_on="id", right_on='sender_id') # attempt on 3
b = (pd.merge(users, messages, left_on="id", right_on='sender_id').groupby(["type", "sender_id"]).min()).reset_index()# attempt on 3

b["delay"] = (b["sendDate"] - b["memberSince"]) // 86400000

plot = plt.figure(4)
to_plot = [b[b["type"]== "FRIEND_LINK_REQUEST"]["delay"], b[b["type"]== "DIRECT_MESSAGE"]["delay"]]
plt.hist(to_plot, color = ["red", "skyblue"], log=True)
plt.title("Delay Times")
plt.xlabel("Delay Time (in days)")
plt.ylabel("Number of Users")
plt.legend(["Friend Link Request", "Direct Message"])




# plt.hist(b[b["type"]== "FRIEND_LINK_REQUEST"]["delay"], color = "red", log=True)
# plt.hist(b[b["type"]== "DIRECT_MESSAGE"]["delay"], color = "skyblue", log=True)



# delay_plot = plt.hist(b["delay"], b["delay"])





plt.show()

messages.groupby("sender_id").sendDate.max() - messages.groupby("sender_id").sendDate.min()




# If we need to convert each column to days right at the start
# users["memberSince"] = users["memberSince"] / to_milliseconds
# messages["sendDate"] = messages["sendDate"] / to_milliseconds
# discussions["createDate"] = discussions["createDate"] / to_milliseconds
# discussion_posts["createDate"] = discussion_posts["createDate"] / to_milliseconds

