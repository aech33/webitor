# INFO
Webitor monitors websites by creating hashes of them at specified intervals. It compares the 
hashes to check for any changes. If it does recognise a change, it will email you. This tool
is especially useful for websites which don't have an app version or any way of notifying its
users when an event occurs. This was initially made for prolific.co but I thought I might as
well share it as it works for any website.


# SETUP
sending emails with smtplib requires authentication so you need an App Password to use this
program. Getting one is pretty simple but you must have 2FA enabled. Go to myaccount.google.com
and go to the 'security' section. Here you can enable 2FA if not already. If you have, click
App passwords and select 'Mail' as the app and select your current any device you can access
your emails from as your device. Press generate. You will be give a 16-digit string and that
is your app password.

The only task now is to edit 'info.txt'. Open this file and enter in all of your information
where the example placeholder text is. Now you've successfully set up Webitor!

-made by aech33 on github