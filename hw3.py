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
top_home_goals = frame.groupby(["Home Team Initials"], as_index=True).sum().reset_index().sort_values(by="Home Team Goals", ignore_index=True, ascending=False)
sb.barplot(x=top_home_goals["Home Team Initials"][0:5], y=top_home_goals["Home Team Goals"][0:5])
plt.show()

#Q6 I think I was using count instead of sum and also tried to use groupby twice?
top5_away_goals = top_home_goals[0:5]
jp.joyplot(data=top5_away_goals, column=["Home Team Goals", "Away Team Goals"], by="Home Team Initials", legend=True, figsize=(7, 7), ylim="own")
plt.show()

#Q7

plt.style.use("ggplot")
pplot(data=top5_away_goals, x="Home Team Goals", y="Away Team Goals", kind = 'qq', display_kws={"identity":True}, height=4, aspect=2)
plt.show()
