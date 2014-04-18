# Install prerequisites

    sudo pip install fabric

# Server bootstrap

Just bootstrap using default run list (which is "recipe[op]"):

    fab -H host1,host2

Custom run list:

    fab deploy:run_list='recipe[mycookbook];recipe[mycookbook2::foo]' -H host1
