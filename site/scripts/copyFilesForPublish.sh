#!binbash
SOURCE_REPO=../Birgisch/
PUBLISH_REPO=../DZB-Wiki/
DEFAULTFILES="scripts/defaultFiles.txt"
WHITELIST="scripts/whitelist.txt"

# Clear the publish folder if it exists, or create it if it doesn't
## TODO: Git pull, if changes exist put them into an folder 'external changes'
## --> https://stackoverflow.com/questions/13715544/shell-script-to-check-git-for-changes-and-then-loop-through-changed-files
rm -rf $PUBLISH_REPO/site
mkdir -p $PUBLISH_REPO/site

# Go to source repo and copy build artifacts into publish repo
cd $SOURCE_REPO

# Copy pages to the publish folder
echo "copy ./  to  $PUBLISH_REPO/site/"
cp -r -u "./" "$PUBLISH_REPO/site/"

# Copy media folder to the publish folder
echo "copy ./media/  to  $PUBLISH_REPO/site/media"
cp -r -u "./media/" "$PUBLISH_REPO/site/media"

# Copy hashover comment system to the publish folder
echo "copy ./hashover/  to  $PUBLISH_REPO/site/hashover"
cp -r -u "./hashover/" "$PUBLISH_REPO/site/hashover"

# Publish

cd $PUBLISH_REPO

#read -p "Press any key to continue" x
git pull && git add -A && git commit -a -m "Automatic publish process: `date +'%d.%m.%Y - %H:%M:%S'`" && git push

read var1
