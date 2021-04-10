import pandas as pd
import matplotlib.pyplot  as plt 

def timestamp():
    days = (
        max(users["memberSince"].max(), messages["sendDate"].max(), discussions["createDate"].max(), discussion_posts["createDate"].max()) - 
    
        min(users["memberSince"].min(), messages["sendDate"].min(), discussions["createDate"].min(), discussion_posts["createDate"].min())
    
        )  // to_days
    
    return days

users = pd.read_csv('traders/users.tsv', sep="\t")
messages = pd.read_csv('traders/messages.tsv', sep="\t")
discussions = pd.read_csv('traders/discussions.tsv', sep="\t")
discussion_posts = pd.read_csv('traders/discussion_posts.tsv', sep="\t")

to_days = (1000*60*60*24)

# If we need to convert each column to days right at the start
# users["memberSince"] = users["memberSince"] / to_milliseconds
# messages["sendDate"] = messages["sendDate"] / to_milliseconds
# discussions["createDate"] = discussions["createDate"] / to_milliseconds
# discussion_posts["createDate"] = discussion_posts["createDate"] / to_milliseconds

print(f"The number of users in the database is: {len(users)}")

print(f"The estimated time span of the database is: {timestamp()} days")

print(f"The estimated time span of the database is: {len(discussions)} days")

message_sizes = [len(users["memberSince"]), len(messages["sendDate"]), len(discussions["createDate"]), len(discussion_posts["createDate"])]

plt.pie(message_sizes)

plt.show()