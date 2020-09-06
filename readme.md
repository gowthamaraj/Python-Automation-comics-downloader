# Python Automation Task

> Blogs and other regularly updating websites usually have a front page with
the most recent post as well as a Previous button on the page that takes you
to the previous post. Then that post will also have a Previous button, and so
on, creating a trail from the most recent page to the first post on the site.
If you wanted a copy of the site’s content to read when you’re not online,
you could manually navigate over every page and save each one. But this is
pretty boring work, so let’s write a program to do it instead.

## Implementaion Steps
1. Download pages with the requests module.
2. Find the URL of the comic image for a page using Beautiful Soup.
3. Download and save the comic image to the hard drive with iter_content().
4. Find the URL of the Previous Comic link, and repeat.