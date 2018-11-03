%name length
names = KSdata.name;
namelength = zeros(size(names));
for(i = 1:size(names,1))
namelength(i) = strlength(names(i));
end
subplot(1,3,1); scatter(namelength,KSdata.backers,'r.');
subplot(1,3,2); scatter(namelength,KSdata.usdpledged,'r.');
subplot(1,3,3); scatter(namelength,KSdata.usd_goal_real,'r.');

% avg word length
avgwordlength = zeros(size(names));
for(i = 1:size(names,1))
name = names(i);
split = strsplit(name);
lengths = strlength(split);
avglength = mean(lengths);
avgwordlength(i) = avglength;
end
figure(2);
subplot(1,3,1); scatter(avgwordlength,KSdata.backers,'b.');
subplot(1,3,2); scatter(avgwordlength,KSdata.usdpledged,'b.');
subplot(1,3,3); scatter(avgwordlength,KSdata.usd_goal_real,'b.');