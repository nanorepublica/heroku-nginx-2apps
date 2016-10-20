# heroku-nginx-2apps

PoC repo showing how to run 2 django projects through nginx on a single dyno

# Proj1 & Proj2

2 simple django projects serving slightly different content to tell them apart

# Config

This contains a modified nginx config template for the nginx buildpack.
This has to `server` directives with differing server_name

## Buildpacks used

1. https://github.com/heroku/heroku-buildpack-nginx.git
2. heroku/python

## Procfile

This contains one web process, which backgrounds the first process, then runs the second app server
