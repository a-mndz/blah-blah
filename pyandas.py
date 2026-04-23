# import pandas as pd

# my={
#     'cars':["BMW","Volvo","Ford"],
#     'passings':[3,7,2]
# }
# myvr=pd.DataFrame(my)
# print(myvr)

# import pandas as pd

# dat={
#     'calories':[460,380,320],
#     'duration':[60,42,46]
# }
# df=pd.DataFrame(dat)
# print(df)

# print(df.loc[1])

import pandas as pd
data={
    'name': ["Arun", "Neha", "Rahul", "Sneha", "Vikram", "Anjali", "Kiran", "Meera", "Rohit", "Divya"],
    'marks': [85, 92, 78, 88, 95, 80, 90, 82, 91, 87]
}
df=pd.DataFrame(data)
print(df)

print(df.loc[[1,7]])