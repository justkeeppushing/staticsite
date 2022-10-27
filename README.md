# My site generator
### It's just a homemade linktree clone :)

## Usage
Put any scripts, images, favicon in includes directory

Have the script that generates your html in src 
run.sh makes a build dir, copies everything from includes (flat), and executes src script 
Everything is hand coded right now because it's just for me 

The rest is configured in github actions.
You could easily use it in gitlab pages or equivalent, so long as you have the ability to
run the script then copy over your build dir.

there shouldn't be any HTML in the repo itself (build dir is ignored so
that local development will never be confused with cloudy development).

On the cloud runner you just need and python3+ and any normie unix

## Running
Github actions makes a temporary ubuntu instance in which to install python, and execute
run.sh which just runs my python script. From there I tee the output of the python script
to build/index.html. Then, github scrapes everything from build dir into their pages cloud.

The github action syntax and uses depend on their documentation and shit, but it's in here
too at `.github/workflows/static.yml`. I only added in the "run.sh" and otherwise had to
make sure other executable file had permissions with git since i'm developing in wsl.

if additional debugging is needed, it should be added inline to the scripts then
monitored from the github actions panels for the corresponding "steps". 

## Other ideas

The code is very much "only i am using this" mode, i could add more switches and config options to make it truly portable. 

I might do that "later" but for now functional is fine.


## Broblems

It's going to run right now even if unrelated files are modified, i think. 
I'm sure that could be fixed up with some kind of setting in the github actions yml but I am lazy.
