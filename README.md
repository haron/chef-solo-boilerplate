# Install

    sudo pip install fabric
    cd chef-solo
    git submodule init && git submodule update

# Server bootstrap

Just bootstrap using default run list (which is "recipe[op]"):

    fab -H host1,host2

Modify run list:

    fab deploy:run_list='recipe[mycookbook];recipe[mycookbook2::foo]' -H host1
