# payup
## what is this?
**payup** is a monthly rent reminder in slack with one-click venmo payment.
You can use it to split rent among your house-mates.

There are two roles:

1. the "master of coin" - this is the person who writes the check to the landlord.
2. roomies - these are the people that need to forward their portion of the rent to the master of coin.

## how does it work?
You can use this repo to generate an aws lambda function.
This function get's executed by an AWS cloudwatch event once a month.

## writing your config file
copy the example_config.json file to config.json
```
cp example_config.json config.json
```
Edit the config.json file to suit your needs.

| parameter           | description                                                      |
|---------------------|------------------------------------------------------------------|
| slack_webhook_url   | Configure an [incoming webhook](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks), and then put your api url here. |
| slack_name          | This is the master of coin's slack user name, starting with an @ |
| venmo_user          | This is the master of coin's venmo username.                     |
| rents               | This is a map of venmo user name to rent owed i.e. "@dan": 99.99 |

## generating your lambda
you need jinja2 to generate the template.

if you don't have it already, you can install it with `pip install jinja2`

now to generate the lambda.py file:
```
python ./render.py
```

## configuring aws
You can now copy the contents of your lambda file to aws lambda.
Once you have entered in the lambda code, click the event sources tab.
Add a new event of type "CloudWatch Events - Schedule".
This new event can be configured similar to cron.

I used `0 9 15 * ? *` as my cron expression.
It triggers reminders at 9am on the 15th of every month.


