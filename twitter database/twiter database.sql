# create new database
drop database if exists twitter;
create database if not exists twitter;
use twitter;

# create users table
drop table if exists users;
create table users (
  user_id int unique not null,
  twitter_handle varchar(15) unique not null, #limited to 15 characters as that is the average username length
  full_name varchar(50) not null, #limited to 50 characters according to average max name length on twitter
  email varchar(320) unique not null, # limited to 320 characters, including domain name after the @
  user_password varchar(12) not null, # limited to 12 characters as that is the common average max length
  short_profile varchar(255), # limited to 12 as per given instructions
  hidden tinyint not null, 
  primary key (user_id)
);

# create tweet table
drop table if exists tweet;
create table tweet (
  tweet_id int unique not null,
  user_id int not null,
  tweet_timestamp datetime not null, 
  tweet_text varchar(160) not null, # limited to 160 according to instructions
  foreign key (user_id) references users(user_id),
  primary key (tweet_id)
);

# create hashtag table
drop table if exists hashtag;
create table hashtag (
hashtag_id int unique not null,
hastag_text varchar(160) unique not null, # limited to 160 as that is the max length of a tweet (includes the # symbol)
primary key (hashtag_id)
);

# create followers joint table where users follow users
drop table if exists follower;
create table follower (
    follower_id int not null,
    followee_id int not null,
    foreign key (follower_id) references users(user_id), # both followers and followees are users
    foreign key (followee_id) references users(user_id)
);


# create hashtag_in_tweet joint table
drop table if exists hashtag_in_tweet;
create table hashtag_in_tweet (
    tweet_id int not null,
    hashtag_id int not null,
    foreign key (tweet_id) references tweet(tweet_id),
    foreign key(hashtag_id) references hashtag(hashtag_id)
);


# create likes joint table where user likes tweet
drop table if exists likes;
create table likes (
    user_id int not null,
    tweet_id int not null,
    foreign key (user_id) references users(user_id),
    foreign key (tweet_id) references tweet(tweet_id)
);

# populate all tables
Insert into users values
(1,'@workdayfrog17','frog','day.f@ortheastern.edu','fastrabbit71','frog enthusiast',1),
(2,'@swolesister','James Charles','james.charl@gmail.com','securepwd','<3', 0),
(3,'@mahimahi','Bob Singh','bobthesingher@gmail.com','1234pass',NULL,1),
(4,'@rucheezy','ruchi swan','ruchi.s12@gmail.com','pwdpwd','art and design',0),
(5,'@yankers','Yan Kohers','kohersyan321@gmail.com','1234pass','husky at heart',0);

INSERT INTO tweet (tweet_id, user_id, tweet_timestamp, tweet_text) VALUES
(1, 2, NOW(), 'just got a new #NEU water bottle, hydration is key! #water #health'),
(2, 4, NOW(), 'Citrus is a great source of Vitamin C #vitamins #health'),
(3, 5, NOW(), 'Proud to announce that I have committed to Northeastern University! #NEU'),
(4, 3, NOW(), 'this #weekend was like a movie #NEU'),
(5, 2, NOW(), 'my #water bottle broke #lol'),
(6, 2, NOW(), '#NEU just sent me a new one! #thanks'),
(7, 2, NOW(), 'water bottle review will drop soon, stay tuned! #thanks #NEU'),
(8, 2, NOW(), 'love the fact that is has the #NEU husky on it!'),
(9, 2, NOW(), 'I dropped my water bottle down the stairs :|');

insert into hashtag values
(1,'#vitamins'),
(2,'#NEU'),
(3,'#water'),
(4,'#weekend'),
(5,'#lol'),
(6, '#thanks'),
(7, '#health');

insert into follower(follower_id, followee_id) values
(4,3),
(3,4),
(4,2),
(3,2),
(1,2),
(5,2),
(5,3),
(5,4),
(4,5);

insert into hashtag_in_tweet values
(1,2),
(1,3),
(1,7),
(2,1),
(2,7),
(3,2),
(4,4),
(4,2),
(5,3),
(5,5),
(6,2),
(6,6),
(7,2),
(7,6),
(8,2);

insert into likes values
(1,1),
(2,1),
(4,1),
(5,2),
(3,2),
(5,3),
(4,3),
(1,5),
(2,5),
(3,5),
(4,5),
(5,5);

#PART C DATABASE VALIDATION
# a) Which user has the most followers? Output just the user_id of that user, and the number of followers.
select followee_id, count(*) as num_followers
from follower
group by followee_id
order by num_followers desc
limit 1;

# b) For one user, list the five most recent tweets by that user, from newest to oldest. Include only tweets containing the hashtag “#NEU”
select tweet_id, user_id, tweet_timestamp, tweet_text
from tweet
where user_id = 2 and tweet_text like '%#NEU%'
order by tweet_timestamp desc
limit 5;

# c) What are the most popular hashtags? Sort from most popular to least popular. Output the hashtag_id, and the number of times that 
# hashtag was used in a tweet. (It is not necessary to display the hashtag name. Doing so without join syntax is possible but requires 
# a subquery and an implicit join.) Rank your output by number of times each hashtag is used in descending order.
select hashtag_id, count(hashtag_id) AS num_hashtags
FROM hashtag_in_tweet
GROUP BY hashtag_id
ORDER BY num_hashtags DESC;

# d) How many tweets have exactly 1 hashtag? Your query output should be a single number.
SELECT count(tweet_id) as one_hashtag_tweets
from (
  select tweet_id, count(tweet_id) as num_tweets
  from hashtag_in_tweet
  group by tweet_id
) as hashtag_count
where num_tweets = 1;

# e) What is the most liked tweet? Output the tweet attributes.
select tweet_id, user_id, tweet_timestamp, tweet_text
from tweet
where tweet_id in (
	select tweet_id
    from (
		select tweet_id, count(*) as tweet_like_count
		from likes
		group by tweet_id
		order by tweet_like_count desc
		limit 1) as most_liked
	);

# f) Use a subquery or subqueries to display a particular user’s home timeline. That is, list tweets posted by users that a selected 
# user follows. (This would be easier with joins but using subqueries is an alternative approach.
select user_id, tweet_id, tweet_timestamp, tweet_text
from tweet
where user_id in (
	select followee_id
    from follower
    where follower_id = 4)
    and user_id not in (
    select user_id
    from users
    where hidden = 1)
    order by tweet_timestamp desc;
