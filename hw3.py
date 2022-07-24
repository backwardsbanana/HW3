from seaborn_qqplot import pplot
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
import joypy as jp

frame = pd.read_csv("WorldCupMatches.csv")

#Q2
goals_by_year = frame[["Year", "Home Team Goals"]].copy()
sb.displot(goals_by_year, x="Home Team Goals", hue="Year", kind="kde").set(xlim=(0, 12))
plt.show()

#Q3
plt.figure(figsize=(10, 5))
sb.violinplot(data=goals_by_year, x="Year", y="Home Team Goals").set(ylim=(0))
ax = plt.gca()
for i in ax.get_xticks():
	if i % 2 == 0:
		ax.xaxis.get_ticklabels()[i].set_visible(False)
plt.show()

#Q4
goals_by_year_both_teams = frame[["Year", "Home Team Goals", "Away Team Goals"]].copy()
plt.style.use("seaborn-white")
jp.joyplot(goals_by_year_both_teams, by="Year", legend=True, figsize=(7, 7), ylim="own")
plt.show()

#Q5
top5_home_goals = frame.groupby(["Home Team Initials"])["Home Team Goals"].count().reset_index().sort_values(by="Home Team Goals", ascending=False, ignore_index=True)[0:5]
sb.barplot(x=top5_home_goals["Home Team Initials"], y=top5_home_goals["Home Team Goals"])
plt.show()

#Q6 Cant get groupby to work for finding the Away Team Goals

top5_away_goals = frame.groupby(["Home Team Initials"])["Away Team Goals"].count().reset_index().sort_values(by="Away Team Goals", ascending=False, ignore_index=True)[0:5]
#plt.style.use("dark_background")

#jp.joyplot(data=NOTHING_HERE, column=["Home Team Goals", "Away Team Goals"], by="Home Team Initials", legend=True, figsize=(7, 7), ylim="own")
#plt.show()

#Q7

#plt.style.use("ggplot")
#pplot(data=NOTHING_HERE, x="Home Team Goals", y="Away Team Goals", kind = 'qq', display_kws={"identity":True}, height=4, aspect=2)
#plt.show()